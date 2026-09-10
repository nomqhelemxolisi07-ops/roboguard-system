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


def html(content: str) -> None:
    st.markdown(textwrap.dedent(content).strip(), unsafe_allow_html=True)


st.markdown(
    """
    <style>
    :root{
        --earth:#5A4436;
        --earth2:#6D5544;
        --clay:#9A624A;
        --terracotta:#B77755;
        --ochre:#C79A4B;
        --sand:#E5D4BC;
        --sand2:#D4BEA0;
        --cream:#F4E9DA;
        --olive:#6C7052;
        --ink:#2E2722;
        --muted:#564A40;
        --line:#9A8269;
    }

    .stApp{
        background:
            radial-gradient(circle at 15% 10%, rgba(199,154,75,.12), transparent 24%),
            linear-gradient(180deg,#E5D4BC 0%,#D8C4A8 100%);
        color:var(--ink);
    }

    .block-container{
        max-width:1200px;
        padding-top:1.25rem;
        padding-bottom:2rem;
    }

    .heritage-band{
        height:14px;
        border-radius:10px;
        margin:0 0 1rem 0;
        background:
            linear-gradient(135deg, transparent 25%, #C79A4B 25%, #C79A4B 50%, transparent 50%) 0 0/28px 14px,
            linear-gradient(225deg, transparent 25%, #9A624A 25%, #9A624A 50%, transparent 50%) 14px 0/28px 14px,
            #5A4436;
        border:1px solid #816956;
    }

    [data-testid="stSidebar"]{
        background:linear-gradient(180deg, rgba(109,85,68,.98), rgba(76,59,48,.99));
        border-right:1px solid #907763;
    }

    [data-testid="stSidebar"] *{
        color:#F7ECDD !important;
    }

    [data-testid="stSidebar"] .stButton > button{
        width:100%;
        min-height:2.9rem;
        background:#7A6250;
        color:#FFF4E7 !important;
        border:1px solid #9B816C;
        border-radius:13px;
        font-weight:750;
    }

    [data-testid="stSidebar"] .stButton > button:hover{
        background:#8B6E58;
        border-color:#C79A4B;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div{
        background:#F0E2D0 !important;
        border:1px solid #A58B72 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] *{
        color:#332B26 !important;
    }

    .brand-box{padding:.4rem .2rem .75rem .2rem;}
    .brand-box h2{margin:0;color:#FFF1DC !important;letter-spacing:.04em;}
    .brand-box .slogan{color:#E2BE76 !important;font-size:.86rem;font-weight:700;margin-top:.25rem;}

    .hero{
        position:relative;
        overflow:hidden;
        background:linear-gradient(135deg, rgba(90,68,54,.98), rgba(116,82,63,.96));
        color:#FAEEDF;
        padding:2.35rem 2.2rem 2.1rem;
        border-radius:24px;
        border:1px solid #8E725E;
        box-shadow:0 14px 30px rgba(63,47,37,.16);
        margin-bottom:1.25rem;
    }

    .hero:after{
        content:"";
        position:absolute;
        right:-20px;
        bottom:-25px;
        width:220px;
        height:110px;
        opacity:.28;
        background:repeating-linear-gradient(45deg,transparent 0 12px,#D3A451 12px 20px,transparent 20px 32px);
        transform:rotate(-5deg);
    }

    .hero h1{
        position:relative;
        z-index:2;
        margin:0;
        color:#FFF3E1 !important;
        font-size:clamp(2.4rem,5vw,4.8rem);
        letter-spacing:.045em;
        line-height:1;
    }

    .hero h3{
        position:relative;
        z-index:2;
        color:#E7C780 !important;
        margin:.65rem 0 .4rem;
        font-weight:800;
    }

    .hero p{
        position:relative;
        z-index:2;
        color:#F6EBDD !important;
        margin:0;
        max-width:850px;
        font-size:1.06rem;
        line-height:1.6;
    }

    .slogan-pill{
        display:inline-block;
        position:relative;
        z-index:2;
        margin-top:1rem;
        padding:.42rem .78rem;
        border-radius:999px;
        border:1px solid rgba(239,205,132,.55);
        color:#F2D08C;
        background:rgba(64,48,38,.3);
        font-size:.88rem;
        font-weight:800;
    }

    .site-card,.info-card,.fact-card,.quiz-card,.chat-user,.chat-bot,.stat-card{
        background:#E0CCB2;
        color:#2F2823;
        border:1px solid #A68B70;
        border-radius:18px;
        box-shadow:0 6px 16px rgba(74,55,43,.09);
    }

    .site-card{
        min-height:255px;
        padding:1.25rem;
        border-top:6px solid #9A624A;
    }

    .site-card h3{color:#3A2E28 !important;margin:.55rem 0 .3rem;font-size:1.35rem;}
    .site-card p,.info-card p,.fact-card p,.chat-user,.chat-bot{color:#40352E !important;line-height:1.55;}
    .site-icon{font-size:2.45rem;line-height:1;}

    .badge{
        display:inline-block;
        margin:.4rem .28rem 0 0;
        padding:.32rem .66rem;
        border-radius:999px;
        background:#735A49;
        color:#FFF0DD;
        border:1px solid #5F4A3C;
        font-size:.78rem;
        font-weight:800;
    }

    .info-card{padding:1.15rem 1.2rem;border-left:5px solid #8C6B4E;}
    .fact-card{padding:1.05rem 1.1rem;margin-bottom:.7rem;min-height:118px;}
    .fact-card h4{color:#6B4937 !important;margin:0 0 .35rem;}

    .unesco-card{
        background:#C9AA73;
        border:1px solid #98733B;
        border-left:7px solid #76572D;
        border-radius:16px;
        padding:1.1rem 1.2rem;
        color:#2D261F !important;
        box-shadow:0 5px 14px rgba(74,55,43,.08);
    }

    .stat-card{padding:.8rem 1rem;text-align:center;min-height:95px;}
    .stat-label{color:#615045;font-size:.8rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;}
    .stat-value{color:#352B25;font-size:1.18rem;font-weight:850;margin-top:.25rem;}

    .quiz-card{padding:1.2rem;border-top:5px solid #8B6545;margin-bottom:.8rem;}
    .quiz-card h3{margin:0;color:#342A24 !important;}

    .chat-user{padding:1rem 1.1rem;margin:.6rem 0;background:#D3B39F;border-left:6px solid #955B42;}
    .chat-bot{padding:1rem 1.1rem;margin:.6rem 0 1rem;background:#D5C09B;border-left:6px solid #A87D32;}
    .chat-user strong,.chat-bot strong{color:#2F2722 !important;}

    div[data-testid="stTextInput"] label,
    div[data-testid="stRadio"] label,
    div[data-testid="stMetric"] label,
    .stMarkdown,.stMarkdown p,.stMarkdown li,h1,h2,h3,h4,h5,h6{color:#332B25;}

    div[data-testid="stTextInput"] input{
        background:#F2E4D1 !important;
        color:#2E2722 !important;
        border:1px solid #8C755F !important;
        border-radius:11px !important;
    }

    div[data-testid="stTextInput"] input::placeholder{color:#65584D !important;opacity:1 !important;}

    div[data-testid="stRadio"]{
        background:#DDC7AA;
        border:1px solid #A78D71;
        border-radius:14px;
        padding:.45rem .7rem;
    }

    div.stButton > button,div[data-testid="stFormSubmitButton"] button{
        background:#765B47;
        color:#FFF0DE !important;
        border:1px solid #604A3B;
        border-radius:12px;
        font-weight:800;
        min-height:2.75rem;
    }

    div.stButton > button:hover,div[data-testid="stFormSubmitButton"] button:hover{
        background:#896B53;
        border-color:#A67C3B;
        color:#FFF7EC !important;
    }

    [data-testid="stMetric"]{
        background:#D9C2A4;
        border:1px solid #A58A6E;
        border-radius:14px;
        padding:.72rem .9rem;
    }

    [data-testid="stMetricValue"]{color:#352B25 !important;}
    [data-testid="stAlert"]{border-radius:13px;}

    .source-note{
        background:#D2BEA3;
        border:1px dashed #9C8268;
        border-radius:12px;
        padding:.8rem 1rem;
        color:#55483E;
        font-size:.86rem;
        margin-top:1rem;
    }

    .footer{
        margin-top:2.4rem;
        padding:1.2rem .8rem;
        border-top:1px solid #9B8168;
        text-align:center;
        color:#4E4138;
        font-size:.9rem;
    }

    .footer strong{color:#6D4B37;}

    @media(max-width:760px){
        .hero{padding:1.6rem 1.35rem;}
        .site-card{min-height:auto;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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

UI = {
    "English": {
        "language": "Language", "explore": "Explore ROBO GUIDE", "home": "Home",
        "matobo": "Matobo Hills", "great": "Great Zimbabwe", "khami": "Khami Ruins",
        "quiz": "Heritage Challenge", "assistant": "Heritage Assistant",
        "hero_sub": "Discover Zimbabwe's Living Heritage",
        "hero_text": "Explore the stories, architecture, art and living traditions of three remarkable Zimbabwean World Heritage Sites.",
        "choose": "Choose a heritage site", "open_site": "Explore", "history": "History",
        "culture": "Culture & People", "features": "Major Features", "unesco": "UNESCO World Heritage",
        "protect": "Respect & Protection", "facts": "Interesting Facts", "significance": "Why It Matters",
        "location": "Location", "inscribed": "UNESCO inscription", "criteria": "Criteria",
        "quiz_title": "Heritage Challenge", "quiz_intro": "Test your knowledge and collect Heritage Points.",
        "question": "Question", "submit": "Check answer", "next": "Next question", "restart": "Restart challenge",
        "correct": "Correct!", "incorrect": "Not quite.", "score": "Score", "points": "Heritage Points",
        "achievement": "Achievement", "guide": "Heritage Guide", "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Heritage Assistant",
        "assistant_intro": "Ask detailed questions about dates, builders, rock art, architecture, trade, UNESCO status, conservation and comparisons.",
        "ask": "Ask a heritage question", "send": "Ask ROBO GUIDE", "clear": "Clear conversation",
        "quick": "Quick questions", "footer": "Zimbabwe Heritage Explorer • WRO 2026",
    },
    "isiNdebele": {
        "language": "Ulimi", "explore": "Hlola i-ROBO GUIDE", "home": "Ikhaya",
        "matobo": "Amagquma eMatobo", "great": "Great Zimbabwe", "khami": "Amanxiwa eKhami",
        "quiz": "Umncintiswano Wamagugu", "assistant": "Umsizi Wamagugu",
        "hero_sub": "Thola Amagugu Aphilayo eZimbabwe",
        "hero_text": "Hlola izindaba, izakhiwo, ubuciko lamasiko aphilayo ezindawo ezintathu zamagugu eZimbabwe.",
        "choose": "Khetha indawo yamagugu", "open_site": "Hlola", "history": "Umlando",
        "culture": "Amasiko Labantu", "features": "Izinto Ezisemqoka", "unesco": "Amagugu Omhlaba e-UNESCO",
        "protect": "Inhlonipho Lokuvikela", "facts": "Amaqiniso Athakazelisayo", "significance": "Kungani Ibalulekile",
        "location": "Indawo", "inscribed": "Ukufakwa ku-UNESCO", "criteria": "Imigomo",
        "quiz_title": "Umncintiswano Wamagugu", "quiz_intro": "Hlola ulwazi lwakho uzuze ama-Heritage Points.",
        "question": "Umbuzo", "submit": "Hlola impendulo", "next": "Umbuzo olandelayo", "restart": "Qalisa kutsha",
        "correct": "Kulungile!", "incorrect": "Akukabi yikho.", "score": "Amaphuzu", "points": "Heritage Points",
        "achievement": "Impumelelo", "guide": "Heritage Guide", "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Umsizi Wamagugu",
        "assistant_intro": "Buza ngeminyaka, abakhi, imidwebo yamadwala, izakhiwo, ukuhweba, UNESCO lokuvikelwa.",
        "ask": "Buza umbuzo wamagugu", "send": "Buza i-ROBO GUIDE", "clear": "Sula ingxoxo",
        "quick": "Imibuzo esheshayo", "footer": "Zimbabwe Heritage Explorer • WRO 2026",
    },
    "Shona": {
        "language": "Mutauro", "explore": "Ongorora ROBO GUIDE", "home": "Musha",
        "matobo": "Matobo Hills", "great": "Great Zimbabwe", "khami": "Khami Ruins",
        "quiz": "Dambudziko reNhaka", "assistant": "Mubatsiri weNhaka",
        "hero_sub": "Ziva Nhaka Mhenyu yeZimbabwe",
        "hero_text": "Ongorora nyaya, zvivakwa, art netsika mhenyu dzenzvimbo nhatu dzeWorld Heritage muZimbabwe.",
        "choose": "Sarudza nzvimbo yenhaka", "open_site": "Ongorora", "history": "Nhoroondo",
        "culture": "Tsika neVanhu", "features": "Zvinhu Zvikuru", "unesco": "UNESCO World Heritage",
        "protect": "Kuremekedza & Kuchengetedza", "facts": "Zvinonakidza Kuziva", "significance": "Kukosha Kwayo",
        "location": "Nzvimbo", "inscribed": "UNESCO inscription", "criteria": "Maitiro",
        "quiz_title": "Dambudziko reNhaka", "quiz_intro": "Edza ruzivo rwako uye uwane Heritage Points.",
        "question": "Mubvunzo", "submit": "Tarisa mhinduro", "next": "Mubvunzo unotevera", "restart": "Tangazve",
        "correct": "Wagona!", "incorrect": "Hausati warurama.", "score": "Zvawabudirira", "points": "Heritage Points",
        "achievement": "Kubudirira", "guide": "Heritage Guide", "guardian": "Heritage Guardian",
        "assistant_title": "ROBO GUIDE Mubatsiri weNhaka",
        "assistant_intro": "Bvunza nezvemakore, vakavaka, rock art, architecture, trade, UNESCO nekuchengetedza.",
        "ask": "Bvunza mubvunzo wenhaka", "send": "Bvunza ROBO GUIDE", "clear": "Bvisa hurukuro",
        "quick": "Mibvunzo inokurumidza", "footer": "Zimbabwe Heritage Explorer • WRO 2026",
    },
}


def T(key: str) -> str:
    return UI[st.session_state.lang][key]


def go(page: str) -> None:
    st.session_state.page = page
    st.rerun()


def reset_quiz() -> None:
    st.session_state.quiz_index = 0
    st.session_state.quiz_score = 0
    st.session_state.quiz_points = 0
    st.session_state.quiz_answered = False
    st.session_state.quiz_choice = None
    st.session_state.quiz_finished = False


SITES = {
    "matobo": {
        "emoji": "⛰️",
        "English": {
            "name": "Matobo Hills", "subtitle": "Granite landscapes, ancient rock art and living sacred traditions",
            "location": "Matabeleland South, Zimbabwe", "inscribed": "2003", "criteria": "(iii), (v), (vi)",
            "history": "Matobo Hills preserves an exceptionally long record of human interaction with the landscape. UNESCO notes archaeological evidence of occupation extending for at least 500,000 years, while the rock-art tradition dates back at least 13,000 years.",
            "culture": "Matobo is a living cultural and spiritual landscape. Sacred shrines and places in the hills continue to be used, and the Mwari religious tradition is closely associated with Matobo.",
            "features": ["Distinctive granite kopjes, balancing boulders and natural rock shelters.", "One of the highest concentrations of rock art in southern Africa.", "Rock paintings showing people, animals and aspects of Stone Age life.", "Sacred shrines associated with continuing spiritual traditions.", "Archaeological evidence spanning an exceptionally long period of human occupation."],
            "unesco": "Matobo Hills was inscribed on the UNESCO World Heritage List in 2003 under cultural criteria (iii), (v) and (vi). UNESCO highlights its outstanding rock art, the long relationship between communities and landscape, and the continuing Mwari religious tradition.",
            "protect": ["Never touch, trace, wet or rub rock paintings.", "Do not scratch, write or draw on rock surfaces.", "Do not remove archaeological objects, stones or cultural material.", "Respect sacred places and follow authorised site guidance."],
            "facts": ["UNESCO states that Matobo's rock art dates back at least 13,000 years.", "The hills contain abundant natural shelters formed by huge granite boulders.", "Matobo combines archaeology, rock art, landscape and living spirituality."],
            "significance": "Matobo Hills is important because it preserves ancient artistic expression, deep archaeological time, dramatic geology and cultural traditions that remain meaningful to communities.",
        },
        "isiNdebele": {
            "name": "Amagquma eMatobo", "subtitle": "Amadwala egranite, imidwebo yasendulo lamasiko angcwele aphilayo",
            "location": "Matabeleland South, Zimbabwe", "inscribed": "2003", "criteria": "(iii), (v), (vi)",
            "history": "IMatobo ilobufakazi bokuhlala kwabantu obude kakhulu. I-UNESCO ithi ubufakazi bemivubukulo bufinyelela okungenani eminyakeni engu-500,000, kanti imidwebo yamadwala ihlehlela emuva okungenani iminyaka engu-13,000.",
            "culture": "IMatobo yindawo yesiko lomoya elisaphilayo. Izindawo ezingcwele zisasebenza emphakathini, futhi isiko likaMwari lihlobene kakhulu lamagquma.",
            "features": ["Amagquma egranite lamatshe amakhulu abhalansile.", "Enye yezindawo ezilemidwebo yamadwala eminengi kakhulu eningizimu ye-Afrika.", "Imidwebo ekhombisa abantu lezinyamazana.", "Izindawo ezingcwele ezisetshenziswa emasikweni omoya.", "Ubufakazi bemivubukulo besikhathi eside kakhulu."],
            "unesco": "IMatobo Hills yafakwa ku-UNESCO ngo-2003 ngaphansi kwemigomo (iii), (v) lo-(vi), ngenxa yemidwebo yamadwala, ubudlelwano phakathi kwabantu lendawo kanye lesiko likaMwari.",
            "protect": ["Ungathinti, umanzise kumbe ukhuhle imidwebo yamadwala.", "Ungabhali kumbe udwebe emadwaleni.", "Ungasusi izinto zemivubukulo.", "Hlonipha izindawo ezingcwele futhi ulalele abaqondisi."],
            "facts": ["Imidwebo ihlehlela emuva okungenani iminyaka engu-13,000.", "Amatshe amakhulu enza izindawo zokukhosela zemvelo.", "IMatobo ihlanganisa imivubukulo, ubuciko lamasiko omoya."],
            "significance": "IMatobo ibalulekile ngoba ihlanganisa ubuciko basendulo, umlando omude, indawo emangalisayo kanye lamasiko asaphila.",
        },
        "Shona": {
            "name": "Matobo Hills", "subtitle": "Matombo egranite, rock art yekare netsika dzinoyera dzichiri kurarama",
            "location": "Matabeleland South, Zimbabwe", "inscribed": "2003", "criteria": "(iii), (v), (vi)",
            "history": "Matobo ine humbowo hwenguva refu kwazvo hwekugara kwevanhu. UNESCO inoti archaeology inoratidza kugara kwevanhu kwemakore angangoita 500,000 kana kupfuura, uye rock art inodzokera kumashure kwemakore angangoita 13,000.",
            "culture": "Matobo inzvimbo yetsika nemweya ichiri kushandiswa. Nzvimbo dzinoyera dzichiri kukosha, uye tsika yaMwari ine hukama hwakasimba nemakomo aya.",
            "features": ["Makomo egranite nematombo makuru anoyevedza.", "Imwe yenzvimbo dzine rock art yakawanda kumaodzanyemba kweAfrica.", "Mifananidzo inoratidza vanhu nemhuka.", "Nzvimbo dzinoyera dzine tsika dzemweya.", "Humbowo hwearchaeology hwenguva refu kwazvo."],
            "unesco": "Matobo Hills yakanyorwa neUNESCO muna 2003 pasi pemaitiro (iii), (v) na(vi), nekuda kwerock art, hukama hwevanhu nenzvimbo uye tsika yaMwari.",
            "protect": ["Usabata, kunyudza kana kukwesha rock art.", "Usanyora kana kudhirowa pamatombo.", "Usabvisa zvinhu zvearchaeology.", "Remekedza nzvimbo dzinoyera uye tevera mirayiridzo."],
            "facts": ["UNESCO inoti rock art yeMatobo ine makore angangoita 13,000 kana kupfuura.", "Matombo makuru anogadzira natural shelters.", "Matobo inosanganisa archaeology, art, landscape netsika dzemweya."],
            "significance": "Matobo yakakosha nekuti inosanganisa art yekare, nhoroondo refu, geology inoshamisa uye tsika dzichiri kurarama.",
        },
    },
    "great": {
        "emoji": "🏛️",
        "English": {
            "name": "Great Zimbabwe", "subtitle": "A monumental Shona stone city and national symbol",
            "location": "About 30 km from Masvingo, Zimbabwe", "inscribed": "1986", "criteria": "(i), (iii), (vi)",
            "history": "Great Zimbabwe was founded in the 11th century and the World Heritage property was built principally between about 1100 and 1450 AD. It became a major political, economic and cultural centre of Shona civilisation and an important trading centre.",
            "culture": "Great Zimbabwe demonstrates sophisticated African state organisation, specialised craftsmanship, architecture and long-distance exchange. Its name and the famous stone-carved birds became powerful symbols of modern Zimbabwe.",
            "features": ["The Hill Ruins, occupied continuously from the 11th to the 15th centuries.", "The Great Enclosure, largely dating to the 14th century.", "The high Conical Tower inside the Great Enclosure.", "Valley Ruins with domestic structures and dry-stone masonry.", "Steatite (soapstone) bird sculptures associated with ritual and national symbolism."],
            "unesco": "Great Zimbabwe National Monument was inscribed on the UNESCO World Heritage List in 1986 under criteria (i), (iii) and (vi). UNESCO describes it as a unique testimony to Shona civilisation between the 11th and 15th centuries.",
            "protect": ["Do not climb, sit or stand on ancient stone walls.", "Do not move or remove stones and archaeological material.", "Follow authorised visitor paths and site instructions.", "Avoid graffiti, littering and actions that could destabilise masonry."],
            "facts": ["UNESCO dates the principal construction of the property to about 1100–1450 AD.", "The Great Enclosure dates mainly to the 14th century.", "The city was an important centre of trade and is renowned for exceptional dry-stone craftsmanship."],
            "significance": "Great Zimbabwe is one of Africa's most important archaeological monuments and a powerful demonstration of indigenous African urbanism, engineering, political organisation and trade.",
        },
        "isiNdebele": {
            "name": "Great Zimbabwe", "subtitle": "Idolobho elikhulu lamatshe lamaShona lophawu lwelizwe",
            "location": "Cishe 30 km ukusuka eMasvingo, Zimbabwe", "inscribed": "1986", "criteria": "(i), (iii), (vi)",
            "history": "IGreat Zimbabwe yasungulwa ngekhulu le-11, futhi indawo enkulu yakhiwa phakathi kuka-1100 lo-1450 AD. Yaba yisikhungo esikhulu sempucuko yamaShona, sezombusazwe, umnotho lamasiko.",
            "culture": "Indawo ikhombisa ukuhleleka kombuso wase-Afrika, ubuciko bokwakha, umsebenzi wezandla kanye lokuthengiselana kwamabanga amade.",
            "features": ["IHill Ruins eyahlalwa kusukela ngekhulu le-11 kusiya kwele-15.", "IGreat Enclosure, ikakhulu yekhulu le-14.", "IConical Tower.", "IValley Ruins le-dry-stone masonry.", "Izinyoni ezabazwa nge-steatite/soapstone."],
            "unesco": "IGreat Zimbabwe National Monument yafakwa ku-UNESCO ngo-1986 ngaphansi kwemigomo (i), (iii) lo-(vi). I-UNESCO iyichaza njengobufakazi obubalulekileyo bempucuko yamaShona phakathi kwekhulu le-11 lele-15.",
            "protect": ["Ungakhweli kumbe uhlale phezu kwemiduli yasendulo.", "Ungasusi amatshe kumbe izinto zemivubukulo.", "Sebenzisa imizila esemthethweni.", "Gwema ukubhala, ukulahla ingcekeza lokulimaza imiduli."],
            "facts": ["Ukwakhiwa okuyinhloko kwenzeka cishe phakathi kuka-1100 lo-1450 AD.", "IGreat Enclosure ingeyekhulu le-14 ikakhulu.", "IGreat Zimbabwe yayiyisikhungo esibalulekileyo sokuthengiselana."],
            "significance": "IGreat Zimbabwe iyisibonelo esikhulu sobuciko bokwakha, ukuhleleka kombuso, umnotho kanye lamasiko ase-Afrika ngaphambi kobukoloni.",
        },
        "Shona": {
            "name": "Great Zimbabwe", "subtitle": "Guta guru rematombo reShona uye chiratidzo chenyika",
            "location": "Anenge 30 km kubva kuMasvingo, Zimbabwe", "inscribed": "1986", "criteria": "(i), (iii), (vi)",
            "history": "Great Zimbabwe yakavambwa muzana remakore rechi11, uye chikamu chikuru chenzvimbo chakavakwa pakati pa1100 na1450 AD. Yakava nzvimbo huru yeShona civilisation, zvematongerwo enyika, hupfumi netsika.",
            "culture": "Nzvimbo iyi inoratidza hutongi hwakarongeka, hunyanzvi hwekuvaka, crafts uye kutengeserana kwemadaro marefu.",
            "features": ["Hill Ruins dzakagarwa kubva muzana remakore rechi11 kusvika rechi15.", "Great Enclosure, zvikuru yezana remakore rechi14.", "Conical Tower.", "Valley Ruins nedry-stone masonry.", "Steatite/soapstone bird sculptures."],
            "unesco": "Great Zimbabwe National Monument yakanyorwa neUNESCO muna 1986 pasi pemaitiro (i), (iii) na(vi). UNESCO inoiona seuchapupu hwakasiyana hweShona civilisation kubva muzana remakore rechi11 kusvika rechi15.",
            "protect": ["Usakwira kana kugara pamadziro ekare.", "Usabvisa matombo kana archaeology material.", "Shandisa nzira dzakatenderwa.", "Dzivisa graffiti, marara uye kukuvadza madziro."],
            "facts": ["Chikamu chikuru chenzvimbo chakavakwa pakati pa1100 na1450 AD.", "Great Enclosure inonyanya kubva muzana remakore rechi14.", "Great Zimbabwe yaiva nzvimbo yakakosha yekutengeserana."],
            "significance": "Great Zimbabwe chiratidzo chakakosha cheAfrican urbanism, engineering, hutongi, hupfumi netsika.",
        },
    },
    "khami": {
        "emoji": "🧱",
        "English": {
            "name": "Khami Ruins", "subtitle": "Terraced dry-stone architecture of the Torwa capital",
            "location": "About 22 km west of Bulawayo, Zimbabwe", "inscribed": "1986", "criteria": "(iii), (iv)",
            "history": "Khami was the capital of the Torwa dynasty and developed as a major centre after the decline of Great Zimbabwe. UNESCO places the Torwa capital within roughly 1450–1650. The main stone-built settlement is therefore approximately 400–600 years old rather than having one exact construction year.",
            "culture": "Khami reflects political authority, social organisation, local craftsmanship, spiritual meaning and long-distance trade. It continued the broader Zimbabwe stone-building tradition while developing distinctive architectural features of its own.",
            "features": ["Complex platforms and stone-faced terraces.", "Retaining or revetment walls used extensively in the architecture.", "Elaborate chevron and chequered wall decoration.", "The Hill Ruin associated with the chief's residence.", "Imported objects showing trade connections with Europe, China and the wider world."],
            "unesco": "Khami Ruins National Monument was inscribed on the UNESCO World Heritage List in 1986 under criteria (iii) and (iv). UNESCO highlights its distinctive later development of the Zimbabwe stone-building tradition, decorated walls and evidence of long-distance trade.",
            "protect": ["Do not climb or lean on the ancient terrace and retaining walls.", "Never remove pottery, stone or archaeological objects.", "Stay on visitor routes and avoid disturbing archaeological deposits.", "Report damage to site staff instead of moving or repairing objects yourself."],
            "facts": ["Khami lies about 22 km west of Bulawayo.", "UNESCO identifies it as the capital of the Torwa dynasty, broadly dating 1450–1650.", "Objects from Europe and China demonstrate Khami's role in long-distance trade."],
            "significance": "Khami is important because it shows how Zimbabwe's monumental stone-building tradition evolved after Great Zimbabwe, with distinctive terraces, retaining walls and elaborate decoration.",
        },
        "isiNdebele": {
            "name": "Amanxiwa eKhami", "subtitle": "Amathala lamadwala enhloko-dolobha yeTorwa",
            "location": "Cishe 22 km entshonalanga yeBulawayo, Zimbabwe", "inscribed": "1986", "criteria": "(iii), (iv)",
            "history": "IKhami yayiyinhloko-dolobha yobukhosi beTorwa futhi yakhula ngemva kokwehla kweGreat Zimbabwe. I-UNESCO ibeka isikhathi sayo esikhulu cishe phakathi kuka-1450 lo-1650. Ngakho amanxiwa amakhulu akhiwe ngamatshe alinganiselwa eminyakeni engu-400 kuya ku-600 ubudala.",
            "culture": "IKhami ikhombisa amandla okubusa, ukuhleleka kwabantu, ubuciko, amasiko omoya kanye lokuthengiselana kwamabanga amade.",
            "features": ["Amathala amakhulu lamaplatform akhiwe ngamatshe.", "Imiduli yokubamba umhlabathi esetshenziswa kakhulu.", "Imihlobiso ye-chevron le-chequered emidulini.", "IHill Ruin ehlotshaniswa lendawo yenkosi.", "Izinto ezivela eYurophu laseChina ezibonisa ukuhweba kwamabanga amade."],
            "unesco": "IKhami Ruins National Monument yafakwa ku-UNESCO ngo-1986 ngaphansi kwemigomo (iii) lo-(iv), ngenxa yezakhiwo zayo ezihlukileyo, imihlobiso kanye lobufakazi bokuthengiselana.",
            "protect": ["Ungakhweli emidulini yamathala.", "Ungasusi pottery, amatshe kumbe izinto zemivubukulo.", "Hamba emizileni yezivakashi.", "Bika umonakalo kubasebenzi bendawo."],
            "facts": ["IKhami icishe ibe 22 km entshonalanga yeBulawayo.", "Yayiyinhloko-dolobha yeTorwa cishe phakathi kuka-1450 lo-1650.", "Izinto zaseYurophu laseChina zibonisa ukuhweba kwamabanga amade."],
            "significance": "IKhami ikhombisa ukuthi isiko lokwakha ngamatshe eZimbabwe laqhubeka futhi laguquka ngemva kweGreat Zimbabwe.",
        },
        "Shona": {
            "name": "Khami Ruins", "subtitle": "Terraced dry-stone architecture yeguta guru reTorwa",
            "location": "Anenge 22 km kumadokero kweBulawayo, Zimbabwe", "inscribed": "1986", "criteria": "(iii), (iv)",
            "history": "Khami yaiva guta guru redzinza reTorwa uye yakakura mushure mekuderera kweGreat Zimbabwe. UNESCO inoisa nguva huru yeTorwa capital pakati pa1450 na1650. Saka main stone-built settlement ine makore anenge 400 kusvika 600, kwete gore rimwe chete rekuvakwa.",
            "culture": "Khami inoratidza hutongi, kurongeka kwevanhu, craftsmanship, zvemweya uye kutengeserana kwemadaro marefu.",
            "features": ["Platforms nema terraces ane stone facing.", "Retaining kana revetment walls.", "Chevron nechequered wall decoration.", "Hill Ruin ine hukama nenzvimbo yemambo.", "Zvinhu zvakabva kuEurope neChina zvinoratidza long-distance trade."],
            "unesco": "Khami Ruins National Monument yakanyorwa neUNESCO muna 1986 pasi pemaitiro (iii) na(iv), nekuda kwearchitecture yayo, wall decoration uye humbowo hwekutengeserana.",
            "protect": ["Usakwira kana kutsamira pamadziro ema terraces.", "Usabvisa pottery, matombo kana archaeology material.", "Shandisa nzira dzevashanyi.", "Bika kukuvara kuvashandi venzvimbo."],
            "facts": ["Khami iri anenge 22 km kumadokero kweBulawayo.", "Yaiva capital yeTorwa, zvikuru pakati pa1450 na1650.", "Zvinhu zveEurope neChina zvinoratidza long-distance trade."],
            "significance": "Khami inoratidza kushanduka kweZimbabwe stone-building tradition mushure meGreat Zimbabwe.",
        },
    },
}

QUIZ = {
    "English": [
        ("Which site has one of the highest concentrations of rock art in southern Africa?", ["Great Zimbabwe", "Matobo Hills", "Khami Ruins", "Mana Pools"], 1, "Matobo Hills is renowned for one of southern Africa's highest concentrations of rock art."),
        ("According to UNESCO, Matobo rock art dates back at least about how long?", ["500 years", "2,000 years", "13,000 years", "100 years"], 2, "UNESCO states that Matobo's rock-art tradition dates back at least 13,000 years."),
        ("When was Great Zimbabwe principally built?", ["1100–1450 AD", "1700–1850 AD", "1900–1950 AD", "500–700 AD"], 0, "UNESCO dates the principal construction of Great Zimbabwe to about 1100–1450 AD."),
        ("Which part of Great Zimbabwe dates mainly to the 14th century?", ["Great Enclosure", "Khami Hill Ruin", "Matobo caves", "Victoria Falls bridge"], 0, "The Great Enclosure dates mainly to the 14th century."),
        ("What material were the famous Zimbabwe Birds carved from?", ["Steel", "Steatite/soapstone", "Glass", "Ivory"], 1, "The famous bird sculptures are carved from steatite, commonly called soapstone."),
        ("Khami was the capital of which dynasty?", ["Torwa", "Roman", "Ottoman", "Mughal"], 0, "Khami was the capital of the Torwa dynasty."),
        ("What broad period does UNESCO associate with the Torwa capital at Khami?", ["1450–1650", "1850–1950", "900–1000", "2000–2020"], 0, "UNESCO describes Khami as the Torwa capital within roughly 1450–1650."),
        ("Which feature is especially characteristic of Khami?", ["Stone-faced terraces and retaining walls", "Glass towers", "Steel bridges", "Mud pyramids"], 0, "Khami is especially noted for platforms, terraces, retaining walls and decorative dry-stone masonry."),
        ("What should a visitor do near Matobo rock paintings?", ["Touch them", "Wet them", "Leave them untouched", "Trace them"], 2, "Rock paintings should not be touched, wetted, traced or rubbed."),
        ("Which two sites provide strong evidence of long-distance trade?", ["Great Zimbabwe and Khami", "Matobo and Mana Pools", "Only Matobo", "None"], 0, "Both Great Zimbabwe and Khami provide archaeological evidence of long-distance trade."),
    ],
    "isiNdebele": [
        ("Yiphi indawo elemidwebo yamadwala eminengi kakhulu eningizimu ye-Afrika?", ["Great Zimbabwe", "Matobo Hills", "Khami Ruins", "Mana Pools"], 1, "IMatobo Hills idume kakhulu ngemidwebo yamadwala."),
        ("Imidwebo yaseMatobo ihlehlela emuva okungenani iminyaka emingaki?", ["500", "2,000", "13,000", "100"], 2, "I-UNESCO ithi imidwebo ihlehlela emuva okungenani iminyaka engu-13,000."),
        ("IGreat Zimbabwe yakhiwa ikakhulu ngasiphi isikhathi?", ["1100–1450 AD", "1700–1850 AD", "1900–1950 AD", "500–700 AD"], 0, "Ukwakhiwa okuyinhloko kwenzeka phakathi kuka-1100 lo-1450 AD."),
        ("Yiphi ingxenye yeGreat Zimbabwe eyakhiwa ikakhulu ngekhulu le-14?", ["Great Enclosure", "Khami Hill Ruin", "Matobo caves", "Victoria Falls bridge"], 0, "IGreat Enclosure ingeyekhulu le-14 ikakhulu."),
        ("IZimbabwe Birds zabazwa ngeliphi ilitshe?", ["Steel", "Steatite/soapstone", "Glass", "Ivory"], 1, "Zabazwa nge-steatite, ebizwa njalo nge-soapstone."),
        ("IKhami yayiyinhloko-dolobha yobukhosi bani?", ["Torwa", "Roman", "Ottoman", "Mughal"], 0, "IKhami yayiyinhloko-dolobha yeTorwa."),
        ("Isikhathi esikhulu seTorwa eKhami sasiphakathi kwamiphi iminyaka?", ["1450–1650", "1850–1950", "900–1000", "2000–2020"], 0, "I-UNESCO ibeka isikhathi esikhulu cishe phakathi kuka-1450 lo-1650."),
        ("Yini ephawuleka kakhulu eKhami?", ["Amathala lamadwala lemiduli yokubamba", "Glass towers", "Steel bridges", "Mud pyramids"], 0, "IKhami idume ngamathala, retaining walls lemihlobiso yamatshe."),
        ("Kumele wenzeni eduze kwemidwebo yaseMatobo?", ["Uyithinte", "Uyimanzise", "Uyitshiye ungayithinti", "Uyilandele ngomdwebo"], 2, "Imidwebo kumele ingathintwa kumbe imanziswe."),
        ("Yiziphi indawo ezimbili ezilobufakazi bokuhweba kwamabanga amade?", ["Great Zimbabwe leKhami", "Matobo leMana Pools", "Matobo kuphela", "Azikho"], 0, "IGreat Zimbabwe leKhami zilobufakazi bokuthengiselana kwamabanga amade."),
    ],
    "Shona": [
        ("Ndeipi nzvimbo ine rock art yakawanda zvikuru kumaodzanyemba kweAfrica?", ["Great Zimbabwe", "Matobo Hills", "Khami Ruins", "Mana Pools"], 1, "Matobo Hills inozivikanwa zvikuru nerock art."),
        ("Rock art yeMatobo inodzokera kumashure kwemakore angangoita mangani kana kupfuura?", ["500", "2,000", "13,000", "100"], 2, "UNESCO inoti rock art ine makore angangoita 13,000 kana kupfuura."),
        ("Great Zimbabwe yakavakwa zvikuru panguva ipi?", ["1100–1450 AD", "1700–1850 AD", "1900–1950 AD", "500–700 AD"], 0, "UNESCO inoisa principal construction pakati pa1100 na1450 AD."),
        ("Ndeipi part yeGreat Zimbabwe inonyanya kubva muzana remakore rechi14?", ["Great Enclosure", "Khami Hill Ruin", "Matobo caves", "Victoria Falls bridge"], 0, "Great Enclosure inonyanya kubva muzana remakore rechi14."),
        ("Zimbabwe Birds dzakavezwa nechii?", ["Steel", "Steatite/soapstone", "Glass", "Ivory"], 1, "Dzaka vezwa nesteatite, inowanzonzi soapstone."),
        ("Khami yaiva capital yedzinza ripi?", ["Torwa", "Roman", "Ottoman", "Mughal"], 0, "Khami yaiva capital yeTorwa dynasty."),
        ("UNESCO inoisa nguva huru yeTorwa capital paKhami papi?", ["1450–1650", "1850–1950", "900–1000", "2000–2020"], 0, "Nguva huru iri pakati pa1450 na1650."),
        ("Chii chinonyanya kuzivikanwa paKhami?", ["Stone-faced terraces neretaining walls", "Glass towers", "Steel bridges", "Mud pyramids"], 0, "Khami inozivikanwa nema terraces, retaining walls uye decorative dry-stone masonry."),
        ("Mushanyi anofanira kuita sei pedyo nerock art yeMatobo?", ["Kuibata", "Kuinyorovesa", "Kusiya isina kubatwa", "Ku trace"], 2, "Rock art haifaniri kubatwa kana kunyudzwa."),
        ("Ndedzipi nzvimbo mbiri dzine humbowo hwelong-distance trade?", ["Great Zimbabwe neKhami", "Matobo neMana Pools", "Matobo chete", "Hapana"], 0, "Great Zimbabwe neKhami zvose zvine humbowo hwekutengeserana kwemadaro marefu."),
    ],
}


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9\s\-]", " ", text.lower()).strip()


def assistant_answer(question: str, lang: str) -> str:
    q = normalize(question)
    R = {
        "English": {
            "great_age": "Great Zimbabwe was not built in a single year. UNESCO dates the principal construction of the property to about 1100–1450 AD. The settlement was founded in the 11th century, and the Great Enclosure dates mainly to the 14th century.",
            "great_who": "Great Zimbabwe was built by Shona people—the ancestors of Shona-speaking communities. UNESCO describes the site as a unique testimony to Shona civilisation between the 11th and 15th centuries.",
            "great_features": "Great Zimbabwe has three principal groups: the Hill Ruins, the Great Enclosure and the Valley Ruins. The Great Enclosure contains a narrow passage and the famous Conical Tower. Much of the monumental masonry was built with carefully fitted stone without mortar.",
            "great_trade": "Great Zimbabwe was an important trading centre. Archaeological evidence shows links between the interior of southern Africa and wider Indian Ocean trade networks.",
            "birds": "The Zimbabwe Birds are carved steatite, or soapstone, bird sculptures found at Great Zimbabwe. They are among the site's most famous artefacts and later became major national symbols of Zimbabwe.",
            "khami_age": "Khami does not have one exact construction year. UNESCO identifies it as the capital of the Torwa dynasty, broadly associated with about 1450–1650. So the main stone-built ruins are roughly 400–600 years old today.",
            "khami_history": "Khami rose as a major centre after the decline of Great Zimbabwe and served as the capital of the Torwa dynasty. UNESCO associates the Torwa capital with roughly 1450–1650.",
            "khami_features": "Khami is especially known for stone-faced platforms and terraces, retaining or revetment walls, narrow passageways and elaborate chevron and chequered decoration.",
            "khami_trade": "Khami was an important long-distance trade centre. UNESCO records imported material including objects from Europe and China, showing links to the wider world.",
            "matobo_age": "Matobo has a very deep human history. UNESCO reports archaeological occupation extending for at least 500,000 years, while its rock art dates back at least 13,000 years.",
            "matobo_art": "Matobo Hills has one of the highest concentrations of rock art in southern Africa. UNESCO says the paintings date back at least 13,000 years and provide valuable evidence about Stone Age societies.",
            "matobo_spiritual": "Matobo is a living sacred landscape. Shrines and sacred places are still used by communities, and the Mwari religious tradition is closely centred on the hills.",
            "unesco": "Great Zimbabwe and Khami Ruins were inscribed on the UNESCO World Heritage List in 1986. Matobo Hills was inscribed in 2003.",
            "compare": "Great Zimbabwe is best known for monumental freestanding dry-stone architecture such as the Great Enclosure. Khami represents a later development of the same broad Zimbabwe stone-building tradition and is especially known for terraces, retaining walls and rich decoration. Matobo is different: its heritage value centres on rock art, a granite cultural landscape and continuing sacred traditions.",
            "protect": "Respect the sites by not touching rock art, not climbing ancient walls, not removing stones or artefacts, staying on authorised paths and avoiding graffiti or littering.",
        },
        "isiNdebele": {
            "great_age": "IGreat Zimbabwe ayakhiwanga ngomnyaka owodwa. I-UNESCO ibeka ukwakhiwa okuyinhloko phakathi kuka-1100 lo-1450 AD. Yasungulwa ngekhulu le-11, kanti iGreat Enclosure ingeyekhulu le-14 ikakhulu.",
            "great_who": "IGreat Zimbabwe yakhiwa ngabantu bamaShona, okhokho bemiphakathi ekhuluma isiShona.",
            "great_features": "IGreat Zimbabwe ihlanganisa iHill Ruins, iGreat Enclosure leValley Ruins. IGreat Enclosure ileConical Tower, futhi imiduli eminengi yakhiwa ngamatshe ngaphandle kodaka.",
            "great_trade": "IGreat Zimbabwe yayiyisikhungo esibalulekileyo sokuthengiselana futhi yayixhumene lenethiwekhi zokuhweba ezazifika e-Indian Ocean.",
            "birds": "IZimbabwe Birds yizithombe zezinyoni ezabazwa nge-steatite/soapstone ezatholakala eGreat Zimbabwe. Zaba luphawu olukhulu lwelizwe.",
            "khami_age": "IKhami ayilawo umnyaka owodwa wokwakhiwa. I-UNESCO iyibeka njengenhloko-dolobha yeTorwa cishe phakathi kuka-1450 lo-1650. Ngakho amanxiwa amakhulu amatshe alinganiselwa eminyakeni engu-400 kuya ku-600 ubudala.",
            "khami_history": "IKhami yakhula yaba yisikhungo esikhulu ngemva kokwehla kweGreat Zimbabwe futhi yaba yinhloko-dolobha yeTorwa.",
            "khami_features": "IKhami idume ngamaplatform lamathala amatshe, retaining walls, imizila emincane kanye lemihlobiso ye-chevron le-chequered.",
            "khami_trade": "IKhami yayiyisikhungo sokuhweba kwamabanga amade. Izinto ezivela eYurophu laseChina zatholakala lapho.",
            "matobo_age": "IMatobo ilomlando omude kakhulu. I-UNESCO ithi ubufakazi bokuhlala kwabantu budlula iminyaka engu-500,000, kanti imidwebo yamadwala ihlehlela emuva okungenani iminyaka engu-13,000.",
            "matobo_art": "IMatobo ilenani elikhulu kakhulu lemidwebo yamadwala eningizimu ye-Afrika. Imidwebo ihlehlela emuva okungenani iminyaka engu-13,000.",
            "matobo_spiritual": "IMatobo yindawo engcwele esaphilayo. Izindawo ezingcwele zisasebenza futhi isiko likaMwari lihlobene kakhulu lamagquma.",
            "unesco": "IGreat Zimbabwe leKhami Ruins zafakwa ku-UNESCO ngo-1986. IMatobo Hills yafakwa ngo-2003.",
            "compare": "IGreat Zimbabwe idume ngezakhiwo ezinkulu ze-dry-stone ezifana leGreat Enclosure. IKhami yathuthukisa isiko elifanayo ngamathala, retaining walls lemihlobiso. IMatobo yona idume ngemidwebo yamadwala, amadwala egranite lamasiko angcwele.",
            "protect": "Hlonipha indawo ngokungathinti imidwebo, ukungakhweli imiduli, ukungasusi izinto zakudala, ukulandela imizila lokungalahli ingcekeza.",
        },
        "Shona": {
            "great_age": "Great Zimbabwe haina kuvakwa mugore rimwe chete. UNESCO inoisa principal construction pakati pa1100 na1450 AD. Yakavambwa muzana remakore rechi11, uye Great Enclosure inonyanya kubva muzana remakore rechi14.",
            "great_who": "Great Zimbabwe yakavakwa nevanhu veShona, madzitateguru evanhu vanotaura chiShona.",
            "great_features": "Great Zimbabwe ine Hill Ruins, Great Enclosure neValley Ruins. Great Enclosure ine Conical Tower, uye monumental walls mazhinji akavakwa nematombo akanyatsorongedzwa pasina mortar.",
            "great_trade": "Great Zimbabwe yaiva nzvimbo yakakosha yekutengeserana uye yaibatanidzwa nemisika yeIndian Ocean.",
            "birds": "Zimbabwe Birds zvivezwa zveshiri zvakagadzirwa nesteatite/soapstone zvakawanikwa paGreat Zimbabwe. Zvakazova zviratidzo zvikuru zvenyika.",
            "khami_age": "Khami haina gore rimwe chete rekuvakwa. UNESCO inoiona secapital yeTorwa inonyanya kubatanidzwa nenguva ya1450–1650. Saka main stone-built ruins ane makore anenge 400 kusvika 600.",
            "khami_history": "Khami yakakura mushure mekuderera kweGreat Zimbabwe uye yakava capital yeTorwa dynasty.",
            "khami_features": "Khami inozivikanwa nemaplatform, stone-faced terraces, retaining walls, passageways uye chevron nechequered decoration.",
            "khami_trade": "Khami yaiva nzvimbo yakakosha yelong-distance trade. Zvinhu kubva kuEurope neChina zvakawanikwa ipapo.",
            "matobo_age": "Matobo ine nhoroondo yakadzika zvikuru. UNESCO inoti archaeology inoratidza kugara kwevanhu kwemakore 500,000 kana kupfuura, uye rock art ine makore 13,000 kana kupfuura.",
            "matobo_art": "Matobo ine imwe yema concentrations makuru erock art kumaodzanyemba kweAfrica. UNESCO inoti mifananidzo inodzokera kumashure kwemakore 13,000 kana kupfuura.",
            "matobo_spiritual": "Matobo inzvimbo inoyera ichiri kurarama. Shrines dzichiri kushandiswa uye tsika yaMwari ine hukama hwakasimba nemakomo aya.",
            "unesco": "Great Zimbabwe neKhami Ruins zvakanyorwa neUNESCO muna 1986. Matobo Hills yakanyorwa muna 2003.",
            "compare": "Great Zimbabwe inozivikanwa nemonumental dry-stone architecture seGreat Enclosure. Khami yakazovandudza stone-building tradition iyi nema terraces, retaining walls nedecoration. Matobo inosiyana nekuda kwerock art, granite landscape netsika dzinoyera.",
            "protect": "Remekedza nzvimbo nekusabata rock art, kusakwira pamadziro ekare, kusabvisa artefacts, kushandisa nzira dzakatenderwa uye kusasiya marara.",
        },
    }[lang]

    if any(x in q for x in ["compare", "difference", "differences", "umehluko", "qhathanisa", "enzanisa", "musiyano"]):
        return R["compare"]
    if any(x in q for x in ["protect", "protection", "conservation", "preserve", "damage", "vikela", "chengetedza", "kuchengetedza"]):
        return R["protect"]

    if "great zimbabwe" in q or "great zim" in q:
        if any(x in q for x in ["who", "built by", "builder", "builders", "ngobani", "ndiani"]):
            return R["great_who"]
        if any(x in q for x in ["when", "what year", "how old", "age", "built", "constructed", "nini", "yakhiwa", "yakavakwa", "mdala"]):
            return R["great_age"]
        if any(x in q for x in ["trade", "trading", "commerce", "kutengesa", "ukuhweba", "ukuthengiselana"]):
            return R["great_trade"]
        return R["great_features"]

    if "khami" in q:
        if any(x in q for x in ["when", "what year", "how old", "age", "built", "constructed", "nini", "yakhiwa", "yakavakwa", "mdala", "makore", "iminyaka"]):
            return R["khami_age"]
        if any(x in q for x in ["trade", "trading", "commerce", "europe", "china", "kutengesa", "ukuhweba", "ukuthengiselana"]):
            return R["khami_trade"]
        if any(x in q for x in ["terrace", "terraces", "wall", "walls", "architecture", "feature", "amathala", "izakhiwo"]):
            return R["khami_features"]
        return R["khami_history"]

    if "matobo" in q or "rock art" in q or "rock painting" in q or "mwari" in q:
        if any(x in q for x in ["how old", "age", "when", "date", "old", "mdala", "nini", "makore", "iminyaka"]):
            return R["matobo_age"]
        if "mwari" in q or any(x in q for x in ["spiritual", "sacred", "religion", "shrine", "ingcwele", "mweya", "dzinoyera"]):
            return R["matobo_spiritual"]
        return R["matobo_art"]

    if any(x in q for x in ["bird", "birds", "inyoni", "shiri", "soapstone", "steatite"]):
        return R["birds"]
    if any(x in q for x in ["unesco", "world heritage", "inscribed", "listed"]):
        return R["unesco"]

    if lang == "isiNdebele":
        return "Buza ngeMatobo Hills, Great Zimbabwe kumbe Khami Ruins — iminyaka, abakhi, imidwebo yamadwala, izakhiwo, ukuhweba, UNESCO kumbe ukuvikela amagugu."
    if lang == "Shona":
        return "Bvunza nezveMatobo Hills, Great Zimbabwe kana Khami Ruins — makore, vakavaka, rock art, architecture, trade, UNESCO kana kuchengetedza."
    return "Ask me about Matobo Hills, Great Zimbabwe or Khami Ruins — dates, builders, rock art, architecture, trade, UNESCO, conservation or comparisons."


with st.sidebar:
    html(f"""
    <div class="brand-box">
        <h2>🗿 ROBO GUIDE</h2>
        <div class="slogan">{escape(SLOGAN)}</div>
    </div>
    """)

    languages = ["English", "isiNdebele", "Shona"]
    selected_lang = st.selectbox(
        T("language"), languages,
        index=languages.index(st.session_state.lang),
        key="language_selector",
    )

    if selected_lang != st.session_state.lang:
        st.session_state.lang = selected_lang
        reset_quiz()
        st.session_state.chat = []
        st.rerun()

    st.markdown(f"### {T('explore')}")
    nav_items = [
        ("🏠", T("home"), "home"),
        ("⛰️", T("matobo"), "matobo"),
        ("🏛️", T("great"), "great"),
        ("🧱", T("khami"), "khami"),
        ("🏆", T("quiz"), "quiz"),
        ("💬", T("assistant"), "assistant"),
    ]

    for i, (icon, label, page_name) in enumerate(nav_items):
        if st.button(f"{icon}  {label}", key=f"nav_{page_name}_{i}", use_container_width=True):
            go(page_name)


def render_band():
    html('<div class="heritage-band"></div>')


def render_home():
    render_band()
    html(f"""
    <div class="hero">
        <h1>ROBO GUIDE</h1>
        <h3>{escape(T('hero_sub'))}</h3>
        <p>{escape(T('hero_text'))}</p>
        <div class="slogan-pill">{escape(SLOGAN)}</div>
    </div>
    """)

    st.markdown(f"## {T('choose')}")
    cols = st.columns(3)
    for col, site_key in zip(cols, ["matobo", "great", "khami"]):
        d = SITES[site_key][st.session_state.lang]
        with col:
            html(f"""
            <div class="site-card">
                <div class="site-icon">{SITES[site_key]['emoji']}</div>
                <h3>{escape(d['name'])}</h3>
                <p>{escape(d['subtitle'])}</p>
                <span class="badge">UNESCO {escape(d['inscribed'])}</span>
                <span class="badge">{escape(d['criteria'])}</span>
            </div>
            """)
            if st.button(f"{T('open_site')} {d['name']}", key=f"home_open_{site_key}", use_container_width=True):
                go(site_key)

    st.markdown("## Discover • Understand • Respect • Protect")
    a, b, c = st.columns(3)
    with a:
        html('<div class="info-card"><h3>📜 Discover</h3><p>Meet the people, stories and places behind Zimbabwe\'s remarkable cultural heritage.</p></div>')
    with b:
        html('<div class="info-card"><h3>🧠 Understand</h3><p>Explore accurate historical facts, architecture, archaeology, trade and living traditions.</p></div>')
    with c:
        html('<div class="info-card"><h3>🛡️ Protect</h3><p>Learn respectful visitor behaviour that helps preserve fragile heritage for future generations.</p></div>')

    html('<div class="source-note">Heritage facts in ROBO GUIDE are aligned to UNESCO World Heritage descriptions for Matobo Hills, Great Zimbabwe National Monument and Khami Ruins National Monument.</div>')


def render_site(site_key: str):
    render_band()
    d = SITES[site_key][st.session_state.lang]
    html(f"""
    <div class="hero">
        <h1 style="font-size:3.35rem">{SITES[site_key]['emoji']} {escape(d['name'])}</h1>
        <h3>{escape(d['subtitle'])}</h3>
        <div class="slogan-pill">{escape(SLOGAN)}</div>
    </div>
    """)

    c1, c2, c3 = st.columns(3)
    with c1:
        html(f'<div class="stat-card"><div class="stat-label">{escape(T("location"))}</div><div class="stat-value">{escape(d["location"])}</div></div>')
    with c2:
        html(f'<div class="stat-card"><div class="stat-label">{escape(T("inscribed"))}</div><div class="stat-value">{escape(d["inscribed"])}</div></div>')
    with c3:
        html(f'<div class="stat-card"><div class="stat-label">{escape(T("criteria"))}</div><div class="stat-value">{escape(d["criteria"])}</div></div>')

    st.markdown(f"## {T('history')}")
    html(f'<div class="info-card"><p>{escape(d["history"])}</p></div>')

    st.markdown(f"## {T('culture')}")
    html(f'<div class="info-card"><p>{escape(d["culture"])}</p></div>')

    st.markdown(f"## {T('features')}")
    fcols = st.columns(2)
    for i, item in enumerate(d["features"]):
        with fcols[i % 2]:
            html(f'<div class="fact-card"><h4>◆ Heritage Feature</h4><p>{escape(item)}</p></div>')

    st.markdown(f"## {T('unesco')}")
    html(f'<div class="unesco-card"><strong>UNESCO</strong><br><br>{escape(d["unesco"])}</div>')

    st.markdown(f"## {T('protect')}")
    pcols = st.columns(2)
    for i, item in enumerate(d["protect"]):
        with pcols[i % 2]:
            html(f'<div class="fact-card"><h4>🛡️ Respect</h4><p>{escape(item)}</p></div>')

    st.markdown(f"## {T('facts')}")
    factcols = st.columns(3)
    for i, item in enumerate(d["facts"]):
        with factcols[i % 3]:
            html(f'<div class="fact-card"><h4>💡 Did you know?</h4><p>{escape(item)}</p></div>')

    st.markdown(f"## {T('significance')}")
    html(f'<div class="unesco-card">{escape(d["significance"])}</div>')

    left, right = st.columns(2)
    with left:
        if st.button("🏆 " + T("quiz"), key=f"site_quiz_{site_key}", use_container_width=True):
            go("quiz")
    with right:
        if st.button("💬 " + T("assistant"), key=f"site_assistant_{site_key}", use_container_width=True):
            go("assistant")


def render_quiz():
    render_band()
    html(f"""
    <div class="hero">
        <h1 style="font-size:3.2rem">🏆 {escape(T('quiz_title'))}</h1>
        <p>{escape(T('quiz_intro'))}</p>
        <div class="slogan-pill">{escape(SLOGAN)}</div>
    </div>
    """)

    questions = QUIZ[st.session_state.lang]
    if st.session_state.quiz_finished:
        total = len(questions)
        pct = round((st.session_state.quiz_score / total) * 100)
        achievement = T("guardian") if pct >= 80 else T("guide")
        c1, c2, c3 = st.columns(3)
        c1.metric(T("score"), f"{st.session_state.quiz_score}/{total}")
        c2.metric(T("points"), st.session_state.quiz_points)
        c3.metric(T("achievement"), achievement)
        if pct >= 80:
            st.success(f"🏅 {achievement} — {pct}%")
            st.balloons()
        else:
            st.info(f"📜 {achievement} — {pct}%")
        if st.button(T("restart"), key="quiz_restart", use_container_width=True):
            reset_quiz()
            st.rerun()
        return

    idx = st.session_state.quiz_index
    q, options, correct_idx, explanation = questions[idx]
    st.progress((idx + 1) / len(questions))
    st.markdown(f"### {T('question')} {idx + 1} / {len(questions)}")
    html(f'<div class="quiz-card"><h3>{escape(q)}</h3></div>')

    choice = st.radio(
        "Answer", options, index=None,
        key=f"quiz_radio_{st.session_state.lang}_{idx}",
        label_visibility="collapsed",
        disabled=st.session_state.quiz_answered,
    )

    if not st.session_state.quiz_answered:
        if st.button(T("submit"), key=f"quiz_submit_{idx}", use_container_width=True):
            if choice is None:
                st.warning("Please choose an answer first.")
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
        chosen_idx = options.index(st.session_state.quiz_choice)
        if chosen_idx == correct_idx:
            st.success(f"✅ {T('correct')} {explanation}")
        else:
            st.error(f"❌ {T('incorrect')} {explanation}")
        m1, m2 = st.columns(2)
        m1.metric(T("score"), st.session_state.quiz_score)
        m2.metric(T("points"), st.session_state.quiz_points)
        if st.button(T("next"), key=f"quiz_next_{idx}", use_container_width=True):
            if idx + 1 >= len(questions):
                st.session_state.quiz_finished = True
            else:
                st.session_state.quiz_index += 1
                st.session_state.quiz_answered = False
                st.session_state.quiz_choice = None
            st.rerun()


def render_assistant():
    render_band()
    html(f"""
    <div class="hero">
        <h1 style="font-size:3.1rem">💬 {escape(T('assistant_title'))}</h1>
        <p>{escape(T('assistant_intro'))}</p>
        <div class="slogan-pill">{escape(SLOGAN)}</div>
    </div>
    """)

    suggestions = {
        "English": ["How old are the Khami Ruins?", "When was Great Zimbabwe built?", "Who built Great Zimbabwe?", "How old is Matobo rock art?", "What are the Zimbabwe Birds?", "Compare Great Zimbabwe, Khami and Matobo."],
        "isiNdebele": ["Amanxiwa eKhami madala kangakanani?", "IGreat Zimbabwe yakhiwa nini?", "Ngobani abakha iGreat Zimbabwe?", "Imidwebo yaseMatobo midala kangakanani?", "Yini amaZimbabwe Birds?", "Qhathanisa iGreat Zimbabwe, iKhami leMatobo."],
        "Shona": ["Khami Ruins ine makore mangani?", "Great Zimbabwe yakavakwa riini?", "Ndiani akavaka Great Zimbabwe?", "Rock art yeMatobo ine makore mangani?", "Zimbabwe Birds chii?", "Enzanisa Great Zimbabwe, Khami neMatobo."],
    }

    st.markdown(f"### {T('quick')}")
    cols = st.columns(2)
    for i, prompt in enumerate(suggestions[st.session_state.lang]):
        with cols[i % 2]:
            if st.button(prompt, key=f"assist_quick_{st.session_state.lang}_{i}", use_container_width=True):
                st.session_state.chat.append((prompt, assistant_answer(prompt, st.session_state.lang)))
                st.rerun()

    for question, answer in st.session_state.chat:
        html(f'<div class="chat-user"><strong>You:</strong><br>{escape(question)}</div>')
        html(f'<div class="chat-bot"><strong>ROBO GUIDE:</strong><br>{escape(answer)}</div>')

    with st.form("assistant_form", clear_on_submit=True):
        question = st.text_input(T("ask"), key="assistant_input", placeholder=T("ask"))
        submitted = st.form_submit_button(T("send"), use_container_width=True)

    if submitted and question.strip():
        st.session_state.chat.append((question.strip(), assistant_answer(question.strip(), st.session_state.lang)))
        st.rerun()

    if st.button(T("clear"), key="assistant_clear", use_container_width=True):
        st.session_state.chat = []
        st.rerun()

    html('<div class="source-note">ROBO GUIDE uses a built-in heritage knowledge base for these three sites. It does not require a paid AI API.</div>')


page = st.session_state.page
if page == "home":
    render_home()
elif page in {"matobo", "great", "khami"}:
    render_site(page)
elif page == "quiz":
    render_quiz()
elif page == "assistant":
    render_assistant()
else:
    st.session_state.page = "home"
    st.rerun()

html(f'<div class="footer"><strong>ROBO GUIDE</strong> — {escape(SLOGAN)}<br>{escape(T("footer"))}</div>')
