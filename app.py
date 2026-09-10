import streamlit as st
import re
import random
from datetime import datetime


# ============================================================
# ROBO GUARD
# WRO 2026 - ROBOTS MEET CULTURE
# Zimbabwe Heritage Protection & Education Platform
# ============================================================


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ROBO GUARD | Zimbabwe Heritage",
    page_icon="🇿🇼",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    /* -------------------------------------------------------
       MAIN APP
    ------------------------------------------------------- */

    .stApp {
        background:
            radial-gradient(circle at top left, #fff9df 0%, transparent 28%),
            linear-gradient(180deg, #f7f8f1 0%, #ffffff 45%, #f7f8f1 100%);
    }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    /* -------------------------------------------------------
       SIDEBAR
    ------------------------------------------------------- */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, #054b2e 0%, #08683d 100%);
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    [data-testid="stSidebar"] .stRadio label {
        color: white !important;
    }

    /* -------------------------------------------------------
       TITLES
    ------------------------------------------------------- */

    h1, h2, h3 {
        color: #075b36;
    }

    .hero {
        background:
            linear-gradient(
                135deg,
                rgba(4,83,48,0.98),
                rgba(9,121,69,0.95)
            );
        border: 2px solid #d4af37;
        border-radius: 24px;
        padding: 35px 28px;
        margin-bottom: 25px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.13);
        text-align: center;
    }

    .hero h1 {
        color: white !important;
        font-size: 48px;
        margin: 0;
        letter-spacing: 1px;
    }

    .hero h2 {
        color: #f7d968 !important;
        margin: 8px 0 4px 0;
        font-size: 24px;
    }

    .hero p {
        color: white;
        font-size: 17px;
        margin: 8px auto 0 auto;
        max-width: 850px;
    }

    .tagline {
        margin-top: 16px;
        color: #ffe78d !important;
        font-weight: 700;
        letter-spacing: 1px;
    }

    /* -------------------------------------------------------
       SITE CARDS
    ------------------------------------------------------- */

    .site-card {
        background: white;
        border-radius: 20px;
        padding: 24px;
        min-height: 260px;
        border-top: 6px solid #d4af37;
        box-shadow: 0 7px 25px rgba(0,0,0,0.09);
        transition: all 0.25s ease;
        margin-bottom: 10px;
    }

    .site-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.14);
    }

    .site-icon {
        font-size: 42px;
        margin-bottom: 5px;
    }

    .site-title {
        font-size: 25px;
        font-weight: 800;
        color: #075b36;
        margin-bottom: 8px;
    }

    .site-subtitle {
        color: #9b7621;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .site-description {
        color: #404040;
        line-height: 1.5;
    }

    /* -------------------------------------------------------
       INFO CARDS
    ------------------------------------------------------- */

    .info-card {
        background: white;
        padding: 20px;
        border-radius: 17px;
        border-left: 6px solid #d4af37;
        box-shadow: 0 4px 14px rgba(0,0,0,0.07);
        margin: 10px 0;
        min-height: 160px;
    }

    .info-card h3 {
        margin-top: 0;
    }

    .culture-card {
        background:
            linear-gradient(135deg, #fffef7, #f6f1db);
        border: 1px solid #e6d28e;
        border-radius: 18px;
        padding: 20px;
        margin: 12px 0;
    }

    .protection-card {
        background:
            linear-gradient(135deg, #e9f8ef, #ffffff);
        border-left: 7px solid #087743;
        border-radius: 17px;
        padding: 20px;
        margin: 15px 0;
    }

    .danger-card {
        background:
            linear-gradient(135deg, #fff3f3, #ffffff);
        border-left: 7px solid #b52727;
        border-radius: 17px;
        padding: 20px;
        margin: 15px 0;
    }

    /* -------------------------------------------------------
       BADGES
    ------------------------------------------------------- */

    .badge {
        display: inline-block;
        background: #075b36;
        color: white;
        padding: 6px 12px;
        margin: 3px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 700;
    }

    .gold-badge {
        display: inline-block;
        background: #d4af37;
        color: #173c2d;
        padding: 6px 12px;
        margin: 3px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 800;
    }

    /* -------------------------------------------------------
       QUIZ
    ------------------------------------------------------- */

    .mission-box {
        background:
            linear-gradient(135deg, #065934, #0b7f4b);
        border: 2px solid #d4af37;
        border-radius: 20px;
        padding: 22px;
        margin-bottom: 18px;
        color: white;
    }

    .mission-box h2,
    .mission-box h3 {
        color: #ffe681 !important;
    }

    .score-card {
        background: white;
        border-radius: 18px;
        padding: 20px;
        border: 2px solid #d4af37;
        text-align: center;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    }

    .guardian {
        background:
            linear-gradient(135deg, #075b36, #0a7544);
        color: white;
        border: 4px solid #d4af37;
        border-radius: 24px;
        padding: 30px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }

    .guardian h1,
    .guardian h2 {
        color: #ffe681 !important;
    }

    /* -------------------------------------------------------
       ROBOT FLOW
    ------------------------------------------------------- */

    .flow-card {
        background: white;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 4px 13px rgba(0,0,0,0.07);
        border-bottom: 5px solid #d4af37;
        min-height: 155px;
    }

    .flow-num {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background: #075b36;
        color: white;
        line-height: 36px;
        margin: auto;
        font-weight: 800;
    }

    /* -------------------------------------------------------
       FOOTER
    ------------------------------------------------------- */

    .footer {
        margin-top: 35px;
        padding: 24px;
        text-align: center;
        color: #075b36;
        border-top: 2px solid #d4af37;
    }

    /* -------------------------------------------------------
       SMALL SCREEN
    ------------------------------------------------------- */

    @media (max-width: 700px) {
        .hero h1 {
            font-size: 35px;
        }

        .hero h2 {
            font-size: 20px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "language" not in st.session_state:
    st.session_state.language = "English"

if "selected_site" not in st.session_state:
    st.session_state.selected_site = None

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_points" not in st.session_state:
    st.session_state.quiz_points = 0

if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False

if "quiz_selected" not in st.session_state:
    st.session_state.quiz_selected = None

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []


# ============================================================
# TRANSLATIONS
# ============================================================

TEXT = {

    "English": {
        "welcome": "Welcome",
        "discover": "Discover Zimbabwe's Living Heritage",
        "intro":
            "Explore the history, culture and protection of some of Zimbabwe's most important cultural heritage sites.",
        "explore": "Explore Site",
        "home": "Home",
        "sites": "Heritage Sites",
        "quiz": "Heritage Challenge",
        "assistant": "Heritage Assistant",
        "robot": "How ROBO GUARD Works",
        "history": "History",
        "culture": "Culture & People",
        "features": "Heritage Features",
        "protect": "Protect This Heritage",
        "facts": "Did You Know?",
        "location": "Location",
        "unesco": "World Heritage",
        "learn_more": "Explore More",
        "correct": "Correct!",
        "wrong": "Not quite.",
        "next": "Next Question",
        "check": "Check Answer",
        "guardian": "Heritage Guardian",
        "points": "Heritage Points",
        "question": "Question",
        "language": "Language",
        "back": "Back to Heritage Sites"
    },

    "isiNdebele": {
        "welcome": "Siyakwamukela",
        "discover": "Hlola Ilifa Eliphilayo LaseZimbabwe",
        "intro":
            "Funda ngembali, amasiko kanye lokuvikelwa kwezindawo eziqakathekileyo zelifa laseZimbabwe.",
        "explore": "Hlola Indawo",
        "home": "Ekhaya",
        "sites": "Izindawo Zelifa",
        "quiz": "Umncintiswano Welifa",
        "assistant": "Umsizi Welifa",
        "robot": "Indlela ROBO GUARD Esebenza Ngayo",
        "history": "Imbali",
        "culture": "Amasiko Labantu",
        "features": "Okuphathelane Lelifa",
        "protect": "Vikela Ilifa",
        "facts": "Ubukwazi Yini?",
        "location": "Indawo",
        "unesco": "Ilifa Lomhlaba",
        "learn_more": "Funda Okunengi",
        "correct": "Kulungile!",
        "wrong": "Akusikho.",
        "next": "Umbuzo Olandelayo",
        "check": "Hlola Impendulo",
        "guardian": "Umlondolozi Welifa",
        "points": "Amaphuzu Elifa",
        "question": "Umbuzo",
        "language": "Ulimi",
        "back": "Buyela Ezindaweni Zelifa"
    },

    "Shona": {
        "welcome": "Mauya",
        "discover": "Ongorora Nhaka Inorarama yeZimbabwe",
        "intro":
            "Dzidza nezvenhoroondo, tsika uye kuchengetedzwa kwenzvimbo dzakakosha dzenhaka yeZimbabwe.",
        "explore": "Ongorora Nzvimbo",
        "home": "Kumba",
        "sites": "Nzvimbo dzeNhaka",
        "quiz": "Muedzo weNhaka",
        "assistant": "Mubatsiri weNhaka",
        "robot": "Mashandiro Anoita ROBO GUARD",
        "history": "Nhoroondo",
        "culture": "Tsika neVanhu",
        "features": "Zvinokosha paNhaka",
        "protect": "Chengetedza Nhaka",
        "facts": "Waizviziva Here?",
        "location": "Nzvimbo",
        "unesco": "Nhaka yePasi Rose",
        "learn_more": "Dzidza Zvimwe",
        "correct": "Ndizvozvo!",
        "wrong": "Hazvisati zvanyatsokwana.",
        "next": "Mubvunzo Unotevera",
        "check": "Tarisa Mhinduro",
        "guardian": "Muchengeti weNhaka",
        "points": "Mapoinzi eNhaka",
        "question": "Mubvunzo",
        "language": "Mutauro",
        "back": "Dzokera kuNzvimbo dzeNhaka"
    }
}


def t(key):
    return TEXT[st.session_state.language].get(key, key)


# ============================================================
# SITE DATABASE
# ============================================================

SITES = {

    "Matobo Hills": {

        "icon": "🎨",

        "subtitle": {
            "English":
                "Rock Art • Sacred Landscapes • Living Traditions",
            "isiNdebele":
                "Imidwebo Yamadwala • Indawo Ezingcwele • Amasiko Aphilayo",
            "Shona":
                "Mifananidzo yeMatombo • Nzvimbo Dzinoera • Tsika Dzinorarama"
        },

        "summary": {
            "English":
                "A dramatic granite landscape containing ancient rock paintings, archaeological sites and important living spiritual traditions.",
            "isiNdebele":
                "Indawo yamadwala amakhulu elomlando wemidwebo yasendulo, izindawo zembali kanye lamasiko aqakathekileyo aphilayo.",
            "Shona":
                "Nzvimbo ine matombo makuru, mifananidzo yekare yematombo, nzvimbo dzezvakawanikwa zvekare uye tsika dzemweya dzichiri kurarama."
        },

        "history": {
            "English":
                """
Matobo Hills preserves evidence of a very long relationship between
people and the landscape. Rock shelters and archaeological sites show
occupation stretching back many thousands of years.

The area is especially famous for its ancient rock paintings. These
paintings help us understand earlier communities, their environment,
animals, beliefs and everyday life.
                """,

            "isiNdebele":
                """
IMatobo Hills ilobufakazi bokuthi abantu sebehlale njalo basebenzisa
indawo le okweminyaka eminengi kakhulu.

Imigede kanye lezindawo zamadwala zigcina imidwebo yasendulo
esinceda ukuqonda impilo, izinyamazana, indawo kanye lamasiko
abantu basendulo.
                """,

            "Shona":
                """
Matobo Hills ine humbowo hwekugara kwevanhu munzvimbo iyi
kwemakore akawanda zvikuru.

Mapako nematombo ane mifananidzo yekare inotibatsira kunzwisisa
mararamiro, mhuka, nharaunda netsika dzevanhu vekare.
                """
        },

        "culture": {
            "English":
                """
Matobo is not only an archaeological landscape. It is also a living
cultural and spiritual landscape.

Local communities continue to associate parts of the hills with sacred
places, ancestral traditions and spiritual practices. Respecting these
living traditions is part of protecting the site's heritage.
                """,

            "isiNdebele":
                """
IMatobo ayisiyo ndawo yembali kuphela. Iyindawo elamasiko
kanye lokukholwa okusaphilayo.

Kulezindawo ezibhekwa njengezingcwele futhi ezihlotshaniswa
lamadlozi kanye lamasiko omphakathi.
                """,

            "Shona":
                """
Matobo haisi nzvimbo yezvakare chete. Inoramba iri nzvimbo
ine tsika uye kukosha kwemweya.

Dzimwe nzvimbo dzichiri kuremekedzwa senzvimbo dzinoera uye
dzine hukama nemadzitateguru netsika dzemunharaunda.
                """
        },

        "location": {
            "English":
                "South-western Zimbabwe, south of Bulawayo.",
            "isiNdebele":
                "Eningizimu-ntshonalanga yeZimbabwe, eningizimu yeBulawayo.",
            "Shona":
                "Kumaodzanyemba kwakadziva kumadokero kweZimbabwe, kumaodzanyemba kweBulawayo."
        },

        "unesco": {
            "English":
                "Matobo Hills became a UNESCO World Heritage Site in 2003.",
            "isiNdebele":
                "IMatobo Hills yafakwa kuLuhlu lwe-UNESCO World Heritage ngo-2003.",
            "Shona":
                "Matobo Hills yakaiswa paUNESCO World Heritage List muna 2003."
        },

        "features": {
            "English": [
                ("🎨", "Rock Art",
                 "Paintings of people, animals and scenes from ancient life."),
                ("🪨", "Granite Landscape",
                 "Distinctive granite formations, caves and shelters."),
                ("🙏", "Sacred Heritage",
                 "Living cultural and spiritual traditions remain important."),
                ("🏺", "Archaeology",
                 "Rock shelters preserve evidence of ancient occupation.")
            ],

            "isiNdebele": [
                ("🎨", "Imidwebo Yamadwala",
                 "Imifanekiso yabantu, izinyamazana kanye lempilo yasendulo."),
                ("🪨", "Amadwala eGranite",
                 "Amadwala, imigede kanye lezindawo zokuphephela."),
                ("🙏", "Ilifa Elingcwele",
                 "Amasiko kanye lokukholwa kusaphila."),
                ("🏺", "Ezembali",
                 "Imigede igcina ubufakazi bempilo yasendulo.")
            ],

            "Shona": [
                ("🎨", "Mifananidzo yeMatombo",
                 "Mifananidzo yevanhu, mhuka uye mararamiro ekare."),
                ("🪨", "Matombo eGranite",
                 "Matombo, mapako nenzvimbo dzekuhwanda."),
                ("🙏", "Nhaka Inoera",
                 "Tsika uye kukosha kwemweya zvichiripo."),
                ("🏺", "Zvakawanikwa Zvekare",
                 "Mapako ane humbowo hwekugara kwevanhu vekare.")
            ]
        },

        "special": {
            "English": {
                "Pomongwe Cave":
                    "Pomongwe is an important Matobo rock shelter containing archaeological deposits and rock paintings.",
                "Bambata Cave":
                    "Bambata is one of Matobo's important prehistoric archaeological and rock-art sites.",
                "Nswatugi Cave":
                    "Nswatugi is well known for its archaeological importance and beautiful rock paintings."
            },

            "isiNdebele": {
                "Pomongwe Cave":
                    "IPomongwe ngomunye wemigede eqakathekileyo elebufakazi bembali kanye lemifanekiso yamadwala.",
                "Bambata Cave":
                    "IBambata iyindawo eqakathekileyo yembali yasendulo kanye lemifanekiso yamadwala.",
                "Nswatugi Cave":
                    "INswatugi yaziwa ngobuqakathekile bayo kwezembali kanye lemifanekiso yamadwala."
            },

            "Shona": {
                "Pomongwe Cave":
                    "Pomongwe ipako rakakosha rine humbowo hwezvakare nemifananidzo yematombo.",
                "Bambata Cave":
                    "Bambata inzvimbo yakakosha yezvakare nemifananidzo yematombo.",
                "Nswatugi Cave":
                    "Nswatugi inozivikanwa nekukosha kwayo munhoroondo nemifananidzo yematombo."
            }
        },

        "protect": {
            "English":
                """
Do not touch or rub rock paintings. Stay in designated visitor areas,
do not write on rocks, do not remove material and respect sacred places.
Even small actions can contribute to gradual deterioration.
                """,

            "isiNdebele":
                """
Ungathinti kumbe ukhuhle imidwebo yamadwala. Hlala ezindaweni
ezivunyelweyo, ungabhali emadwaleni njalo hlonipha izindawo ezingcwele.
                """,

            "Shona":
                """
Usabata kana kukwesha mifananidzo yematombo. Gara munzvimbo
dzakatenderwa, usanyora pamatombo uye remekedza nzvimbo dzinoera.
                """
        },

        "facts": {
            "English": [
                "Matobo contains a very high concentration of rock art.",
                "Its landscape remains culturally and spiritually important.",
                "Rock art is fragile and cannot simply be replaced if damaged."
            ],

            "isiNdebele": [
                "IMatobo ilemidwebo yamadwala eminengi kakhulu.",
                "Indawo le isaqakathekile emasikweni kanye kwezomoya.",
                "Imidwebo yamadwala ibuthakathaka njalo kayibuyiselwa lula nxa yonakele."
            ],

            "Shona": [
                "Matobo ine mifananidzo yakawanda zvikuru yematombo.",
                "Nzvimbo iyi ichiri yakakosha patsika nepamweya.",
                "Mifananidzo yematombo yakapfava uye haigoni kutsiviwa nyore kana yakuvadzwa."
            ]
        }
    },


    "Great Zimbabwe": {

        "icon": "🏰",

        "subtitle": {
            "English":
                "Stone Architecture • Shona Civilisation • Trade",
            "isiNdebele":
                "Ukwakhiwa Kwamatshe • Impucuko • Ukuthengiselana",
            "Shona":
                "Zvivakwa zveMatombo • Budiriro yeShona • Kutengeserana"
        },

        "summary": {
            "English":
                "A monumental stone-built centre that became one of southern Africa's most important political and trading centres.",
            "isiNdebele":
                "Indawo enkulu eyakhiwe ngamatshe eyaba yisikhungo esiqakathekileyo sezombuso kanye lokuthengiselana.",
            "Shona":
                "Nzvimbo huru yakavakwa nematombo yakava pakati pezvematongerwo enyika nekutengeserana kwakakosha."
        },

        "history": {
            "English":
                """
Great Zimbabwe developed into a major political, economic and cultural
centre between approximately the 11th and 15th centuries.

Its monumental architecture was created by indigenous African communities,
particularly ancestors of Shona-speaking peoples.
                """,

            "isiNdebele":
                """
IGreat Zimbabwe yakhula yaba yisikhungo esikhulu sezombuso,
ezomnotho kanye lamasiko phakathi kweminyaka yekhulu le-11
kusiya kwelama-15.

Izakhiwo zayo zakhiwa ngabantu bomdabu base-Afrika.
                """,

            "Shona":
                """
Great Zimbabwe yakakura kuva nzvimbo huru yezvematongerwo enyika,
hupfumi uye tsika kubva muzana remakore rechi11 kusvika rechi15.

Zvivakwa zvayo zvakagadzirwa nevanhu vemuAfrica vemuno,
kusanganisira madzitateguru evanhu vanotaura Shona.
                """
        },

        "culture": {
            "English":
                """
Great Zimbabwe represents the achievements of an indigenous African
civilisation. Its rulers, craftspeople, farmers and traders participated
in a sophisticated society connected to regional and international trade.

Its name and famous stone birds later became powerful symbols of modern
Zimbabwean identity.
                """,

            "isiNdebele":
                """
IGreat Zimbabwe itshengisa impumelelo yempucuko yabantu bomdabu
base-Afrika.

Ababusi, izingcitshi, abalimi kanye labathengisi babe yingxenye
yomphakathi owawuxhumene lokuthengiselana kwezindawo ezikhatshana.
                """,

            "Shona":
                """
Great Zimbabwe inoratidza budiriro huru hwevanhu vemuAfrica.

Vatongi, mhizha, varimi nevatengesi vaiva chikamu chenzanga yakanga
yakabatana nekutengeserana mudunhu uye nedzimwe nzvimbo dziri kure.
                """
        },

        "location": {
            "English":
                "Near Masvingo in south-eastern Zimbabwe.",
            "isiNdebele":
                "Eduze leMasvingo eningizimu-mpumalanga yeZimbabwe.",
            "Shona":
                "Pedyo neMasvingo kumaodzanyemba kwakadziva kumabvazuva kweZimbabwe."
        },

        "unesco": {
            "English":
                "Great Zimbabwe National Monument became a UNESCO World Heritage Site in 1986.",
            "isiNdebele":
                "IGreat Zimbabwe National Monument yafakwa ku-UNESCO World Heritage List ngo-1986.",
            "Shona":
                "Great Zimbabwe National Monument yakaiswa paUNESCO World Heritage List muna 1986."
        },

        "features": {
            "English": [
                ("🏰", "Great Enclosure",
                 "One of the site's most famous monumental structures."),
                ("🗼", "Conical Tower",
                 "A major stone feature inside the Great Enclosure."),
                ("🐦", "Zimbabwe Birds",
                 "Carved soapstone birds that became national symbols."),
                ("🧱", "Dry-Stone Walls",
                 "Granite stones carefully laid without mortar.")
            ],

            "isiNdebele": [
                ("🏰", "Great Enclosure",
                 "Esinye sezakhiwo ezaziwayo kakhulu kule indawo."),
                ("🗼", "Conical Tower",
                 "Isakhiwo esiqakathekileyo esingaphakathi kweGreat Enclosure."),
                ("🐦", "Inyoni zeZimbabwe",
                 "Inyoni eziqoshwe etsheni ezaba luphawu lwelizwe."),
                ("🧱", "Amadonga Angela Simende",
                 "Amatshe abekwa ngobuciko kungasetshenziswa simende.")
            ],

            "Shona": [
                ("🏰", "Great Enclosure",
                 "Chimwe chezvivakwa zvikuru zvinozivikanwa panzvimbo iyi."),
                ("🗼", "Conical Tower",
                 "Chivakwa chikuru chematombo mukati meGreat Enclosure."),
                ("🐦", "Zimbabwe Birds",
                 "Shiri dzakavezwa mudombo dzakava zviratidzo zvenyika."),
                ("🧱", "Madziro Asina Dhaka",
                 "Matombo akaiswa zvine hunyanzvi pasina mortar.")
            ]
        },

        "special": {
            "English": {
                "Great Enclosure":
                    "The Great Enclosure contains massive dry-stone walls and the famous Conical Tower.",
                "Conical Tower":
                    "The Conical Tower is a solid stone feature inside the Great Enclosure. Its exact historical purpose remains debated.",
                "Zimbabwe Birds":
                    "Carved soapstone birds discovered at Great Zimbabwe later became important national symbols.",
                "Ancient Trade":
                    "Great Zimbabwe participated in long-distance trade networks connecting inland southern Africa with wider commercial systems."
            },

            "isiNdebele": {
                "Great Enclosure":
                    "IGreat Enclosure ilamadonga amakhulu amatshe kanye leConical Tower.",
                "Conical Tower":
                    "IConical Tower yisakhiwo samatshe ngaphakathi kweGreat Enclosure.",
                "Zimbabwe Birds":
                    "Inyoni eziqoshwe etsheni eGreat Zimbabwe zaba luphawu oluqakathekileyo lweZimbabwe.",
                "Ancient Trade":
                    "IGreat Zimbabwe yayixhumene lenethiwekhi zokuthengiselana kwezindawo ezikhatshana."
            },

            "Shona": {
                "Great Enclosure":
                    "Great Enclosure ine madziro makuru ematombo uye Conical Tower.",
                "Conical Tower":
                    "Conical Tower chivakwa chematombo chiri mukati meGreat Enclosure.",
                "Zimbabwe Birds":
                    "Shiri dzakavezwa mudombo kuGreat Zimbabwe dzakava zviratidzo zvakakosha zveZimbabwe.",
                "Ancient Trade":
                    "Great Zimbabwe yaibatanidzwa mukutengeserana kwenzvimbo dziri kure."
            }
        },

        "protect": {
            "English":
                """
Do not climb fragile stone walls, move stones, remove artifacts or write
on structures. Visitors should follow designated routes and respect
restricted archaeological areas.
                """,

            "isiNdebele":
                """
Ungakhweli amadonga amatshe, ungasusi amatshe kumbe izinto zembali,
njalo ungabhali ezakhiweni. Landela indlela ezivunyelweyo.
                """,

            "Shona":
                """
Usakwira pamadziro ematombo, usafambisa matombo, usabvisa zvinhu
zvekare uye usanyora pazvivakwa. Tevera nzira dzakatenderwa.
                """
        },

        "facts": {
            "English": [
                "Great Zimbabwe gave modern Zimbabwe its name.",
                "Its walls were built without mortar.",
                "The Zimbabwe Bird became a national symbol."
            ],

            "isiNdebele": [
                "IGreat Zimbabwe yanceda ukunikeza ilizwe ibizo lalo.",
                "Amadonga ayo akhiwa kungasetshenziswa simende.",
                "Inyoni yeZimbabwe yaba luphawu lwelizwe."
            ],

            "Shona": [
                "Great Zimbabwe yakapa nyika yeZimbabwe zita rayo.",
                "Madziro ayo akavakwa pasina mortar.",
                "Zimbabwe Bird yakava chiratidzo chenyika."
            ]
        }
    },


    "Khami Ruins": {

        "icon": "🧱",

        "subtitle": {
            "English":
                "Torwa Heritage • Terraces • Decorative Stonework",
            "isiNdebele":
                "Ilifa leTorwa • AmaTerrace • Imidwebo Yamatshe",
            "Shona":
                "Nhaka yeTorwa • Matanho • Kushongedzwa kweMatombo"
        },

        "summary": {
            "English":
                "A major post-Great Zimbabwe centre known for terraced platforms, decorated stone walls and long-distance trade.",
            "isiNdebele":
                "Indawo enkulu eyakhula ngemva kweGreat Zimbabwe, eyaziwa ngama-terrace kanye lamadonga ahlotshiswe ngamatshe.",
            "Shona":
                "Nzvimbo huru yakakura mushure meGreat Zimbabwe, ichizivikanwa nematanho uye madziro ematombo akashongedzwa."
        },

        "history": {
            "English":
                """
Khami became an important centre after the decline of Great Zimbabwe.
It was associated with the Torwa dynasty and continued Zimbabwe's
tradition of sophisticated dry-stone architecture.

The settlement became a political, economic and trading centre.
                """,

            "isiNdebele":
                """
IKhami yakhula yaba yindawo eqakathekileyo ngemva kokwehla
kweGreat Zimbabwe.

Yayihlotshaniswa lababusi beTorwa futhi yaqhubekisela phambili
isiko lokwakha ngamatshe.
                """,

            "Shona":
                """
Khami yakava nzvimbo yakakosha mushure mekuderera kweGreat Zimbabwe.

Yakabatana nevatongi veTorwa uye yakaramba ichishandisa nzira
dzeZimbabwe dzekuvaka nematombo.
                """
        },

        "culture": {
            "English":
                """
Khami reflects an important period in Zimbabwe's political and cultural
history. Its architecture demonstrates continuity with earlier
stone-building traditions while also developing its own distinctive style.

Decorated wall patterns reveal the skill and creativity of its builders.
                """,

            "isiNdebele":
                """
IKhami imele isikhathi esiqakathekileyo sembali kanye lamasiko
eZimbabwe.

Amaphetheni asemadongeni atshengisa ubuciko kanye lobungcitshi
babakhi bendawo.
                """,

            "Shona":
                """
Khami inomiririra nguva yakakosha munhoroondo netsika dzeZimbabwe.

Mapatani emadziro anoratidza hunyanzvi uye kugona kwevakavaka nzvimbo iyi.
                """
        },

        "location": {
            "English":
                "About 22 kilometres west of Bulawayo.",
            "isiNdebele":
                "Cishe amakhilomitha angu-22 entshonalanga yeBulawayo.",
            "Shona":
                "Anenge makiromita 22 kumadokero kweBulawayo."
        },

        "unesco": {
            "English":
                "Khami Ruins National Monument became a UNESCO World Heritage Site in 1986.",
            "isiNdebele":
                "IKhami Ruins National Monument yafakwa ku-UNESCO World Heritage List ngo-1986.",
            "Shona":
                "Khami Ruins National Monument yakaiswa paUNESCO World Heritage List muna 1986."
        },

        "features": {
            "English": [
                ("👑", "Torwa Dynasty",
                 "Khami served as an important Torwa political centre."),
                ("🧱", "Terraced Platforms",
                 "Stone retaining walls created raised platforms."),
                ("🔶", "Decorative Walls",
                 "Chevron and chequered stone patterns are distinctive."),
                ("🌍", "Trade",
                 "Imported objects show links with long-distance commerce.")
            ],

            "isiNdebele": [
                ("👑", "Ababusi beTorwa",
                 "IKhami yaba yisikhungo esiqakathekileyo seTorwa."),
                ("🧱", "AmaTerrace",
                 "Amadonga amatshe ayesekela izindawo eziphakemeyo."),
                ("🔶", "Amadonga Ahlotshisiweyo",
                 "Amaphetheni amatshe ayisici esiqakathekileyo seKhami."),
                ("🌍", "Ukuthengiselana",
                 "Izinto ezivela kwezinye indawo zitshengisa ukuhweba kwezindawo ezikhatshana.")
            ],

            "Shona": [
                ("👑", "Torwa Dynasty",
                 "Khami yaiva nzvimbo yakakosha yehutongi hweTorwa."),
                ("🧱", "Matanho eMatombo",
                 "Madziro ematombo aigadzira nzvimbo dzakakwirira."),
                ("🔶", "Madziro Akashongedzwa",
                 "Mapatani ematombo akakosha pakuzivikanwa kweKhami."),
                ("🌍", "Kutengeserana",
                 "Zvinhu zvakabva kure zvinoratidza hukama hwekutengeserana.")
            ]
        },

        "special": {
            "English": {
                "Torwa Dynasty":
                    "Khami became an important capital associated with the Torwa dynasty after the decline of Great Zimbabwe.",
                "Terraces":
                    "Khami is famous for stone-faced terraces and platforms supported by retaining walls.",
                "Decorative Walls":
                    "Chevron and chequered patterns make Khami's stonework visually distinctive.",
                "Artifacts & Trade":
                    "Imported archaeological objects provide evidence that Khami participated in long-distance trade."
            },

            "isiNdebele": {
                "Torwa Dynasty":
                    "IKhami yaba yisikhungo esiqakathekileyo sababusi beTorwa ngemva kweGreat Zimbabwe.",
                "Terraces":
                    "IKhami yaziwa ngama-terrace kanye lezindawo eziphakemeyo ezisekelwe ngamatshe.",
                "Decorative Walls":
                    "Amaphetheni e-chevron kanye le-chequered ahlobisa amadonga eKhami.",
                "Artifacts & Trade":
                    "Izinto ezivela kwezinye indawo zitshengisa ukuthi iKhami yayihweba lezindawo ezikhatshana."
            },

            "Shona": {
                "Torwa Dynasty":
                    "Khami yakava nzvimbo yakakosha yeTorwa mushure mekuderera kweGreat Zimbabwe.",
                "Terraces":
                    "Khami inozivikanwa nematanho uye mapuratifomu akavakwa nemadziro ematombo.",
                "Decorative Walls":
                    "Chevron nechequered patterns ndizvo zvinoita madziro eKhami ave akasarudzika.",
                "Artifacts & Trade":
                    "Zvinhu zvakawanikwa kubva kune dzimwe nzvimbo zvinoratidza kutengeserana kwenguva refu."
            }
        },

        "protect": {
            "English":
                """
Stay on permitted routes, do not climb or disturb stone walls,
do not remove stones or artifacts and respect restricted archaeological areas.
                """,

            "isiNdebele":
                """
Hlala emzileni evunyelweyo, ungakhweli kumbe uphazamise amadonga
amatshe njalo ungasusi izinto zembali.
                """,

            "Shona":
                """
Gara munzira dzakatenderwa, usakwira kana kuvhiringidza madziro
ematombo uye usabvisa matombo kana zvinhu zvekare.
                """
        },

        "facts": {
            "English": [
                "Khami developed after the decline of Great Zimbabwe.",
                "Its decorated walls are one of its most distinctive features.",
                "Archaeological finds show participation in long-distance trade."
            ],

            "isiNdebele": [
                "IKhami yakhula ngemva kokwehla kweGreat Zimbabwe.",
                "Amadonga ahlotshiswe ngamatshe ayisici esikhulu seKhami.",
                "Izinto ezatholakala zitshengisa ukuthengiselana kwezindawo ezikhatshana."
            ],

            "Shona": [
                "Khami yakakura mushure mekuderera kweGreat Zimbabwe.",
                "Madziro ayo akashongedzwa ndiwo anonyanya kuizivisa.",
                "Zvakawanikwa zvinoratidza kutengeserana nenzvimbo dziri kure."
            ]
        }
    }
}


# ============================================================
# CHATBOT DATABASE
# ============================================================

CHAT_TOPICS = {

    "pomongwe": ("Matobo Hills", "Pomongwe Cave"),
    "bambata": ("Matobo Hills", "Bambata Cave"),
    "nswatugi": ("Matobo Hills", "Nswatugi Cave"),

    "great enclosure": ("Great Zimbabwe", "Great Enclosure"),
    "conical tower": ("Great Zimbabwe", "Conical Tower"),
    "zimbabwe bird": ("Great Zimbabwe", "Zimbabwe Birds"),
    "zimbabwe birds": ("Great Zimbabwe", "Zimbabwe Birds"),

    "torwa": ("Khami Ruins", "Torwa Dynasty"),
    "terrace": ("Khami Ruins", "Terraces"),
    "terraces": ("Khami Ruins", "Terraces"),
    "decorative wall": ("Khami Ruins", "Decorative Walls"),
    "chevron": ("Khami Ruins", "Decorative Walls")
}


def normalize(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s'-]", " ", text)
    return re.sub(r"\s+", " ", text)


def detect_site(question):

    q = normalize(question)

    if any(x in q for x in [
        "matobo",
        "matopos",
        "rock art",
        "rock painting",
        "pomongwe",
        "bambata",
        "nswatugi"
    ]):
        return "Matobo Hills"

    if any(x in q for x in [
        "great zimbabwe",
        "great enclosure",
        "conical tower",
        "zimbabwe bird"
    ]):
        return "Great Zimbabwe"

    if any(x in q for x in [
        "khami",
        "torwa",
        "terrace",
        "chevron"
    ]):
        return "Khami Ruins"

    return None


def chatbot_answer(question):

    q = normalize(question)
    language = st.session_state.language

    # Greeting
    if q in ["hello", "hi", "hey", "hie"]:

        if language == "English":
            return (
                "Hello! I am the ROBO GUARD Heritage Assistant. "
                "Ask me about Matobo Hills, Great Zimbabwe or Khami Ruins."
            )

        elif language == "isiNdebele":
            return (
                "Siyakwamukela! Ngingu ROBO GUARD Heritage Assistant. "
                "Buza ngeMatobo Hills, Great Zimbabwe kumbe Khami Ruins."
            )

        else:
            return (
                "Mauya! Ndiri ROBO GUARD Heritage Assistant. "
                "Bvunza nezveMatobo Hills, Great Zimbabwe kana Khami Ruins."
            )

    # Special topics
    for keyword, result in sorted(
        CHAT_TOPICS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):

        if keyword in q:

            site, topic = result

            special = SITES[site]["special"][language]

            if topic in special:
                return special[topic]

    site = detect_site(q)

    if not site:

        if language == "English":
            return (
                "Please mention Matobo Hills, Great Zimbabwe or Khami Ruins. "
                "You can ask about history, culture, location, UNESCO status, "
                "architecture, rock art, artifacts, trade or conservation."
            )

        elif language == "isiNdebele":
            return (
                "Ngicela utsho iMatobo Hills, Great Zimbabwe kumbe Khami Ruins. "
                "Ungabuza ngembali, amasiko, indawo, UNESCO kumbe ukuvikela ilifa."
            )

        else:
            return (
                "Ndapota taura Matobo Hills, Great Zimbabwe kana Khami Ruins. "
                "Unogona kubvunza nezvenhoroondo, tsika, UNESCO kana kuchengetedza nhaka."
            )

    data = SITES[site]

    if any(x in q for x in [
        "where",
        "located",
        "location",
        "how far"
    ]):
        return data["location"][language]

    if "unesco" in q or "world heritage" in q:
        return data["unesco"][language]

    if any(x in q for x in [
        "protect",
        "preserve",
        "touch",
        "damage",
        "conservation",
        "visitor rule"
    ]):
        return data["protect"][language]

    if any(x in q for x in [
        "culture",
        "people",
        "tradition",
        "spiritual"
    ]):
        return data["culture"][language]

    if any(x in q for x in [
        "history",
        "when",
        "built",
        "old",
        "date"
    ]):
        return data["history"][language]

    if any(x in q for x in [
        "important",
        "special",
        "significance",
        "why"
    ]):
        return data["summary"][language]

    return (
        data["summary"][language]
        + "\n\n"
        + data["history"][language].strip()
    )


# ============================================================
# QUIZ
# ============================================================

QUIZ = [

    {
        "mission": "DISCOVER",
        "question": {
