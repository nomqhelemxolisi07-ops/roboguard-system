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


def html(content: str):
    st.markdown(textwrap.dedent(content).strip(), unsafe_allow_html=True)


# --------------------------------------------------
# DARK-NEUTRAL HERITAGE THEME
# --------------------------------------------------
st.markdown(
    """
    <style>
    :root {
        --bg: #D8CBB8;
        --bg2: #C8B79F;
        --panel: #BDAA90;
        --panel2: #AD987C;
        --stone: #6E5B48;
        --stone2: #5A493B;
        --stone3: #493B31;
        --clay: #8A5A44;
        --gold: #A67C3B;
        --gold2: #8B6733;
        --olive: #66705A;
        --cream: #F3EADF;
        --ink: #2F2924;
        --muted: #4E453D;
        --border: #8B7863;
    }

    .stApp {
        background: linear-gradient(180deg, var(--bg) 0%, var(--bg2) 100%);
        color: var(--ink);
    }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #625244 0%, #4A3E34 100%);
        border-right: 1px solid #7A6653;
    }

    [data-testid="stSidebar"] * {
        color: #F4ECE2 !important;
    }

    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        background: #6F5C4B;
        color: #F8F1E8 !important;
        border: 1px solid #8E7863;
        border-radius: 12px;
        min-height: 2.8rem;
        font-weight: 700;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background: #7B6652;
        border-color: #B48A4A;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background: #5B4A3C !important;
        border-color: #8D7660 !important;
    }

    .hero {
        background: linear-gradient(135deg, #75604E 0%, #55463A 100%);
        color: #F8F0E6;
        padding: 2rem;
        border-radius: 22px;
        border: 1px solid #8A745E;
        box-shadow: 0 10px 28px rgba(57, 45, 35, 0.18);
        margin-bottom: 1.2rem;
    }

    .hero h1 {
        color: #F5E8D8;
        margin: 0;
        font-size: clamp(2.1rem, 5vw, 4.1rem);
        letter-spacing: 0.03em;
    }

    .hero h3 {
        color: #E2C38A;
        margin: 0.5rem 0 0.4rem 0;
    }

    .hero p {
        color: #F3EADF;
        margin: 0;
        max-width: 900px;
        font-size: 1.03rem;
    }

    .site-card, .info-card, .fact-card, .quiz-card, .assistant-box {
        background: #C9B79F;
        border: 1px solid #8F7B66;
        border-radius: 16px;
        padding: 1.1rem 1.15rem;
        color: #2F2924;
        box-shadow: 0 5px 14px rgba(57, 45, 35, 0.10);
        height: 100%;
    }

    .site-card h3, .info-card h3, .fact-card h4, .quiz-card h3 {
        color: #3A3028;
        margin-top: 0;
    }

    .site-card p, .info-card p, .fact-card p, .assistant-box p {
        color: #40372F;
    }

    .badge {
        display: inline-block;
        background: #8A735C;
        color: #FFF7EB;
        border: 1px solid #6E5B48;
        padding: 0.28rem 0.6rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 800;
        margin-right: 0.35rem;
        margin-top: 0.25rem;
    }

    .gold-strip {
        background: #B79B68;
        color: #2F2924;
        border-left: 6px solid #7D5D2E;
        border-radius: 12px;
        padding: 1rem 1.15rem;
        margin: 0.75rem 0 1rem 0;
        font-weight: 600;
    }

    .chat-user {
        background: #B89B84;
        color: #2D2621;
        border: 1px solid #8E725E;
        border-left: 5px solid #86513D;
        border-radius: 13px;
        padding: 0.9rem 1rem;
        margin: 0.55rem 0;
    }

    .chat-bot {
        background: #C4B28F;
        color: #2D2822;
        border: 1px solid #8C7758;
        border-left: 5px solid #8A6934;
        border-radius: 13px;
        padding: 0.9rem 1rem;
        margin: 0.55rem 0 0.95rem 0;
    }

    .chat-user strong, .chat-bot strong {
        color: #2A241F;
    }

    div[data-testid="stTextInput"] label,
    div[data-testid="stRadio"] label,
    div[data-testid="stMetric"] label,
    .stMarkdown p,
    .stMarkdown li,
    h1, h2, h3, h4, h5, h6 {
        color: #2F2924;
    }

    div[data-testid="stTextInput"] input {
        background: #EEE3D4 !important;
        color: #2E2823 !important;
        border: 1px solid #806D59 !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: #5B5046 !important;
        opacity: 1 !important;
    }

    div[data-baseweb="radio"] {
        color: #2F2924 !important;
    }

    div.stButton > button {
        background: #6C5847;
        color: #F8EFE4;
        border: 1px solid #58483B;
        border-radius: 12px;
        font-weight: 700;
    }

    div.stButton > button:hover {
        background: #7C6550;
        color: #FFF7ED;
        border-color: #8B6733;
    }

    div[data-testid="stFormSubmitButton"] button {
        background: #765E48;
        color: #FAF2E8;
        border: 1px solid #5B493A;
        font-weight: 700;
    }

    div[data-testid="stMetric"] {
        background: #C5B399;
        border: 1px solid #8D7964;
        border-radius: 14px;
        padding: 0.7rem 0.9rem;
    }

    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #3A3028;
    }

    [data-testid="stAlert"] {
        color: #2D2823 !important;
    }

    .footer {
        margin-top: 2rem;
        padding: 1rem;
        border-top: 1px solid #8F7B66;
        text-align: center;
        color: #473D35;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# STATE
# --------------------------------------------------
defaults = {
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

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# --------------------------------------------------
# UI TRANSLATIONS
# --------------------------------------------------
UI = {
    "English": {
        "language": "Language",
        "explore": "Explore ROBO GUIDE",
        "home": "Home",
        "matobo": "Matobo Hills",
        "great": "Great Zimbabwe",
        "khami": "Khami Ruins",
        "quiz": "Heritage Challenge",
        "assistant": "Heritage Assistant",
        "hero_sub": "Discover Zimbabwe's Living Heritage",
        "hero_text": "Explore remarkable places, stories, architecture and traditions through an interactive heritage experience.",
        "choose": "Choose a heritage site",
        "open_site": "Explore site",
        "history": "History",
        "culture": "Culture & People",
        "features": "Major Features",
        "unesco": "UNESCO Information",
        "protect": "How to Protect the Site",
        "facts": "Interesting Facts",
        "significance": "Why It Matters",
        "location": "Location",
        "inscribed": "UNESCO Inscribed",
        "criteria": "Criteria",
        "quiz_title": "Heritage Challenge",
        "quiz_intro": "Test what you know about Matobo Hills, Great Zimbabwe and Khami Ruins.",
        "question": "Question",
        "submit": "Check answer",
        "next": "Next question",
        "restart": "Restart challenge",
        "correct": "Correct!",
        "incorrect": "Not quite.",
        "score": "Score",
        "points": "Heritage Points",
        "achievement": "Achievement",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Heritage Assistant",
        "assistant_intro": "Ask about history, builders, rock art, architecture, trade, UNESCO, conservation or comparisons.",
        "ask": "Ask a heritage question",
        "send": "Ask ROBO GUIDE",
        "clear": "Clear conversation",
        "footer": "ROBO GUIDE • Zimbabwe Heritage Explorer • WRO 2026",
    },

    "isiNdebele": {
        "language": "Ulimi",
        "explore": "Hlola i-ROBO GUIDE",
        "home": "Ikhaya",
        "matobo": "Amagquma eMatobo",
        "great": "Great Zimbabwe",
        "khami": "Amanxiwa eKhami",
        "quiz": "Umncintiswano Wamagugu",
        "assistant": "Umsizi Wamagugu",
        "hero_sub": "Thola Amagugu Aphilayo eZimbabwe",
        "hero_text": "Hlola izindawo, izindaba, izakhiwo lamasiko ngendlela ephendulanayo.",
        "choose": "Khetha indawo yamagugu",
        "open_site": "Hlola indawo",
        "history": "Umlando",
        "culture": "Amasiko Labantu",
        "features": "Izinto Ezisemqoka",
        "unesco": "Ulwazi lwe-UNESCO",
        "protect": "Indlela Yokuvikela Indawo",
        "facts": "Amaqiniso Athakazelisayo",
        "significance": "Kungani Ibalulekile",
        "location": "Indawo",
        "inscribed": "Yangeniswa ku-UNESCO",
        "criteria": "Imigomo",
        "quiz_title": "Umncintiswano Wamagugu",
        "quiz_intro": "Hlola ulwazi lwakho ngeMatobo Hills, Great Zimbabwe leKhami Ruins.",
        "question": "Umbuzo",
        "submit": "Hlola impendulo",
        "next": "Umbuzo olandelayo",
        "restart": "Qalisa kutsha",
        "correct": "Kulungile!",
        "incorrect": "Akukabi yikho.",
        "score": "Amaphuzu",
        "points": "Heritage Points",
        "achievement": "Impumelelo",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Umsizi Wamagugu",
        "assistant_intro": "Buza ngomlando, abakhi, imidwebo yamadwala, izakhiwo, ukuhweba, UNESCO loba ukuvikelwa.",
        "ask": "Buza umbuzo wamagugu",
        "send": "Buza i-ROBO GUIDE",
        "clear": "Sula ingxoxo",
        "footer": "ROBO GUIDE • Zimbabwe Heritage Explorer • WRO 2026",
    },

    "Shona": {
        "language": "Mutauro",
        "explore": "Ongorora ROBO GUIDE",
        "home": "Musha",
        "matobo": "Matobo Hills",
        "great": "Great Zimbabwe",
        "khami": "Khami Ruins",
        "quiz": "Dambudziko reNhaka",
        "assistant": "Mubatsiri weNhaka",
        "hero_sub": "Ziva Nhaka Mhenyu yeZimbabwe",
        "hero_text": "Ongorora nzvimbo, nyaya, zvivakwa netsika kuburikidza nechiitiko chinodyidzana.",
        "choose": "Sarudza nzvimbo yenhaka",
        "open_site": "Ongorora nzvimbo",
        "history": "Nhoroondo",
        "culture": "Tsika neVanhu",
        "features": "Zvinhu Zvikuru",
        "unesco": "Ruzivo rweUNESCO",
        "protect": "Kuchengetedza Nzvimbo",
        "facts": "Zvinonakidza Kuziva",
        "significance": "Kukosha Kwayo",
        "location": "Nzvimbo",
        "inscribed": "Yakanyorwa neUNESCO",
        "criteria": "Maitiro",
        "quiz_title": "Dambudziko reNhaka",
        "quiz_intro": "Edza ruzivo rwako pamusoro peMatobo Hills, Great Zimbabwe neKhami Ruins.",
        "question": "Mubvunzo",
        "submit": "Tarisa mhinduro",
        "next": "Mubvunzo unotevera",
        "restart": "Tangazve",
        "correct": "Wagona!",
        "incorrect": "Hausati warurama.",
        "score": "Zvawabudirira",
        "points": "Heritage Points",
        "achievement": "Kubudirira",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Mubatsiri weNhaka",
        "assistant_intro": "Bvunza nezvenhoroondo, vakavaka, rock art, zvivakwa, kutengeserana, UNESCO kana kuchengetedza.",
        "ask": "Bvunza mubvunzo wenhaka",
        "send": "Bvunza ROBO GUIDE",
        "clear": "Bvisa hurukuro",
        "footer": "ROBO GUIDE • Zimbabwe Heritage Explorer • WRO 2026",
    },
}


def T(k):
    return UI[st.session_state.lang][k]


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


# --------------------------------------------------
# SITE DATA
# --------------------------------------------------
SITES = {
    "matobo": {
        "emoji": "⛰️",

        "English": {
            "name": "Matobo Hills",
            "subtitle": "Granite landscapes, sacred traditions and ancient rock art",
            "location": "Matabeleland South, near Bulawayo",
            "inscribed": "2003",
            "criteria": "(iii), (v), (vi)",
            "history":
                "Matobo Hills has been used by communities for thousands of years. "
                "Its granite landscape preserves archaeological evidence, caves and rock shelters "
                "with prehistoric paintings. It also has strong connections to later Ndebele history "
                "and remains culturally important today.",
            "culture":
                "Matobo is a living cultural landscape. Local communities maintain spiritual "
                "traditions associated with sacred places, rain-making and the Mwari belief system.",
            "features": [
                "Granite kopjes and balancing rock formations.",
                "Caves and rock shelters with prehistoric paintings.",
                "One of southern Africa's richest concentrations of rock art.",
                "Sacred places linked to living spiritual traditions.",
                "Archaeological remains showing long human occupation.",
            ],
            "unesco":
                "UNESCO inscribed Matobo Hills in 2003 as a cultural landscape because of its "
                "rock art, archaeology, long interaction between people and landscape, and continuing "
                "spiritual importance.",
            "protection": [
                "Do not touch, trace, wet or rub rock paintings.",
                "Do not write on rocks or remove stones or artefacts.",
                "Use marked paths and follow site guidance.",
                "Treat sacred places quietly and respectfully.",
            ],
            "facts": [
                "Some rock shelters contain images of people and animals painted by hunter-gatherer communities.",
                "The landscape is famous for dramatic rounded granite boulders.",
                "Matobo combines archaeology, art, geology and living tradition.",
            ],
            "significance":
                "Matobo Hills links natural geology, ancient art, archaeology, spirituality and "
                "living community traditions in one cultural landscape.",
        },

        "isiNdebele": {
            "name": "Amagquma eMatobo",
            "subtitle": "Amadwala egranite, amasiko angcwele lemidwebo yasendulo",
            "location": "Matabeleland South, eduze leBulawayo",
            "inscribed": "2003",
            "criteria": "(iii), (v), (vi)",
            "history":
                "Amagquma eMatobo asetshenziswa ngabantu okwezinkulungwane zeminyaka. "
                "Kule ndawo kukhona imihume, imidwebo yamadwala kanye lobufakazi bemivubukulo.",
            "culture":
                "IMatobo yindawo yesiko eliphilayo, ehlobene lezindawo ezingcwele, "
                "ukunxusa izulu kanye lenkolo kaMwari.",
            "features": [
                "Amagquma egranite lamadwala abhalansile.",
                "Imihume lemidwebo yasendulo.",
                "Imidwebo yamadwala eminengi kakhulu.",
                "Izindawo ezingcwele.",
                "Ubufakazi bokuhlala kwabantu isikhathi eside.",
            ],
            "unesco":
                "I-UNESCO yafaka iMatobo Hills ohlwini ngo-2003 ngenxa yemidwebo yamadwala, "
                "imivubukulo kanye lamasiko omoya aqhubekayo.",
            "protection": [
                "Ungathinti imidwebo yamadwala.",
                "Ungabhali emadwaleni kumbe ususe izinto zakudala.",
                "Sebenzisa imizila ebekiweyo.",
                "Hlonipha izindawo ezingcwele.",
            ],
            "facts": [
                "Eminye imihume ilondoloza imidwebo yabantu lezinyamazana.",
                "IMatobo idume ngamatshe amakhulu egranite.",
                "Iyindawo yemivubukulo kanye lamasiko aphilayo.",
            ],
            "significance":
                "IMatobo ihlanganisa ubunjalo bomhlaba, ubuciko basendulo, "
                "imivubukulo kanye lamasiko aphilayo.",
        },

        "Shona": {
            "name": "Matobo Hills",
            "subtitle": "Matombo egranite, tsika dzinoyera uye rock art yekare",
            "location": "Matabeleland South, pedyo neBulawayo",
            "inscribed": "2003",
            "criteria": "(iii), (v), (vi)",
            "history":
                "Matobo Hills yakashandiswa nevanhu kwezviuru zvemakore. "
                "Mune mapako, rock art uye humbowo hwekugara kwevanhu vekare.",
            "culture":
                "Matobo inzvimbo yetsika mhenyu ine nzvimbo dzinoyera, "
                "tsika dzekunamatira mvura uye kutenda kwaMwari.",
            "features": [
                "Makomo egranite nematombo anoyevedza.",
                "Mapako ane rock art yekare.",
                "Rock art yakawanda kumaodzanyemba kweAfrica.",
                "Nzvimbo dzinoyera.",
                "Humbowo hwekugara kwevanhu kwenguva refu.",
            ],
            "unesco":
                "UNESCO yakanyora Matobo Hills muna 2003 nekuda kwerock art, "
                "archaeology uye tsika dzemweya dzichiri kurarama.",
            "protection": [
                "Usabata kana kukwesha rock art.",
                "Usanyora pamatombo kana kubvisa artefacts.",
                "Shandisa nzira dzakatemwa.",
                "Remekedza nzvimbo dzinoyera.",
            ],
            "facts": [
                "Mamwe mapako ane mifananidzo yevanhu nemhuka.",
                "Matobo inozivikanwa nematombo makuru egranite.",
                "Inobatanidza archaeology netsika mhenyu.",
            ],
            "significance":
                "Matobo Hills inobatanidza geology, art yekare, archaeology "
                "uye tsika dzemweya.",
        },
    },

    "great": {
        "emoji": "🏛️",

        "English": {
            "name": "Great Zimbabwe",
            "subtitle": "A monumental stone city and symbol of Zimbabwe",
            "location": "Masvingo Province",
            "inscribed": "1986",
            "criteria": "(i), (iii), (vi)",
            "history":
                "Great Zimbabwe developed over several centuries and flourished mainly between "
                "the 11th and 15th centuries. It was a major political, economic and cultural centre "
                "built by ancestors of Shona-speaking communities.",
            "culture":
                "The site reflects sophisticated African state formation, leadership, craftsmanship, "
                "social organisation and long-distance exchange. Its legacy is central to Zimbabwean "
                "national identity.",
            "features": [
                "The Hill Complex among natural granite boulders.",
                "The Great Enclosure.",
                "The Conical Tower.",
                "Valley Ruins and dry-stone walls.",
                "Soapstone Zimbabwe Birds.",
            ],
            "unesco":
                "Great Zimbabwe National Monument was inscribed by UNESCO in 1986 for its "
                "exceptional architecture and testimony to a major African civilisation.",
            "protection": [
                "Do not climb, sit or stand on ancient walls.",
                "Never remove stones or artefacts.",
                "Keep to official paths and viewing areas.",
                "Avoid graffiti, littering and damage.",
            ],
            "facts": [
                "Many walls were built without mortar.",
                "Imported objects show long-distance trade connections.",
                "The Zimbabwe Birds were carved from soapstone.",
            ],
            "significance":
                "Great Zimbabwe demonstrates the engineering skill, economic power and cultural "
                "sophistication of a major pre-colonial African civilisation.",
        },

        "isiNdebele": {
            "name": "Great Zimbabwe",
            "subtitle": "Idolobho elikhulu lamatshe eliyisibonakaliso seZimbabwe",
            "location": "Masvingo Province",
            "inscribed": "1986",
            "criteria": "(i), (iii), (vi)",
            "history":
                "IGreat Zimbabwe yakhula phakathi kwamakhulu eminyaka futhi yaphumelela kakhulu "
                "phakathi kwekhulu le-11 lele-15. Yakhiwa ngabokhokho bemiphakathi ekhuluma isiShona.",
            "culture":
                "Indawo ibonisa ubuhlakani bokubusa, ubuciko bemisebenzi yezandla kanye "
                "lokuhleleka kwabantu base-Afrika.",
            "features": [
                "Hill Complex.",
                "Great Enclosure.",
                "Conical Tower.",
                "Valley Ruins lemiduli yamatshe.",
                "Zimbabwe Birds ze-soapstone.",
            ],
            "unesco":
                "IGreat Zimbabwe National Monument yafakwa ku-UNESCO ngo-1986 ngenxa yobuciko "
                "bayo bezakhiwo kanye lokubaluleka kwayo emlandweni wase-Afrika.",
            "protection": [
                "Ungakhweli phezu kwemiduli yasendulo.",
                "Ungasusi amatshe kumbe izinto zemivubukulo.",
                "Hamba emizileni esemthethweni.",
                "Gwema ukulimaza kumbe ukulahla ingcekeza.",
            ],
            "facts": [
                "Imiduli eminengi yakhiwa ngaphandle kodaka.",
                "Izinto ezatholakala lapha zibonisa ukuthengiselana kwamabanga amade.",
                "IZimbabwe Birds zabazwa nge-soapstone.",
            ],
            "significance":
                "IGreat Zimbabwe ibonisa ubuciko bokwakha, amandla omnotho "
                "kanye lobuhlakani bempucuko enkulu yase-Afrika.",
        },

        "Shona": {
            "name": "Great Zimbabwe",
            "subtitle": "Guta guru rematombo uye chiratidzo cheZimbabwe",
            "location": "Masvingo Province",
            "inscribed": "1986",
            "criteria": "(i), (iii), (vi)",
            "history":
                "Great Zimbabwe yakakura kwemazana emakore uye yakabudirira zvikuru kubva "
                "muzana remakore rechi11 kusvika rechi15. Yakavakwa nemadzitateguru evanhu "
                "vanotaura chiShona.",
            "culture":
                "Nzvimbo iyi inoratidza hutongi hwakarongeka, hunyanzvi hwekugadzira, "
                "kurongeka kwevanhu uye kutengeserana kwemadaro marefu.",
            "features": [
                "Hill Complex.",
                "Great Enclosure.",
                "Conical Tower.",
                "Valley Ruins nemadziro edry-stone.",
                "Zimbabwe Birds dzesoapstone.",
            ],
            "unesco":
                "Great Zimbabwe National Monument yakanyorwa neUNESCO muna 1986 nekuda "
                "kwezvivakwa zvayo uye kukosha kwayo mubudiriro yeAfrica.",
            "protection": [
                "Usakwira pamadziro ekare.",
                "Usabvisa matombo kana artefacts.",
                "Famba munzira dziri pamutemo.",
                "Dzivisa graffiti nemarara.",
            ],
            "facts": [
                "Madziro mazhinji akavakwa pasina mortar.",
                "Zvakawanikwa zvinoratidza kutengeserana kwemadaro marefu.",
                "Zimbabwe Birds dzakavezwa nesoapstone.",
            ],
            "significance":
                "Great Zimbabwe inoratidza hunyanzvi hwekuvaka, simba rehupfumi "
                "netsika dzebudiriro huru yeAfrica.",
        },
    },

    "khami": {
        "emoji": "🧱",

        "English": {
            "name": "Khami Ruins",
            "subtitle": "Terraced stone architecture of the Torwa state",
            "location": "Near Bulawayo",
            "inscribed": "1986",
            "criteria": "(iii), (iv)",
            "history":
                "Khami rose to prominence after the decline of Great Zimbabwe. From the 15th "
                "into the 17th century it became an important centre of the Torwa state.",
            "culture":
                "Khami reflects political authority, social organisation, craftsmanship and "
                "exchange in south-western Zimbabwe.",
            "features": [
                "Massive stone-faced terraces.",
                "Decorative dry-stone wall patterns.",
                "Retaining walls adapted to the landscape.",
                "Evidence of local production and long-distance trade.",
                "A distinctive architectural tradition related to Great Zimbabwe.",
            ],
            "unesco":
                "Khami Ruins National Monument was inscribed by UNESCO in 1986 and is recognised "
                "for its cultural testimony and distinctive terraced architecture.",
            "protection": [
                "Do not climb on terrace walls.",
                "Do not remove pottery, stone or archaeological material.",
                "Stay on visitor routes.",
                "Report damage rather than moving objects.",
            ],
            "facts": [
                "Khami is especially famous for terraced construction.",
                "Decorative walling patterns give the ruins a distinctive appearance.",
                "Trade goods show connections to wider commercial networks.",
            ],
            "significance":
                "Khami shows how Zimbabwe's stone-building tradition continued and changed "
                "after Great Zimbabwe.",
        },

        "isiNdebele": {
            "name": "Amanxiwa eKhami",
            "subtitle": "Izakhiwo zamatshe ezitebhisi zombuso weTorwa",
            "location": "Eduze leBulawayo",
            "inscribed": "1986",
            "criteria": "(iii), (iv)",
            "history":
                "IKhami yakhula ngemva kokwehla kweGreat Zimbabwe. Kusukela ngekhulu le-15 "
                "kusiya kwele-17 yaba yisikhungo esibalulekileyo sombuso weTorwa.",
            "culture":
                "IKhami ibonisa amandla okubusa, ukuhleleka kwabantu, ubuciko kanye lokuthengiselana.",
            "features": [
                "Amathala amakhulu avalwe ngamatshe.",
                "Imiduli yamatshe elemihlobiso.",
                "Imiduli yokubamba umhlabathi.",
                "Ubufakazi bokuthengiselana kwamabanga amade.",
                "Isitayela sokwakha esihlobene leGreat Zimbabwe.",
            ],
            "unesco":
                "IKhami Ruins National Monument yafakwa ku-UNESCO ngo-1986 ngenxa yesitayela "
                "sayo esiyingqayizivele kanye lobufakazi bamasiko abalulekileyo.",
            "protection": [
                "Ungakhweli phezu kwemiduli yamathala.",
                "Ungasusi amatshe kumbe izinto zemivubukulo.",
                "Hamba emizileni yezivakashi.",
                "Bika umonakalo kubasebenzi.",
            ],
            "facts": [
                "IKhami idume ngamathala ayo.",
                "Imihlobiso yemiduli yenza indawo ibonakale yehlukile.",
                "Izinto ezatholakala lapha zibonisa ukuhweba lezinye izindawo.",
            ],
            "significance":
                "IKhami ikhombisa ukuthi isiko lokwakha ngamatshe eZimbabwe laqhubeka "
                "futhi latshintsha ngemva kweGreat Zimbabwe.",
        },

        "Shona": {
            "name": "Khami Ruins",
            "subtitle": "Zvivakwa zvematombo zvine terraces zvehurumende yeTorwa",
            "location": "Pedyo neBulawayo",
            "inscribed": "1986",
            "criteria": "(iii), (iv)",
            "history":
                "Khami yakasimukira mushure mekuderera kweGreat Zimbabwe. Kubva muzana remakore "
                "rechi15 kusvika rechi17 yakava nzvimbo yakakosha yehurumende yeTorwa.",
            "culture":
                "Khami inoratidza hutongi, kurongeka kwevanhu, hunyanzvi uye kutengeserana.",
            "features": [
                "Terraces huru dzine madziro ematombo.",
                "Dry-stone walling ine mapatani ekushongedza.",
                "Retaining walls.",
                "Humbowo hwekutengeserana kwemadaro marefu.",
                "Nzira yekuvaka ine hukama neGreat Zimbabwe.",
            ],
            "unesco":
                "Khami Ruins National Monument yakanyorwa neUNESCO muna 1986 nekuda kweuchapupu "
                "hwetsika uye chimiro chayo cheterraced architecture.",
            "protection": [
                "Usakwira pamadziro eterraces.",
                "Usabvisa pottery, matombo kana artefacts.",
                "Shandisa nzira dzevashanyi.",
                "Kana ukaona kukuvara, zviudze vashandi.",
            ],
            "facts": [
                "Khami inozivikanwa nema terraces.",
                "Mapatani pamadziro anoipa chimiro chakasiyana.",
                "Trade goods dzinoratidza hukama nemisika iri kure.",
            ],
            "significance":
                "Khami inoratidza kuenderera nekushanduka kwetsika yekuvaka nematombo muZimbabwe.",
        },
    },
}


# --------------------------------------------------
# QUIZ DATA
# --------------------------------------------------
QUIZ = {
    "English": [
        (
            "Which site is especially famous for prehistoric rock paintings?",
            ["Great Zimbabwe", "Matobo Hills", "Khami Ruins", "Victoria Falls"],
            1,
            "Matobo Hills contains one of southern Africa's richest concentrations of rock art.",
        ),
        (
            "In which year was Matobo Hills inscribed by UNESCO?",
            ["1980", "1986", "2003", "2010"],
            2,
            "Matobo Hills was inscribed in 2003.",
        ),
        (
            "Which major structure is found at Great Zimbabwe?",
            ["Great Enclosure", "Stonehenge", "Pyramids", "Colosseum"],
            0,
            "The Great Enclosure is one of Great Zimbabwe's best-known structures.",
        ),
        (
            "How were many Great Zimbabwe walls constructed?",
            ["With concrete", "Dry-stone masonry", "With steel", "With timber"],
            1,
            "Many walls were built from carefully fitted stone without mortar.",
        ),
        (
            "The Zimbabwe Birds were carved mainly from what?",
            ["Soapstone", "Gold", "Wood", "Bronze"],
            0,
            "The Zimbabwe Birds were carved from soapstone.",
        ),
        (
            "Khami became an important centre of which state?",
            ["Torwa", "Roman", "Ottoman", "Aztec"],
            0,
            "Khami became an important centre of the Torwa state.",
        ),
        (
            "What architectural feature is especially associated with Khami?",
            ["Stone-faced terraces", "Glass towers", "Wooden palaces", "Brick domes"],
            0,
            "Khami is especially known for stone-faced terraces.",
        ),
        (
            "What is the safest behaviour near ancient rock paintings?",
            ["Touch them", "Wet them", "Do not touch them", "Trace them"],
            2,
            "Touching or wetting ancient paintings can damage them.",
        ),
        (
            "What connected Great Zimbabwe to wider trading networks?",
            ["Long-distance trade", "Air travel", "Rail transport", "Modern shipping"],
            0,
            "Long-distance trade linked Great Zimbabwe to regional and Indian Ocean networks.",
        ),
        (
            "Which comparison is correct?",
            [
                "Great Zimbabwe and Khami are identical",
                "Both use stone-building traditions, but Khami is especially known for terraces",
                "Neither has stone walls",
                "Both were built in the 20th century",
            ],
            1,
            "Both belong to Zimbabwe's stone-building tradition, but Khami has a distinctive terraced style.",
        ),
    ],

    "isiNdebele": [
        (
            "Yiphi indawo eyaziwa ngemidwebo yasendulo emadwaleni?",
            ["Great Zimbabwe", "Matobo Hills", "Khami Ruins", "Victoria Falls"],
            1,
            "IMatobo Hills ilenani elikhulu lemidwebo yamadwala.",
        ),
        (
            "IMatobo Hills yafakwa ku-UNESCO ngamuphi umnyaka?",
            ["1980", "1986", "2003", "2010"],
            2,
            "Yafakwa ngo-2003.",
        ),
        (
            "Yisiphi isakhiwo esidumileyo eGreat Zimbabwe?",
            ["Great Enclosure", "Stonehenge", "Pyramids", "Colosseum"],
            0,
            "IGreat Enclosure ngesinye sezakhiwo ezaziwa kakhulu.",
        ),
        (
            "Imiduli eminengi yakhiwa njani?",
            ["Ngekhonkolo", "Ngamatshe ngaphandle kodaka", "Ngensimbi", "Ngezigodo"],
            1,
            "Yakhiwa ngamatshe ngaphandle kodaka.",
        ),
        (
            "IZimbabwe Birds zabazwa ngani?",
            ["Soapstone", "Igolide", "Isihlahla", "Bronze"],
            0,
            "Zabazwa nge-soapstone.",
        ),
        (
            "IKhami yaba yisikhungo sombuso bani?",
            ["Torwa", "Roman", "Ottoman", "Aztec"],
            0,
            "Yaba yisikhungo sombuso weTorwa.",
        ),
        (
            "Yini edume kakhulu eKhami?",
            ["Amathala amatshe", "Glass towers", "Wooden palaces", "Brick domes"],
            0,
            "IKhami idume ngamathala ayo.",
        ),
        (
            "Kumele wenzeni eduze kwemidwebo yasendulo?",
            ["Uyithinte", "Uyimanzise", "Ungayithinti", "Uyidwebe"],
            2,
            "Ukuyithinta kungayilimaza.",
        ),
        (
            "Yini eyaxhumanisa iGreat Zimbabwe lezinye izindawo?",
            ["Ukuthengiselana kwamabanga amade", "Izindiza", "Izitimela", "Ama-container"],
            0,
            "Ukuthengiselana kwamabanga amade.",
        ),
        (
            "Yiphi inkulumo elungileyo?",
            [
                "Zifana ngokupheleleyo",
                "Zombili zisebenzisa isiko lamatshe kodwa iKhami idume ngamathala",
                "Azila miduli",
                "Zakhiwa ngekhulu lama-20",
            ],
            1,
            "Zombili zihlobene lesiko lokwakha ngamatshe.",
        ),
    ],

    "Shona": [
        (
            "Ndeipi nzvimbo inonyanya kuzivikanwa nerock art yekare?",
            ["Great Zimbabwe", "Matobo Hills", "Khami Ruins", "Victoria Falls"],
            1,
            "Matobo Hills ine rock art yakawanda.",
        ),
        (
            "Matobo Hills yakanyorwa neUNESCO mugore ripi?",
            ["1980", "1986", "2003", "2010"],
            2,
            "Yakanyorwa muna 2003.",
        ),
        (
            "Ndechipi chimwe chezvivakwa zvikuru paGreat Zimbabwe?",
            ["Great Enclosure", "Stonehenge", "Pyramids", "Colosseum"],
            0,
            "Great Enclosure ndechimwe chezvivakwa zvinonyanya kuzivikanwa.",
        ),
        (
            "Madziro mazhinji akavakwa sei?",
            ["Nekongiri", "Dry-stone masonry", "Nesimbi", "Nemapuranga"],
            1,
            "Matombo akaiswa pamwe chete pasina mortar.",
        ),
        (
            "Zimbabwe Birds dzakavezwa nechii?",
            ["Soapstone", "Goridhe", "Huni", "Bronze"],
            0,
            "Dzaka vezwa nesoapstone.",
        ),
        (
            "Khami yakava nzvimbo yakakosha yehurumende ipi?",
            ["Torwa", "Roman", "Ottoman", "Aztec"],
            0,
            "Yaiva nzvimbo yakakosha yeTorwa.",
        ),
        (
            "Chii chinonyanya kuzivikanwa paKhami?",
            ["Stone-faced terraces", "Glass towers", "Wooden palaces", "Brick domes"],
            0,
            "Khami inonyanya kuzivikanwa nema terraces.",
        ),
        (
            "Unofanira kuita sei pedyo nerock art?",
            ["Kuibata", "Kuinyorovesa", "Kusabata", "Kuitevera nechalk"],
            2,
            "Kubata rock art kunogona kuikuvadza.",
        ),
        (
            "Chii chakabatanidza Great Zimbabwe nemisika iri kure?",
            ["Long-distance trade", "Ndege", "Chitima", "Containers"],
            0,
            "Long-distance trade yakabatanidza Great Zimbabwe nemisika iri kure.",
        ),
        (
            "Ndeipi tsananguro yakarurama?",
            [
                "Dzakaenzana chose",
                "Dzose dzine stone-building tradition asi Khami inozivikanwa nema terraces",
                "Hadzina madziro",
                "Dzese dzakavakwa mu20th century",
            ],
            1,
            "Dzose dzine stone-building tradition, asi Khami ine terraced style.",
        ),
    ],
}


# --------------------------------------------------
# ASSISTANT
# --------------------------------------------------
def assistant_answer(question, lang):
    q = re.sub(r"\s+", " ", question.lower().strip())

    responses = {
        "English": {
            "great_when":
                "Great Zimbabwe was not built in one single year. It developed over several centuries "
                "and flourished mainly between the 11th and 15th centuries.",

            "great_who":
                "Great Zimbabwe was built by ancestors of Shona-speaking communities. "
                "It was a major African political, economic and cultural centre.",

            "great_arch":
                "Great Zimbabwe is famous for the Hill Complex, Great Enclosure, Conical Tower, "
                "Valley Ruins and highly skilled dry-stone masonry built largely without mortar.",

            "birds":
                "The Zimbabwe Birds are soapstone sculptures found at Great Zimbabwe. "
                "Their image later became an important national symbol of Zimbabwe.",

            "matobo":
                "Matobo Hills is famous for granite landforms, caves, rock shelters, prehistoric "
                "rock art, archaeology and living spiritual traditions.",

            "khami":
                "Khami Ruins became an important centre of the Torwa state after the decline "
                "of Great Zimbabwe. It is especially known for stone-faced terraces and decorative "
                "dry-stone walling.",

            "unesco":
                "Great Zimbabwe and Khami Ruins were inscribed on the UNESCO World Heritage List "
                "in 1986. Matobo Hills was inscribed in 2003.",

            "trade":
                "Great Zimbabwe and Khami show evidence of long-distance trade. Imported ceramics "
                "and other objects indicate links to wider regional and Indian Ocean trade networks.",

            "protect":
                "Protect heritage by not touching rock art, not climbing ancient walls, not removing "
                "stones or artefacts, staying on marked routes and avoiding graffiti or littering.",

            "compare":
                "Great Zimbabwe is best known for monumental freestanding stone walls and the Great Enclosure. "
                "Khami is especially known for terraces and decorative retaining walls. Matobo is different "
                "because it combines rock art, granite landscapes and living sacred traditions.",
        },

        "isiNdebele": {
            "great_when":
                "IGreat Zimbabwe ayizange yakhiwe ngomnyaka owodwa. Yakhula phakathi kwamakhulu "
                "eminyaka futhi yaphumelela kakhulu phakathi kwekhulu le-11 lele-15.",

            "great_who":
                "IGreat Zimbabwe yakhiwa ngabokhokho bemiphakathi ekhuluma isiShona.",

            "great_arch":
                "IGreat Zimbabwe idume ngeHill Complex, Great Enclosure, Conical Tower, Valley Ruins "
                "kanye lemiduli yamatshe eyakhiwa ngaphandle kodaka.",

            "birds":
                "IZimbabwe Birds yizithombe ze-soapstone ezatholakala eGreat Zimbabwe futhi zaba "
                "luphawu olubalulekileyo lwelizwe.",

            "matobo":
                "IMatobo Hills idume ngamatshe egranite, imihume, imidwebo yamadwala, imivubukulo "
                "kanye lamasiko omoya.",

            "khami":
                "IKhami Ruins yaba yisikhungo sombuso weTorwa futhi idume ngamathala amatshe "
                "lemihlobiso yemiduli.",

            "unesco":
                "IGreat Zimbabwe leKhami Ruins zafakwa ku-UNESCO ngo-1986. "
                "IMatobo Hills yafakwa ngo-2003.",

            "trade":
                "IGreat Zimbabwe leKhami zibonisa ubufakazi bokuthengiselana kwamabanga amade.",

            "protect":
                "Vikela amagugu ngokungathinti imidwebo yamadwala, ukungakhweli imiduli yasendulo, "
                "ukungasusi izinto kanye lokungalahli ingcekeza.",

            "compare":
                "IGreat Zimbabwe idume ngemiduli emikhulu leGreat Enclosure. IKhami idume ngamathala. "
                "IMatobo yona idume ngemidwebo yamadwala lamasiko angcwele.",
        },

        "Shona": {
            "great_when":
                "Great Zimbabwe haina kuvakwa mugore rimwe chete. Yakakura kwemazana emakore "
                "uye yakabudirira zvikuru kubva muzana remakore rechi11 kusvika rechi15.",

            "great_who":
                "Great Zimbabwe yakavakwa nemadzitateguru evanhu vanotaura chiShona.",

            "great_arch":
                "Great Zimbabwe inozivikanwa neHill Complex, Great Enclosure, Conical Tower, "
                "Valley Ruins uye dry-stone masonry yakavakwa pasina mortar.",

            "birds":
                "Zimbabwe Birds zvivezwa zvesoapstone zvakawanikwa paGreat Zimbabwe uye zvakazova "
                "chiratidzo chakakosha chenyika.",

            "matobo":
                "Matobo Hills inozivikanwa nematombo egranite, mapako, rock art, archaeology "
                "uye tsika dzemweya.",

            "khami":
                "Khami Ruins yakava nzvimbo yakakosha yehurumende yeTorwa uye inozivikanwa "
                "nema terraces nemadziro ane mapatani.",

            "unesco":
                "Great Zimbabwe neKhami Ruins zvakanyorwa neUNESCO muna 1986. "
                "Matobo Hills yakanyorwa muna 2003.",

            "trade":
                "Great Zimbabwe neKhami zvinoratidza humbowo hwekutengeserana kwemadaro marefu.",

            "protect":
                "Chengetedza nhaka nekusabata rock art, kusakwira pamadziro ekare, kusabvisa "
                "artefacts uye kusasiya marara.",

            "compare":
                "Great Zimbabwe inozivikanwa nemadziro makuru neGreat Enclosure. "
                "Khami inozivikanwa nema terraces. Matobo inosiyana nekuti ine rock art, "
                "granite landscape netsika dzinoyera.",
        },
    }[lang]

    if (
        ("great zimbabwe" in q or "great zim" in q)
        and any(x in q for x in ["what year", "when", "built", "constructed", "yakhiwa", "wakhiwa"])
    ):
        return responses["great_when"]

    if (
        ("great zimbabwe" in q or "great zim" in q)
        and any(x in q for x in ["who", "builder", "builders", "ngobani", "ndiani"])
    ):
        return responses["great_who"]

    if any(
        x in q
        for x in [
            "great enclosure",
            "conical tower",
            "hill complex",
            "dry stone",
            "dry-stone",
            "architecture",
        ]
    ):
        return responses["great_arch"]

    if any(x in q for x in ["zimbabwe bird", "zimbabwe birds", "soapstone bird", "inyoni", "shiri"]):
        return responses["birds"]

    if any(
        x in q
        for x in ["compare", "difference", "differences", "qhathanisa", "umehluko", "enzanisa", "musiyano"]
    ):
        return responses["compare"]

    if any(x in q for x in ["unesco", "world heritage", "inscribed", "listed"]):
        return responses["unesco"]

    if any(x in q for x in ["trade", "commerce", "kutengesa", "ukuthengiselana", "indian ocean"]):
        return responses["trade"]

    if any(
        x in q
        for x in ["protect", "conservation", "preserve", "damage", "vikela", "chengetedza", "kuchengetedza"]
    ):
        return responses["protect"]

    if any(x in q for x in ["matobo", "rock art", "cave", "caves", "granite", "mwari", "imihume", "mapako"]):
        return responses["matobo"]

    if any(x in q for x in ["khami", "torwa", "terrace", "terraces", "retaining wall", "amathala"]):
        return responses["khami"]

    if "great zimbabwe" in q or "great zim" in q:
        return responses["great_arch"]

    if lang == "isiNdebele":
        return (
            "Buza ngeMatobo Hills, Great Zimbabwe kumbe Khami Ruins — umlando, abakhi, "
            "imidwebo yamadwala, izakhiwo, UNESCO, ukuhweba loba ukuvikela amagugu."
        )

    if lang == "Shona":
        return (
            "Bvunza nezveMatobo Hills, Great Zimbabwe kana Khami Ruins — nhoroondo, "
            "vakavaka, rock art, architecture, UNESCO, trade kana kuchengetedza nhaka."
        )

    return (
        "Ask me about Matobo Hills, Great Zimbabwe or Khami Ruins — history, builders, "
        "rock art, architecture, UNESCO, trade, conservation or comparisons."
    )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.markdown("## 🗿 ROBO GUIDE")
    st.caption("Zimbabwe Heritage Explorer")

    langs = ["English", "isiNdebele", "Shona"]

    selected_lang = st.selectbox(
        T("language"),
        langs,
        index=langs.index(st.session_state.lang),
        key="language_selector_unique",
    )

    if selected_lang != st.session_state.lang:
        st.session_state.lang = selected_lang
        reset_quiz()
        st.session_state.chat = []
        st.rerun()

    st.markdown(f"### {T('explore')}")

    nav = [
        ("🏠", T("home"), "home"),
        ("⛰️", T("matobo"), "matobo"),
        ("🏛️", T("great"), "great"),
        ("🧱", T("khami"), "khami"),
        ("🏆", T("quiz"), "quiz"),
        ("💬", T("assistant"), "assistant"),
    ]

    for i, (icon, label, page) in enumerate(nav):
        if st.button(
            f"{icon}  {label}",
            key=f"sidebar_{page}_{i}",
            use_container_width=True,
        ):
            go(page)


# --------------------------------------------------
# HOME
# --------------------------------------------------
def render_home():
    html(
        f"""
        <div class="hero">
            <h1>ROBO GUIDE</h1>
            <h3>{escape(T('hero_sub'))}</h3>
            <p>{escape(T('hero_text'))}</p>
        </div>
        """
    )

    st.markdown(f"## {T('choose')}")

    cols = st.columns(3)

    for col, key in zip(cols, ["matobo", "great", "khami"]):
        d = SITES[key][st.session_state.lang]

        with col:
            html(
                f"""
                <div class="site-card">
                    <div style="font-size:2.5rem;">{SITES[key]['emoji']}</div>
                    <h3>{escape(d['name'])}</h3>
                    <p>{escape(d['subtitle'])}</p>
                    <span class="badge">UNESCO {escape(d['inscribed'])}</span>
                    <span class="badge">{escape(d['criteria'])}</span>
                </div>
                """
            )

            if st.button(
                f"{T('open_site')}: {d['name']}",
                key=f"home_open_{key}",
                use_container_width=True,
            ):
                go(key)

    st.markdown("## Explore • Learn • Respect • Protect")

    c1, c2, c3 = st.columns(3)

    with c1:
        html(
            """
            <div class="info-card">
                <h3>📚 Learn</h3>
                <p>Discover Zimbabwean history, architecture, archaeology and living traditions.</p>
            </div>
            """
        )

    with c2:
        html(
            """
            <div class="info-card">
                <h3>🏆 Challenge</h3>
                <p>Test your knowledge and earn Heritage Points through the ROBO GUIDE Heritage Challenge.</p>
            </div>
            """
        )

    with c3:
        html(
            """
            <div class="info-card">
                <h3>🛡️ Protect</h3>
                <p>Learn how visitors can respect and help preserve important heritage places.</p>
            </div>
            """
        )


# --------------------------------------------------
# SITE PAGE
# --------------------------------------------------
def render_site(site_key):
    d = SITES[site_key][st.session_state.lang]

    html(
        f"""
        <div class="hero">
            <div style="font-size:2.7rem;">{SITES[site_key]['emoji']}</div>
            <h1 style="font-size:3rem;">{escape(d['name'])}</h1>
            <h3>{escape(d['subtitle'])}</h3>
        </div>
        """
    )

    a, b, c = st.columns(3)

    a.metric(T("location"), d["location"])
    b.metric(T("inscribed"), d["inscribed"])
    c.metric(T("criteria"), d["criteria"])

    st.markdown(f"## {T('history')}")

    html(
        f"""
        <div class="info-card">
            <p>{escape(d['history'])}</p>
        </div>
        """
    )

    st.markdown(f"## {T('culture')}")

    html(
        f"""
        <div class="info-card">
            <p>{escape(d['culture'])}</p>
        </div>
        """
    )

    st.markdown(f"## {T('features')}")

    fcols = st.columns(2)

    for i, item in enumerate(d["features"]):
        with fcols[i % 2]:
            html(
                f"""
                <div class="fact-card">
                    <h4>◆</h4>
                    <p>{escape(item)}</p>
                </div>
                """
            )

    st.markdown(f"## {T('unesco')}")

    html(
        f"""
        <div class="gold-strip">
            <strong>UNESCO World Heritage</strong><br><br>
            {escape(d['unesco'])}
        </div>
        """
    )

    st.markdown(f"## {T('protect')}")

    pcols = st.columns(2)

    for i, item in enumerate(d["protection"]):
        with pcols[i % 2]:
            html(
                f"""
                <div class="fact-card">
                    <h4>🛡️</h4>
                    <p>{escape(item)}</p>
                </div>
                """
            )

    st.markdown(f"## {T('facts')}")

    factcols = st.columns(3)

    for i, item in enumerate(d["facts"]):
        with factcols[i % 3]:
            html(
                f"""
                <div class="fact-card">
                    <h4>💡</h4>
                    <p>{escape(item)}</p>
                </div>
                """
            )

    st.markdown(f"## {T('significance')}")

    html(
        f"""
        <div class="gold-strip">
            {escape(d['significance'])}
        </div>
        """
    )

    l, r = st.columns(2)

    with l:
        if st.button(
            "🏆 " + T("quiz"),
            key=f"site_quiz_{site_key}",
            use_container_width=True,
        ):
            go("quiz")

    with r:
        if st.button(
            "💬 " + T("assistant"),
            key=f"site_assistant_{site_key}",
            use_container_width=True,
        ):
            go("assistant")


# --------------------------------------------------
# QUIZ PAGE
# --------------------------------------------------
def render_quiz():
    html(
        f"""
        <div class="hero">
            <h1 style="font-size:3rem;">🏆 {escape(T('quiz_title'))}</h1>
            <p>{escape(T('quiz_intro'))}</p>
        </div>
        """
    )

    questions = QUIZ[st.session_state.lang]

    if st.session_state.quiz_finished:
        total = len(questions)

        pct = round(
            st.session_state.quiz_score
            / total
            * 100
        )

        achievement = (
            T("guardian")
            if pct >= 80
            else T("guide")
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            T("score"),
            f"{st.session_state.quiz_score}/{total}",
        )

        c2.metric(
            T("points"),
            st.session_state.quiz_points,
        )

        c3.metric(
            T("achievement"),
            achievement,
        )

        st.success(
            f"🎉 {achievement} — {pct}%"
        )

        if st.button(
            T("restart"),
            key="quiz_restart_unique",
            use_container_width=True,
        ):
            reset_quiz()
            st.rerun()

        return

    idx = st.session_state.quiz_index

    q, options, correct_idx, explanation = questions[idx]

    st.progress(
        (idx + 1)
        / len(questions)
    )

    st.markdown(
        f"### {T('question')} "
        f"{idx + 1} / {len(questions)}"
    )

    html(
        f"""
        <div class="quiz-card">
            <h3>{escape(q)}</h3>
        </div>
        """
    )

    choice = st.radio(
        "Answer",
        options,
        index=None,
        key=f"quiz_radio_{st.session_state.lang}_{idx}",
        label_visibility="collapsed",
        disabled=st.session_state.quiz_answered,
    )

    if not st.session_state.quiz_answered:

        if st.button(
            T("submit"),
            key=f"quiz_submit_{idx}",
            use_container_width=True,
        ):

            if choice is None:
                st.warning(
                    "Please choose an answer first."
                )

            else:
                st.session_state.quiz_choice = choice
                st.session_state.quiz_answered = True

                if options.index(choice) == correct_idx:
                    st.session_state.quiz_score += 1
                    st.session_state.quiz_points += 100

                else:
                    st.session_state.quiz_points += 20

                st.rerun()

    else:

        chosen_idx = options.index(
            st.session_state.quiz_choice
        )

        if chosen_idx == correct_idx:

            st.success(
                f"✅ {T('correct')} "
                f"{explanation}"
            )

        else:

            st.error(
                f"❌ {T('incorrect')} "
                f"{explanation}"
            )

        c1, c2 = st.columns(2)

        c1.metric(
            T("score"),
            st.session_state.quiz_score,
        )

        c2.metric(
            T("points"),
            st.session_state.quiz_points,
        )

        if st.button(
            T("next"),
            key=f"quiz_next_{idx}",
            use_container_width=True,
        ):

            if idx + 1 >= len(questions):
                st.session_state.quiz_finished = True

            else:
                st.session_state.quiz_index += 1
                st.session_state.quiz_answered = False
                st.session_state.quiz_choice = None

            st.rerun()


# --------------------------------------------------
# ASSISTANT PAGE
# --------------------------------------------------
def render_assistant():
    html(
        f"""
        <div class="hero">
            <h1 style="font-size:3rem;">
                💬 {escape(T('assistant_title'))}
            </h1>
            <p>{escape(T('assistant_intro'))}</p>
        </div>
        """
    )

    suggestions = {
        "English": [
            "What year was Great Zimbabwe built?",
            "Who built Great Zimbabwe?",
            "What is special about Matobo rock art?",
            "What are the Zimbabwe Birds?",
            "What is special about Khami terraces?",
            "Compare all three heritage sites.",
        ],

        "isiNdebele": [
            "IGreat Zimbabwe yakhiwa nini?",
            "Ngobani abakha iGreat Zimbabwe?",
            "Yini eqakathekileyo ngemidwebo yaseMatobo?",
            "Yini amaZimbabwe Birds?",
            "Yini ekhethekileyo ngamathala eKhami?",
            "Qhathanisa indawo ezintathu.",
        ],

        "Shona": [
            "Great Zimbabwe yakavakwa riini?",
            "Ndiani akavaka Great Zimbabwe?",
            "Chii chakakosha nezverock art yeMatobo?",
            "Zimbabwe Birds chii?",
            "Chii chakakosha nema terraces eKhami?",
            "Enzanisa nzvimbo nhatu dzese.",
        ],
    }

    st.markdown("### Quick questions")

    qcols = st.columns(2)

    for i, prompt in enumerate(
        suggestions[st.session_state.lang]
    ):

        with qcols[i % 2]:

            if st.button(
                prompt,
                key=f"assistant_suggest_{st.session_state.lang}_{i}",
                use_container_width=True,
            ):

                st.session_state.chat.append(
                    (
                        prompt,
                        assistant_answer(
                            prompt,
                            st.session_state.lang,
                        ),
                    )
                )

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

    with st.form(
        "assistant_form_unique",
        clear_on_submit=True,
    ):

        question = st.text_input(
            T("ask"),
            key="assistant_input_unique",
            placeholder=T("ask"),
        )

        submitted = st.form_submit_button(
            T("send"),
            use_container_width=True,
        )

        if submitted and question.strip():

            st.session_state.chat.append(
                (
                    question.strip(),
                    assistant_answer(
                        question,
                        st.session_state.lang,
                    ),
                )
            )

            st.rerun()

    if st.button(
        T("clear"),
        key="assistant_clear_unique",
        use_container_width=True,
    ):

        st.session_state.chat = []

        st.rerun()

    st.caption(
        "ROBO GUIDE uses built-in heritage knowledge. "
        "No paid API is required."
    )


# --------------------------------------------------
# ROUTER
# --------------------------------------------------
page = st.session_state.page

if page == "home":
    render_home()

elif page in [
    "matobo",
    "great",
    "khami",
]:
    render_site(page)

elif page == "quiz":
    render_quiz()

elif page == "assistant":
    render_assistant()

else:
    st.session_state.page = "home"
    st.rerun()


html(
    f"""
    <div class="footer">
        {escape(T('footer'))}
    </div>
    """
)
