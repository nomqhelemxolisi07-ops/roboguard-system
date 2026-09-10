
import re
import textwrap
from html import escape
import streamlit as st

st.set_page_config(
    page_title="ROBO GUIDE | Zimbabwe Heritage Explorer",
    page_icon="🗿",
    layout="wide",
    initial_sidebar_state="expanded",
)

SLOGAN = "Where Heritage Speaks to the Future"


def html(content: str):
    st.markdown(textwrap.dedent(content).strip(), unsafe_allow_html=True)


# ============================================================
# DARK HERITAGE / MUSEUM THEME
# ============================================================

st.markdown(
    """
    <style>
    :root {
        --bg: #181512;
        --bg2: #211B17;
        --panel: #2A211C;
        --panel2: #332821;
        --panel3: #3B2E26;
        --clay: #8B4F3B;
        --clay2: #A45F46;
        --bronze: #C49A55;
        --bronze2: #D4B06D;
        --sand: #EADDC8;
        --sand2: #D8C8B0;
        --muted: #B9AA96;
        --line: #5A493C;
        --green: #65705C;
        --text: #F2E7D8;
    }

    .stApp {
        background:
            radial-gradient(circle at 15% 0%, rgba(196,154,85,0.08), transparent 28%),
            radial-gradient(circle at 90% 8%, rgba(139,79,59,0.11), transparent 25%),
            linear-gradient(180deg, var(--bg) 0%, #1E1915 100%);
        color: var(--text);
    }

    .block-container {
        max-width: 1220px;
        padding-top: 1rem;
        padding-bottom: 2.5rem;
    }

    /* Sidebar shell */
    [data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, #241D18 0%, #1D1814 100%);
        border-right: 1px solid #47392F;
        box-shadow: 12px 0 30px rgba(0,0,0,0.18);
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0.6rem;
    }

    [data-testid="stSidebar"] * {
        color: #F2E7D8 !important;
    }

    /* Sidebar brand block */
    .sidebar-brand {
        background:
            linear-gradient(145deg, #332720, #2A211B);
        border: 1px solid #5A4638;
        border-top: 4px solid #C49A55;
        border-radius: 18px;
        padding: 1rem;
        margin: 0.25rem 0 0.9rem;
        box-shadow: 0 8px 18px rgba(0,0,0,0.18);
    }

    .sidebar-brand-title {
        font-size: 1.35rem;
        font-weight: 900;
        letter-spacing: 0.06em;
        color: #F5E8D3;
    }

    .sidebar-brand-sub {
        margin-top: 0.35rem;
        font-size: 0.78rem;
        color: #D7B678;
        font-weight: 750;
        line-height: 1.35;
    }

    .sidebar-section {
        color: #C8AA72;
        text-transform: uppercase;
        letter-spacing: 0.11em;
        font-size: 0.72rem;
        font-weight: 850;
        margin: 0.75rem 0 0.35rem;
    }

    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        background: #2F261F;
        color: #F0E5D4 !important;
        border: 1px solid #4D3E33;
        border-radius: 12px;
        min-height: 2.75rem;
        font-weight: 760;
        text-align: left;
        padding-left: 0.85rem;
        transition: all 0.15s ease;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background: #3C2E26;
        border-color: #C49A55;
        transform: translateX(2px);
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background: #2D241E !important;
        border: 1px solid #5A493B !important;
        border-radius: 11px !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] * {
        color: #F2E7D8 !important;
    }

    /* Hero */
    .hero {
        position: relative;
        overflow: hidden;
        background:
            linear-gradient(135deg, #3A2D25 0%, #4A3127 60%, #33261F 100%);
        border: 1px solid #614C3C;
        border-left: 6px solid #C49A55;
        border-radius: 24px;
        padding: 2.2rem 2rem;
        box-shadow: 0 18px 38px rgba(0,0,0,0.22);
        margin-bottom: 1.2rem;
    }

    .hero::after {
        content: "";
        position: absolute;
        right: -20px;
        bottom: -40px;
        width: 290px;
        height: 170px;
        opacity: 0.18;
        background:
            repeating-linear-gradient(
                45deg,
                transparent 0 14px,
                #C49A55 14px 20px,
                transparent 20px 34px
            );
    }

    .hero h1 {
        position: relative;
        z-index: 2;
        margin: 0;
        color: #F6E9D5 !important;
        font-size: clamp(2.5rem, 6vw, 4.8rem);
        letter-spacing: 0.04em;
        line-height: 1;
    }

    .hero h3 {
        position: relative;
        z-index: 2;
        color: #D4B06D !important;
        margin: 0.7rem 0 0.45rem;
    }

    .hero p {
        position: relative;
        z-index: 2;
        max-width: 860px;
        color: #E6D8C4 !important;
        line-height: 1.65;
        font-size: 1.03rem;
        margin: 0;
    }

    .slogan {
        position: relative;
        z-index: 2;
        display: inline-block;
        margin-top: 1rem;
        padding: 0.45rem 0.75rem;
        border-radius: 999px;
        color: #F0D59D;
        background: rgba(18,14,12,0.28);
        border: 1px solid #8D6B3A;
        font-size: 0.82rem;
        font-weight: 850;
        letter-spacing: 0.03em;
    }

    .cultural-strip {
        height: 12px;
        border-radius: 999px;
        margin: 0 0 1rem;
        background:
            linear-gradient(90deg,
                #8B4F3B 0 14%,
                #C49A55 14% 28%,
                #65705C 28% 42%,
                #3E3028 42% 58%,
                #65705C 58% 72%,
                #C49A55 72% 86%,
                #8B4F3B 86% 100%);
        box-shadow: inset 0 0 0 1px #59483A;
    }

    /* Main cards */
    .site-card,
    .info-card,
    .fact-card,
    .quiz-card,
    .chat-user,
    .chat-bot,
    .source-note,
    .stat-card {
        box-sizing: border-box;
    }

    .site-card {
        background:
            linear-gradient(145deg, #2C231D 0%, #352821 100%);
        border: 1px solid #574438;
        border-top: 5px solid #8B4F3B;
        border-radius: 18px;
        padding: 1.2rem;
        min-height: 270px;
        box-shadow: 0 10px 22px rgba(0,0,0,0.18);
    }

    .site-card h3 {
        color: #F0DFC9 !important;
        margin: 0.55rem 0 0.35rem;
    }

    .site-card p {
        color: #CBB9A4 !important;
        line-height: 1.55;
    }

    .site-icon {
        font-size: 2.65rem;
    }

    .badge {
        display: inline-block;
        background: #46372C;
        border: 1px solid #6C5543;
        color: #E7C985;
        border-radius: 999px;
        padding: 0.3rem 0.6rem;
        margin: 0.35rem 0.25rem 0 0;
        font-size: 0.76rem;
        font-weight: 820;
    }

    .info-card {
        background: #29211C;
        border: 1px solid #514238;
        border-left: 5px solid #8B4F3B;
        border-radius: 15px;
        padding: 1.05rem 1.1rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 6px 15px rgba(0,0,0,0.13);
    }

    .info-card p {
        color: #D7C8B6 !important;
        line-height: 1.65;
        margin: 0;
    }

    .fact-card {
        background: #30261F;
        border: 1px solid #59473A;
        border-radius: 15px;
        padding: 1rem;
        min-height: 125px;
        margin-bottom: 0.7rem;
    }

    .fact-card h4 {
        color: #D6B56F !important;
        margin-top: 0;
    }

    .fact-card p {
        color: #D3C2AE !important;
        line-height: 1.55;
    }

    .unesco-card {
        background:
            linear-gradient(135deg, #4A392A 0%, #5D432C 100%);
        border: 1px solid #806039;
        border-left: 6px solid #C49A55;
        border-radius: 16px;
        padding: 1.1rem;
        color: #F0DFC5;
        line-height: 1.6;
        box-shadow: 0 8px 18px rgba(0,0,0,0.15);
    }

    .stat-card {
        background: #2C241E;
        border: 1px solid #514137;
        border-radius: 14px;
        padding: 0.85rem;
        min-height: 105px;
        text-align: center;
    }

    .stat-label {
        color: #AF9D89;
        font-size: 0.72rem;
        font-weight: 850;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .stat-value {
        color: #EAD9C2;
        font-size: 1.05rem;
        font-weight: 900;
        margin-top: 0.35rem;
    }

    .quiz-card {
        background: #2E251F;
        border: 1px solid #564438;
        border-top: 5px solid #C49A55;
        border-radius: 16px;
        padding: 1.1rem;
        margin-bottom: 0.8rem;
    }

    .quiz-card h3 {
        color: #F0DFC9 !important;
        margin: 0;
    }

    div[data-testid="stRadio"] {
        background: #27201B;
        border: 1px solid #4B3C32;
        border-radius: 14px;
        padding: 0.7rem;
    }

    /* Assistant */
    .chat-user {
        background: #33241E;
        border: 1px solid #634839;
        border-left: 5px solid #A45F46;
        border-radius: 14px;
        padding: 0.9rem 1rem;
        margin: 0.55rem 0;
        color: #E8D8C5;
    }

    .chat-bot {
        background: #30291F;
        border: 1px solid #62533A;
        border-left: 5px solid #C49A55;
        border-radius: 14px;
        padding: 0.9rem 1rem;
        margin: 0.55rem 0 0.9rem;
        color: #E7DAC7;
    }

    .chat-user strong,
    .chat-bot strong {
        color: #F0D59D !important;
    }

    div[data-testid="stTextInput"] label {
        color: #DCCDBB !important;
        font-weight: 800 !important;
    }

    div[data-testid="stTextInput"] input {
        background: #28211C !important;
        color: #F1E5D5 !important;
        border: 1px solid #5A493B !important;
        border-radius: 12px !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: #A99B8B !important;
        opacity: 1 !important;
    }

    /* Buttons */
    div.stButton > button,
    div[data-testid="stFormSubmitButton"] button {
        background: #5A4032;
        color: #F5E8D7 !important;
        border: 1px solid #765543;
        border-radius: 11px;
        font-weight: 820;
        min-height: 2.75rem;
    }

    div.stButton > button:hover,
    div[data-testid="stFormSubmitButton"] button:hover {
        background: #704C39;
        border-color: #C49A55;
        color: #FFF0D9 !important;
    }

    /* General Streamlit typography */
    .stMarkdown,
    .stMarkdown p,
    .stMarkdown li,
    h1, h2, h3, h4, h5, h6 {
        color: #EADDC8;
    }

    div[data-testid="stMetric"] {
        background: #2C241E;
        border: 1px solid #514137;
        border-radius: 14px;
        padding: 0.75rem;
    }

    div[data-testid="stMetric"] label {
        color: #B8A996 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #EEDFCB !important;
    }

    [data-testid="stAlert"] {
        background: #2A231E !important;
        border: 1px solid #5C4A3E !important;
        color: #E6D9C8 !important;
    }

    .source-note {
        background: #25201B;
        border: 1px dashed #665342;
        border-radius: 13px;
        padding: 0.85rem 0.95rem;
        color: #BFAF9B;
        font-size: 0.84rem;
        margin-top: 1rem;
    }

    .footer {
        margin-top: 2.2rem;
        padding: 1.1rem;
        text-align: center;
        border-top: 1px solid #4D3D32;
        color: #AA9A88;
    }

    .footer strong {
        color: #D7B678;
    }

    .image-explorer-card {
        background: #261F1A;
        border: 1px solid #514137;
        border-radius: 16px;
        padding: 0.85rem;
        margin-bottom: 0.85rem;
        box-shadow: 0 8px 18px rgba(0,0,0,0.15);
    }

    .protect-focus {
        display: inline-block;
        background: #6D3E31;
        color: #F3DFC9;
        border: 1px solid #965944;
        border-radius: 999px;
        padding: 0.28rem 0.58rem;
        font-size: 0.74rem;
        font-weight: 850;
        margin-bottom: 0.5rem;
    }

    .image-note {
        color: #D7C7B4;
        line-height: 1.55;
        font-size: 0.92rem;
    }

    .pronounce-card {
        background: linear-gradient(135deg, #32281F, #3B2B22);
        border: 1px solid #66503E;
        border-left: 5px solid #C49A55;
        border-radius: 15px;
        padding: 1rem;
        margin: 0.9rem 0 1rem;
    }

    .pronounce-word {
        color: #F0DFC9;
        font-size: 1.18rem;
        font-weight: 900;
        letter-spacing: 0.02em;
    }

    .pronounce-guide {
        color: #D6B56F;
        font-size: 1.05rem;
        font-weight: 850;
        margin-top: 0.3rem;
    }

    .pronounce-note {
        color: #BAAA98;
        font-size: 0.84rem;
        margin-top: 0.35rem;
        line-height: 1.45;
    }

    @media(max-width: 760px) {
        .hero {
            padding: 1.5rem 1.2rem;
        }
        .site-card {
            min-height: auto;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

DEFAULTS = {
    "page": "home",
    "lang": "English",
    "quiz_index": 0,
    "quiz_score": 0,
    "quiz_points": 0,
    "quiz_answered": False,
    "quiz_choice": None,
    "quiz_finished": False,
    "chat": [],
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# UI TRANSLATIONS
# ============================================================

UI = {
    "English": {
        "language": "Language",
        "explore": "Explore",
        "home": "Home",
        "matobo": "Matobo Hills",
        "great": "Great Zimbabwe",
        "khami": "Khami Ruins",
        "quiz": "Heritage Challenge",
        "assistant": "Heritage Assistant",
        "hero_sub": "Discover Zimbabwe's Living Heritage",
        "hero_text": "Explore remarkable places, architecture, rock art, trade and living traditions through an interactive cultural journey.",
        "choose": "Explore Zimbabwe's Heritage",
        "explore_site": "Explore",
        "history": "History",
        "culture": "Culture & People",
        "features": "Major Features",
        "unesco": "UNESCO World Heritage",
        "protect": "Respect & Protection",
        "facts": "Interesting Facts",
        "significance": "Why It Matters",
        "location": "Location",
        "inscribed": "UNESCO inscription",
        "criteria": "Criteria",
        "quiz_title": "Heritage Challenge",
        "quiz_intro": "Test your knowledge and earn Heritage Points.",
        "question": "Question",
        "submit": "Check Answer",
        "next": "Next Question",
        "restart": "Restart Challenge",
        "correct": "Correct!",
        "incorrect": "Not quite.",
        "score": "Score",
        "points": "Heritage Points",
        "achievement": "Achievement",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Heritage Assistant",
        "assistant_intro": "Ask about dates, age, builders, architecture, rock art, trade, UNESCO status or cultural importance.",
        "ask": "Ask a heritage question",
        "send": "Ask ROBO GUIDE",
        "clear": "Clear Conversation",
        "quick": "Try a question",
        "footer": "Zimbabwe Heritage Explorer • WRO 2026",
    },
    "isiNdebele": {
        "language": "Ulimi",
        "explore": "Hlola",
        "home": "Ikhaya",
        "matobo": "Amagquma eMatobo",
        "great": "Great Zimbabwe",
        "khami": "Amanxiwa eKhami",
        "quiz": "Umncintiswano Wamagugu",
        "assistant": "Umsizi Wamagugu",
        "hero_sub": "Thola Amagugu Aphilayo eZimbabwe",
        "hero_text": "Hlola indawo, izakhiwo, imidwebo yamadwala, ukuhweba lamasiko aphilayo eZimbabwe.",
        "choose": "Hlola Amagugu eZimbabwe",
        "explore_site": "Hlola",
        "history": "Umlando",
        "culture": "Amasiko Labantu",
        "features": "Izinto Ezisemqoka",
        "unesco": "Amagugu Omhlaba e-UNESCO",
        "protect": "Inhlonipho Lokuvikela",
        "facts": "Amaqiniso Athakazelisayo",
        "significance": "Kungani Ibalulekile",
        "location": "Indawo",
        "inscribed": "Ukufakwa ku-UNESCO",
        "criteria": "Imigomo",
        "quiz_title": "Umncintiswano Wamagugu",
        "quiz_intro": "Hlola ulwazi lwakho uzuze ama-Heritage Points.",
        "question": "Umbuzo",
        "submit": "Hlola Impendulo",
        "next": "Umbuzo Olandelayo",
        "restart": "Qalisa Kutsha",
        "correct": "Kulungile!",
        "incorrect": "Akukabi yikho.",
        "score": "Amaphuzu",
        "points": "Heritage Points",
        "achievement": "Impumelelo",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Umsizi Wamagugu",
        "assistant_intro": "Buza ngeminyaka, umlando, abakhi, izakhiwo, imidwebo yamadwala, ukuhweba loba i-UNESCO.",
        "ask": "Buza umbuzo wamagugu",
        "send": "Buza i-ROBO GUIDE",
        "clear": "Sula Ingxoxo",
        "quick": "Zama umbuzo",
        "footer": "Zimbabwe Heritage Explorer • WRO 2026",
    },
    "Shona": {
        "language": "Mutauro",
        "explore": "Ongorora",
        "home": "Musha",
        "matobo": "Matobo Hills",
        "great": "Great Zimbabwe",
        "khami": "Khami Ruins",
        "quiz": "Dambudziko reNhaka",
        "assistant": "Mubatsiri weNhaka",
        "hero_sub": "Ziva Nhaka Mhenyu yeZimbabwe",
        "hero_text": "Ongorora nzvimbo, zvivakwa, rock art, kutengeserana netsika mhenyu dzeZimbabwe.",
        "choose": "Ongorora Nhaka yeZimbabwe",
        "explore_site": "Ongorora",
        "history": "Nhoroondo",
        "culture": "Tsika neVanhu",
        "features": "Zvinhu Zvikuru",
        "unesco": "UNESCO World Heritage",
        "protect": "Kuremekedza & Kuchengetedza",
        "facts": "Zvinonakidza Kuziva",
        "significance": "Kukosha Kwayo",
        "location": "Nzvimbo",
        "inscribed": "UNESCO inscription",
        "criteria": "Maitiro",
        "quiz_title": "Dambudziko reNhaka",
        "quiz_intro": "Edza ruzivo rwako uwane Heritage Points.",
        "question": "Mubvunzo",
        "submit": "Tarisa Mhinduro",
        "next": "Mubvunzo Unotevera",
        "restart": "Tangazve",
        "correct": "Wagona!",
        "incorrect": "Hausati warurama.",
        "score": "Zvawabudirira",
        "points": "Heritage Points",
        "achievement": "Kubudirira",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Mubatsiri weNhaka",
        "assistant_intro": "Bvunza nezvemakore, nhoroondo, vakavaka, architecture, rock art, trade kana UNESCO.",
        "ask": "Bvunza mubvunzo wenhaka",
        "send": "Bvunza ROBO GUIDE",
        "clear": "Bvisa Hurukuro",
        "quick": "Edza mubvunzo",
        "footer": "Zimbabwe Heritage Explorer • WRO 2026",
    },
}


def T(key):
    return UI[st.session_state.lang][key]


# ============================================================
# HERITAGE SITE DATA
# ============================================================

SITES = {
    "matobo": {
        "emoji": "⛰️",
        "English": {
            "name": "Matobo Hills",
            "subtitle": "Ancient rock art, granite landscapes and living sacred traditions",
            "location": "About 35 km south of Bulawayo",
            "inscribed": "2003",
            "criteria": "(iii), (v), (vi)",
            "history": (
                "Matobo Hills preserves an exceptionally long record of human interaction with the landscape. "
                "Archaeological evidence from the wider Matobo area stretches back hundreds of thousands of years, "
                "while the surviving rock-art tradition dates back at least 13,000 years."
            ),
            "culture": (
                "Matobo is a living cultural and spiritual landscape. Sacred shrines continue to be used by communities, "
                "and the Mwari religious tradition has a strong historical association with the hills."
            ),
            "features": [
                "Distinctive granite kopjes and balancing boulders.",
                "Natural caves and rock shelters among granite formations.",
                "One of the highest concentrations of rock art in southern Africa.",
                "Paintings that provide insight into Stone Age societies and beliefs.",
                "Sacred places that remain culturally important today.",
            ],
            "unesco": (
                "Matobo Hills was inscribed on the UNESCO World Heritage List in 2003. "
                "UNESCO recognises its exceptional rock art, the long relationship between people and landscape, "
                "and the continuing importance of spiritual traditions."
            ),
            "protect": [
                "Never touch, wet, trace or rub rock paintings.",
                "Do not scratch, write or draw on rock surfaces.",
                "Do not remove stones, archaeological objects or cultural material.",
                "Respect sacred places and follow authorised guidance.",
            ],
            "facts": [
                "The rock-art tradition dates back at least 13,000 years.",
                "The landscape is famous for dramatic granite formations.",
                "Matobo remains a living spiritual landscape, not only an archaeological site.",
            ],
            "significance": (
                "Matobo Hills brings together archaeology, ancient artistic expression, spectacular geology "
                "and living spiritual traditions."
            ),
        },
        "isiNdebele": {
            "name": "Amagquma eMatobo",
            "subtitle": "Imidwebo yasendulo, amadwala egranite lamasiko angcwele",
            "location": "Cishe 35 km eningizimu yeBulawayo",
            "inscribed": "2003",
            "criteria": "(iii), (v), (vi)",
            "history": (
                "IMatobo ilobufakazi obude kakhulu bokusetshenziswa kwendawo ngabantu. "
                "Imidwebo yamadwala esekhona ihlehlela emuva okungenani iminyaka engu-13,000."
            ),
            "culture": (
                "IMatobo iyindawo ephilayo yamasiko lezomoya. Izindawo ezingcwele zisasebenza, "
                "futhi isiko likaMwari lixhumene kakhulu lamagquma."
            ),
            "features": [
                "Amagquma egranite lamadwala amakhulu abhalansile.",
                "Imihume lezindawo zokukhosela phakathi kwamadwala.",
                "Enye yezindawo ezilemidwebo yamadwala eminengi kakhulu eningizimu ye-Afrika.",
                "Imidwebo ekhombisa impilo lezinkolelo zabantu basendulo.",
                "Izindawo ezingcwele ezisaligugu emphakathini.",
            ],
            "unesco": (
                "IMatobo Hills yafakwa ku-UNESCO ngo-2003 ngenxa yemidwebo yayo yamadwala, "
                "ubudlelwano obude phakathi kwabantu lendawo kanye lamasiko omoya aqhubekayo."
            ),
            "protect": [
                "Ungathinti kumbe umanzise imidwebo yamadwala.",
                "Ungabhali kumbe udwebe emadwaleni.",
                "Ungasusi amatshe kumbe izinto zemivubukulo.",
                "Hlonipha izindawo ezingcwele.",
            ],
            "facts": [
                "Imidwebo yaseMatobo ileminyaka okungenani engu-13,000.",
                "Indawo idume ngamatshe amakhulu egranite.",
                "IMatobo iseyindawo ebalulekileyo kwezomoya.",
            ],
            "significance": (
                "IMatobo ihlanganisa imivubukulo, ubuciko basendulo, amadwala amahle kanye lamasiko aphilayo."
            ),
        },
        "Shona": {
            "name": "Matobo Hills",
            "subtitle": "Rock art yekare, granite landscape netsika dzinoyera",
            "location": "Anenge 35 km kumaodzanyemba kweBulawayo",
            "inscribed": "2003",
            "criteria": "(iii), (v), (vi)",
            "history": (
                "Matobo ine nhoroondo yakareba zvikuru yekushandiswa kwevanhu. "
                "Rock art iripo inodzokera kumashure kwemakore anosvika 13,000 kana kupfuura."
            ),
            "culture": (
                "Matobo inzvimbo yetsika nemweya ichiri kurarama. Nzvimbo dzinoyera dzichiri kushandiswa "
                "uye Mwari religious tradition ine hukama hwakakura nemakomo aya."
            ),
            "features": [
                "Makomo egranite nematombo makuru anoyevedza.",
                "Mapako nemarock shelters.",
                "Imwe yenzvimbo dzine rock art yakawanda kumaodzanyemba kweAfrica.",
                "Mifananidzo inoratidza hupenyu nezvitendero zvevanhu vekare.",
                "Nzvimbo dzinoyera dzichiri kukosha munharaunda.",
            ],
            "unesco": (
                "Matobo Hills yakanyorwa neUNESCO muna 2003 nekuda kwerock art yayo, "
                "hukama hwenguva refu pakati pevanhu nenzvimbo, uye tsika dzemweya dzichiri kurarama."
            ),
            "protect": [
                "Usabata kana kunyudza rock art.",
                "Usanyora kana kudhirowa pamatombo.",
                "Usabvisa matombo kana artefacts.",
                "Remekedza nzvimbo dzinoyera.",
            ],
            "facts": [
                "Rock art ine makore anosvika 13,000 kana kupfuura.",
                "Matobo inozivikanwa nematombo makuru egranite.",
                "Ichiri nzvimbo yakakosha yemweya.",
            ],
            "significance": (
                "Matobo inobatanidza archaeology, art yekare, geology uye tsika dzichiri kurarama."
            ),
        },
    },
    "great": {
        "emoji": "🏛️",
        "English": {
            "name": "Great Zimbabwe",
            "subtitle": "The monumental stone city that gave Zimbabwe its name",
            "location": "About 30 km from Masvingo",
            "inscribed": "1986",
            "criteria": "(i), (iii), (vi)",
            "history": (
                "Great Zimbabwe was built principally between about 1100 and 1450 AD. "
                "It became the capital of a powerful African state and an important political, economic and commercial centre. "
                "At its height in the 14th century, the city supported a population of more than 10,000 people."
            ),
            "culture": (
                "Great Zimbabwe is a major expression of Shona civilisation. Its builders created sophisticated dry-stone architecture "
                "and participated in farming, cattle keeping, gold production and long-distance trade."
            ),
            "features": [
                "The Hill Ruins, occupied from the 11th to the 15th centuries.",
                "The Great Enclosure, dating mainly to the 14th century.",
                "The famous Conical Tower inside the Great Enclosure.",
                "The Valley Ruins, containing extensive stone-built remains.",
                "Steatite, or soapstone, bird sculptures known as the Zimbabwe Birds.",
            ],
            "unesco": (
                "Great Zimbabwe National Monument was inscribed on the UNESCO World Heritage List in 1986. "
                "It is recognised as an outstanding testimony to Shona civilisation and a remarkable achievement of African architecture."
            ),
            "protect": [
                "Do not climb or sit on ancient stone walls.",
                "Never remove stones, pottery or archaeological material.",
                "Use designated visitor paths.",
                "Do not scratch, write or carve on monuments.",
            ],
            "facts": [
                "Great Zimbabwe was built principally between about 1100 and 1450 AD.",
                "The population exceeded 10,000 people during the 14th century.",
                "Imported objects including Chinese and Persian ceramics show extensive trade connections.",
            ],
            "significance": (
                "Great Zimbabwe demonstrates engineering ability, political organisation, economic strength "
                "and the cultural achievement of a major African civilisation."
            ),
        },
        "isiNdebele": {
            "name": "Great Zimbabwe",
            "subtitle": "Idolobho elikhulu lamatshe elapha iZimbabwe ibizo layo",
            "location": "Cishe 30 km ukusuka eMasvingo",
            "inscribed": "1986",
            "criteria": "(i), (iii), (vi)",
            "history": (
                "IGreat Zimbabwe yakhiwa ikakhulu phakathi kuka-1100 lo-1450 AD. "
                "Yakhula yaba yinhloko-dolobha yombuso omkhulu wase-Afrika futhi yaba yisikhungo sezombusazwe, umnotho lokuhweba."
            ),
            "culture": (
                "IGreat Zimbabwe iyisibonelo esikhulu sempucuko yamaShona. "
                "Abakhi bayo babelobuciko bokwakha ngamatshe njalo babenza ezolimo, befuyile futhi behweba kwamabanga amade."
            ),
            "features": [
                "IHill Ruins eyahlalwa phakathi kwekhulu le-11 lele-15.",
                "IGreat Enclosure eyakhiwa kakhulu ngekhulu le-14.",
                "IConical Tower.",
                "IValley Ruins.",
                "IZimbabwe Birds ezabazwa nge-steatite kumbe soapstone.",
            ],
            "unesco": (
                "IGreat Zimbabwe National Monument yafakwa ku-UNESCO ngo-1986. "
                "Ibonakala njengobufakazi obuqakathekileyo bempucuko yamaShona kanye lobuciko bokwakha base-Afrika."
            ),
            "protect": [
                "Ungakhweli kumbe uhlale phezu kwemiduli yasendulo.",
                "Ungasusi amatshe kumbe izinto zemivubukulo.",
                "Sebenzisa imizila yezivakashi.",
                "Ungabhali kumbe uqophe emidulini.",
            ],
            "facts": [
                "Yakhiwa ikakhulu phakathi kuka-1100 lo-1450 AD.",
                "Ngekhulu le-14 abantu babedlula 10,000.",
                "Izinto ezivela eChina lePersia zibonisa ukuhweba kwamabanga amade.",
            ],
            "significance": (
                "IGreat Zimbabwe ibonisa ubuciko bokwakha, amandla ezombusazwe, umnotho kanye lempucuko enkulu yase-Afrika."
            ),
        },
        "Shona": {
            "name": "Great Zimbabwe",
            "subtitle": "Guta guru rematombo rakapa Zimbabwe zita rayo",
            "location": "Anenge 30 km kubva kuMasvingo",
            "inscribed": "1986",
            "criteria": "(i), (iii), (vi)",
            "history": (
                "Great Zimbabwe yakavakwa zvikuru pakati pa1100 na1450 AD. "
                "Yakakura ikava capital yehurumende ine simba uye nzvimbo yakakosha yezvematongerwo enyika, hupfumi nekutengeserana."
            ),
            "culture": (
                "Great Zimbabwe chiratidzo chikuru cheShona civilisation. "
                "Vakavaka nzvimbo iyi vaiva nehunyanzvi hwekuvaka nematombo uye vaiita zvekurima, kuchengeta mombe nekutengeserana."
            ),
            "features": [
                "Hill Ruins yakashandiswa kubva muzana remakore rechi11 kusvika rechi15.",
                "Great Enclosure yakanyanya kuvakwa muzana remakore rechi14.",
                "Conical Tower.",
                "Valley Ruins.",
                "Zimbabwe Birds dzakavezwa nesteatite kana soapstone.",
            ],
            "unesco": (
                "Great Zimbabwe National Monument yakanyorwa neUNESCO muna 1986. "
                "Inoonekwa seuchapupu hwakakosha hweShona civilisation uye hunyanzvi hweAfrican architecture."
            ),
            "protect": [
                "Usakwira kana kugara pamadziro ekare.",
                "Usabvisa matombo kana archaeological material.",
                "Shandisa nzira dzevashanyi.",
                "Usanyora kana kuveza pamadziro.",
            ],
            "facts": [
                "Yakavakwa zvikuru pakati pa1100 na1450 AD.",
                "Muzana remakore rechi14 vanhu vaipfuura 10,000.",
                "Chinese nePersian ceramics zvinoratidza long-distance trade.",
            ],
            "significance": (
                "Great Zimbabwe inoratidza engineering skill, hutongi, simba rehupfumi uye kubudirira kweAfrican civilisation."
            ),
        },
    },
    "khami": {
        "emoji": "🧱",
        "English": {
            "name": "Khami Ruins",
            "subtitle": "Terraced stone architecture and the legacy of the Torwa dynasty",
            "location": "About 22 km west of Bulawayo",
            "inscribed": "1986",
            "criteria": "(iii), (iv)",
            "history": (
                "Khami became the capital of the Torwa dynasty after the decline of Great Zimbabwe. "
                "The site developed mainly between the 15th and 17th centuries and represents a later development "
                "of Zimbabwe's dry-stone architectural tradition."
            ),
            "culture": (
                "Khami was an important political and commercial centre. Its architecture and archaeology provide evidence "
                "of local craftsmanship, social organisation and long-distance exchange."
            ),
            "features": [
                "Extensive platforms and stone-faced terraces.",
                "Retaining or revetment walls adapted to the landscape.",
                "Chevron and chequered decorative stone patterns.",
                "The Hill Ruin, associated with the ruler's residence.",
                "Imported objects demonstrating long-distance trade.",
            ],
            "unesco": (
                "Khami Ruins National Monument was inscribed on the UNESCO World Heritage List in 1986. "
                "It is recognised for its archaeological importance and distinctive terraced architecture."
            ),
            "protect": [
                "Do not climb or lean on terrace walls.",
                "Do not remove pottery, stones or archaeological objects.",
                "Stay on authorised visitor routes.",
                "Report damage to heritage staff rather than moving objects.",
            ],
            "facts": [
                "Khami is about 22 km west of Bulawayo.",
                "It was the capital of the Torwa dynasty.",
                "Imported objects show that Khami was connected to long-distance trade networks.",
            ],
            "significance": (
                "Khami demonstrates how Zimbabwe's monumental stone-building tradition continued and developed after Great Zimbabwe."
            ),
        },
        "isiNdebele": {
            "name": "Amanxiwa eKhami",
            "subtitle": "Amathala amatshe kanye lelifa lobukhosi beTorwa",
            "location": "Cishe 22 km entshonalanga yeBulawayo",
            "inscribed": "1986",
            "criteria": "(iii), (iv)",
            "history": (
                "IKhami yaba yinhloko-dolobha yobukhosi beTorwa ngemva kokwehla kweGreat Zimbabwe. "
                "Indawo yathuthuka kakhulu phakathi kwekhulu le-15 lele-17."
            ),
            "culture": (
                "IKhami yayiyisikhungo esibalulekileyo sezombusazwe lokuhweba. "
                "Izakhiwo zayo zibonisa ubuciko, ukuhleleka kwabantu kanye lokuhweba kwamabanga amade."
            ),
            "features": [
                "Amathala amakhulu avalwe ngamatshe.",
                "Imiduli yokubamba umhlabathi.",
                "Imihlobiso ye-chevron le-chequered emadwaleni.",
                "IHill Ruin ehlobene lendawo yenkosi.",
                "Izinto ezivela kwamanye amazwe ezibonisa ukuhweba.",
            ],
            "unesco": (
                "IKhami Ruins National Monument yafakwa ku-UNESCO ngo-1986. "
                "Ibalulekile ngenxa yemivubukulo kanye lesitayela sayo samathala amatshe."
            ),
            "protect": [
                "Ungakhweli kumbe uncike emidulini yamathala.",
                "Ungasusi amatshe kumbe izinto zemivubukulo.",
                "Sebenzisa imizila yabavakashi.",
                "Bika umonakalo kubasebenzi.",
            ],
            "facts": [
                "IKhami icishe ibe 22 km entshonalanga yeBulawayo.",
                "Yayiyinhloko-dolobha yeTorwa dynasty.",
                "Izinto ezivela kwamanye amazwe zibonisa ukuhweba kwamabanga amade.",
            ],
            "significance": (
                "IKhami ikhombisa ukuthi ubuciko bokwakha ngamatshe baqhubeka futhi bathuthuka ngemva kweGreat Zimbabwe."
            ),
        },
        "Shona": {
            "name": "Khami Ruins",
            "subtitle": "Terraced stone architecture uye nhaka yeTorwa dynasty",
            "location": "Anenge 22 km kumadokero kweBulawayo",
            "inscribed": "1986",
            "criteria": "(iii), (iv)",
            "history": (
                "Khami yakava capital yeTorwa dynasty mushure mekuderera kweGreat Zimbabwe. "
                "Nzvimbo iyi yakanyanya kukura pakati pezana remakore rechi15 nerechi17."
            ),
            "culture": (
                "Khami yaiva nzvimbo yakakosha yezvematongerwo enyika nekutengeserana. "
                "Architecture yayo inoratidza craftsmanship, social organisation uye long-distance trade."
            ),
            "features": [
                "Platforms nema stone-faced terraces.",
                "Retaining kana revetment walls.",
                "Chevron nechequered wall decoration.",
                "Hill Ruin ine hukama nenzvimbo yemambo.",
                "Imported objects dzinoratidza long-distance trade.",
            ],
            "unesco": (
                "Khami Ruins National Monument yakanyorwa neUNESCO muna 1986. "
                "Inokosheswa nekuda kwearchaeology yayo uye terraced architecture."
            ),
            "protect": [
                "Usakwira kana kutsamira pamadziro ema terraces.",
                "Usabvisa pottery, matombo kana artefacts.",
                "Shandisa visitor routes.",
                "Bika kukuvara kuvashandi.",
            ],
            "facts": [
                "Khami iri anenge 22 km kumadokero kweBulawayo.",
                "Yaiva capital yeTorwa dynasty.",
                "Imported objects dzinoratidza long-distance trade.",
            ],
            "significance": (
                "Khami inoratidza kuenderera nekushanduka kweZimbabwe stone-building tradition mushure meGreat Zimbabwe."
            ),
        },
    },
}


# ============================================================
# QUIZ DATA
# ============================================================

QUIZ = {
    "English": [
        (
            "Which site is especially famous for prehistoric rock paintings?",
            ["Great Zimbabwe", "Matobo Hills", "Khami Ruins", "Victoria Falls"],
            1,
            "Matobo Hills has one of the highest concentrations of rock art in southern Africa.",
        ),
        (
            "How old is some of the surviving Matobo rock art?",
            ["About 100 years", "About 500 years", "At least 13,000 years", "About 1,000 years"],
            2,
            "The surviving rock-art tradition dates back at least 13,000 years.",
        ),
        (
            "When was Great Zimbabwe principally built?",
            ["1100–1450 AD", "1700–1850 AD", "1900–1950 AD", "500–700 AD"],
            0,
            "Great Zimbabwe was built principally between about 1100 and 1450 AD.",
        ),
        (
            "Which structure is found at Great Zimbabwe?",
            ["Great Enclosure", "Stonehenge", "Pyramids of Giza", "Colosseum"],
            0,
            "The Great Enclosure is one of Great Zimbabwe's best-known structures.",
        ),
        (
            "The Zimbabwe Birds were carved mainly from what?",
            ["Steel", "Steatite or soapstone", "Glass", "Bronze"],
            1,
            "The Zimbabwe Birds are carved steatite, commonly called soapstone.",
        ),
        (
            "Khami was the capital of which dynasty?",
            ["Torwa", "Roman", "Ottoman", "Mughal"],
            0,
            "Khami became the capital of the Torwa dynasty.",
        ),
        (
            "What is especially characteristic of Khami architecture?",
            ["Stone-faced terraces", "Glass towers", "Steel bridges", "Brick domes"],
            0,
            "Khami is especially known for terraces, retaining walls and decorative stonework.",
        ),
        (
            "What should visitors do near ancient rock paintings?",
            ["Touch them", "Wet them", "Leave them untouched", "Trace them"],
            2,
            "Rock paintings should not be touched or wetted because this can damage them.",
        ),
        (
            "Which two sites show strong evidence of long-distance trade?",
            ["Great Zimbabwe and Khami", "Matobo and Mana Pools", "Only Matobo", "None"],
            0,
            "Archaeological evidence from both Great Zimbabwe and Khami shows long-distance trade.",
        ),
        (
            "Which comparison is correct?",
            [
                "All three sites are identical",
                "Great Zimbabwe is monumental stone architecture, Khami is famous for terraces, and Matobo for rock art and sacred landscape",
                "None contains stone architecture",
                "All were built in the 20th century",
            ],
            1,
            "Each site represents a different but connected part of Zimbabwe's cultural heritage.",
        ),
    ],
    "isiNdebele": [
        (
            "Yiphi indawo eyaziwa kakhulu ngemidwebo yamadwala?",
            ["Great Zimbabwe", "Matobo Hills", "Khami Ruins", "Victoria Falls"],
            1,
            "IMatobo Hills idume kakhulu ngemidwebo yamadwala.",
        ),
        (
            "Imidwebo yaseMatobo ileminyaka engakanani?",
            ["100", "500", "Okungenani 13,000", "1,000"],
            2,
            "Imidwebo yaseMatobo ihlehlela emuva okungenani iminyaka engu-13,000.",
        ),
        (
            "IGreat Zimbabwe yakhiwa ikakhulu ngasiphi isikhathi?",
            ["1100–1450 AD", "1700–1850 AD", "1900–1950 AD", "500–700 AD"],
            0,
            "IGreat Zimbabwe yakhiwa ikakhulu phakathi kuka-1100 lo-1450 AD.",
        ),
        (
            "Yisiphi isakhiwo esiseGreat Zimbabwe?",
            ["Great Enclosure", "Stonehenge", "Pyramids", "Colosseum"],
            0,
            "IGreat Enclosure ngesinye sezakhiwo ezaziwayo eGreat Zimbabwe.",
        ),
        (
            "IZimbabwe Birds zabazwa ngani?",
            ["Steel", "Steatite kumbe soapstone", "Glass", "Bronze"],
            1,
            "Zabazwa nge-steatite kumbe soapstone.",
        ),
        (
            "IKhami yayiyinhloko-dolobha yobukhosi bani?",
            ["Torwa", "Roman", "Ottoman", "Mughal"],
            0,
            "IKhami yayiyinhloko-dolobha yeTorwa dynasty.",
        ),
        (
            "Yini edume kakhulu ngezakhiwo zeKhami?",
            ["Amathala amatshe", "Glass towers", "Steel bridges", "Brick domes"],
            0,
            "IKhami idume ngamathala, retaining walls lemihlobiso yamatshe.",
        ),
        (
            "Kumele wenzeni eduze kwemidwebo yasendulo?",
            ["Uyithinte", "Uyimanzise", "Ungayithinti", "Uyilandele"],
            2,
            "Imidwebo yamadwala kumele ingathintwa.",
        ),
        (
            "Yiziphi indawo ezimbili ezilobufakazi bokuhweba kwamabanga amade?",
            ["Great Zimbabwe leKhami", "Matobo leMana Pools", "Matobo kuphela", "Azikho"],
            0,
            "IGreat Zimbabwe leKhami zilobufakazi bokuhweba kwamabanga amade.",
        ),
        (
            "Yiphi inkulumo elungileyo?",
            [
                "Zonke indawo ziyafana",
                "Great Zimbabwe idume ngezakhiwo ezinkulu, Khami ngamathala, Matobo ngemidwebo yamadwala",
                "Azikho ezilamatshe",
                "Zonke zakhiwa ngekhulu lama-20",
            ],
            1,
            "Indawo ngayinye imele ingxenye ehlukileyo yamasiko eZimbabwe.",
        ),
    ],
    "Shona": [
        (
            "Ndeipi nzvimbo inonyanya kuzivikanwa nerock art?",
            ["Great Zimbabwe", "Matobo Hills", "Khami Ruins", "Victoria Falls"],
            1,
            "Matobo Hills inozivikanwa zvikuru nerock art.",
        ),
        (
            "Rock art yeMatobo ine makore angangoita mangani kana kupfuura?",
            ["100", "500", "13,000", "1,000"],
            2,
            "Rock art yeMatobo ine makore anosvika 13,000 kana kupfuura.",
        ),
        (
            "Great Zimbabwe yakavakwa zvikuru panguva ipi?",
            ["1100–1450 AD", "1700–1850 AD", "1900–1950 AD", "500–700 AD"],
            0,
            "Great Zimbabwe yakavakwa zvikuru pakati pa1100 na1450 AD.",
        ),
        (
            "Ndechipi chivakwa chiri paGreat Zimbabwe?",
            ["Great Enclosure", "Stonehenge", "Pyramids", "Colosseum"],
            0,
            "Great Enclosure ndechimwe chezvivakwa zvikuru paGreat Zimbabwe.",
        ),
        (
            "Zimbabwe Birds dzakavezwa nechii?",
            ["Steel", "Steatite kana soapstone", "Glass", "Bronze"],
            1,
            "Zimbabwe Birds dzakavezwa nesteatite kana soapstone.",
        ),
        (
            "Khami yaiva capital yedzinza ripi?",
            ["Torwa", "Roman", "Ottoman", "Mughal"],
            0,
            "Khami yaiva capital yeTorwa dynasty.",
        ),
        (
            "Chii chinonyanya kuzivikanwa paKhami?",
            ["Stone-faced terraces", "Glass towers", "Steel bridges", "Brick domes"],
            0,
            "Khami inozivikanwa nema terraces, retaining walls nedecorative stonework.",
        ),
        (
            "Mushanyi anofanira kuita sei pedyo nerock art?",
            ["Kuibata", "Kuinyorovesa", "Kusabata", "Ku trace"],
            2,
            "Rock art haifaniri kubatwa kana kunyoroveswa.",
        ),
        (
            "Ndedzipi nzvimbo mbiri dzine humbowo hwelong-distance trade?",
            ["Great Zimbabwe neKhami", "Matobo neMana Pools", "Matobo chete", "Hapana"],
            0,
            "Great Zimbabwe neKhami zvose zvine humbowo hwelong-distance trade.",
        ),
        (
            "Ndeipi tsananguro yakarurama?",
            [
                "Nzvimbo nhatu dzakafanana",
                "Great Zimbabwe ine monumental stone architecture, Khami ine terraces, Matobo ine rock art uye sacred landscape",
                "Hadzina stone architecture",
                "Dzese dzakavakwa mu20th century",
            ],
            1,
            "Nzvimbo imwe neimwe inomiririra chikamu chakasiyana chenhaka yeZimbabwe.",
        ),
    ],
}


# ============================================================
# ON-SITE IMAGE EXPLORER + LOCAL PRONUNCIATION GUIDES
# ============================================================

PRONUNCIATION = {
    "matobo": {
        "English": ("Matobo", "ma-TO-bo", "Keep the vowels clear. The middle 'to' is closer to 'taw' than the English word 'toe'."),
        "isiNdebele": ("Matobo", "ma-TO-bo", "Biza onkamisa ngokucacileyo; ungayenzi izwakale njenge-English 'toe'."),
        "Shona": ("Matobo", "ma-TO-bo", "Taura mavhawero akajeka; 'to' haisi English 'toe'."),
    },
    "great": {
        "English": ("Zimbabwe", "zi-MBA-bwe", "Say the syllables cleanly: zi • mba • bwe. Avoid stretching the last syllable into an English 'way'."),
        "isiNdebele": ("Zimbabwe", "zi-MBA-bwe", "Biza izigaba ngokucacileyo: zi • mba • bwe. Ungaluli u-'bwe' ngendlela yesiNgisi."),
        "Shona": ("Zimbabwe", "zi-MBA-bwe", "Taura zvikamu zvakajeka: zi • mba • bwe. Usashandure 'bwe' kuita English 'way'."),
    },
    "khami": {
        "English": ("Khami", "KHA-mi", "The 'kh' begins with a firm, slightly breathy k sound; keep the final 'mi' short and clear."),
        "isiNdebele": ("Khami", "KHA-mi", "U-'kh' uqala ngo-k ophefumulayo kancane; u-'mi' makabe mfutshane futhi acace."),
        "Shona": ("Khami", "KHA-mi", "'Kh' inotanga nek yakasimba ine mhepo shoma; 'mi' ipfupi uye yakajeka."),
    },
}

PROTECTION_IMAGES = {
    "matobo": [
        {
            "url": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Fondazione_Passar%C3%A9_V40_203.jpg",
            "title": "Rock art at Nswatugi Cave",
            "focus": "PROTECT: painted rock surface",
            "note": "Look closely at the painted animal figures. These pigments are fragile: touching, wetting, rubbing or tracing can permanently damage the art.",
        },
        {
            "url": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Intunjambili_Cave%2C_Matobo.jpg",
            "title": "Sacred cave landscape",
            "focus": "PROTECT: cave surface and sacred setting",
            "note": "The cave setting itself needs care. Visitors should avoid graffiti, smoke, scraping rock surfaces or disturbing culturally sensitive areas.",
        },
    ],
    "great": [
        {
            "url": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Wall_of_the_great_enclosure%2C_Great_Zimbabwe.JPG",
            "title": "Wall of the Great Enclosure",
            "focus": "PROTECT: dry-stone wall face and wall top",
            "note": "The carefully fitted stones rely on balance and original construction. Climbing, sitting on wall tops or pulling loose stones can accelerate collapse.",
        },
        {
            "url": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Zimbabwe_wall.jpg",
            "title": "Ancient circumferential wall",
            "focus": "PROTECT: joints, edges and loose masonry",
            "note": "Notice the exposed edges and joints. Visitors should keep off the masonry and never move stones, even when a stone appears loose.",
        },
    ],
    "khami": [
        {
            "url": "https://commons.wikimedia.org/wiki/Special:Redirect/file/ZW_Khami_Ruins.JPG",
            "title": "Khami terrace walls and passage",
            "focus": "PROTECT: terrace retaining walls",
            "note": "Khami's terraces are both archaeological structures and retaining walls. Leaning, climbing or stepping on their edges can disturb fragile masonry.",
        },
        {
            "url": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Khami_ruins_%28ZW%29.jpg",
            "title": "Khami stone-built remains",
            "focus": "PROTECT: surviving stonework",
            "note": "The surviving walls preserve construction patterns and archaeological evidence. Stones, pottery and other material should remain exactly where they are found.",
        },
    ],
}


# ============================================================
# NAVIGATION HELPERS
# ============================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def reset_quiz():
    st.session_state.quiz_index = 0
    st.session_state.quiz_score = 0
    st.session_state.quiz_points = 0
    st.session_state.quiz_answered = False
    st.session_state.quiz_choice = None
    st.session_state.quiz_finished = False


def cultural_strip():
    html('<div class="cultural-strip"></div>')


# ============================================================
# HERITAGE ASSISTANT
# ============================================================

def normalise(question):
    q = question.lower().strip()
    q = re.sub(r"[^a-z0-9\s\-]", " ", q)
    return re.sub(r"\s+", " ", q).strip()


def assistant_answer(question, lang):
    q = normalise(question)

    answers = {
        "English": {
            "great_age": (
                "Great Zimbabwe was not built in one single year. "
                "It was built principally between about 1100 and 1450 AD. "
                "The Great Enclosure dates mainly to the 14th century."
            ),
            "great_builder": (
                "Great Zimbabwe was built by the ancestors of Shona-speaking communities. "
                "It became the centre of a major African state."
            ),
            "great_population": (
                "At its height in the 14th century, Great Zimbabwe supported a population of more than 10,000 people."
            ),
            "great_arch": (
                "Great Zimbabwe's best-known features include the Hill Ruins, Great Enclosure, Conical Tower, Valley Ruins "
                "and highly skilled dry-stone masonry built without mortar."
            ),
            "great_birds": (
                "The Zimbabwe Birds are carved steatite, or soapstone, sculptures associated with Great Zimbabwe. "
                "They later became important national symbols."
            ),
            "great_trade": (
                "Great Zimbabwe participated in long-distance trade. Archaeological finds such as imported ceramics and glass beads "
                "show connections with wider regional and Indian Ocean trade networks."
            ),
            "khami_age": (
                "Khami does not have one exact construction year. It developed mainly between the 15th and 17th centuries "
                "and became the capital of the Torwa dynasty after the decline of Great Zimbabwe."
            ),
            "khami_builder": (
                "Khami was developed under the Torwa dynasty. Its builders continued Zimbabwe's dry-stone architectural tradition "
                "while developing distinctive terraces and decorative walls."
            ),
            "khami_arch": (
                "Khami is especially famous for stone-faced platforms and terraces, retaining or revetment walls, "
                "and decorative chevron and chequered stone patterns."
            ),
            "khami_trade": (
                "Khami was an important commercial centre. Imported objects show links to wider long-distance trade networks."
            ),
            "khami_location": "Khami Ruins is about 22 kilometres west of Bulawayo.",
            "matobo_age": (
                "Matobo has an exceptionally deep human history. The surviving rock-art tradition dates back at least 13,000 years."
            ),
            "matobo_art": (
                "Matobo Hills has one of the highest concentrations of rock art in southern Africa. "
                "The paintings provide important evidence about Stone Age societies and beliefs."
            ),
            "matobo_spiritual": (
                "Matobo is a living spiritual landscape. Sacred shrines continue to be used, and the Mwari religious tradition "
                "has a strong association with the hills."
            ),
            "matobo_location": "The Matobo Hills World Heritage landscape lies about 35 kilometres south of Bulawayo.",
            "unesco": (
                "Great Zimbabwe and Khami Ruins were inscribed on the UNESCO World Heritage List in 1986. "
                "Matobo Hills was inscribed in 2003."
            ),
            "compare": (
                "Great Zimbabwe is best known for monumental dry-stone architecture and the Great Enclosure. "
                "Khami represents a later stone-building tradition characterised by terraces and decorative retaining walls. "
                "Matobo is different because its importance centres on granite landscapes, ancient rock art and living sacred traditions."
            ),
            "protect": (
                "Visitors should not touch rock paintings, climb ancient walls, remove stones or artefacts, "
                "write on heritage surfaces or leave litter."
            ),
            "fallback": (
                "I can help with Matobo Hills, Great Zimbabwe and Khami Ruins. "
                "Ask about dates, age, builders, architecture, rock art, trade, UNESCO or heritage protection."
            ),
        },
        "isiNdebele": {
            "great_age": "IGreat Zimbabwe yakhiwa ikakhulu phakathi kuka-1100 lo-1450 AD. IGreat Enclosure yakhiwa kakhulu ngekhulu le-14.",
            "great_builder": "IGreat Zimbabwe yakhiwa ngabokhokho bemiphakathi ekhuluma isiShona futhi yaba yisikhungo sombuso omkhulu wase-Afrika.",
            "great_population": "Ngekhulu le-14 abantu baseGreat Zimbabwe babedlula 10,000.",
            "great_arch": "IGreat Zimbabwe idume ngeHill Ruins, Great Enclosure, Conical Tower, Valley Ruins lemiduli yamatshe eyakhiwa ngaphandle kodaka.",
            "great_birds": "IZimbabwe Birds yizithombe zezinyoni ezabazwa nge-steatite kumbe soapstone futhi zaba luphawu oluqakathekileyo lwelizwe.",
            "great_trade": "IGreat Zimbabwe yayihweba kwamabanga amade. Izinto ezivela kwamanye amazwe zibonisa ukuxhumana leIndian Ocean trade networks.",
            "khami_age": "IKhami yathuthuka kakhulu phakathi kwekhulu le-15 lele-17 futhi yaba yinhloko-dolobha yeTorwa dynasty.",
            "khami_builder": "IKhami yathuthukiswa ngaphansi kweTorwa dynasty. Abakhi bayo benza amathala lemiduli ehlotshisiweyo.",
            "khami_arch": "IKhami idume ngamathala amatshe, retaining walls kanye lemihlobiso ye-chevron le-chequered.",
            "khami_trade": "IKhami yayiyisikhungo esibalulekileyo sokuhweba kwamabanga amade.",
            "khami_location": "IKhami Ruins icishe ibe 22 km entshonalanga yeBulawayo.",
            "matobo_age": "Imidwebo yaseMatobo ihlehlela emuva okungenani iminyaka engu-13,000.",
            "matobo_art": "IMatobo ilenani elikhulu kakhulu lemidwebo yamadwala eningizimu ye-Afrika.",
            "matobo_spiritual": "IMatobo yindawo yomoya ephilayo. Izindawo ezingcwele zisasebenza futhi isiko likaMwari lixhumene kakhulu lamagquma.",
            "matobo_location": "IMatobo Hills icishe ibe 35 km eningizimu yeBulawayo.",
            "unesco": "IGreat Zimbabwe leKhami Ruins zafakwa ku-UNESCO ngo-1986. IMatobo Hills yafakwa ngo-2003.",
            "compare": "IGreat Zimbabwe idume ngezakhiwo ezinkulu zamatshe, iKhami ngamathala lemiduli ehlotshisiweyo, kuthi iMatobo idume ngemidwebo yamadwala lamasiko angcwele.",
            "protect": "Ungathinti imidwebo yamadwala, ungakhweli imiduli yasendulo, ungasusi izinto zemivubukulo futhi ungabhali ezindaweni zamagugu.",
            "fallback": "Ngingakunceda ngeMatobo Hills, Great Zimbabwe leKhami Ruins. Buza ngomlando, iminyaka, abakhi, izakhiwo, ukuhweba loba i-UNESCO.",
        },
        "Shona": {
            "great_age": "Great Zimbabwe yakavakwa zvikuru pakati pa1100 na1450 AD. Great Enclosure inonyanya kubva muzana remakore rechi14.",
            "great_builder": "Great Zimbabwe yakavakwa nemadzitateguru evanhu vanotaura chiShona uye yakava centre yehurumende ine simba.",
            "great_population": "Muzana remakore rechi14 vanhu vaigara paGreat Zimbabwe vaipfuura 10,000.",
            "great_arch": "Great Zimbabwe inozivikanwa neHill Ruins, Great Enclosure, Conical Tower, Valley Ruins uye dry-stone masonry.",
            "great_birds": "Zimbabwe Birds zvivezwa zveshiri zvakagadzirwa nesteatite kana soapstone uye zvakazova zviratidzo zvakakosha zveZimbabwe.",
            "great_trade": "Great Zimbabwe yakabatana nelong-distance trade. Imported ceramics neglass beads zvinoratidza hukama neIndian Ocean trade networks.",
            "khami_age": "Khami yakanyanya kukura pakati pezana remakore rechi15 nerechi17 uye yakava capital yeTorwa dynasty.",
            "khami_builder": "Khami yakavakwa pasi peTorwa dynasty. Vakavaka terraces, retaining walls uye decorative dry-stone walls.",
            "khami_arch": "Khami inozivikanwa nema stone-faced terraces, retaining walls uye chevron nechequered patterns.",
            "khami_trade": "Khami yaiva nzvimbo yakakosha yelong-distance trade.",
            "khami_location": "Khami Ruins iri anenge 22 km kumadokero kweBulawayo.",
            "matobo_age": "Rock art yeMatobo ine makore anosvika 13,000 kana kupfuura.",
            "matobo_art": "Matobo ine imwe yerock art yakawanda zvikuru kumaodzanyemba kweAfrica.",
            "matobo_spiritual": "Matobo inzvimbo yemweya ichiri kurarama. Nzvimbo dzinoyera dzichiri kushandiswa uye Mwari tradition ine hukama nemakomo.",
            "matobo_location": "Matobo Hills iri anenge 35 km kumaodzanyemba kweBulawayo.",
            "unesco": "Great Zimbabwe neKhami Ruins zvakanyorwa neUNESCO muna 1986. Matobo Hills yakanyorwa muna 2003.",
            "compare": "Great Zimbabwe inozivikanwa nemonumental stone architecture, Khami nema terraces, uye Matobo nerock art nesacred landscape.",
            "protect": "Usabata rock art, usakwira pamadziro ekare, usabvisa artefacts kana matombo uye usanyora panzvimbo dzenhaka.",
            "fallback": "Ndinogona kukubatsira nezveMatobo Hills, Great Zimbabwe neKhami Ruins. Bvunza nezvemakore, vakavaka, architecture, rock art, trade kana UNESCO.",
        },
    }

    R = answers[lang]

    if any(x in q for x in ["compare", "difference", "different", "qhathanisa", "umehluko", "enzanisa", "musiyano"]):
        return R["compare"]

    if any(x in q for x in ["protect", "preserve", "conservation", "damage", "respect", "vikela", "chengetedza"]):
        return R["protect"]

    if "unesco" in q or "world heritage" in q or "inscribed" in q:
        return R["unesco"]

    if "great zimbabwe" in q or "great zim" in q:
        if any(x in q for x in ["when", "what year", "how old", "built", "date", "yakhiwa", "yakavakwa", "riini", "nini"]):
            return R["great_age"]
        if any(x in q for x in ["who", "builder", "builders", "built by", "ngobani", "ndiani", "vakavaka"]):
            return R["great_builder"]
        if any(x in q for x in ["population", "people lived", "inhabitants", "abantu", "vanhu"]):
            return R["great_population"]
        if any(x in q for x in ["bird", "birds", "soapstone", "steatite", "inyoni", "shiri"]):
            return R["great_birds"]
        if any(x in q for x in ["trade", "china", "persia", "commerce", "kutengesa", "ukuhweba"]):
            return R["great_trade"]
        return R["great_arch"]

    if any(x in q for x in ["zimbabwe bird", "zimbabwe birds", "soapstone bird"]):
        return R["great_birds"]

    if "khami" in q or "torwa" in q:
        if any(x in q for x in ["how old", "what year", "when", "built", "date", "madala", "makore"]):
            return R["khami_age"]
        if any(x in q for x in ["who", "builder", "builders", "torwa", "ngobani", "ndiani"]):
            return R["khami_builder"]
        if any(x in q for x in ["terrace", "terraces", "wall", "walls", "architecture", "chevron", "chequered", "amathala"]):
            return R["khami_arch"]
        if any(x in q for x in ["trade", "china", "europe", "commerce", "ukuhweba"]):
            return R["khami_trade"]
        if any(x in q for x in ["where", "location", "distance", "kuphi", "kupi"]):
            return R["khami_location"]
        return R["khami_arch"]

    if "matobo" in q or "rock art" in q:
        if any(x in q for x in ["how old", "age", "years old", "madala", "makore"]):
            return R["matobo_age"]
        if any(x in q for x in ["painting", "paintings", "drawings", "rock art", "imidwebo", "mifananidzo"]):
            return R["matobo_art"]
        if any(x in q for x in ["spiritual", "sacred", "mwari", "religion", "shrine", "shrines"]):
            return R["matobo_spiritual"]
        if any(x in q for x in ["where", "location", "distance", "kuphi", "kupi"]):
            return R["matobo_location"]
        return R["matobo_art"]

    return R["fallback"]


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    html(
        f"""
        <div class="sidebar-brand">
            <div class="sidebar-brand-title">🗿 ROBO GUIDE</div>
            <div class="sidebar-brand-sub">{escape(SLOGAN)}</div>
        </div>
        """
    )

    languages = ["English", "isiNdebele", "Shona"]

    selected_language = st.selectbox(
        T("language"),
        languages,
        index=languages.index(st.session_state.lang),
        key="main_language_selector",
    )

    if selected_language != st.session_state.lang:
        st.session_state.lang = selected_language
        reset_quiz()
        st.session_state.chat = []
        st.rerun()

    html('<div class="sidebar-section">Heritage Menu</div>')

    navigation = [
        ("🏠", T("home"), "home"),
        ("⛰️", T("matobo"), "matobo"),
        ("🏛️", T("great"), "great"),
        ("🧱", T("khami"), "khami"),
        ("🏆", T("quiz"), "quiz"),
        ("💬", T("assistant"), "assistant"),
    ]

    for index, (icon, label, page_name) in enumerate(navigation):
        prefix = "◆" if st.session_state.page == page_name else ""
        if st.button(
            f"{prefix} {icon}  {label}",
            key=f"sidebar_navigation_{page_name}_{index}",
            use_container_width=True,
        ):
            go(page_name)


# ============================================================
# HOME
# ============================================================

def render_home():
    cultural_strip()

    html(
        f"""
        <div class="hero">
            <h1>ROBO GUIDE</h1>
            <h3>{escape(T('hero_sub'))}</h3>
            <p>{escape(T('hero_text'))}</p>
            <div class="slogan">{escape(SLOGAN)}</div>
        </div>
        """
    )

    st.markdown(f"## {T('choose')}")

    columns = st.columns(3)

    for column, site_key in zip(columns, ["matobo", "great", "khami"]):
        data = SITES[site_key][st.session_state.lang]

        with column:
            html(
                f"""
                <div class="site-card">
                    <div class="site-icon">{SITES[site_key]['emoji']}</div>
                    <h3>{escape(data['name'])}</h3>
                    <p>{escape(data['subtitle'])}</p>
                    <span class="badge">UNESCO {escape(data['inscribed'])}</span>
                    <span class="badge">{escape(data['criteria'])}</span>
                </div>
                """
            )

            if st.button(
                f"{T('explore_site')} {data['name']}",
                key=f"home_site_button_{site_key}",
                use_container_width=True,
            ):
                go(site_key)

    st.markdown("## Discover • Understand • Respect")

    c1, c2, c3 = st.columns(3)

    with c1:
        html(
            """
            <div class="info-card">
                <h3>📜 Discover</h3>
                <p>Explore the people, stories and places behind Zimbabwe's cultural heritage.</p>
            </div>
            """
        )

    with c2:
        html(
            """
            <div class="info-card">
                <h3>🧠 Understand</h3>
                <p>Learn about history, archaeology, architecture, rock art and trade.</p>
            </div>
            """
        )

    with c3:
        html(
            """
            <div class="info-card">
                <h3>🛡️ Respect</h3>
                <p>Learn how visitors can help preserve irreplaceable heritage for future generations.</p>
            </div>
            """
        )

    html(
        """
        <div class="source-note">
            ROBO GUIDE heritage information is based on the official UNESCO World Heritage descriptions
            for Matobo Hills, Great Zimbabwe National Monument and Khami Ruins National Monument.
        </div>
        """
    )


# ============================================================
# SITE PAGE
# ============================================================

def render_site(site_key):
    cultural_strip()

    data = SITES[site_key][st.session_state.lang]

    html(
        f"""
        <div class="hero">
            <h1 style="font-size:3.2rem;">{SITES[site_key]['emoji']} {escape(data['name'])}</h1>
            <h3>{escape(data['subtitle'])}</h3>
            <div class="slogan">{escape(SLOGAN)}</div>
        </div>
        """
    )

    pronounce_word, pronounce_guide, pronounce_note = PRONUNCIATION[site_key][st.session_state.lang]

    with st.expander("🔊 Local pronunciation guide", expanded=False):
        html(
            f"""
            <div class="pronounce-card">
                <div class="pronounce-word">{escape(pronounce_word)}</div>
                <div class="pronounce-guide">{escape(pronounce_guide)}</div>
                <div class="pronounce-note">{escape(pronounce_note)}</div>
            </div>
            """
        )
        st.caption("The previous synthetic voice has been removed because browser text-to-speech can fall back to an English voice and distort Zimbabwean names.")

    c1, c2, c3 = st.columns(3)

    with c1:
        html(
            f"""
            <div class="stat-card">
                <div class="stat-label">{escape(T('location'))}</div>
                <div class="stat-value">{escape(data['location'])}</div>
            </div>
            """
        )

    with c2:
        html(
            f"""
            <div class="stat-card">
                <div class="stat-label">{escape(T('inscribed'))}</div>
                <div class="stat-value">{escape(data['inscribed'])}</div>
            </div>
            """
        )

    with c3:
        html(
            f"""
            <div class="stat-card">
                <div class="stat-label">{escape(T('criteria'))}</div>
                <div class="stat-value">{escape(data['criteria'])}</div>
            </div>
            """
        )

    st.markdown(f"## {T('history')}")
    html(f'<div class="info-card"><p>{escape(data["history"])}</p></div>')

    st.markdown(f"## {T('culture')}")
    html(f'<div class="info-card"><p>{escape(data["culture"])}</p></div>')

    st.markdown(f"## {T('features')}")
    feature_columns = st.columns(2)

    for index, feature in enumerate(data["features"]):
        with feature_columns[index % 2]:
            html(
                f"""
                <div class="fact-card">
                    <h4>◆ Heritage Feature</h4>
                    <p>{escape(feature)}</p>
                </div>
                """
            )

    st.markdown("## 📷 Protection Image Explorer")
    st.caption("These pictures focus on the parts of each heritage site that visitors need to protect most carefully.")

    image_columns = st.columns(2)
    for image_index, image_data in enumerate(PROTECTION_IMAGES[site_key]):
        with image_columns[image_index % 2]:
            st.image(image_data["url"], caption=image_data["title"], use_container_width=True)
            html(
                f"""
                <div class="image-explorer-card">
                    <div class="protect-focus">{escape(image_data['focus'])}</div>
                    <div class="image-note">{escape(image_data['note'])}</div>
                </div>
                """
            )

    st.markdown(f"## {T('unesco')}")
    html(
        f"""
        <div class="unesco-card">
            <strong>UNESCO World Heritage</strong><br><br>
            {escape(data['unesco'])}
        </div>
        """
    )

    st.markdown(f"## {T('protect')}")
    protection_columns = st.columns(2)

    for index, item in enumerate(data["protect"]):
        with protection_columns[index % 2]:
            html(
                f"""
                <div class="fact-card">
                    <h4>🛡️ Respect the Heritage</h4>
                    <p>{escape(item)}</p>
                </div>
                """
            )

    st.markdown(f"## {T('facts')}")
    fact_columns = st.columns(3)

    for index, fact in enumerate(data["facts"]):
        with fact_columns[index % 3]:
            html(
                f"""
                <div class="fact-card">
                    <h4>💡 Did You Know?</h4>
                    <p>{escape(fact)}</p>
                </div>
                """
            )

    st.markdown(f"## {T('significance')}")
    html(f'<div class="unesco-card">{escape(data["significance"])}</div>')

    left, right = st.columns(2)

    with left:
        if st.button(
            "🏆 " + T("quiz"),
            key=f"site_quiz_button_{site_key}",
            use_container_width=True,
        ):
            go("quiz")

    with right:
        if st.button(
            "💬 " + T("assistant"),
            key=f"site_assistant_button_{site_key}",
            use_container_width=True,
        ):
            go("assistant")


# ============================================================
# QUIZ PAGE
# ============================================================

def render_quiz():
    cultural_strip()

    html(
        f"""
        <div class="hero">
            <h1 style="font-size:3rem;">🏆 {escape(T('quiz_title'))}</h1>
            <p>{escape(T('quiz_intro'))}</p>
            <div class="slogan">{escape(SLOGAN)}</div>
        </div>
        """
    )

    questions = QUIZ[st.session_state.lang]

    if st.session_state.quiz_finished:
        total = len(questions)
        percentage = round((st.session_state.quiz_score / total) * 100)
        achievement = T("guardian") if percentage >= 80 else T("guide")

        c1, c2, c3 = st.columns(3)
        c1.metric(T("score"), f"{st.session_state.quiz_score}/{total}")
        c2.metric(T("points"), st.session_state.quiz_points)
        c3.metric(T("achievement"), achievement)

        if percentage >= 80:
            st.success(f"🏅 {achievement} — {percentage}%")
            st.balloons()
        else:
            st.info(f"📜 {achievement} — {percentage}%")

        if st.button(
            T("restart"),
            key="quiz_restart_button",
            use_container_width=True,
        ):
            reset_quiz()
            st.rerun()
        return

    index = st.session_state.quiz_index
    question, options, correct_index, explanation = questions[index]

    st.progress((index + 1) / len(questions))
    st.markdown(f"### {T('question')} {index + 1} / {len(questions)}")

    html(f'<div class="quiz-card"><h3>{escape(question)}</h3></div>')

    selected = st.radio(
        "Answer",
        options,
        index=None,
        key=f"quiz_radio_{st.session_state.lang}_{index}",
        label_visibility="collapsed",
        disabled=st.session_state.quiz_answered,
    )

    if not st.session_state.quiz_answered:
        if st.button(
            T("submit"),
            key=f"quiz_submit_button_{index}",
            use_container_width=True,
        ):
            if selected is None:
                st.warning("Please choose an answer first.")
            else:
                st.session_state.quiz_choice = selected
                st.session_state.quiz_answered = True

                if options.index(selected) == correct_index:
                    st.session_state.quiz_score += 1
                    st.session_state.quiz_points += 100
                else:
                    st.session_state.quiz_points += 20

                st.rerun()
    else:
        chosen_index = options.index(st.session_state.quiz_choice)

        if chosen_index == correct_index:
            st.success(f"✅ {T('correct')} {explanation}")
        else:
            st.error(f"❌ {T('incorrect')} {explanation}")

        score_col, points_col = st.columns(2)
        score_col.metric(T("score"), st.session_state.quiz_score)
        points_col.metric(T("points"), st.session_state.quiz_points)

        if st.button(
            T("next"),
            key=f"quiz_next_button_{index}",
            use_container_width=True,
        ):
            if index + 1 >= len(questions):
                st.session_state.quiz_finished = True
            else:
                st.session_state.quiz_index += 1
                st.session_state.quiz_answered = False
                st.session_state.quiz_choice = None

            st.rerun()


# ============================================================
# ASSISTANT PAGE
# ============================================================

def render_assistant():
    cultural_strip()

    html(
        f"""
        <div class="hero">
            <h1 style="font-size:3rem;">💬 {escape(T('assistant_title'))}</h1>
            <p>{escape(T('assistant_intro'))}</p>
            <div class="slogan">{escape(SLOGAN)}</div>
        </div>
        """
    )

    suggestions = {
        "English": [
            "When was Great Zimbabwe built?",
            "Who built Great Zimbabwe?",
            "How old are the Khami Ruins?",
            "What is special about Khami architecture?",
            "How old is Matobo rock art?",
            "Compare all three heritage sites.",
        ],
        "isiNdebele": [
            "IGreat Zimbabwe yakhiwa nini?",
            "Ngobani abakha iGreat Zimbabwe?",
            "Amanxiwa eKhami madala kangakanani?",
            "Yini ekhethekileyo ngezakhiwo zeKhami?",
            "Imidwebo yaseMatobo midala kangakanani?",
            "Qhathanisa zonke indawo ezintathu.",
        ],
        "Shona": [
            "Great Zimbabwe yakavakwa riini?",
            "Ndiani akavaka Great Zimbabwe?",
            "Khami Ruins ine makore mangani?",
            "Chii chakakosha nearchitecture yeKhami?",
            "Rock art yeMatobo ine makore mangani?",
            "Enzanisa nzvimbo nhatu dzese.",
        ],
    }

    st.markdown(f"### {T('quick')}")
    quick_columns = st.columns(2)

    for index, suggestion in enumerate(suggestions[st.session_state.lang]):
        with quick_columns[index % 2]:
            if st.button(
                suggestion,
                key=f"assistant_suggestion_{st.session_state.lang}_{index}",
                use_container_width=True,
            ):
                answer = assistant_answer(suggestion, st.session_state.lang)
                st.session_state.chat.append((suggestion, answer))
                st.rerun()

    for question, answer in st.session_state.chat:
        html(
            f"""
            <div class="chat-user">
                <strong>You:</strong><br>
                {escape(question)}
            </div>
            """
        )

        html(
            f"""
            <div class="chat-bot">
                <strong>ROBO GUIDE:</strong><br>
                {escape(answer)}
            </div>
            """
        )

    with st.form("heritage_assistant_form", clear_on_submit=True):
        question = st.text_input(
            T("ask"),
            key="heritage_assistant_input",
            placeholder=T("ask"),
        )

        submitted = st.form_submit_button(
            T("send"),
            use_container_width=True,
        )

    if submitted and question.strip():
        clean_question = question.strip()
        answer = assistant_answer(clean_question, st.session_state.lang)
        st.session_state.chat.append((clean_question, answer))
        st.rerun()

    if st.button(
        T("clear"),
        key="assistant_clear_conversation_button",
        use_container_width=True,
    ):
        st.session_state.chat = []
        st.rerun()

    html(
        """
        <div class="source-note">
            ROBO GUIDE uses a built-in heritage knowledge base focused on Matobo Hills,
            Great Zimbabwe and Khami Ruins. No paid AI service is required.
        </div>
        """
    )


# ============================================================
# ROUTER
# ============================================================

current_page = st.session_state.page

if current_page == "home":
    render_home()
elif current_page in {"matobo", "great", "khami"}:
    render_site(current_page)
elif current_page == "quiz":
    render_quiz()
elif current_page == "assistant":
    render_assistant()
else:
    st.session_state.page = "home"
    st.rerun()


# ============================================================
# FOOTER
# ============================================================

html(
    f"""
    <div class="footer">
        <strong>ROBO GUIDE</strong><br>
        {escape(SLOGAN)}<br><br>
        {escape(T('footer'))}
    </div>
    """
)
