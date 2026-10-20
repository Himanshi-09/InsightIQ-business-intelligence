
import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>
        /* =========================================
           INSIGHTIQ — DESIGN SYSTEM
           White + Blue + Purple Ombre
        ========================================= */

        :root {
            --iq-primary: #6257F5;
            --iq-primary-dark: #4940D8;
            --iq-blue: #3978FF;
            --iq-purple: #9875FF;
            --iq-text: #151D45;
            --iq-muted: #68738F;
            --iq-border: #E6EAF6;
            --iq-surface: #FFFFFF;
            --iq-soft: #F6F8FF;
            --iq-shadow: 0 8px 28px rgba(65, 79, 160, 0.08);
        }

        /* =========================================
           GLOBAL
        ========================================= */

        html, body, [class*="css"] {
            font-family: Inter, -apple-system, BlinkMacSystemFont,
                         "Segoe UI", sans-serif;
        }

        .stApp {
            background:
                radial-gradient(
                    ellipse at 10% 0%,
                    rgba(91, 132, 255, 0.07),
                    transparent 34%
                ),
                radial-gradient(
                    ellipse at 90% 8%,
                    rgba(156, 112, 255, 0.08),
                    transparent 32%
                ),
                #FBFCFF;
            color: var(--iq-text);
        }

        [data-testid="stHeader"] {
            background: rgba(255, 255, 255, 0.82);
        }

        [data-testid="stToolbar"] {
            right: 1rem;
        }

        .main .block-container {
            max-width: 1500px;
            padding: 2rem 2.4rem 3rem;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        /* =========================================
           SIDEBAR
        ========================================= */

        [data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #FFFFFF 0%,
                #F9FAFF 65%,
                #F2F5FF 100%
            );
            border-right: 1px solid var(--iq-border);
        }

        [data-testid="stSidebar"] > div:first-child {
            padding: 1.4rem 1rem;
        }

        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            gap: 0.65rem;
        }

        .iq-brand {
            display: flex;
            align-items: center;
            gap: 11px;
            padding: 0.6rem 0.35rem 1rem;
        }

        .iq-brand-icon {
            width: 43px;
            height: 43px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 14px;
            background: linear-gradient(
                135deg,
                #3978FF 0%,
                #7959FF 55%,
                #B28BFF 100%
            );
            color: white;
            font-size: 25px;
            box-shadow: 0 5px 15px rgba(98, 87, 245, 0.22);
        }

        .iq-brand-name {
            color: var(--iq-text);
            font-size: 1.65rem;
            line-height: 1.2;
            font-weight: 800;
            letter-spacing: -1px;
        }

        .iq-brand-subtitle {
            color: var(--iq-muted);
            font-size: 0.59rem;
            letter-spacing: 1.25px;
            font-weight: 700;
            margin-top: 3px;
        }

        .iq-sidebar-footer {
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--iq-muted);
            font-size: 0.73rem;
            padding: 0.6rem 0.2rem;
        }

        .iq-status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #25B887;
            box-shadow: 0 0 0 4px rgba(37, 184, 135, 0.10);
        }

        [data-testid="stSidebar"] [data-testid="stButton"] button {
            min-height: 42px;
            justify-content: flex-start;
            border-radius: 10px;
            border: 1px solid transparent;
            background: transparent;
            color: #65708D;
            font-size: 0.88rem;
            font-weight: 500;
            text-align: left;
            padding: 0.55rem 0.8rem;
            transition: all 0.2s ease;
        }

        [data-testid="stSidebar"] [data-testid="stButton"] button:hover {
            background: #EEF1FF;
            border-color: #E0E4FF;
            color: var(--iq-primary);
        }

        [data-testid="stSidebar"] [data-testid="stButton"] button[kind="primary"] {
            background: linear-gradient(
                105deg,
                #E9EDFF,
                #F1E9FF
            );
            color: #5548DF;
            border-color: #E3DEFF;
            font-weight: 700;
        }

        [data-testid="stSidebar"] hr {
            border-color: var(--iq-border);
            margin: 0.6rem 0;
        }

        /* =========================================
           HEADINGS & TYPOGRAPHY
        ========================================= */

        h1, h2, h3, h4 {
            color: var(--iq-text);
            letter-spacing: -0.6px;
        }

        h1 {
            font-weight: 800 !important;
            letter-spacing: -1.5px !important;
        }

        h2, h3 {
            font-weight: 750 !important;
        }

        p, li {
            color: #586582;
            line-height: 1.65;
        }

        [data-testid="stCaptionContainer"] p {
            color: var(--iq-muted);
            font-size: 0.82rem;
        }

        .iq-eyebrow {
            color: #6658E9;
            font-size: 0.72rem;
            letter-spacing: 2px;
            font-weight: 800;
            margin-bottom: 1rem;
        }

        .iq-section-title {
            color: var(--iq-text);
            font-size: 1.35rem;
            font-weight: 800;
            letter-spacing: -0.6px;
            margin: 1rem 0 0.45rem;
        }

        /* =========================================
           LANDING PAGE HERO
        ========================================= */

        .iq-topbar {
            position: relative;
            overflow: hidden;
            display: grid;
            grid-template-columns: 1.05fr 0.95fr;
            align-items: center;
            gap: 1.5rem;
            min-height: 365px;
            padding: 2.6rem 2.5rem;
            border: 1px solid #E8EBFF;
            border-radius: 25px;
            background:
                radial-gradient(
                    circle at 83% 15%,
                    rgba(158, 126, 255, 0.20),
                    transparent 33%
                ),
                radial-gradient(
                    circle at 65% 95%,
                    rgba(74, 135, 255, 0.16),
                    transparent 35%
                ),
                linear-gradient(120deg, #FFFFFF, #F8FAFF);
            box-shadow: var(--iq-shadow);
        }

        .iq-hero-title {
            font-size: clamp(2.2rem, 4vw, 3.65rem);
            line-height: 1.12;
            margin: 0 0 1rem;
            color: #121B47;
        }

        .iq-hero-title span {
            background: linear-gradient(
                100deg,
                #3978FF 5%,
                #6758F5 48%,
                #A06EFF 100%
            );
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .iq-hero-description {
            max-width: 530px;
            color: #65708D;
            font-size: 1rem;
            line-height: 1.8;
        }

        .iq-hero-art {
            position: relative;
            min-height: 270px;
            display: flex;
            align-items: center;
            justify-content: center;
            isolation: isolate;
        }

        .iq-art-orb {
            position: absolute;
            width: 235px;
            height: 235px;
            border-radius: 50%;
            background: linear-gradient(
                135deg,
                rgba(75, 133, 255, 0.20),
                rgba(151, 100, 255, 0.20)
            );
            filter: blur(2px);
            z-index: -1;
        }

        .iq-art-card {
            position: absolute;
            width: 205px;
            padding: 18px;
            border: 1px solid rgba(255, 255, 255, 0.95);
            border-radius: 17px;
            background: rgba(255, 255, 255, 0.90);
            box-shadow: 0 15px 40px rgba(77, 86, 180, 0.16);
            backdrop-filter: blur(12px);
            animation: iq-float 5s ease-in-out infinite;
        }

        .iq-art-card-one {
            top: 15px;
            left: 0;
            transform: rotate(-7deg);
        }

        .iq-art-card-two {
            right: 0;
            bottom: 18px;
            animation-delay: -2.5s;
            transform: rotate(5deg);
        }

        .iq-art-label {
            font-size: 0.61rem;
            letter-spacing: 1px;
            color: #7983A2;
            font-weight: 800;
        }

        .iq-art-number {
            font-size: 1.1rem;
            font-weight: 800;
            color: #5147E7;
            margin-top: 9px;
        }

        .iq-art-bars {
            height: 50px;
            display: flex;
            align-items: flex-end;
            gap: 7px;
            margin-top: 10px;
        }

        .iq-art-bars span {
            flex: 1;
            border-radius: 5px 5px 1px 1px;
            background: linear-gradient(
                180deg,
                #8B7AFF,
                #4B7CFF
            );
        }

        .iq-art-bars span:nth-child(1) { height: 35%; }
        .iq-art-bars span:nth-child(2) { height: 55%; }
        .iq-art-bars span:nth-child(3) { height: 42%; }
        .iq-art-bars span:nth-child(4) { height: 72%; }
        .iq-art-bars span:nth-child(5) { height: 62%; }
        .iq-art-bars span:nth-child(6) { height: 95%; }

        .iq-art-line {
            color: #7E6AFF;
            font-size: 1.6rem;
            margin-top: 8px;
        }

        .iq-art-center {
            width: 57px;
            height: 57px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 19px;
            background: linear-gradient(135deg, #4D80FF, #9466FF);
            color: white;
            font-size: 2rem;
            box-shadow: 0 12px 28px rgba(102, 91, 242, 0.35);
        }

        @keyframes iq-float {
            0%, 100% {
                margin-top: 0;
            }
            50% {
                margin-top: -10px;
            }
        }

        /* =========================================
           FEATURE CARDS
        ========================================= */

        .iq-feature-card {
            min-height: 195px;
            padding: 1.35rem;
            margin: 0.5rem 0 0.65rem;
            border: 1px solid var(--iq-border);
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.94);
            box-shadow: 0 4px 18px rgba(65, 79, 160, 0.035);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .iq-feature-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--iq-shadow);
        }

        .iq-feature-icon {
            width: 44px;
            height: 44px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 13px;
            color: #6357EF;
            background: linear-gradient(
                135deg,
                #EAF0FF,
                #F1E9FF
            );
            font-size: 1.45rem;
            font-weight: 800;
            margin-bottom: 1rem;
        }

        .iq-feature-card h4 {
            font-size: 1.04rem;
            margin: 0 0 0.45rem;
        }

        .iq-feature-card p {
            font-size: 0.86rem;
            line-height: 1.65;
            margin: 0;
        }

        /* =========================================
           WORKFLOW STEPS
        ========================================= */

        .iq-step-card {
            height: 100%;
            min-height: 135px;
            padding: 1.1rem;
            border: 1px solid var(--iq-border);
            border-radius: 16px;
            background: linear-gradient(
                145deg,
                #FFFFFF,
                #F8F9FF
            );
        }

        .iq-step-number {
            width: 34px;
            height: 34px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 11px;
            background: linear-gradient(135deg, #4D83FF, #8B65F5);
            color: white;
            font-size: 0.8rem;
            font-weight: 800;
            margin-bottom: 0.85rem;
        }

        .iq-step-card h4 {
            margin: 0 0 0.3rem;
            font-size: 1rem;
        }

        .iq-step-card p {
            font-size: 0.8rem;
            line-height: 1.5;
            margin: 0;
        }

        /* =========================================
           KPI METRIC CARDS
        ========================================= */

        .iq-metric-card {
            min-height: 128px;
            padding: 1.15rem 1.2rem;
            border: 1px solid #E7EAF6;
            border-radius: 16px;
            background: #FFFFFF;
            box-shadow: 0 5px 20px rgba(60, 78, 160, 0.045);
            transition: transform 0.2s ease;
        }

        .iq-metric-card:hover {
            transform: translateY(-2px);
        }

        .iq-metric-label {
            color: #737D99;
            font-size: 0.79rem;
            font-weight: 600;
            margin-bottom: 0.8rem;
        }

        .iq-metric-value {
            color: #17224D;
            font-size: clamp(1.25rem, 2vw, 1.85rem);
            font-weight: 800;
            letter-spacing: -0.8px;
            overflow-wrap: anywhere;
        }

        .iq-metric-caption {
            color: #8590A9;
            font-size: 0.72rem;
            margin-top: 0.6rem;
            line-height: 1.4;
        }

        /* =========================================
           EMPTY STATE
        ========================================= */

        .iq-empty-state {
            padding: 2.5rem 1.5rem;
            margin-top: 2rem;
            text-align: center;
            border: 1px dashed #C8CFF5;
            border-radius: 20px;
            background: linear-gradient(
                120deg,
                #FFFFFF,
                #F5F7FF,
                #F9F5FF
            );
        }

        .iq-empty-state h3 {
            font-size: 1.3rem;
            margin: 0.7rem 0 0.3rem;
        }

        .iq-empty-state p {
            max-width: 580px;
            margin: 0 auto;
            font-size: 0.9rem;
        }

        
        /* =========================================
           BUTTONS — HIGH CONTRAST TEXT
        ========================================= */

        /* Base styling for all main-page buttons */
        .stApp .stButton > button,
        .stApp .stDownloadButton > button {
            min-height: 44px;
            border-radius: 11px;
            font-size: 0.92rem;
            font-weight: 750;
            letter-spacing: 0.1px;

            color: #26345C !important;
            background: #FFFFFF !important;

            border: 1px solid #D9DFF2 !important;
            box-shadow: 0 3px 10px rgba(48, 66, 130, 0.06);

            transition:
                background 0.2s ease,
                color 0.2s ease,
                box-shadow 0.2s ease,
                transform 0.2s ease;
        }

        /* Ensure nested button text and icons remain visible */
        .stApp .stButton > button *,
        .stApp .stDownloadButton > button * {
            color: inherit !important;
            font-weight: inherit;
        }

        /* Primary gradient buttons */
        .stApp .stButton > button[kind="primary"],
        .stApp .stDownloadButton > button[kind="primary"] {
            color: #FFFFFF !important;

            background: linear-gradient(
                105deg,
                #2864F5 0%,
                #6250F5 55%,
                #8648F5 100%
            ) !important;

            border: 1px solid transparent !important;
            font-weight: 800 !important;

            text-shadow: 0 1px 2px rgba(25, 20, 80, 0.18);
            box-shadow: 0 5px 16px rgba(79, 83, 230, 0.22);
        }

        .stApp .stButton > button[kind="primary"] *,
        .stApp .stDownloadButton > button[kind="primary"] * {
            color: #FFFFFF !important;
        }

        /* Hover: stronger gradient and readable white text */
        .stApp .stButton > button[kind="primary"]:hover,
        .stApp .stDownloadButton > button[kind="primary"]:hover {
            color: #FFFFFF !important;

            background: linear-gradient(
                105deg,
                #174FE0 0%,
                #5040E5 55%,
                #7435E8 100%
            ) !important;

            border-color: transparent !important;
            box-shadow: 0 7px 22px rgba(79, 70, 220, 0.32);
            transform: translateY(-1px);
        }

        /* Hover: white buttons */
        .stApp .stButton > button:not([kind="primary"]):hover,
        .stApp .stDownloadButton > button:not([kind="primary"]):hover {
            color: #4937D5 !important;
            background: #F0EEFF !important;
            border-color: #A9A0FF !important;
            box-shadow: 0 4px 14px rgba(98, 87, 245, 0.12);
        }

        /* Keyboard focus accessibility */
        .stApp .stButton > button:focus-visible,
        .stApp .stDownloadButton > button:focus-visible {
            outline: 3px solid #8B7CFF !important;
            outline-offset: 3px;
        }

        /* Disabled buttons */
        .stApp .stButton > button:disabled,
        .stApp .stDownloadButton > button:disabled {
            color: #858DA5 !important;
            background: #EDEFF5 !important;
            border-color: #E0E4ED !important;
            box-shadow: none !important;
            text-shadow: none !important;
        }

        /* =========================================
           INPUTS
        ========================================= */

        [data-baseweb="input"],
        [data-baseweb="select"],
        [data-baseweb="textarea"] {
            border-radius: 10px;
        }

        [data-baseweb="input"] > div,
        [data-baseweb="textarea"] > div {
            background: #FFFFFF;
            border-color: #DFE4F2;
        }

        [data-baseweb="select"] > div {
            background: #FFFFFF;
            border-color: #DFE4F2;
        }

        [data-baseweb="input"]:focus-within,
        [data-baseweb="select"]:focus-within,
        [data-baseweb="textarea"]:focus-within {
            border-color: #8273FF;
            box-shadow: 0 0 0 1px #8273FF;
        }

        [data-testid="stFileUploader"] {
            padding: 1.1rem;
            border: 1px dashed #BFC8F3;
            border-radius: 15px;
            background: #FAFBFF;
        }

        /* =========================================
           CHARTS, TABLES & CONTAINERS
        ========================================= */

        [data-testid="stPlotlyChart"],
        [data-testid="stVegaLiteChart"],
        [data-testid="stArrowVegaLiteChart"],
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
            border: 1px solid #E8EBF6;
            border-radius: 14px;
            overflow: hidden;
            background: #FFFFFF;
        }

        [data-testid="stExpander"] {
            border: 1px solid var(--iq-border);
            border-radius: 12px;
            background: #FFFFFF;
        }

        [data-testid="stAlert"] {
            border-radius: 12px;
        }

        hr {
            border-color: #E9ECF7;
        }

        /* =========================================
           RESPONSIVE LAYOUT
        ========================================= */

        @media (max-width: 900px) {
            .main .block-container {
                padding: 1.4rem 1.2rem 2rem;
            }

            .iq-topbar {
                grid-template-columns: 1fr;
                padding: 2rem 1.5rem;
            }

            .iq-hero-art {
                min-height: 230px;
            }

            .iq-hero-title {
                font-size: 2.5rem;
            }
        }

        @media (max-width: 600px) {
            .main .block-container {
                padding: 1rem 0.8rem 1.5rem;
            }

            .iq-topbar {
                padding: 1.5rem 1.1rem;
                border-radius: 18px;
            }

            .iq-hero-title {
                font-size: 2.05rem;
                letter-spacing: -1px;
            }

            .iq-hero-description {
                font-size: 0.9rem;
            }

            .iq-hero-art {
                min-height: 210px;
            }

            .iq-art-card {
                width: 170px;
                padding: 13px;
            }

            .iq-metric-card {
                padding: 0.9rem;
            }

            .iq-metric-value {
                font-size: 1.25rem;
            }
        }

        /* Respect accessibility preferences */
        @media (prefers-reduced-motion: reduce) {
            *,
            *::before,
            *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
                scroll-behavior: auto !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
