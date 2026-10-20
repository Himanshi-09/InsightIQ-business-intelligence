
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path
from styles import apply_styles

# =========================================================
# INSIGHTIQ — AI BUSINESS INTELLIGENCE ASSISTANT
# =========================================================

st.set_page_config(
    page_title="InsightIQ | AI Business Intelligence",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_styles()

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "data" not in st.session_state:
    st.session_state.data = None

if "filename" not in st.session_state:
    st.session_state.filename = None

if "business_context" not in st.session_state:
    st.session_state.business_context = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# =========================================================
# REUSABLE HELPERS
# =========================================================

def money(value):
    if pd.isna(value):
        return "N/A"

    value = float(value)
    absolute = abs(value)

    if absolute >= 1e7:
        return f"₹{value / 1e7:.2f} Cr"
    if absolute >= 1e5:
        return f"₹{value / 1e5:.2f} L"
    if absolute >= 1e3:
        return f"₹{value / 1e3:.1f} K"

    return f"₹{value:,.2f}"


def numeric_columns(df):
    return df.select_dtypes(include=np.number).columns.tolist()


def find_column(columns, keywords):
    for keyword in keywords:
        for column in columns:
            if keyword in str(column).lower().replace("_", " "):
                return column
    return None


def get_business_metrics(df, revenue_col, cost_col, profit_col):
    revenue = (
        pd.to_numeric(df[revenue_col], errors="coerce").sum()
        if revenue_col else None
    )

    cost = (
        pd.to_numeric(df[cost_col], errors="coerce").sum()
        if cost_col else None
    )

    profit = (
        pd.to_numeric(df[profit_col], errors="coerce").sum()
        if profit_col
        else (
            revenue - cost
            if revenue is not None and cost is not None
            else None
        )
    )

    margin = (
        profit / revenue * 100
        if profit is not None and revenue not in (None, 0)
        else None
    )

    return revenue, cost, profit, margin


def metric_card(label, value, caption="Based on uploaded data"):
    st.markdown(
        f"""
        <div class="iq-metric-card">
            <div class="iq-metric-label">{label}</div>
            <div class="iq-metric-value">{value}</div>
            <div class="iq-metric-caption">{caption}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def section_heading(title, subtitle=None):
    st.markdown(f'<div class="iq-section-title">{title}</div>',
                unsafe_allow_html=True)
    if subtitle:
        st.caption(subtitle)


def go_to(page):
    st.session_state.page = page


def show_empty_state():
    st.markdown(
        """
        <div class="iq-empty-state">
            <div style="font-size:42px;">📊</div>
            <h3>Your business intelligence starts here</h3>
            <p>
                Upload your startup's dataset to explore revenue, profit,
                regional performance, forecasts, and growth opportunities.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Upload Business Dataset", type="primary"):
        go_to("Upload Data")
        st.rerun()


def require_data():
    if st.session_state.data is None:
        st.info(
            "Upload a business dataset first to unlock data-driven insights."
        )
        if st.button("Go to Dataset Upload", type="primary"):
            go_to("Upload Data")
            st.rerun()
        return False

    return True


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

with st.sidebar:
    st.markdown(
        """
        <div class="iq-brand">
            <div class="iq-brand-icon">✦</div>
            <div>
                <div class="iq-brand-name">InsightIQ</div>
                <div class="iq-brand-subtitle">BUSINESS INTELLIGENCE</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.caption("WORKSPACE")

    navigation = [
        ("Home", "⌂", "Overview"),
        ("Dashboard", "▦", "Business Dashboard"),
        ("Upload Data", "↑", "Upload Dataset"),
        ("Business Analysis", "◫", "Performance Analysis"),
        ("Regional Insights", "◎", "Regional Intelligence"),
        ("Forecasting", "↗", "Revenue Forecasting"),
        ("Market Opportunities", "◇", "Market Discovery"),
        ("AI Advisor", "✧", "AI Growth Advisor"),
        ("Reports", "▤", "Business Reports"),
    ]

    for page, icon, label in navigation:
        active = st.session_state.page == page

        if st.button(
            f"{icon}   {label}",
            key=f"nav_{page}",
            use_container_width=True,
            type="primary" if active else "secondary"
        ):
            go_to(page)
            st.rerun()

    st.markdown("---")

    if st.session_state.filename:
        st.markdown("**Current dataset**")
        st.caption(f"📄 {st.session_state.filename}")

    st.markdown(
        """
        <div class="iq-sidebar-footer">
            <div class="iq-status-dot"></div>
            <span>Business Intelligence Workspace</span>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# LOAD DATASET
# =========================================================

df = st.session_state.data

# =========================================================
# HOME — LANDING PAGE
# =========================================================

if st.session_state.page == "Home":

    st.markdown(
        """
        <div class="iq-topbar">
            <div>
                <div class="iq-eyebrow">AI-POWERED BUSINESS INTELLIGENCE</div>
                <h1 class="iq-hero-title">
                    Smarter Decisions<br>
                    for a <span>Bigger Tomorrow.</span>
                </h1>
                <p class="iq-hero-description">
                    Transform your business data into real opportunities.
                    Understand performance, discover profitable markets,
                    forecast growth, and build a smarter startup.
                </p>
            </div>
            <div class="iq-hero-art">
                <div class="iq-art-orb"></div>
                <div class="iq-art-card iq-art-card-one">
                    <div class="iq-art-label">REVENUE GROWTH</div>
                    <div class="iq-art-number">↗ Insights</div>
                    <div class="iq-art-bars">
                        <span></span><span></span><span></span>
                        <span></span><span></span><span></span>
                    </div>
                </div>
                <div class="iq-art-card iq-art-card-two">
                    <div class="iq-art-label">MARKET INTELLIGENCE</div>
                    <div class="iq-art-number">◎ Opportunities</div>
                    <div class="iq-art-line">⌁ ── ⌁ ─── ⌁</div>
                </div>
                <div class="iq-art-center">✦</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1.2, 1, 1])

    with col1:
        if st.button(
            "✦  Get Started — Analyze Your Data",
            type="primary",
            use_container_width=True
        ):
            go_to("Upload Data")
            st.rerun()

    with col2:
        if st.button("Explore Dashboard", use_container_width=True):
            go_to("Dashboard")
            st.rerun()

    with col3:
        if st.button("Meet Your AI Advisor", use_container_width=True):
            go_to("AI Advisor")
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    section_heading(
        "Business intelligence, all in one place",
        "Everything you need to make informed startup decisions."
    )

    feature_columns = st.columns(3)

    features = [
        (
            "◫",
            "Business Performance",
            "Understand revenue, expenses, profit margins, and growth trends.",
            "Business Analysis"
        ),
        (
            "◎",
            "Regional Intelligence",
            "Compare locations and identify promising markets using available data.",
            "Regional Insights"
        ),
        (
            "↗",
            "Growth Forecasting",
            "Explore potential revenue trends and future business scenarios.",
            "Forecasting"
        ),
        (
            "◇",
            "Market Opportunities",
            "Discover promising products, categories, and expansion opportunities.",
            "Market Opportunities"
        ),
        (
            "✧",
            "AI Growth Advisor",
            "Turn business findings into practical, prioritized recommendations.",
            "AI Advisor"
        ),
        (
            "▤",
            "Intelligent Reports",
            "Bring important metrics, findings, and action plans together.",
            "Reports"
        ),
    ]

    for i, (symbol, title, description, destination) in enumerate(features):
        with feature_columns[i % 3]:
            st.markdown(
                f"""
                <div class="iq-feature-card">
                    <div class="iq-feature-icon">{symbol}</div>
                    <h4>{title}</h4>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"Explore {title} →",
                key=f"feature_{i}",
                use_container_width=True
            ):
                go_to(destination)
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    section_heading("Your journey with InsightIQ")

    steps = st.columns(5)

    workflow = [
        ("01", "Upload", "Bring your business data"),
        ("02", "Understand", "Identify relevant metrics"),
        ("03", "Analyze", "Discover patterns and trends"),
        ("04", "Forecast", "Explore possible scenarios"),
        ("05", "Grow", "Take informed action"),
    ]

    for column, (number, title, description) in zip(steps, workflow):
        with column:
            st.markdown(
                f"""
                <div class="iq-step-card">
                    <div class="iq-step-number">{number}</div>
                    <h4>{title}</h4>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    if df is None:
        show_empty_state()


# =========================================================
# UPLOAD DATA
# =========================================================

elif st.session_state.page == "Upload Data":

    st.title("Upload Your Business Data")
    st.write(
        "Import your startup dataset to unlock business performance "
        "analytics, regional comparisons, forecasting, and growth insights."
    )

    uploaded_file = st.file_uploader(
        "Choose a business dataset",
        type=["csv", "xlsx", "xls"],
        help="Supported formats: CSV and Excel."
    )

    if uploaded_file is not None:
        try:
            if uploaded_file.name.lower().endswith(".csv"):
                uploaded_df = pd.read_csv(uploaded_file)
            else:
                uploaded_df = pd.read_excel(uploaded_file)

            if uploaded_df.empty:
                st.error("The uploaded dataset contains no records.")
            else:
                st.session_state.data = uploaded_df
                st.session_state.filename = uploaded_file.name
                df = uploaded_df

                st.success(
                    f"Dataset loaded: {len(df):,} rows and "
                    f"{len(df.columns):,} columns."
                )

                a, b, c = st.columns(3)

                with a:
                    metric_card("Records", f"{len(df):,}")
                with b:
                    metric_card("Business Fields", f"{len(df.columns):,}")
                with c:
                    metric_card(
                        "Numeric Fields",
                        f"{len(numeric_columns(df)):,}"
                    )

                st.subheader("Dataset Preview")
                st.dataframe(df.head(10), use_container_width=True)

                st.subheader("Tell us about your business")

                st.session_state.business_context = st.text_area(
                    "Business context (optional)",
                    value=st.session_state.business_context,
                    placeholder=(
                        "Example: We run a small clothing brand and want "
                        "to improve profit and expand into new cities."
                    )
                )

                if st.button(
                    "Open Business Dashboard →",
                    type="primary"
                ):
                    go_to("Dashboard")
                    st.rerun()

        except Exception as exc:
            st.error(
                "We couldn't read this file. Please check that it is a "
                "valid CSV or Excel business dataset."
            )
            st.caption(f"Technical details: {exc}")

    st.info(
        "InsightIQ will prepare data in the background when needed. "
        "Its main purpose is business intelligence and growth advice, "
        "not data cleaning."
    )


# =========================================================
# SHARED DATA-DRIVEN ANALYSIS
# =========================================================

elif st.session_state.page in [
    "Dashboard",
    "Business Analysis",
    "Regional Insights",
    "Forecasting",
    "Market Opportunities",
    "AI Advisor",
    "Reports"
]:

    if not require_data():
        st.stop()

    columns = df.columns.tolist()
    numbers = numeric_columns(df)

    suggested_revenue = find_column(
        columns, ["revenue", "sales", "turnover", "income"]
    )
    suggested_cost = find_column(
        columns, ["expense", "expenses", "cost", "costs", "spending"]
    )
    suggested_profit = find_column(
        columns, ["profit", "net income", "earnings"]
    )
    suggested_region = find_column(
        columns, [
            "region", "state", "city", "location", "country",
            "market", "area", "province"
        ]
    )
    suggested_date = find_column(
        columns, ["date", "month", "year", "timestamp", "period"]
    )
    suggested_category = find_column(
        columns, [
            "product", "category", "service", "industry",
            "business type", "segment"
        ]
    )

    def choose_column(label, suggested, options, key):
        choices = ["Not available"] + options

        default = (
            choices.index(suggested)
            if suggested in options
            else 0
        )

        selected = st.selectbox(
            label,
            choices,
            index=default,
            key=key
        )

        return None if selected == "Not available" else selected

    # -----------------------------------------------------
    # COLUMN MAPPING
    # -----------------------------------------------------

    with st.expander("⚙️ Configure Business Metrics", expanded=False):
        st.caption(
            "Review the detected columns to ensure your financial "
            "analysis uses the correct fields."
        )

        map1, map2 = st.columns(2)

        with map1:
            revenue_col = choose_column(
                "Revenue / Sales",
                suggested_revenue,
                numbers,
                "revenue_column"
            )

            cost_col = choose_column(
                "Expenses / Costs",
                suggested_cost,
                numbers,
                "cost_column"
            )

        with map2:
            profit_col = choose_column(
                "Profit (if recorded)",
                suggested_profit,
                numbers,
                "profit_column"
            )

            region_col = choose_column(
                "Region / Location",
                suggested_region,
                columns,
                "region_column"
            )

        map3, map4 = st.columns(2)

        with map3:
            date_col = choose_column(
                "Date / Period",
                suggested_date,
                columns,
                "date_column"
            )

        with map4:
            category_col = choose_column(
                "Product / Category",
                suggested_category,
                columns,
                "category_column"
            )

    revenue, cost, profit, margin = get_business_metrics(
        df, revenue_col, cost_col, profit_col
    )

    # =====================================================
    # DASHBOARD
    # =====================================================

    if st.session_state.page == "Dashboard":

        st.title("Business Intelligence Dashboard")
        st.caption(
            "Your startup's performance at a glance, based on the "
            "dataset you uploaded."
        )

        k1, k2, k3, k4 = st.columns(4)

        with k1:
            metric_card(
                "Total Revenue",
                money(revenue) if revenue is not None else "Map revenue"
            )

        with k2:
            metric_card(
                "Total Expenses",
                money(cost) if cost is not None else "Map expenses"
            )

        with k3:
            metric_card(
                "Net Profit",
                money(profit) if profit is not None else "Map profit"
            )

        with k4:
            metric_card(
                "Profit Margin",
                f"{margin:.1f}%" if margin is not None else "N/A",
                "Profit as a percentage of revenue"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        left, right = st.columns(2)

        with left:
            section_heading("Revenue & Profit Overview")

            if revenue_col and profit_col:
                chart_df = df[[revenue_col, profit_col]].copy()

                for col in [revenue_col, profit_col]:
                    chart_df[col] = pd.to_numeric(
                        chart_df[col], errors="coerce"
                    )

                st.line_chart(chart_df, height=300)
            elif revenue_col:
                st.line_chart(
                    pd.to_numeric(df[revenue_col], errors="coerce"),
                    height=300
                )
            else:
                st.info(
                    "Map your revenue field to display financial trends."
                )

        with right:
            section_heading("Performance by Region")

            # Use a geographical map whenever latitude and longitude exist.
            # This supports datasets such as AB_NYC_2019.csv, which may not
            # contain a revenue column but do contain listing coordinates.
            latitude_col = find_column(columns, ["latitude", "lat"])
            longitude_col = find_column(
                columns, ["longitude", "lon", "lng"]
            )

            if latitude_col and longitude_col:
                map_df = df.copy()
                map_df[latitude_col] = pd.to_numeric(
                    map_df[latitude_col], errors="coerce"
                )
                map_df[longitude_col] = pd.to_numeric(
                    map_df[longitude_col], errors="coerce"
                )
                map_df = map_df.dropna(
                    subset=[latitude_col, longitude_col]
                )
                map_df = map_df[
                    map_df[latitude_col].between(-90, 90)
                    & map_df[longitude_col].between(-180, 180)
                ]

                if map_df.empty:
                    st.info("No valid latitude and longitude values were found.")
                else:
                    # Limit plotted points for responsiveness on large files.
                    if len(map_df) > 5000:
                        map_df = map_df.sample(5000, random_state=42)

                    price_col = find_column(
                        columns, ["price", "listing price", "average price"]
                    )
                    name_col = find_column(
                        columns, ["name", "listing name", "property name"]
                    )
                    hover_columns = [
                        col for col in [
                            region_col,
                            find_column(columns, ["neighbourhood", "neighborhood"]),
                            find_column(columns, ["room type"]),
                            price_col,
                        ]
                        if col and col in map_df.columns
                        and col not in [latitude_col, longitude_col]
                    ]

                    color_col = None
                    if price_col:
                        map_df[price_col] = pd.to_numeric(
                            map_df[price_col], errors="coerce"
                        )
                        if map_df[price_col].notna().any():
                            color_col = price_col

                    center_lat = float(map_df[latitude_col].median())
                    center_lon = float(map_df[longitude_col].median())
                    zoom_level = 9

                    # Center the map on NYC for the AB_NYC_2019 dataset.
                    if (
                        40.4 <= center_lat <= 41.1
                        and -74.4 <= center_lon <= -73.5
                    ):
                        center_lat, center_lon = 40.73, -73.94

                    fig = px.scatter_map(
                        map_df,
                        lat=latitude_col,
                        lon=longitude_col,
                        color=color_col,
                        hover_name=(
                            name_col if name_col in map_df.columns else None
                        ) if name_col else None,
                        hover_data=hover_columns,
                        color_continuous_scale=[
                            "#60A5FA", "#6366F1", "#7C3AED"
                        ] if color_col else None,
                        center={"lat": center_lat, "lon": center_lon},
                        zoom=zoom_level,
                        map_style="carto-positron",
                        height=300,
                        labels={
                            latitude_col: "Latitude",
                            longitude_col: "Longitude",
                        },
                    )
                    fig.update_traces(
                        marker={"size": 7, "opacity": 0.75}
                    )
                    fig.update_layout(
                        margin={"l": 0, "r": 0, "t": 0, "b": 0},
                        paper_bgcolor="rgba(0,0,0,0)",
                        font={"color": "#172554"},
                    )
                    st.plotly_chart(
                        fig,
                        use_container_width=True,
                        config={"scrollZoom": True, "displayModeBar": True},
                    )
                    st.caption(
                        f"Showing {len(map_df):,} mapped records. "
                        "Marker colors represent price when available."
                    )

            elif region_col and revenue_col:
                regional_df = df.copy()
                regional_df[revenue_col] = pd.to_numeric(
                    regional_df[revenue_col], errors="coerce"
                )

                regional = (
                    regional_df.groupby(region_col, dropna=False)[revenue_col]
                    .sum()
                    .sort_values(ascending=False)
                    .head(10)
                )

                st.bar_chart(regional, height=300)
            else:
                st.info(
                    "A latitude/longitude field is needed for a geographical map. "
                    "For a bar-chart comparison, map a region/location and revenue field."
                )

        st.markdown("<br>", unsafe_allow_html=True)

        section_heading("Quick Business Observations")

        observations = []

        if revenue is not None and profit is not None:
            observations.append(
                f"Your recorded profit is {money(profit)} "
                f"against revenue of {money(revenue)}."
            )

            if margin is not None:
                observations.append(
                    f"The calculated profit margin is {margin:.1f}%."
                )

        if region_col and revenue_col:
            observations.append(
                "Regional revenue can help compare recorded sales "
                "performance, but not necessarily regional profitability."
            )

        if not observations:
            observations.append(
                "Configure the relevant financial columns to generate "
                "business observations."
            )

        for observation in observations:
            st.markdown(f"- {observation}")

        st.caption(
            "These observations describe uploaded records; they are not "
            "independent verification of business performance."
        )
        

    # =====================================================
    # BUSINESS ANALYSIS
    # =====================================================

    elif st.session_state.page == "Business Analysis":

        st.title("Business Performance Analysis")
        st.write(
            "Explore financial performance, profit margins, product "
            "contributions, and changes over time."
        )

        a, b, c = st.columns(3)

        with a:
            metric_card(
                "Revenue",
                money(revenue) if revenue is not None else "N/A"
            )
        with b:
            metric_card(
                "Profit",
                money(profit) if profit is not None else "N/A"
            )
        with c:
            metric_card(
                "Profit Margin",
                f"{margin:.2f}%" if margin is not None else "N/A"
            )

        if revenue_col and cost_col and profit_col is None:
            st.info(
                "Profit is calculated as total revenue minus total costs. "
                "This simplified calculation may not include taxes, "
                "interest, or other accounting adjustments."
            )

        left, right = st.columns(2)

        with left:
            section_heading("Revenue vs Expenses")

            if revenue_col and cost_col:
                comparison = df[[revenue_col, cost_col]].copy()

                for col in comparison:
                    comparison[col] = pd.to_numeric(
                        comparison[col], errors="coerce"
                    )

                st.bar_chart(comparison, height=330)
            else:
                st.info(
                    "Map revenue and expense fields to compare them."
                )

        with right:
            section_heading("Product / Category Performance")

            if category_col and revenue_col:
                category_data = df.copy()
                category_data[revenue_col] = pd.to_numeric(
                    category_data[revenue_col], errors="coerce"
                )

                category_sales = (
                    category_data.groupby(category_col)[revenue_col]
                    .sum()
                    .sort_values(ascending=False)
                    .head(10)
                )

                st.bar_chart(category_sales, height=330)

                st.caption(
                    "Revenue rankings are not profit rankings unless "
                    "product-level costs and profit are also available."
                )
            else:
                st.info(
                    "Map a product/category field and revenue to compare "
                    "your business offerings."
                )

        if date_col and revenue_col:
            st.subheader("Financial Trends Over Time")

            trend = df[[date_col, revenue_col]].copy()
            trend[date_col] = pd.to_datetime(
                trend[date_col], errors="coerce"
            )
            trend[revenue_col] = pd.to_numeric(
                trend[revenue_col], errors="coerce"
            )
            trend = trend.dropna().sort_values(date_col)

            if not trend.empty:
                trend = trend.set_index(date_col)
                st.line_chart(
                    trend[revenue_col].resample("MS").sum(),
                    height=320
                )
            else:
                st.info(
                    "No valid date values were found for a time-series chart."
                )

    # =====================================================
    # REGIONAL INSIGHTS
    # =====================================================

    elif st.session_state.page == "Regional Insights":

        st.title("Regional Business Intelligence")
        st.write(
            "Compare business performance across locations and "
            "identify regions that deserve further investigation."
        )

        if region_col is None:
            st.warning(
                "Your dataset needs a region, city, state, or location "
                "field for regional analysis."
            )

        elif revenue_col is None:
            st.warning(
                "Map the revenue field to compare financial performance "
                "across regions."
            )

        else:
            regional_df = df.copy()

            regional_df[revenue_col] = pd.to_numeric(
                regional_df[revenue_col], errors="coerce"
            )

            aggregation = {revenue_col: "sum"}

            if cost_col:
                regional_df[cost_col] = pd.to_numeric(
                    regional_df[cost_col], errors="coerce"
                )
                aggregation[cost_col] = "sum"

            if profit_col:
                regional_df[profit_col] = pd.to_numeric(
                    regional_df[profit_col], errors="coerce"
                )
                aggregation[profit_col] = "sum"

            regional = (
                regional_df.groupby(region_col, dropna=False)
                .agg(aggregation)
                .sort_values(revenue_col, ascending=False)
            )

            if profit_col:
                regional["Profit Margin (%)"] = np.where(
                    regional[revenue_col] != 0,
                    regional[profit_col] / regional[revenue_col] * 100,
                    np.nan
                )
            elif cost_col:
                regional["Estimated Profit"] = (
                    regional[revenue_col] - regional[cost_col]
                )

                regional["Profit Margin (%)"] = np.where(
                    regional[revenue_col] != 0,
                    regional["Estimated Profit"]
                    / regional[revenue_col] * 100,
                    np.nan
                )

            top_n = st.slider(
                "Number of regions to compare",
                min_value=3,
                max_value=20,
                value=10
            )

            st.subheader("Regional Revenue Ranking")
            st.bar_chart(
                regional[revenue_col].head(top_n),
                height=350
            )

            st.subheader("Regional Performance Table")
            st.dataframe(
                regional.head(top_n).reset_index(),
                use_container_width=True
            )

            if profit_col or cost_col:
                st.caption(
                    "Revenue and recorded profit can rank regions "
                    "differently. Verify that cost allocation is "
                    "comparable between regions."
                )
            else:
                st.info(
                    "This dataset currently supports regional revenue "
                    "comparisons, not regional profit calculations. "
                    "Add cost or profit data for profitability analysis."
                )

            st.subheader("Business Interpretation")

            best_region = regional[revenue_col].idxmax()

            st.markdown(
                f"""
                - **Highest recorded revenue:** {best_region}
                - **Revenue:** {money(regional.loc[best_region, revenue_col])}
                - **Next step:** Investigate customer demand, operating
                  costs, competition, and profit margins before making
                  an expansion decision.
                """
            )

            st.caption(
                "High recorded revenue does not prove that a region has "
                "the highest market demand or future growth potential."
            )

    # =====================================================
    # FORECASTING
    # =====================================================

    elif st.session_state.page == "Forecasting":

        st.title("Revenue Forecasting & Growth Scenarios")
        st.write(
            "Explore possible future revenue trends using historical "
            "business data where sufficient observations are available."
        )

        if revenue_col is None or date_col is None:
            st.warning(
                "Forecasting requires both a date/period field and a "
                "revenue field."
            )

        else:
            forecast_df = df[[date_col, revenue_col]].copy()

            forecast_df[date_col] = pd.to_datetime(
                forecast_df[date_col], errors="coerce"
            )
            forecast_df[revenue_col] = pd.to_numeric(
                forecast_df[revenue_col], errors="coerce"
            )

            forecast_df = forecast_df.dropna().sort_values(date_col)

            if forecast_df.empty:
                st.warning(
                    "No usable date and revenue observations were found."
                )
            else:
                monthly = (
                    forecast_df.set_index(date_col)[revenue_col]
                    .resample("MS")
                    .sum()
                    .dropna()
                )

                if len(monthly) < 3:
                    st.warning(
                        "At least three months of usable observations "
                        "are required for this simple baseline forecast. "
                        "More history is preferable."
                    )
                else:
                    horizon = st.slider(
                        "Forecast horizon (months)",
                        min_value=3,
                        max_value=12,
                        value=6
                    )

                    # Simple linear trend baseline.
                    # This is not a full predictive ML model.
                    x = np.arange(len(monthly))
                    slope, intercept = np.polyfit(
                        x, monthly.values, 1
                    )

                    future_x = np.arange(
                        len(monthly), len(monthly) + horizon
                    )

                    future_values = slope * future_x + intercept

                    future_dates = pd.date_range(
                        monthly.index[-1] + pd.offsets.MonthBegin(1),
                        periods=horizon,
                        freq="MS"
                    )

                    forecast_series = pd.Series(
                        future_values,
                        index=future_dates,
                        name="Baseline forecast"
                    )

                    historical = monthly.rename("Historical revenue")

                    chart_df = pd.concat(
                        [historical, forecast_series],
                        axis=1
                    )

                    st.subheader("Historical Revenue & Baseline Forecast")
                    st.line_chart(chart_df, height=380)

                    last_actual = float(monthly.iloc[-1])
                    final_forecast = float(future_values[-1])

                    c1, c2, c3 = st.columns(3)

                    with c1:
                        metric_card(
                            "Latest Period Revenue",
                            money(last_actual)
                        )

                    with c2:
                        metric_card(
                            f"Revenue in {horizon} Months",
                            money(final_forecast)
                        )

                    with c3:
                        change = (
                            (final_forecast / last_actual - 1) * 100
                            if last_actual != 0
                            else None
                        )

                        metric_card(
                            "Scenario Change",
                            f"{change:+.1f}%"
                            if change is not None else "N/A",
                            "Compared with the latest period"
                        )

                    st.subheader("Forecast Table")
                    st.dataframe(
                        pd.DataFrame({
                            "Month": future_dates,
                            "Baseline Forecast": future_values
                        }),
                        use_container_width=True
                    )

                    st.warning(
                        "This is a simple linear-trend baseline, not a "
                        "validated prediction of future revenue. It does "
                        "not account for seasonality, inflation, market "
                        "changes, or business strategy. Forecasts may "
                        "be negative or inaccurate, especially with "
                        "limited or irregular historical data."
                    )

    # =====================================================
    # MARKET OPPORTUNITIES
    # =====================================================

    elif st.session_state.page == "Market Opportunities":

        st.title("Market & Business Opportunities")
        st.write(
            "Investigate which products and regions perform well in "
            "your existing records before deciding where to expand."
        )

        if category_col and revenue_col:
            market_df = df.copy()

            market_df[revenue_col] = pd.to_numeric(
                market_df[revenue_col], errors="coerce"
            )

            category_summary = (
                market_df.groupby(category_col)[revenue_col]
                .sum()
                .sort_values(ascending=False)
            )

            st.subheader("Highest-Revenue Categories")
            st.bar_chart(category_summary.head(10), height=320)

            st.dataframe(
                category_summary.rename(
                    "Recorded Revenue"
                ).reset_index(),
                use_container_width=True
            )

        else:
            st.info(
                "Map your product/category and revenue fields to compare "
                "business offerings."
            )

        if region_col and revenue_col:
            regional = df.copy()
            regional[revenue_col] = pd.to_numeric(
                regional[revenue_col], errors="coerce"
            )

            regional_summary = (
                regional.groupby(region_col)[revenue_col]
                .sum()
                .sort_values(ascending=False)
            )

            st.subheader("Regions With the Highest Recorded Revenue")
            st.bar_chart(regional_summary.head(10), height=300)

        st.subheader("Opportunity Assessment")

        st.markdown(
            """
            To assess a genuine new-market opportunity, compare:

            - Customer demand and target audience size.
            - Competitor presence and pricing.
            - Rent, salaries, logistics, and customer acquisition costs.
            - Expected profit margins and operational capacity.
            - Local regulations and other market-specific risks.
            """
        )

        st.info(
            "Your uploaded data can reveal existing performance patterns. "
            "It cannot establish external market demand or competitor "
            "strength unless those factors are represented in the data "
            "or supported by additional market research."
        )

    # =====================================================
    # AI GROWTH ADVISOR
    # =====================================================

    elif st.session_state.page == "AI Advisor":

        st.title("AI Startup Growth Advisor")
        st.write(
            "Explore practical next steps based on your business "
            "performance and the data available."
        )

        context = st.session_state.business_context

        if context:
            st.markdown("**Your business context**")
            st.write(context)

        st.subheader("Evidence-based business observations")

        observations = []

        if revenue is not None and profit is not None:
            observations.append(
                f"Recorded revenue is {money(revenue)} and recorded "
                f"or calculated profit is {money(profit)}."
            )

        if margin is not None:
            if margin < 0:
                observations.append(
                    "The calculated profit margin is negative. "
                    "Review cost structure, pricing, and accounting inputs."
                )
            elif margin < 10:
                observations.append(
                    "The calculated profit margin is below 10%. "
                    "Investigate cost drivers and pricing before changing "
                    "your business model."
                )
            else:
                observations.append(
                    f"The calculated profit margin is {margin:.1f}%. "
                    "Compare this with your industry's economics and "
                    "historical performance."
                )

        if region_col and revenue_col:
            regional_copy = df.copy()
            regional_copy[revenue_col] = pd.to_numeric(
                regional_copy[revenue_col], errors="coerce"
            )

            regional_sales = (
                regional_copy.groupby(region_col)[revenue_col]
                .sum()
                .sort_values(ascending=False)
            )

            if not regional_sales.empty:
                observations.append(
                    f"{regional_sales.index[0]} has the highest "
                    "recorded revenue among the regions in this dataset. "
                    "Check local costs and demand before expanding."
                )

        if category_col and revenue_col:
            category_copy = df.copy()
            category_copy[revenue_col] = pd.to_numeric(
                category_copy[revenue_col], errors="coerce"
            )

            category_sales = (
                category_copy.groupby(category_col)[revenue_col]
                .sum()
                .sort_values(ascending=False)
            )

            if not category_sales.empty:
                observations.append(
                    f"{category_sales.index[0]} is the highest-revenue "
                    "category in the uploaded records. Revenue alone "
                    "does not establish which category is most profitable."
                )

        if observations:
            for item in observations:
                st.markdown(f"- {item}")
        else:
            st.info(
                "Configure revenue, cost, profit, region, or category "
                "fields to generate more useful business observations."
            )

        st.subheader("Build a growth action plan")

        priority = st.selectbox(
            "What is your biggest current priority?",
            [
                "Increase revenue",
                "Improve profit margins",
                "Expand into new regions",
                "Identify profitable products",
                "Reduce operating costs",
                "Plan future growth"
            ]
        )

        budget = st.selectbox(
            "Available budget for growth initiatives",
            [
                "Not specified",
                "Under ₹25,000",
                "₹25,000–₹1 lakh",
                "₹1 lakh–₹5 lakh",
                "Above ₹5 lakh"
            ]
        )

        business_stage = st.selectbox(
            "Current startup stage",
            [
                "Idea / Pre-launch",
                "Early-stage startup",
                "Growing business",
                "Established small or medium business"
            ]
        )

        if st.button(
            "Generate My Business Action Plan",
            type="primary"
        ):
            recommendations = {
                "Increase revenue": [
                    "Identify the customer segments and offerings "
                    "associated with the strongest recorded sales.",
                    "Test one targeted marketing campaign and measure "
                    "conversion rate and customer acquisition cost.",
                    "Compare repeat purchases, average order value, "
                    "and new-customer sales."
                ],
                "Improve profit margins": [
                    "Compare revenue and fully allocated costs by "
                    "product, service, and region.",
                    "Review supplier costs, pricing, discounting, "
                    "returns, and delivery expenses.",
                    "Prioritize controlled experiments that improve "
                    "profit without damaging customer retention."
                ],
                "Expand into new regions": [
                    "Shortlist regions with promising recorded performance.",
                    "Estimate local demand, competition, rent, logistics, "
                    "and customer acquisition costs.",
                    "Run a small pilot before committing to a major "
                    "expansion investment."
                ],
                "Identify profitable products": [
                    "Compare product-level revenue with direct and "
                    "allocated operating costs.",
                    "Evaluate profit per unit, sales volume, returns, "
                    "and repeat-purchase behavior.",
                    "Test whether improving or bundling lower-performing "
                    "products could increase contribution margin."
                ],
                "Reduce operating costs": [
                    "Separate fixed costs from variable costs.",
                    "Identify rising expense categories and compare "
                    "cost per order or customer over time.",
                    "Prioritize changes that protect product quality "
                    "and customer experience."
                ],
                "Plan future growth": [
                    "Establish a baseline for revenue, profit, and cash flow.",
                    "Develop conservative, expected, and optimistic "
                    "scenarios with explicit assumptions.",
                    "Define monthly KPIs and review actual performance "
                    "against the plan."
                ]
            }

            st.markdown("### Your initial action plan")

            for index, action in enumerate(
                recommendations[priority], start=1
            ):
                st.markdown(f"**{index}.** {action}")

            st.markdown(f"**Business stage:** {business_stage}")
            st.markdown(f"**Growth budget:** {budget}")

            st.caption(
                "These are rule-based starter recommendations informed "
                "by your selected goal and available data. A connected "
                "LLM or additional market data source is needed for "
                "genuinely AI-generated, context-rich advice."
            )

        st.subheader("Ask a business question")

        question = st.text_input(
            "Your question",
            placeholder=(
                "Example: How can I improve profit in my best-performing "
                "region?"
            )
        )

        if st.button("Analyze Question"):
            if question.strip():
                st.session_state.chat_history.append({
                    "question": question.strip(),
                    "answer": (
                        "To answer this reliably, InsightIQ needs to "
                        "analyze the relevant financial columns and, "
                        "for external market questions, supporting market "
                        "data. Use the observations and action plan above "
                        "as a starting point. A live AI model is not yet "
                        "connected to this version of the application."
                    )
                })
                st.rerun()
            else:
                st.warning("Please enter a business question.")

        for chat in st.session_state.chat_history:
            st.markdown(f"**You:** {chat['question']}")
            st.markdown(f"**InsightIQ:** {chat['answer']}")

    # =====================================================
    # REPORTS
    # =====================================================

    elif st.session_state.page == "Reports":

        st.title("Business Intelligence Reports")
        st.write(
            "Generate a downloadable summary of your uploaded data "
            "and the business metrics that can currently be calculated."
        )

        report_lines = [
            "# InsightIQ Business Intelligence Report",
            "",
            f"**Dataset:** {st.session_state.filename or 'Uploaded dataset'}",
            f"**Records analyzed:** {len(df):,}",
            f"**Fields:** {len(df.columns):,}",
            "",
            "## Financial Overview",
            "",
            f"- Total revenue: {money(revenue) if revenue is not None else 'Unavailable'}",
            f"- Total expenses: {money(cost) if cost is not None else 'Unavailable'}",
            f"- Total profit: {money(profit) if profit is not None else 'Unavailable'}",
            f"- Profit margin: {f'{margin:.2f}%' if margin is not None else 'Unavailable'}",
            "",
            "## Business Context",
            "",
            st.session_state.business_context or "Not provided",
            "",
            "## Interpretation Notes",
            "",
            "- Results depend on the accuracy and meaning of the uploaded fields.",
            "- Forecasts and market opportunities require appropriate supporting data.",
            "- Historical performance is not a guarantee of future success.",
        ]

        if region_col and revenue_col:
            report_lines.extend([
                "",
                "## Regional Revenue",
                ""
            ])

            report_df = df.copy()
            report_df[revenue_col] = pd.to_numeric(
                report_df[revenue_col], errors="coerce"
            )

            regional = (
                report_df.groupby(region_col)[revenue_col]
                .sum()
                .sort_values(ascending=False)
            )

            for region, amount in regional.head(10).items():
                report_lines.append(f"- {region}: {money(amount)}")

        report_text = "\n".join(report_lines)

        st.markdown("### Report Preview")
        st.markdown(report_text)

        st.download_button(
            "Download Business Report (.md)",
            data=report_text,
            file_name="InsightIQ_Business_Report.md",
            mime="text/markdown",
            type="primary"
        )

        st.download_button(
            "Download Regional / Financial Data (.csv)",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="InsightIQ_Analyzed_Data.csv",
            mime="text/csv"
        )

        st.caption(
            "This version generates a basic report. Automated AI-written "
            "executive summaries and advanced PDF reports can be added "
            "when we build the reporting and AI integration layers."
        )
