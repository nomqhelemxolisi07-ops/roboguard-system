import re
import streamlit as st
from html import escape

st.set_page_config(
    page_title="ROBO GUIDE | Zimbabwe Heritage Explorer",
    page_icon="🗿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Heritage visual theme
# -----------------------------
st.markdown(
    """
    <style>
    :root {
        --sand: #F3EBDD;
        --sand-2: #E7DAC6;
        --stone: #5D5146;
        --stone-dark: #302A25;
        --clay: #A65F3D;
        --gold: #B58A3A;
        --cream: #FFFDF8;
        --olive: #6C7350;
        --ink: #2B2723;
    }

    .stApp {
        background: linear-gradient(180deg, #F7F1E8 0%, #EFE4D4 100%);
        color: var(--ink);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #40372F 0%, #2E2925 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stSidebar"] * {
        color: #FFF8EE;
    }

    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stMarkdown p {
        color: #FFF8EE !important;
    }

    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.15);
        background: rgba(255,255,255,0.07);
        color: white;
        padding: 0.65rem 0.8rem;
        text-align: left;
        transition: 0.15s ease;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        border-color: #CBA85D;
        background: rgba(203,168,93,0.14);
    }

    .hero {
        background:
          radial-gradient(circle at top right, rgba(181,138,58,0.18), transparent 34%),
          linear-gradient(135deg, #5A493B 0%, #342D27 100%);
        color: #FFF8EE;
        padding: 2.2rem 2rem;
        border-radius: 22px;
        box-shadow: 0 16px 34px rgba(48,42,37,0.16);
        margin-bottom: 1.2rem;
        border: 1px solid rgba(255,255,255,0.08);
    }

    .hero h1 {
        margin: 0;
        font-size: clamp(2.2rem, 6vw, 4.7rem);
        line-height: 0.95;
        letter-spacing: 0.04em;
        color: #FFF7E7;
    }

    .hero h3 {
        margin: 0.65rem 0 0.4rem 0;
        color: #E6C982;
        font-weight: 600;
    }

    .hero p {
        margin: 0;
        max-width: 850px;
        font-size: 1.03rem;
        color: #F2E9DB;
    }

    .site-card, .info-card, .fact-card, .assistant-card, .quiz-card {
        background: rgba(255,253,248,0.96);
        border: 1px solid #D8C8B0;
        border-radius: 18px;
        padding: 1.15rem 1.2rem;
        box-shadow: 0 8px 22px rgba(62,49,37,0.07);
        height: 100%;
    }

    .site-card h3, .info-card h3, .fact-card h4 {
        color: #5B4536;
        margin-top: 0;
    }

    .badge {
        display: inline-block;
        background: #E7DAC6;
        color: #5D5146;
        border: 1px solid #D3C0A3;
        padding: 0.26rem 0.58rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        margin-right: 0.3rem;
        margin-bottom: 0.25rem;
    }

    .gold-strip {
        background: #E5D1A5;
        border-left: 6px solid #B58A3A;
        color: #453A30;
        padding: 1rem 1.1rem;
        border-radius: 12px;
        margin: 0.8rem 0 1rem 0;
    }

    .section-title {
        color: #5A4638;
        font-weight: 800;
        margin-top: 0.7rem;
        margin-bottom: 0.65rem;
    }

    .tiny {
        font-size: 0.84rem;
        color: #776B60;
    }

    .points {
        font-size: 1.45rem;
        font-weight: 800;
        color: #8A6425;
    }

    .chat-user {
        background: #EEE2D0;
        border-radius: 14px;
        padding: 0.85rem 1rem;
        margin: 0.45rem 0;
        border-left: 4px solid #A65F3D;
    }

    .chat-bot {
        background: #FFFDF8;
        border-radius: 14px;
        padding: 0.85rem 1rem;
        margin: 0.45rem 0 0.9rem 0;
        border-left: 4px solid #B58A3A;
        box-shadow: 0 4px 12px rgba(62,49,37,0.05);
    }

    .footer {
        margin-top: 2.4rem;
        padding: 1.1rem;
        text-align: center;
        border-top: 1px solid #D3C0A3;
        color: #6F6257;
        font-size: 0.88rem;
    }

    div.stButton > button {
        border-radius: 12px;
        border: 1px solid #BBA68D;
    }

    div.stButton > button:hover {
        border-color: #A65F3D;
        color: #6F432F;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Session state
# -----------------------------
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

# -----------------------------
# Translations
# -----------------------------
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
        "progress": "Progress",
        "achievement": "Achievement",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Heritage Assistant",
        "assistant_intro": "Ask about the history, builders, rock art, architecture, trade, UNESCO status, conservation or differences between the three sites.",
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
        "hero_text": "Hlola izindawo ezimangalisayo, izindaba, ubuciko bokwakha lamasiko ngendlela yokufunda ephendulanayo.",
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
        "progress": "Inqubekela phambili",
        "achievement": "Impumelelo",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Umsizi Wamagugu",
        "assistant_intro": "Buza ngomlando, abakhi, imidwebo yamadwala, izakhiwo, ezokuthengiselana, i-UNESCO, ukuvikelwa kumbe umehluko wezindawo ezintathu.",
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
        "hero_text": "Ongorora nzvimbo dzinoshamisa, nyaya, zvivakwa netsika kuburikidza nechiitiko chinodyidzana.",
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
        "progress": "Kufambira mberi",
        "achievement": "Kubudirira",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Mubatsiri weNhaka",
        "assistant_intro": "Bvunza nezvenhoroondo, vakavaka, rock art, zvivakwa, kutengeserana, UNESCO, kuchengetedza kana misiyano yenzvimbo nhatu.",
        "ask": "Bvunza mubvunzo wenhaka",
        "send": "Bvunza ROBO GUIDE",
        "clear": "Bvisa hurukuro",
        "footer": "ROBO GUIDE • Zimbabwe Heritage Explorer • WRO 2026",
    },
}

# -----------------------------
# Heritage site content
# -----------------------------
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
                "Matobo Hills has been occupied and used by communities for thousands of years. "
                "Its granite landscape contains archaeological evidence from the Stone Age and a "
                "remarkable concentration of rock paintings. The area also became important in later "
                "Ndebele history and continues to hold deep cultural and spiritual meaning.",
            "culture":
                "The hills are part of a living cultural landscape. Local communities maintain "
                "spiritual traditions connected with shrines, rain-making and the Mwari belief system. "
                "Respect for sacred places, community practices and ancestral connections is central "
                "to understanding Matobo.",
            "features": [
                "Granite kopjes and balancing rock formations shaped by erosion.",
                "Caves and rock shelters containing prehistoric paintings.",
                "One of southern Africa's richest concentrations of rock art.",
                "Sacred places associated with long-standing spiritual traditions.",
                "Archaeological remains showing a very long history of human occupation.",
            ],
            "unesco":
                "UNESCO inscribed Matobo Hills in 2003 as a cultural landscape. Its value comes "
                "from the long interaction between people and the granite environment, the outstanding "
                "rock-art record and the continuing importance of spiritual traditions.",
            "protection": [
                "Never touch, trace, wet or rub rock paintings.",
                "Do not write on rocks or remove stones, plants or artefacts.",
                "Use marked paths and follow the instructions of site staff and local custodians.",
                "Keep sacred places quiet and respectful.",
            ],
            "facts": [
                "Some rock shelters preserve images of people and animals painted by hunter-gatherer communities.",
                "The landscape is famous for huge rounded granite boulders and dramatic balancing formations.",
                "Matobo is both an archaeological landscape and a living spiritual landscape.",
            ],
            "significance":
                "Matobo Hills links natural geology, ancient art, archaeology, spirituality and living "
                "community traditions in one landscape.",
        },

        "isiNdebele": {
            "name": "Amagquma eMatobo",
            "subtitle": "Amadwala egranite, amasiko angcwele lemidwebo yasendulo",
            "location": "Matabeleland South, eduze leBulawayo",
            "inscribed": "2003",
            "criteria": "(iii), (v), (vi)",
            "history":
                "Amagquma eMatobo asetshenziswa ngabantu okwezinkulungwane zeminyaka. "
                "Kule ndawo kukhona ubufakazi bezikhathi zasendulo kanye lemidwebo eminingi yamadwala. "
                "Indawo iphinde ibaluleke emlandweni wamaNdebele futhi ilokhu ilenhlonipho enkulu "
                "kwezamasiko lezomoya.",
            "culture":
                "IMatobo yindawo yesiko eliphilayo. Imiphakathi ilondoloza amasiko ahlobene "
                "lezindawo ezingcwele, ukunxusa izulu kanye lenkolo kaMwari.",
            "features": [
                "Amagquma egranite lamadwala abukeka ebhalansile.",
                "Imihume lezindawo zokukhosela ezilemifanekiso yasendulo.",
                "Inani elikhulu lemidwebo yamadwala eningizimu ye-Afrika.",
                "Izindawo ezingcwele ezixhumene lamasiko omoya.",
                "Ubufakazi bemivubukulo bokuhlala kwabantu isikhathi eside.",
            ],
            "unesco":
                "I-UNESCO yafaka iMatobo Hills ohlwini ngo-2003 njengendawo yesiko. "
                "Ibaluleke ngenxa yobudlelwano obude phakathi kwabantu lendawo, "
                "imidwebo yamadwala kanye lamasiko omoya asaqhubekayo.",
            "protection": [
                "Ungathinti kumbe ukhuhle imidwebo yamadwala.",
                "Ungabhali emadwaleni futhi ungasusi amatshe kumbe izinto zakudala.",
                "Sebenzisa indlela ebekiweyo futhi ulalele iziqondiso zabasebenzi.",
                "Hlonipha ukuthula kwezindawo ezingcwele.",
            ],
            "facts": [
                "Eminye imihume ilondoloza imidwebo yabantu lezinyamazana yasendulo.",
                "IMatobo idume ngamatshe amakhulu egranite abhalansile.",
                "Iyindawo yemivubukulo kanye lendawo yesiko lomoya eliphilayo.",
            ],
            "significance":
                "IMatobo ihlanganisa ubunjalo bomhlaba, ubuciko basendulo, "
                "imivubukulo, ukholo lamasiko kanye lempilo yemiphakathi.",
        },

        "Shona": {
            "name": "Matobo Hills",
            "subtitle": "Matombo egranite, tsika dzinoyera uye rock art yekare",
            "location": "Matabeleland South, pedyo neBulawayo",
            "inscribed": "2003",
            "criteria": "(iii), (v), (vi)",
            "history":
                "Matobo Hills yakashandiswa nevanhu kwezviuru zvemakore. Munzvimbo iyi mune "
                "humbowo hwekugara kwevanhu vekare uye rock art yakawanda. Yakazove yakakosha "
                "munhoroondo yeNdebele uye ichiri nzvimbo ine kukosha kukuru kwetsika nemweya.",
            "culture":
                "Matobo inzvimbo yetsika mhenyu. Nharaunda dzinoramba dzichichengeta tsika "
                "dzine chekuita nenzvimbo dzinoyera, kunamatira mvura uye kutenda kwaMwari.",
            "features": [
                "Makomo egranite nematombo anoita seakatsiga pamusoro pemamwe.",
                "Mapako nematumba ane mifananidzo yekare pamadziro.",
                "Imwe yenzvimbo dzine rock art yakawanda kumaodzanyemba kweAfrica.",
                "Nzvimbo dzinoyera dzine hukama netsika dzemweya.",
                "Humbowo hwekuchera matongo hunoratidza kugara kwevanhu kwenguva refu.",
            ],
            "unesco":
                "UNESCO yakanyora Matobo Hills muna 2003 senzvimbo yetsika. "
                "Kukosha kwayo kunobva pahukama hwenguva refu pakati pevanhu nenzvimbo, "
                "rock art yakakosha uye tsika dzemweya dzichiri kurarama.",
            "protection": [
                "Usabata, kunyudza kana kukwesha rock art.",
                "Usanyora pamatombo uye usabvisa zvinhu zvekare.",
                "Famba munzira dzakatemwa uye tevera mirayiridzo yevashandi.",
                "Remekedza runyararo rwenzvimbo dzinoyera.",
            ],
            "facts": [
                "Mamwe mapako ane mifananidzo yevanhu nemhuka yakapendwa kare kare.",
                "Matobo inozivikanwa nematombo makuru egranite anoyevedza.",
                "Inobatanidza archaeology netsika dzemweya dzichiri kushandiswa.",
            ],
            "significance":
                "Matobo Hills inobatanidza geology, art yekare, archaeology, "
                "tsika nemweya munzvimbo imwe chete.",
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
                "Great Zimbabwe flourished mainly between the 11th and 15th centuries. "
                "It became a major political, economic and cultural centre built by ancestors "
                "of Shona-speaking communities. Its wealth was connected to cattle, agriculture, "
                "gold and long-distance trade linking the interior of southern Africa to Indian Ocean networks.",
            "culture":
                "The site reflects sophisticated African state formation, leadership, craftsmanship "
                "and social organisation. Its legacy remains central to national identity.",
            "features": [
                "The Hill Complex, built among natural granite boulders.",
                "The Great Enclosure, one of the site's best-known monumental structures.",
                "The Conical Tower inside the Great Enclosure.",
                "Valley Ruins made from carefully fitted dry-stone walls.",
                "Soapstone Zimbabwe Birds, important national symbols.",
            ],
            "unesco":
                "Great Zimbabwe National Monument was inscribed by UNESCO in 1986. "
                "UNESCO recognises its exceptional architecture, its testimony to a major African "
                "civilisation and its powerful historical and cultural significance.",
            "protection": [
                "Do not climb, sit or stand on ancient walls.",
                "Never remove stones or artefacts from the site.",
                "Keep to official paths and viewing areas.",
                "Avoid damage, graffiti and littering.",
            ],
            "facts": [
                "Its walls were built largely without mortar using carefully dressed stone blocks.",
                "Objects found at the site show contact with long-distance trade networks.",
                "The famous Zimbabwe Birds were carved from soapstone.",
            ],
            "significance":
                "Great Zimbabwe demonstrates the engineering, economic power and cultural sophistication "
                "of a major pre-colonial African civilisation.",
        },

        "isiNdebele": {
            "name": "Great Zimbabwe",
            "subtitle": "Idolobho elikhulu lamatshe eliyisibonakaliso seZimbabwe",
            "location": "Masvingo Province",
            "inscribed": "1986",
            "criteria": "(i), (iii), (vi)",
            "history":
                "IGreat Zimbabwe yakhula kakhulu phakathi kwekhulu le-11 nele-15. "
                "Yaba yisikhungo esikhulu sezombusazwe, umnotho lamasiko, yakhiwa ngabokhokho "
                "bemiphakathi ekhuluma isiShona.",
            "culture":
                "Indawo ibonisa ubuhlakani bokubusa, umsebenzi wezandla kanye lenhlangano yabantu base-Afrika.",
            "features": [
                "IHill Complex ephakathi kwamadwala egranite.",
                "IGreat Enclosure.",
                "IConical Tower phakathi kweGreat Enclosure.",
                "IValley Ruins ezakhiwe ngamatshe ngaphandle kodaka.",
                "IZimbabwe Birds ezabazwa ngetshe lesoapstone.",
            ],
            "unesco":
                "IGreat Zimbabwe National Monument yafakwa ku-UNESCO ngo-1986 ngenxa yobuciko bayo "
                "bezakhiwo kanye lokubaluleka kwayo emlandweni lasemasikweni.",
            "protection": [
                "Ungakhweli kumbe uhlale phezu kwemiduli yasendulo.",
                "Ungasusi amatshe kumbe izinto zemivubukulo.",
                "Hamba emizileni esemthethweni.",
                "Gwema ukubhala, ukulimaza kumbe ukulahla ingcekeza.",
            ],
            "facts": [
                "Imiduli eminengi yakhiwa ngaphandle kodaka.",
                "Izinto ezatholakala lapha zibonisa ukuthengiselana kwamabanga amade.",
                "IZimbabwe Birds zabazwa ngetshe lesoapstone.",
            ],
            "significance":
                "IGreat Zimbabwe ibonisa ubuciko bokwakha, amandla omnotho kanye lobuhlakani "
                "bempucuko enkulu yase-Afrika.",
        },

        "Shona": {
            "name": "Great Zimbabwe",
            "subtitle": "Guta guru rematombo uye chiratidzo cheZimbabwe",
            "location": "Masvingo Province",
            "inscribed": "1986",
            "criteria": "(i), (iii), (vi)",
            "history":
                "Great Zimbabwe yakabudirira zvikuru kubva muzana remakore rechi11 kusvika rechi15. "
                "Yakava nzvimbo huru yezvematongerwo enyika, hupfumi netsika, yakavakwa "
                "nemadzitateguru evanhu vanotaura chiShona.",
            "culture":
                "Nzvimbo iyi inoratidza hutongi hwakarongeka, hunyanzvi hwekugadzira uye "
                "kurongeka kwevanhu vemuAfrica.",
            "features": [
                "Hill Complex yakavakwa pakati pematombo egranite.",
                "Great Enclosure.",
                "Conical Tower iri mukati meGreat Enclosure.",
                "Valley Ruins dzine madziro edry-stone.",
                "Zimbabwe Birds dzakavezwa nesoapstone.",
            ],
            "unesco":
                "Great Zimbabwe National Monument yakanyorwa neUNESCO muna 1986 nekuda kwezvivakwa "
                "zvayo zvinoshamisa uye kukosha kwayo munhoroondo netsika.",
            "protection": [
                "Usakwira kana kugara pamusoro pemadziro ekare.",
                "Usabvisa matombo kana artefacts.",
                "Famba munzira dziri pamutemo.",
                "Dzivisa graffiti, kukuvara uye marara.",
            ],
            "facts": [
                "Madziro mazhinji akavakwa pasina mortar.",
                "Zvakawanikwa zvinoratidza kutengeserana kwemadaro marefu.",
                "Zimbabwe Birds dzakavezwa nesoapstone.",
            ],
            "significance":
                "Great Zimbabwe inoratidza hunyanzvi hwekuvaka, simba rehupfumi netsika "
                "dzebudiriro huru yeAfrica.",
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
                "Khami rose to prominence after the decline of Great Zimbabwe. From the 15th century "
                "into the 17th century it became an important centre of the Torwa state. "
                "The site continued regional traditions of elite stone building while developing "
                "its own distinctive terraced style.",
            "culture":
                "Khami reflects political authority, social organisation, craftsmanship and exchange "
                "in south-western Zimbabwe.",
            "features": [
                "Massive stone-faced terraces.",
                "Decorative dry-stone wall patterns.",
                "Retaining walls adapted to the natural landscape.",
                "Evidence of local production and long-distance trade.",
                "A distinctive architectural tradition related to Great Zimbabwe.",
            ],
            "unesco":
                "Khami Ruins National Monument was inscribed by UNESCO in 1986. "
                "It is recognised for its testimony to an important cultural tradition and "
                "its distinctive architecture.",
            "protection": [
                "Do not climb on terrace walls.",
                "Do not remove pottery, stone or archaeological material.",
                "Stay on visitor routes where provided.",
                "Report damage rather than moving objects yourself.",
            ],
            "facts": [
                "Khami is especially famous for terraced construction.",
                "Decorative walling patterns give the ruins a distinctive appearance.",
                "Trade goods found at Khami show connections to wider commercial networks.",
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
                "IKhami ibonisa amandla okubusa, ukuhleleka kwabantu, ubuciko bemisebenzi yezandla "
                "kanye lokuthengiselana.",
            "features": [
                "Amathala amakhulu avalwe ngamatshe.",
                "Imiduli yamatshe elemihlobiso.",
                "Imiduli yokubamba umhlabathi.",
                "Ubufakazi bokuthengiselana kwamabanga amade.",
                "Isitayela sokwakha esihlobene leGreat Zimbabwe.",
            ],
            "unesco":
                "IKhami Ruins National Monument yafakwa ku-UNESCO ngo-1986 ngenxa yobufakazi "
                "bamasiko abalulekileyo kanye lesitayela sayo sokwakha.",
            "protection": [
                "Ungakhweli phezu kwemiduli yamathala.",
                "Ungasusi amatshe kumbe izinto zemivubukulo.",
                "Hamba emizileni yezivakashi.",
                "Bika umonakalo kubasebenzi.",
            ],
            "facts": [
                "IKhami idume ngamathala ayo akhiwe ngamatshe.",
                "Imihlobiso yemiduli yenza indawo ibonakale yehlukile.",
                "Izinto ezatholakala lapha zibonisa ukuthengiselana lezinye izindawo.",
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
                "Khami inoratidza hutongi, kurongeka kwevanhu, hunyanzvi hwekugadzira "
                "uye kutengeserana.",
            "features": [
                "Terraces huru dzine madziro ematombo.",
                "Dry-stone walling ine mapatani ekushongedza.",
                "Retaining walls.",
                "Humbowo hwekutengeserana kwemadaro marefu.",
                "Nzira yekuvaka ine hukama neGreat Zimbabwe.",
            ],
            "unesco":
                "Khami Ruins National Monument yakanyorwa neUNESCO muna 1986 nekuda kweuchapupu "
                "hwayo hwetsika yakakosha uye chimiro chayo chakasiyana.",
            "protection": [
                "Usakwira pamadziro e terraces.",
                "Usabvisa pottery, matombo kana artefacts.",
                "Shandisa nzira dzevashanyi.",
                "Kana ukaona kukuvara, zviudze vashandi.",
            ],
            "facts": [
                "Khami inozivikanwa zvikuru nema terraces.",
                "Mapatani pamadziro anoipa chimiro chakasiyana.",
                "Trade goods dzinoratidza hukama nemisika iri kure.",
            ],
            "significance":
                "Khami inoratidza kuenderera nekushanduka kwetsika yekuvaka nematombo muZimbabwe.",
        },
    },
}

# -----------------------------
# Quiz
# -----------------------------
QUIZ = {
    "English": [
        (
            "Which heritage site is especially famous for prehistoric rock paintings?",
            ["Great Zimbabwe", "Matobo Hills", "Khami Ruins", "Victoria Falls"],
            1,
            "Matobo Hills contains one of southern Africa's richest concentrations of rock art.",
        ),
        (
            "In which year was Matobo Hills inscribed on the UNESCO World Heritage List?",
            ["1980", "1986", "2003", "2010"],
            2,
            "Matobo Hills was inscribed in 2003.",
        ),
        (
            "Which major structure is found at Great Zimbabwe?",
            ["Great Enclosure", "Stonehenge", "Acropolis", "Pyramids"],
            0,
            "The Great Enclosure is one of Great Zimbabwe's best-known structures.",
        ),
        (
            "How were many Great Zimbabwe walls constructed?",
            ["With concrete", "With steel", "Dry-stone masonry", "With timber"],
            2,
            "Many walls were built from carefully fitted stone without mortar.",
        ),
        (
            "The famous Zimbabwe Birds were carved mainly from what?",
            ["Soapstone", "Gold", "Wood", "Bronze"],
            0,
            "The Zimbabwe Birds were carved from soapstone.",
        ),
        (
            "Khami became an important centre of which state?",
            ["Torwa", "Roman", "Ottoman", "Aztec"],
            0,
            "Khami was an important centre of the Torwa state.",
        ),
        (
            "What architectural feature is especially associated with Khami?",
            ["Glass towers", "Stone-faced terraces", "Wooden palaces", "Brick domes"],
            1,
            "Khami is especially known for its extensive stone-faced terraces.",
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
            "Which statement best compares Great Zimbabwe and Khami?",
            [
                "They are exactly the same",
                "Both use stone-building traditions but Khami is especially known for terraces",
                "Neither contains stone walls",
                "Both were built in the 20th century",
            ],
            1,
            "Both belong to Zimbabwe's stone-building tradition, but Khami has a distinctive terraced style.",
        ),
    ],

    "isiNdebele": [
        (
            "Yiphi indawo eyaziwa kakhulu ngemidwebo yasendulo emadwaleni?",
            ["Great Zimbabwe", "Matobo Hills", "Khami Ruins", "Victoria Falls"],
            1,
            "IMatobo Hills ilenani elikhulu lemidwebo yasendulo emadwaleni.",
        ),
        (
            "IMatobo Hills yafakwa ku-UNESCO ngamuphi umnyaka?",
            ["1980", "1986", "2003", "2010"],
            2,
            "IMatobo Hills yafakwa ku-UNESCO ngo-2003.",
        ),
        (
            "Yisiphi isakhiwo esidumileyo eGreat Zimbabwe?",
            ["Great Enclosure", "Stonehenge", "Acropolis", "Pyramids"],
            0,
            "IGreat Enclosure ngesinye sezakhiwo ezaziwa kakhulu.",
        ),
        (
            "Imiduli eminengi yeGreat Zimbabwe yakhiwa njani?",
            ["Ngekhonkolo", "Ngensimbi", "Ngamatshe ngaphandle kodaka", "Ngezigodo"],
            2,
            "Amatshe ayehlanganiswa ngobuciko kungasetshenziswanga udaka.",
        ),
        (
            "IZimbabwe Birds zabazwa ngani?",
            ["Soapstone", "Igolide", "Isihlahla", "Bronze"],
            0,
            "IZimbabwe Birds zabazwa nge-soapstone.",
        ),
        (
            "IKhami yaba yisikhungo sombuso bani?",
            ["Torwa", "Roman", "Ottoman", "Aztec"],
            0,
            "IKhami yaba yisikhungo esibalulekileyo sombuso weTorwa.",
        ),
        (
            "Yisiphi isakhiwo esidume kakhulu eKhami?",
            ["Glass towers", "Amathala agqitshwe ngamatshe", "Wooden palaces", "Brick domes"],
            1,
            "IKhami idume ngamathala ayo amakhulu akhiwe ngamatshe.",
        ),
        (
            "Kumele wenzeni eduze kwemidwebo yasendulo?",
            ["Uyithinte", "Uyimanzise", "Ungayithinti", "Uyidwebe"],
            2,
            "Ukuthinta imidwebo kungayilimaza.",
        ),
        (
            "Yini eyaxhumanisa iGreat Zimbabwe lezinye izindawo?",
            ["Ukuthengiselana kwamabanga amade", "Izindiza", "Izitimela", "Ama-container"],
            0,
            "Ukuthengiselana kwamabanga amade kwaxhumanisa iGreat Zimbabwe lezinye izimakethe.",
        ),
        (
            "Yiphi inkulumo elungileyo ngeGreat Zimbabwe leKhami?",
            [
                "Zifana ngokupheleleyo",
                "Zombili zisebenzisa isiko lamatshe kodwa iKhami idume ngamathala",
                "Azila miduli yamatshe",
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
            "Matobo Hills yakanyorwa muna 2003.",
        ),
        (
            "Ndechipi chimwe chezvivakwa zvikuru paGreat Zimbabwe?",
            ["Great Enclosure", "Stonehenge", "Acropolis", "Pyramids"],
            0,
            "Great Enclosure ndechimwe chezvivakwa zvinonyanya kuzivikanwa.",
        ),
        (
            "Madziro mazhinji eGreat Zimbabwe akavakwa sei?",
            ["Nekongiri", "Nesimbi", "Dry-stone masonry", "Nemapuranga"],
            2,
            "Matombo akaiswa pamwe chete pasina mortar.",
        ),
        (
            "Zimbabwe Birds dzakavezwa nechii?",
            ["Soapstone", "Goridhe", "Huni", "Bronze"],
            0,
            "Zimbabwe Birds dzakavezwa nesoapstone.",
        ),
        (
            "Khami yakava nzvimbo yakakosha yehurumende ipi?",
            ["Torwa", "Roman", "Ottoman", "Aztec"],
            0,
            "Khami yaiva nzvimbo yakakosha yehurumende yeTorwa.",
        ),
        (
            "Chii chinonyanya kuzivikanwa paKhami?",
            ["Glass towers", "Stone-faced terraces", "Wooden palaces", "Brick domes"],
            1,
            "Khami inonyanya kuzivikanwa nema terraces ayo.",
        ),
        (
            "Unofanira kuita sei pedyo nerock art yekare?",
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
            "Ndeipi tsananguro yakarurama yeGreat Zimbabwe neKhami?",
            [
                "Dzakaenzana chose",
                "Dzose dzine stone-building tradition asi Khami inozivikanwa nema terraces",
                "Hadzina madziro ematombo",
                "Dzose dzakavakwa muzana remakore rechi20",
            ],
            1,
            "Dzose dzine stone-building tradition, asi Khami ine terraced style.",
        ),
    ],
}

# -----------------------------
# Assistant knowledge
# -----------------------------
ASSISTANT_KB = {
    "English": {
        "matobo":
            "Matobo Hills is a UNESCO cultural landscape near Bulawayo, inscribed in 2003. "
            "It is famous for granite landforms, caves, rock shelters, prehistoric rock art, "
            "archaeology and living spiritual traditions.",
        "great":
            "Great Zimbabwe flourished mainly from the 11th to 15th centuries. It was a major "
            "political, economic and cultural centre built by ancestors of Shona-speaking communities. "
            "Important features include the Hill Complex, Great Enclosure, Conical Tower, Valley Ruins "
            "and Zimbabwe Birds.",
        "khami":
            "Khami Ruins rose after the decline of Great Zimbabwe and became an important centre "
            "of the Torwa state. It is known for stone-faced terraces, retaining walls and decorative "
            "dry-stone patterns.",
        "compare":
            "Great Zimbabwe and Khami are both part of Zimbabwe's stone-building tradition. "
            "Great Zimbabwe is famous for monumental freestanding walls and the Great Enclosure, "
            "while Khami is especially known for terraces and decorative retaining walls. "
            "Matobo is different because its heritage includes rock art, granite landscapes and living sacred traditions.",
        "unesco":
            "Great Zimbabwe and Khami Ruins were inscribed on the UNESCO World Heritage List in 1986. "
            "Matobo Hills was inscribed in 2003.",
        "trade":
            "Great Zimbabwe and Khami both show evidence of long-distance exchange. Imported objects "
            "and ceramics demonstrate connections to wider regional and Indian Ocean trade networks.",
        "protect":
            "Good heritage conservation means not touching rock art, not climbing ancient walls, "
            "not removing artefacts or stones, staying on marked routes and avoiding graffiti or litter.",
        "birds":
            "The Zimbabwe Birds are famous soapstone sculptures associated with Great Zimbabwe. "
            "Their image became an important national symbol.",
        "torwa":
            "The Torwa state was an important political power in south-western Zimbabwe. "
            "Khami became one of its major centres.",
    },

    "isiNdebele": {
        "matobo":
            "IMatobo Hills yindawo yesiko ye-UNESCO eduze leBulawayo. Idume ngamatshe egranite, "
            "imihume, imidwebo yasendulo kanye lamasiko omoya.",
        "great":
            "IGreat Zimbabwe yakhula phakathi kwekhulu le-11 lele-15. Yaba yisikhungo esikhulu "
            "sezombusazwe, umnotho lamasiko.",
        "khami":
            "IKhami Ruins yakhula ngemva kokwehla kweGreat Zimbabwe futhi yaba yisikhungo sombuso weTorwa.",
        "compare":
            "IGreat Zimbabwe leKhami zombili zisebenzisa isiko lokwakha ngamatshe, kodwa iKhami "
            "idume ngamathala. IMatobo yona idume ngemidwebo yamadwala lamasiko angcwele.",
        "unesco":
            "IGreat Zimbabwe leKhami Ruins zafakwa ku-UNESCO ngo-1986. IMatobo Hills yafakwa ngo-2003.",
        "trade":
            "IGreat Zimbabwe leKhami zombili zibonisa ubufakazi bokuthengiselana kwamabanga amade.",
        "protect":
            "Ukuvikela amagugu kutsho ukungathinti imidwebo yamadwala, ukungakhweli imiduli "
            "yasendulo kanye lokungasusi izinto.",
        "birds":
            "IZimbabwe Birds yizithombe ezabazwa nge-soapstone ezihlobene leGreat Zimbabwe.",
        "torwa":
            "Umbuso weTorwa wawungamandla abalulekileyo eningizimu-ntshonalanga yeZimbabwe.",
    },

    "Shona": {
        "matobo":
            "Matobo Hills inzvimbo yetsika yeUNESCO pedyo neBulawayo. Inozivikanwa nematombo egranite, "
            "mapako, rock art yekare uye tsika dzemweya.",
        "great":
            "Great Zimbabwe yakabudirira kubva muzana remakore rechi11 kusvika rechi15. "
            "Yaiva nzvimbo huru yezvematongerwo enyika, hupfumi netsika.",
        "khami":
            "Khami Ruins yakasimukira mushure mekuderera kweGreat Zimbabwe uye yakava nzvimbo "
            "yakakosha yehurumende yeTorwa.",
        "compare":
            "Great Zimbabwe neKhami dzose dzine tsika yekuvaka nematombo. Khami inonyanya "
            "kuzivikanwa nema terraces, uku Matobo ichizivikanwa nerock art netsika dzinoyera.",
        "unesco":
            "Great Zimbabwe neKhami Ruins zvakanyorwa neUNESCO muna 1986. Matobo Hills yakanyorwa muna 2003.",
        "trade":
            "Great Zimbabwe neKhami zvose zvinoratidza humbowo hwekutengeserana kwemadaro marefu.",
        "protect":
            "Kuchengetedza nhaka kunoreva kusabata rock art, kusakwira pamadziro ekare uye kusabvisa artefacts.",
        "birds":
            "Zimbabwe Birds zvivezwa zvesoapstone zvakabatana neGreat Zimbabwe.",
        "torwa":
            "Hurumende yeTorwa yaiva simba rakakosha kumaodzanyemba-kumadokero kweZimbabwe.",
    },
}


def T(key):
    return UI[st.session_state.lang][key]


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


def assistant_answer(question, lang):
    q = re.sub(r"\s+", " ", question.lower().strip())
    kb = ASSISTANT_KB[lang]

    if any(x in q for x in [
        "compare", "difference", "differences",
        "umehluko", "qhathanisa", "musiyano", "enzanisa"
    ]):
        return kb["compare"]

    if any(x in q for x in [
        "unesco", "world heritage", "inscribed",
        "year", "unyaka", "gore"
    ]):
        return kb["unesco"]

    if any(x in q for x in [
        "protect", "conservation", "preserve",
        "damage", "vikela", "chengetedza", "kuchengetedza"
    ]):
        return kb["protect"]

    if any(x in q for x in [
        "trade", "commerce", "gold",
        "kutengesa", "ukuthengiselana"
    ]):
        return kb["trade"]

    if any(x in q for x in [
        "bird", "birds", "inyoni", "shiri"
    ]):
        return kb["birds"]

    if "torwa" in q:
        return kb["torwa"]

    if any(x in q for x in [
        "matobo", "rock art", "cave",
        "caves", "granite", "mwari",
        "imihume", "amadwala", "mapako"
    ]):
        return kb["matobo"]

    if any(x in q for x in [
        "great zimbabwe", "great enclosure",
        "conical tower", "hill complex", "soapstone"
    ]):
        return kb["great"]

    if any(x in q for x in [
        "khami", "terrace", "terraces",
        "retaining wall", "amathala"
    ]):
        return kb["khami"]

    if lang == "isiNdebele":
        return (
            "Ngiyakwazi ukuphendula ngeMatobo Hills, Great Zimbabwe leKhami Ruins. "
            "Buza ngomlando, imidwebo yamadwala, izakhiwo, iTorwa, ukuhweba, "
            "iUNESCO kumbe ukuvikela amagugu."
        )

    if lang == "Shona":
        return (
            "Ndinogona kupindura nezveMatobo Hills, Great Zimbabwe neKhami Ruins. "
            "Bvunza nezvenhoroondo, rock art, architecture, Torwa, trade, UNESCO "
            "kana kuchengetedza nhaka."
        )

    return (
        "I can help with Matobo Hills, Great Zimbabwe and Khami Ruins. "
        "Ask about history, rock art, architecture, the Torwa state, trade, "
        "UNESCO, conservation or comparisons."
    )


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.markdown("## 🗿 ROBO GUIDE")
    st.caption("Zimbabwe Heritage Explorer")

    selected_lang = st.selectbox(
        T("language"),
        ["English", "isiNdebele", "Shona"],
        index=["English", "isiNdebele", "Shona"].index(st.session_state.lang),
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
            key=f"sidebar_nav_{page}_{i}",
            use_container_width=True,
        ):
            go(page)


# -----------------------------
# Home page
# -----------------------------
def render_home():

    st.markdown(
        f"""
        <div class="hero">
            <h1>ROBO GUIDE</h1>
            <h3>{escape(T('hero_sub'))}</h3>
            <p>{escape(T('hero_text'))}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f"## {T('choose')}")

    cols = st.columns(3)

    for col, key in zip(
        cols,
        ["matobo", "great", "khami"]
    ):

        data = SITES[key][st.session_state.lang]

        with col:

            st.markdown(
                f"""
                <div class="site-card">
                    <div style="font-size:2.4rem">
                        {SITES[key]['emoji']}
                    </div>

                    <h3>{escape(data['name'])}</h3>

                    <p>{escape(data['subtitle'])}</p>

                    <span class="badge">
                        UNESCO {escape(data['inscribed'])}
                    </span>

                    <span class="badge">
                        {escape(data['criteria'])}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                T("open_site"),
                key=f"home_open_{key}",
                use_container_width=True,
            ):
                go(key)

    st.markdown("### Explore • Learn • Respect • Protect")

    a, b, c = st.columns(3)

    with a:
        st.markdown(
            """
            <div class="info-card">
                <h3>📚 Learn</h3>
                <p>
                Discover Zimbabwean history, architecture,
                archaeology and living traditions.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with b:
        st.markdown(
            """
            <div class="info-card">
                <h3>🎯 Challenge</h3>
                <p>
                Earn Heritage Points through the
                ROBO GUIDE Heritage Challenge.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c:
        st.markdown(
            """
            <div class="info-card">
                <h3>🌍 Protect</h3>
                <p>
                Learn simple actions visitors can take
                to help preserve heritage sites.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------
# Heritage site pages
# -----------------------------
def render_site(site_key):

    data = SITES[site_key][st.session_state.lang]

    st.markdown(
        f"""
        <div class="hero">
            <h1 style="font-size:3rem">
                {SITES[site_key]['emoji']} {escape(data['name'])}
            </h1>

            <h3>
                {escape(data['subtitle'])}
            </h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        T("location"),
        data["location"]
    )

    c2.metric(
        T("inscribed"),
        data["inscribed"]
    )

    c3.metric(
        T("criteria"),
        data["criteria"]
    )

    st.markdown(f"### {T('history')}")

    st.markdown(
        f"""
        <div class="info-card">
            <p>{escape(data['history'])}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f"### {T('culture')}")

    st.markdown(
        f"""
        <div class="info-card">
            <p>{escape(data['culture'])}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f"### {T('features')}")

    cols = st.columns(2)

    for i, item in enumerate(data["features"]):
        with cols[i % 2]:

            st.markdown(
                f"""
                <div class="fact-card">
                    <h4>◆</h4>
                    <p>{escape(item)}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(f"### {T('unesco')}")

    st.markdown(
        f"""
        <div class="gold-strip">
            {escape(data['unesco'])}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f"### {T('protect')}")

    pcols = st.columns(2)

    for i, item in enumerate(data["protection"]):

        with pcols[i % 2]:

            st.markdown(
                f"""
                <div class="fact-card">
                    <h4>🛡️</h4>
                    <p>{escape(item)}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(f"### {T('facts')}")

    for item in data["facts"]:
        st.markdown(f"- {item}")

    st.markdown(f"### {T('significance')}")

    st.info(data["significance"])

    left, right = st.columns(2)

    with left:

        if st.button(
            "🏆 " + T("quiz"),
            key=f"site_quiz_{site_key}",
            use_container_width=True,
        ):
            go("quiz")

    with right:

        if st.button(
            "💬 " + T("assistant"),
            key=f"site_assistant_{site_key}",
            use_container_width=True,
        ):
            go("assistant")


# -----------------------------
# Quiz
# -----------------------------
def render_quiz():

    st.markdown(
        f"""
        <div class="hero">

            <h1 style="font-size:3rem">
                🏆 {escape(T('quiz_title'))}
            </h1>

            <p>
                {escape(T('quiz_intro'))}
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    questions = QUIZ[st.session_state.lang]

    if st.session_state.quiz_finished:

        total = len(questions)

        pct = round(
            (
                st.session_state.quiz_score
                / total
            )
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
        idx / len(questions)
    )

    st.markdown(
        f"### {T('question')} "
        f"{idx + 1} / {len(questions)}"
    )

    st.markdown(
        f"""
        <div class="quiz-card">
            <h3>{escape(q)}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    choice = st.radio(
        "Choose one answer",
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


# -----------------------------
# Heritage Assistant
# -----------------------------
def render_assistant():

    st.markdown(
        f"""
        <div class="hero">

            <h1 style="font-size:3rem">
                💬 {escape(T('assistant_title'))}
            </h1>

            <p>
                {escape(T('assistant_intro'))}
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    suggestions = {

        "English": [
            "What is special about Matobo rock art?",
            "Who built Great Zimbabwe?",
            "Why is the Great Enclosure important?",
            "What is special about Khami terraces?",
            "What was the Torwa state?",
            "Compare all three heritage sites.",
        ],

        "isiNdebele": [
            "Yini eqakathekileyo ngemidwebo yaseMatobo?",
            "Ngobani abakha iGreat Zimbabwe?",
            "Kungani iGreat Enclosure iqakathekile?",
            "Yini ekhethekileyo ngamathala eKhami?",
            "Yayiyini iTorwa state?",
            "Qhathanisa zonke indawo ezintathu.",
        ],

        "Shona": [
            "Chii chakakosha nezverock art yeMatobo?",
            "Ndiani akavaka Great Zimbabwe?",
            "Great Enclosure yakakosha nei?",
            "Chii chakakosha nema terraces eKhami?",
            "Torwa state yaive chii?",
            "Enzanisa nzvimbo nhatu dzese.",
        ],
    }

    st.markdown("#### Quick questions")

    cols = st.columns(2)

    for i, prompt in enumerate(
        suggestions[st.session_state.lang]
    ):

        with cols[i % 2]:

            if st.button(
                prompt,
                key=f"assistant_suggestion_{st.session_state.lang}_{i}",
                use_container_width=True,
            ):

                answer = assistant_answer(
                    prompt,
                    st.session_state.lang,
                )

                st.session_state.chat.append(
                    (
                        prompt,
                        answer,
                    )
                )

                st.rerun()

    for question, answer in st.session_state.chat:

        st.markdown(
            f"""
            <div class="chat-user">
                <b>You:</b>
                {escape(question)}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="chat-bot">
                <b>ROBO GUIDE:</b>
                {escape(answer)}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with st.form(
        "assistant_form_unique",
        clear_on_submit=True,
    ):

        question = st.text_input(
            T("ask"),
            key="assistant_text_unique",
        )

        submitted = st.form_submit_button(
            T("send"),
            use_container_width=True,
        )

        if submitted and question.strip():

            answer = assistant_answer(
                question,
                st.session_state.lang,
            )

            st.session_state.chat.append(
                (
                    question.strip(),
                    answer,
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


# -----------------------------
# Router
# -----------------------------
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


# -----------------------------
# Footer
# -----------------------------
st.markdown(
    f"""
    <div class="footer">
        {escape(T('footer'))}
    </div>
    """,
    unsafe_allow_html=True,
)
