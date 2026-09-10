import streamlit as st
import re
from html import escape

st.set_page_config(
    page_title="ROBO GUIDE | Zimbabwe Heritage Explorer",
    page_icon="🗿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# ROBO GUIDE
# WRO 2026 Zimbabwe National Finals
# Theme: Robots Meet Culture
# ============================================================

# ------------------------------------------------------------
# DESIGN
# ------------------------------------------------------------

st.markdown(
    """
<style>

:root {
    --green: #08683A;
    --deepgreen: #034725;
    --gold: #E5B72E;
    --lightgold: #FFF7DA;
    --cream: #FFFDF5;
    --text: #183126;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%,
        rgba(229,183,46,0.10), transparent 22%),
        radial-gradient(circle at 90% 20%,
        rgba(8,104,58,0.08), transparent 25%),
        linear-gradient(180deg,#fffdf7,#f5faf6);
}

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #033d22 0%,
            #086238 60%,
            #034326 100%
        );
    border-right: 3px solid #E5B72E;
}

[data-testid="stSidebar"] * {
    color:white;
}

.brand {
    text-align:center;
    padding:20px 10px;
    margin-bottom:16px;

    border-radius:22px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,.12),
            rgba(229,183,46,.08)
        );

    border:1px solid rgba(229,183,46,.45);
}

.brand-logo {
    font-size:46px;
}

.brand h2 {
    margin:2px 0;
    color:white;
    letter-spacing:2px;
}

.brand p {
    color:#FFE899;
    font-size:13px;
}

.hero {

    border-radius:30px;

    padding:42px;

    margin-bottom:26px;

    color:white;

    position:relative;

    overflow:hidden;

    background:

        linear-gradient(
            120deg,
            rgba(3,65,35,.98),
            rgba(9,119,63,.94)
        );

    border:1px solid rgba(229,183,46,.6);

    box-shadow:
        0 20px 50px
        rgba(0,70,38,.18);
}

.hero:after {

    content:"";

    position:absolute;

    width:320px;
    height:320px;

    border-radius:50%;

    right:-110px;
    top:-100px;

    border:
        35px solid
        rgba(229,183,46,.18);

    box-shadow:
        0 0 0 30px
        rgba(255,255,255,.03);
}

.kicker {

    color:#F6D35C;

    font-size:13px;

    font-weight:800;

    letter-spacing:2px;

    text-transform:uppercase;
}

.hero h1 {

    margin:6px 0;

    font-size:
        clamp(
            2.7rem,
            6vw,
            5.2rem
        );

    line-height:1;

    color:white;
}

.hero h2 {

    color:#F8D766;

    margin-top:5px;
}

.hero p {

    max-width:900px;

    line-height:1.7;

    font-size:1.08rem;

    color:#F4FFF8;
}

.badge {

    display:inline-block;

    background:
        rgba(255,255,255,.10);

    border:
        1px solid
        rgba(255,255,255,.20);

    padding:
        7px 12px;

    border-radius:100px;

    margin:
        4px 4px 0 0;

    font-size:13px;
}

.section-title {

    font-size:30px;

    font-weight:850;

    color:#034725;

    margin-top:24px;
}

.section-sub {

    color:#65746A;

    line-height:1.6;

    margin-bottom:18px;
}

.card {

    background:
        rgba(255,255,255,.96);

    border:
        1px solid
        #E0EAE3;

    border-top:
        4px solid
        #E5B72E;

    border-radius:20px;

    padding:22px;

    min-height:220px;

    box-shadow:
        0 10px 25px
        rgba(31,70,45,.07);
}

.card h3 {

    color:#034725;

    margin-top:5px;
}

.card h4 {

    color:#034725;
}

.card p {

    line-height:1.6;

    color:#435349;
}

.site-icon {
    font-size:36px;
}

.stat {

    background:white;

    border:
        1px solid
        #E2EAE4;

    border-radius:17px;

    padding:
        16px;

    box-shadow:
        0 8px 20px
        rgba(30,60,40,.05);
}

.stat-number {

    color:#08683A;

    font-size:24px;

    font-weight:850;
}

.stat-label {

    font-size:13px;

    color:#68786E;
}

.goldbox {

    background:#FFF8E0;

    border:
        1px solid
        #EAD17A;

    padding:16px;

    border-radius:16px;

    margin:
        10px 0;
}

.greenbox {

    background:#F1FAF5;

    border:
        1px solid
        #CAE3D3;

    border-left:
        5px solid
        #08683A;

    padding:16px;

    border-radius:16px;

    margin:
        10px 0;
}

.unesco {

    background:
        linear-gradient(
            90deg,
            #08683A,
            #0E7946
        );

    border-left:
        6px solid
        #E5B72E;

    color:white;

    border-radius:17px;

    padding:20px;

    margin:
        18px 0;
}

.quizbox {

    background:white;

    border:
        1px solid
        #DFE8E1;

    border-radius:22px;

    padding:24px;

    box-shadow:
        0 10px 26px
        rgba(25,65,40,.07);
}

.achievement {

    text-align:center;

    padding:32px;

    border-radius:25px;

    background:
        linear-gradient(
            135deg,
            #033D22,
            #087343
        );

    color:white;

    border:
        2px solid
        #E5B72E;

    box-shadow:
        0 18px 40px
        rgba(0,85,45,.20);
}

.achievement h2 {

    color:#F6D35C;

    margin:
        7px 0;
}

.achievement-icon {
    font-size:58px;
}

.chat-user {

    max-width:82%;

    margin:
        8px 0 8px auto;

    background:#E8F5ED;

    border:
        1px solid
        #CEE5D5;

    padding:
        13px 15px;

    border-radius:
        18px 18px 4px 18px;
}

.chat-bot {

    max-width:90%;

    margin:
        8px auto 8px 0;

    background:#FFF7DE;

    border:
        1px solid
        #EBD482;

    padding:
        13px 15px;

    border-radius:
        18px 18px 18px 4px;
}

.footer {

    margin-top:40px;

    padding-top:24px;

    border-top:
        1px solid
        #DAE5DC;

    text-align:center;

    font-size:13px;

    color:#66766C;
}

div.stButton > button {

    border-radius:13px;

    border:
        1px solid
        #08703E;

    font-weight:700;

    transition:.2s;
}

div.stButton > button:hover {

    transform:
        translateY(-1px);

    border-color:
        #E5B72E;

    box-shadow:
        0 6px 15px
        rgba(0,90,45,.13);
}

div.stButton > button[kind="primary"] {

    background:
        linear-gradient(
            90deg,
            #08683A,
            #0C7C46
        );

    color:white;
}

.stProgress > div > div > div > div {

    background:
        #08683A;
}

[data-testid="stMetric"] {

    background:white;

    border:
        1px solid
        #E2EAE4;

    padding:
        10px;

    border-radius:
        14px;
}

</style>
""",
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# SESSION STATE
# ------------------------------------------------------------

DEFAULTS = {

    "page":
        "Home",

    "lang":
        "English",

    "quiz_index":
        0,

    "quiz_score":
        0,

    "quiz_points":
        0,

    "quiz_answered":
        False,

    "quiz_feedback":
        None,

    "quiz_finished":
        False,

    "chat":
        [],
}

for key, value in DEFAULTS.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ------------------------------------------------------------
# INTERFACE TRANSLATIONS
# ------------------------------------------------------------

UI = {

    "English": {

        "tagline":
            "Robots Meet Culture • WRO 2026 Zimbabwe",

        "language":
            "Language",

        "navigation":
            "Explore ROBO GUIDE",

        "home":
            "Home",

        "matobo":
            "Matobo Hills",

        "great":
            "Great Zimbabwe",

        "khami":
            "Khami Ruins",

        "quiz":
            "Heritage Challenge",

        "assistant":
            "Heritage Assistant",

        "prototype":
            "Robot + Website",

        "hero":
            "Meet Zimbabwe through technology.",

        "hero_text":
            "ROBO GUIDE connects a physical heritage-protection prototype with a multilingual digital guide, helping visitors learn, explore and protect Zimbabwe's cultural treasures.",

        "explore":
            "Explore Zimbabwe's heritage",

        "explore_sub":
            "Choose a heritage site and discover its history, people, architecture, stories and protection needs.",

        "open":
            "Open site guide",

        "history":
            "History",

        "culture":
            "Culture & People",

        "features":
            "Major Features",

        "unesco":
            "UNESCO World Heritage",

        "protection":
            "Protect This Heritage",

        "facts":
            "Interesting Facts",

        "significance":
            "Why It Matters",

        "location":
            "Location",

        "inscription":
            "UNESCO inscription",

        "criteria":
            "UNESCO criteria",

        "why":
            "Why ROBO GUIDE?",

        "why_text":
            "Culture is strongest when people understand it, experience it and help protect it. ROBO GUIDE turns heritage learning into an interactive visitor journey while demonstrating how affordable robotics can support respectful visitor behaviour.",

        "learn":
            "Learn",

        "learn_text":
            "Detailed heritage guides and learning in three languages.",

        "play":
            "Play",

        "play_text":
            "Earn Heritage Points through an interactive gamified challenge.",

        "protect":
            "Protect",

        "protect_text":
            "Use technology to encourage safe behaviour near sensitive heritage.",

        "connect":
            "Connect",

        "connect_text":
            "Link the physical prototype to deeper learning through QR access.",

        "challenge":
            "Take the Heritage Challenge",

        "ask":
            "Ask ROBO GUIDE",

        "robot":
            "Explore Robot Integration",

        "back":
            "← Back to Home",

        "quiz_title":
            "Heritage Challenge",

        "quiz_intro":
            "Test what you have learned about Zimbabwe's heritage. Correct answers earn Heritage Points and every answer includes an explanation.",

        "question":
            "Question",

        "score":
            "Score",

        "points":
            "Heritage Points",

        "submit":
            "Check Answer",

        "next":
            "Next Question →",

        "finish":
            "See My Achievement",

        "correct":
            "Correct!",

        "incorrect":
            "Not quite.",

        "replay":
            "Play Again",

        "achievement":
            "Achievement Unlocked",

        "guide":
            "Heritage Guide",

        "guardian":
            "Heritage Guardian",

        "guide_desc":
            "You have built a strong foundation. Keep exploring Zimbabwe's heritage and share what you learn.",

        "guardian_desc":
            "Outstanding work! You demonstrated excellent heritage knowledge and a strong conservation mindset.",

        "assistant_title":
            "ROBO GUIDE Heritage Assistant",

        "assistant_intro":
            "Ask detailed questions about Matobo Hills, Great Zimbabwe or Khami Ruins — including history, dates, builders, caves, rock art, architecture, artifacts, trade, culture, UNESCO, conservation or comparisons.",

        "assistant_placeholder":
            "Example: Who built Great Zimbabwe?",

        "try_question":
            "Try a question",

        "clear":
            "Clear Conversation",

        "no_answer":
            "I can answer questions about Matobo Hills, Great Zimbabwe and Khami Ruins. Try asking about history, builders, dates, caves, rock art, architecture, artifacts, trade, culture, UNESCO status, conservation, significance or comparisons.",

        "prototype_title":
            "How ROBO GUIDE Connects the Robot and Website",

        "prototype_intro":
            "ROBO GUIDE is one connected visitor-learning system. The physical prototype provides immediate guidance and protection while the website delivers deeper multilingual heritage education and data interpretation.",

        "flow":
            "Visitor Journey",

        "oled":
            "Multilingual OLED Education",

        "oled_text":
            "The physical prototype displays short heritage messages in English, isiNdebele and Shona so visitors can learn in a language they understand.",

        "qr":
            "QR Access",

        "qr_text":
            "A QR code on the physical ROBO GUIDE prototype opens this website, moving visitors from short exhibit messages into a detailed interactive heritage guide.",

        "visitor":
            "Visitor Guidance",

        "visitor_text":
            "ROBO GUIDE teaches respectful visitor behaviour such as staying behind protected boundaries, not touching rock art or stone structures, following site rules and respecting sacred places.",

        "ir":
            "IR Protected-Boundary Monitoring",

        "ir_text":
            "An infrared sensor detects when a visitor crosses the demonstration heritage-protection boundary. It provides a low-cost example of preventive conservation technology.",

        "buzzer":
            "Buzzer Warning",

        "buzzer_text":
            "When the protected boundary is crossed, the buzzer immediately warns the visitor to step back without requiring physical contact.",

        "dashboard":
            "Laptop Management Dashboard",

        "dashboard_text":
            "Boundary-crossing events can be recorded and analysed by time, frequency and trend. This can help identify high-risk periods and improve visitor education, staffing or protection measures.",

        "footer":
            "ROBO GUIDE • WRO 2026 Zimbabwe National Finals • Robots Meet Culture • Learn • Respect • Protect",
    },


    "isiNdebele": {

        "tagline":
            "Amarobhothi Ahlangana Lamasiko • WRO 2026 Zimbabwe",

        "language":
            "Ulimi",

        "navigation":
            "Hlola i-ROBO GUIDE",

        "home":
            "Ikhaya",

        "matobo":
            "Amagquma eMatobo",

        "great":
            "IGreat Zimbabwe",

        "khami":
            "Amanxiwa eKhami",

        "quiz":
            "Inselele Yamagugu",

        "assistant":
            "Umsizi Wamagugu",

        "prototype":
            "Irobhothi + Iwebhusayithi",

        "hero":
            "Hlangana leZimbabwe ngobuchwepheshe.",

        "hero_text":
            "I-ROBO GUIDE ixhumanisa irobhothi lokuvikela amagugu lomhlahlandlela wedijithali osebenza ngezindimi ezintathu, ukuze izivakashi zifunde, zihlole njalo zivikele amagugu amasiko eZimbabwe.",

        "explore":
            "Hlola amagugu eZimbabwe",

        "explore_sub":
            "Khetha indawo yamagugu ufunde ngomlando, abantu, izakhiwo, izindaba kanye lendlela yokuyivikela.",

        "open":
            "Vula umhlahlandlela",

        "history":
            "Umlando",

        "culture":
            "Amasiko Labantu",

        "features":
            "Izinto Eziqakathekileyo",

        "unesco":
            "Amagugu Omhlaba e-UNESCO",

        "protection":
            "Vikela Amagugu La",

        "facts":
            "Amaqiniso Athakazelisayo",

        "significance":
            "Kungani Kuqakathekile",

        "location":
            "Indawo",

        "inscription":
            "Ukubhaliswa yi-UNESCO",

        "criteria":
            "Imigomo ye-UNESCO",

        "why":
            "Kungani i-ROBO GUIDE?",

        "why_text":
            "Amasiko aqina nxa abantu bewazwisisa, bewabona njalo besiza ukuwavikela. I-ROBO GUIDE yenza ukufunda amagugu kube ngumsebenzi osebenzisanayo futhi iveze indlela amarobhothi anganceda ngayo ekuvikeleni indawo.",

        "learn":
            "Funda",

        "learn_text":
            "Imihlahlandlela ejulileyo yamagugu ngezindimi ezintathu.",

        "play":
            "Dlala",

        "play_text":
            "Thola amaHeritage Points ngokuphendula imibuzo.",

        "protect":
            "Vikela",

        "protect_text":
            "Sebenzisa ubuchwepheshe ukukhuthaza ukuziphatha okuphephileyo.",

        "connect":
            "Xhumanisa",

        "connect_text":
            "Xhumanisa irobhothi lolwazi olujulileyo ngeQR.",

        "challenge":
            "Yenza Inselele Yamagugu",

        "ask":
            "Buza i-ROBO GUIDE",

        "robot":
            "Bona Ukuxhumana Kwerobhothi",

        "back":
            "← Buyela Ekhaya",

        "quiz_title":
            "Inselele Yamagugu",

        "quiz_intro":
            "Hlola ulwazi lwakho ngamagugu eZimbabwe. Impendulo elungileyo iletha amaHeritage Points futhi yonke impendulo ilencazelo.",

        "question":
            "Umbuzo",

        "score":
            "Amaphuzu",

        "points":
            "AmaHeritage Points",

        "submit":
            "Hlola Impendulo",

        "next":
            "Umbuzo Olandelayo →",

        "finish":
            "Bona Umklomelo",

        "correct":
            "Kulungile!",

        "incorrect":
            "Akukabi yikho.",

        "replay":
            "Dlala Futhi",

        "achievement":
            "Umklomelo Uvuliwe",

        "guide":
            "Heritage Guide",

        "guardian":
            "Heritage Guardian",

        "guide_desc":
            "Usulolwazi oluqinileyo. Qhubeka uhlola amagugu eZimbabwe njalo wabelane ngalokho okufundayo.",

        "guardian_desc":
            "Umsebenzi omuhle kakhulu! Utshengise ulwazi olukhulu kanye lomqondo oqinileyo wokuvikela amagugu.",

        "assistant_title":
            "Umsizi Wamagugu we-ROBO GUIDE",

        "assistant_intro":
            "Buza ngeMatobo Hills, Great Zimbabwe kumbe Khami Ruins — umlando, izinsuku, abakhi, imigede, imidwebo emadwaleni, izakhiwo, izinto zakudala, ukuhweba, amasiko, UNESCO, ukuvikelwa kumbe ukuqhathanisa.",

        "assistant_placeholder":
            "Isibonelo: Ngubani owakha iGreat Zimbabwe?",

        "try_question":
            "Zama umbuzo",

        "clear":
            "Sula Ingxoxo",

        "no_answer":
            "Nginganceda ngezindawo ezintathu zeROBO GUIDE. Buza ngomlando, abakhi, izinsuku, imigede, imidwebo, izakhiwo, izinto zakudala, ukuhweba, amasiko, UNESCO, ukuvikelwa kumbe ukuqhathanisa.",

        "prototype_title":
            "Indlela i-ROBO GUIDE Exhumanisa Ngayo Irobhothi Lewebhusayithi",

        "prototype_intro":
            "I-ROBO GUIDE iyisistimu eyodwa yokufundisa izivakashi. Irobhothi linika ulwazi lokuvikela masinyane kuthi iwebhusayithi inike ulwazi olujulileyo ngezindimi ezintathu.",

        "flow":
            "Uhambo Lwesivakashi",

        "oled":
            "Imfundo ye-OLED Ngezindimi Ezintathu",

        "oled_text":
            "Iprototype iveza imilayezo emifitshane ngesiNgisi, isiNdebele kanye lesiShona ukuze izivakashi zifunde ngolimi eziluzwisisayo.",

        "qr":
            "Ukungena nge-QR",

        "qr_text":
            "Ikhodi yeQR embukisweni ivula iwebhusayithi yeROBO GUIDE, isusa isivakashi emlayezweni omfitshane isise emhlahlandleleni ogcweleyo.",

        "visitor":
            "Ukuqondisa Izivakashi",

        "visitor_text":
            "I-ROBO GUIDE ifundisa ukuziphatha okuhloniphayo: hlala ngaphandle kwemingcele evikelweyo, ungathinti imidwebo kumbe izakhiwo zamatshe njalo uhloniphe izindawo ezingcwele.",

        "ir":
            "Ukuqapha Umngcele nge-IR",

        "ir_text":
            "I-infrared sensor ibona nxa isivakashi siwela umngcele wokuvikela, itshengisa indlela ubuchwepheshe obunganceda ngayo ekuvikelweni kwamagugu.",

        "buzzer":
            "Isixwayiso se-Buzzer",

        "buzzer_text":
            "Nxa umngcele oweqiwa i-buzzer inika isixwayiso masinyane, ikhuthaze isivakashi ukuthi sihlehle.",

        "dashboard":
            "Ideshibhodi Yokuphatha Kukhompyutha",

        "dashboard_text":
            "Izehlakalo zokweqa umngcele zingarekhodwa futhi zihlaziywe ngesikhathi, ngobunengi kanye lemikhuba ukuze abaphathi bathuthukise ukuvikelwa.",

        "footer":
            "ROBO GUIDE • WRO 2026 Zimbabwe National Finals • Robots Meet Culture • Funda • Hlonipha • Vikela",
    },


    "Shona": {

        "tagline":
            "Marobhoti Anosangana Netsika • WRO 2026 Zimbabwe",

        "language":
            "Mutauro",

        "navigation":
            "Ongorora ROBO GUIDE",

        "home":
            "Kumba",

        "matobo":
            "Matobo Hills",

        "great":
            "Great Zimbabwe",

        "khami":
            "Khami Ruins",

        "quiz":
            "Heritage Challenge",

        "assistant":
            "Mubatsiri weNhaka",

        "prototype":
            "Robhoti + Webhusaiti",

        "hero":
            "Sangana neZimbabwe kuburikidza netekinoroji.",

        "hero_text":
            "ROBO GUIDE inobatanidza prototype yerobhoti rekuchengetedza nhaka nemutungamiriri wedhijitari wemitauro mitatu, ichibatsira vashanyi kudzidza, kuongorora uye kuchengetedza pfuma yetsika yeZimbabwe.",

        "explore":
            "Ongorora nhaka yeZimbabwe",

        "explore_sub":
            "Sarudza nzvimbo kuti uzive nhoroondo, vanhu, zvivakwa, nyaya uye nzira dzekuichengetedza.",

        "open":
            "Vhura Mutungamiriri",

        "history":
            "Nhoroondo",

        "culture":
            "Tsika Nevanhu",

        "features":
            "Zvinhu Zvikuru",

        "unesco":
            "UNESCO World Heritage",

        "protection":
            "Chengetedza Nhaka Iyi",

        "facts":
            "Mashoko Anonakidza",

        "significance":
            "Kukosha Kwayo",

        "location":
            "Nzvimbo",

        "inscription":
            "Kunyoreswa neUNESCO",

        "criteria":
            "Mitemo yeUNESCO",

        "why":
            "Sei ROBO GUIDE?",

        "why_text":
            "Tsika dzinosimba kana vanhu vachidzinzwisisa, vachidziona uye vachibatsira kudzichengetedza. ROBO GUIDE inoita kuti kudzidza nhaka kuve chiitiko chinodyidzana uye inoratidza mashandisirwo etekinoroji mukuchengetedza nzvimbo.",

        "learn":
            "Dzidza",

        "learn_text":
            "Mitungamiriri yakadzama yenzvimbo dzenhaka mumitauro mitatu.",

        "play":
            "Tamba",

        "play_text":
            "Wana Heritage Points kuburikidza nemibvunzo inodyidzana.",

        "protect":
            "Chengetedza",

        "protect_text":
            "Shandisa tekinoroji kukurudzira maitiro anoremekedza nhaka.",

        "connect":
            "Batanidza",

        "connect_text":
            "QR inobatanidza physical prototype neruzivo rwakadzama.",

        "challenge":
            "Tora Heritage Challenge",

        "ask":
            "Bvunza ROBO GUIDE",

        "robot":
            "Ona Kubatana Kwerobhoti",

        "back":
            "← Dzokera Kumba",

        "quiz_title":
            "Heritage Challenge",

        "quiz_intro":
            "Edza ruzivo rwako rwenhaka yeZimbabwe. Mhinduro dzakarurama dzinokupa Heritage Points uye mhinduro dzese dzine tsananguro.",

        "question":
            "Mubvunzo",

        "score":
            "Zvawawana",

        "points":
            "Heritage Points",

        "submit":
            "Tarisa Mhinduro",

        "next":
            "Mubvunzo Unotevera →",

        "finish":
            "Ona Mubairo",

        "correct":
            "Zvakarurama!",

        "incorrect":
            "Hazvisati zvanyatsonaka.",

        "replay":
            "Tamba Zvakare",

        "achievement":
            "Mubairo Wavhurwa",

        "guide":
            "Heritage Guide",

        "guardian":
            "Heritage Guardian",

        "guide_desc":
            "Wava neruzivo rwakanaka. Ramba uchiongorora nhaka yeZimbabwe uye ugovane zvaunodzidza.",

        "guardian_desc":
            "Basa rakanaka zvikuru! Waratidza ruzivo rwakadzama uye pfungwa yakasimba yekuchengetedza nhaka.",

        "assistant_title":
            "ROBO GUIDE Heritage Assistant",

        "assistant_intro":
            "Bvunza nezveMatobo Hills, Great Zimbabwe kana Khami Ruins — nhoroondo, mazuva, vavaki, mapako, rock art, architecture, artifacts, trade, tsika, UNESCO, conservation kana comparisons.",

        "assistant_placeholder":
            "Semuenzaniso: Ndiani akavaka Great Zimbabwe?",

        "try_question":
            "Edza mubvunzo",

        "clear":
            "Bvisa Hurukuro",

        "no_answer":
            "Ndinogona kubatsira nezvenzvimbo nhatu dzeROBO GUIDE. Bvunza nezvenhoroondo, vavaki, mazuva, mapako, rock art, architecture, artifacts, trade, tsika, UNESCO, conservation kana comparisons.",

        "prototype_title":
            "Maitiro ROBO GUIDE Anobatanidza Robhoti Newebhusaiti",

        "prototype_intro":
            "ROBO GUIDE ihurongwa humwe hwekudzidzisa vashanyi. Prototype inopa yambiro nekudzidzisa ipapo, uku webhusaiti ichipa ruzivo rwakadzama rwemitauro mitatu.",

        "flow":
            "Rwendo Rwemushanyi",

        "oled":
            "Dzidzo yeOLED Yemitauro Mitatu",

        "oled_text":
            "Prototype inoratidza mashoko mapfupi muEnglish, isiNdebele neShona kuitira kuti vashanyi vadzidze nemutauro wavanonzwisisa.",

        "qr":
            "QR Access",

        "qr_text":
            "QR code iri paprototype inovhura ROBO GUIDE webhusaiti, ichiendesa mushanyi kubva pamashoko mapfupi kuenda kumutungamiriri wakadzama.",

        "visitor":
            "Kutungamirira Vashanyi",

        "visitor_text":
            "ROBO GUIDE inodzidzisa maitiro anoremekedza nhaka: gara kunze kwemiganhu yakachengetedzwa, usabata rock art kana ancient stonework uye remekedza nzvimbo dzinoyera.",

        "ir":
            "IR Protected-Boundary Monitoring",

        "ir_text":
            "Infrared sensor inoona kana mushanyi ayambuka muganhu wekuchengetedza, ichiratidza kuti tekinoroji inogona kubatsira sei mukudzivirira kukuvara.",

        "buzzer":
            "Yambiro yeBuzzer",

        "buzzer_text":
            "Kana muganhu wayambukwa buzzer inopa yambiro ipapo uye inokurudzira mushanyi kudzokera shure.",

        "dashboard":
            "Laptop Management Dashboard",

        "dashboard_text":
            "Boundary-crossing events dzinogona kurekodhwa nekuongororwa nenguva, frequency uye trend kuti mamaneja avandudze visitor education nekuchengetedza.",

        "footer":
            "ROBO GUIDE • WRO 2026 Zimbabwe National Finals • Robots Meet Culture • Dzidza • Remekedza • Chengetedza",
    },
}


# ------------------------------------------------------------
# HERITAGE SITE CONTENT
# ------------------------------------------------------------

SITES = {

    "Matobo Hills": {

        "emoji":
            "🪨",

        "English": {

            "name":
                "Matobo Hills",

            "subtitle":
                "A living cultural landscape of granite hills, sacred places, caves and extraordinary rock art.",

            "location":
                "Matabeleland South, south of Bulawayo, Zimbabwe",

            "inscribed":
                "2003",

            "criteria":
                "(iii), (v), (vi)",

            "history":
                """
Matobo Hills is one of Zimbabwe's most remarkable cultural landscapes.
Its granite formations have provided shelter, food, spiritual meaning and
strategic refuge to people for thousands of years.

Archaeological evidence in the hills reaches far back into the Stone Age.
Hunter-gatherer communities used the caves and rock shelters and left behind
a remarkable artistic record in the form of paintings.

Later farming communities occupied the wider landscape, while Matobo also
became closely connected with Ndebele history during the nineteenth century.

The landscape therefore records many different periods of Zimbabwean history
rather than representing only one community or one time.
""",

            "culture":
                """
Matobo remains a living cultural and spiritual landscape.

Sacred hills, shrines, oral traditions and ancestral associations remain
important to communities around the area. The Mwari religious tradition,
rain-making beliefs and respect for sacred places contribute to the continuing
cultural significance of Matobo.

The hills are also strongly connected to Ndebele history, including memories
of King Mzilikazi and important nineteenth-century events.

This means that protecting Matobo requires protecting both physical heritage
and living traditions.
""",

            "features": [

                "Granite kopjes, balancing rocks and dramatic valleys created through long geological weathering.",

                "Natural caves and rock shelters that protected people and preserved archaeological evidence.",

                "A very high concentration of prehistoric rock paintings.",

                "Paintings showing humans, animals, hunting, movement and aspects of past social and spiritual life.",

                "Archaeological deposits that help researchers understand changing human occupation over thousands of years.",

                "Sacred hills and shrines that remain culturally important to surrounding communities.",

                "A landscape strongly associated with Zimbabwean and Ndebele history.",
            ],

            "unesco":
                """
Matobo Hills was inscribed on the UNESCO World Heritage List in 2003
as a cultural landscape under criteria (iii), (v) and (vi).

UNESCO recognizes its exceptional concentration of rock art, the very long
relationship between communities and the landscape, and the continuing
importance of powerful religious traditions associated with the hills.
""",

            "protection": [

                "Never touch rock paintings because oils and moisture from human hands can damage fragile surfaces.",

                "Never wet paintings to make their colours appear stronger.",

                "Do not trace paintings using chalk, pencil, paint or any other material.",

                "Stay behind barriers and use approved visitor paths.",

                "Do not remove stones, pottery fragments or archaeological material.",

                "Respect sacred areas and instructions given by local custodians and heritage guides.",

                "Avoid graffiti, fire, littering and climbing over sensitive painted surfaces.",
            ],

            "facts": [

                "Matobo has one of the highest concentrations of rock art in southern Africa.",

                "Some rock shelters contain several layers of paintings created during different periods.",

                "Granite shelters helped preserve both paintings and archaeological deposits.",

                "Matobo is not simply an archaeological site — it remains a living spiritual landscape.",

                "The landscape combines natural beauty with archaeology, history, belief and art.",
            ],

            "significance":
                """
Matobo demonstrates that heritage can be both ancient and living.
Its caves, paintings, archaeology, oral history and sacred landscape allow
visitors to understand how generations of people interacted with the same
environment in very different ways.
""",
        },


        "isiNdebele": {

            "name":
                "Amagquma eMatobo",

            "subtitle":
                "Indawo yamasiko ephilayo elamagquma egranite, izindawo ezingcwele, imigede kanye lemidwebo emangalisayo emadwaleni.",

            "location":
                "EMatabeleland South, eningizimu yeBulawayo, eZimbabwe",

            "inscribed":
                "2003",

            "criteria":
                "(iii), (v), (vi)",

            "history":
                """
IMatobo ingenye yezindawo zamasiko eziqakathekileyo kakhulu eZimbabwe.
Amadwala ayo egranite anike abantu indawo yokukhosela kanye lendawo
yokuphila okweminyaka eminengi.

Ubufakazi bezinto zakudala bubuyela eStone Age.
Abazingeli labaqoqi basebenzisa imigede lezindawo zokukhosela
futhi batshiya imidwebo emangalisayo emadwaleni.

Abalimi abalandelayo labo bahlala endaweni le.
IMatobo yabuye yaba yindawo eqakathekileyo emlandweni wamaNdebele.

Ngakho iMatobo igcina umlando wezikhathi lemiphakathi etshiyeneyo.
""",

            "culture":
                """
IMatobo iseyindawo ephilayo yamasiko lokomoya.

Amagquma angcwele, izindawo zokukhulekela, izindaba zomlomo kanye
lobudlelwano labokhokho kusaqakathekile emiphakathini.

Inkolelo kaMwari kanye lamasiko ahlobene lokucela izulu lawo ayingxenye
yokubaluleka kwendawo.

IMatobo iphinde ixhumane kakhulu lomlando wamaNdebele, okuhlanganisa
inkumbulo yeNkosi uMzilikazi.

Ukuvikela iMatobo yikho ukuvikela kokubili izinto ezibonakalayo
kanye lamasiko aphilayo.
""",

            "features": [

                "Amagquma egranite, amatshe azilinganisileyo kanye lezihotsha ezinhle.",

                "Imigede lezindawo zemvelo zokukhosela.",

                "Imidwebo eminengi kakhulu yakudala emadwaleni.",

                "Imidwebo yabantu, izinyamazana, ukuzingela kanye lezinye izenzo.",

                "Ubufakazi bezinto zakudala obunceda ukufunda impilo yabantu bakudala.",

                "Izindawo ezingcwele ezisaqakathekile emphakathini.",

                "Indawo exhumene kakhulu lomlando wamaNdebele.",
            ],

            "unesco":
                """
IMatobo Hills yabhaliswa ku-UNESCO World Heritage List ngo-2003
njengendawo yamasiko ngaphansi kwemigomo (iii), (v) kanye (vi).

I-UNESCO iqaphela ubunengi bemidwebo emadwaleni, ubudlelwano obude
phakathi kwabantu lendawo, kanye lokuqhubeka kwamasiko okomoya.
""",

            "protection": [

                "Ungathinti imidwebo emadwaleni ngoba amafutha asezandleni angayonakalisa.",

                "Ungamanzisi imidwebo ukuze imibala ibonakale kakhulu.",

                "Ungayicuphi ngechalk, ipensela loba upende.",

                "Hamba ngemizila evunyelweyo njalo uhlale ngemva kwemingcele.",

                "Ungasusi amatshe kumbe ezinye izinto zakudala.",

                "Hlonipha izindawo ezingcwele kanye lemithetho yendawo.",

                "Gwema ingcekeza, umlilo, graffiti kanye lokugibela phezu kwamatshe avikelweyo.",
            ],

            "facts": [

                "IMatobo ilobunengi obukhulu bemidwebo emadwaleni eSouthern Africa.",

                "Ezinye indawo zilezigaba eziningi zemidwebo ezenziwa ngezikhathi ezitshiyeneyo.",

                "Imigede yegranite yanceda ukugcina imidwebo.",

                "IMatobo ayisiyo archaeological site kuphela — iyindawo ephilayo ngokomoya.",

                "Indawo ixhumanisa ubuhle bemvelo, umlando, amasiko kanye lobuciko.",
            ],

            "significance":
                """
IMatobo itshengisa ukuthi amagugu angaba madala kodwa aqhubeke ephila.
Imigede, imidwebo, izinto zakudala, izindaba zabantu kanye lezindawo
ezingcwele kwenza iMatobo ibe yingxenye eqakathekileyo yobuwena beZimbabwe.
""",
        },


        "Shona": {

            "name":
                "Matobo Hills",

            "subtitle":
                "Nzvimbo yetsika inorarama ine zvikomo zvegranite, nzvimbo dzinoyera, mapako uye rock art inoshamisa.",

            "location":
                "Matabeleland South, kumaodzanyemba kweBulawayo, Zimbabwe",

            "inscribed":
                "2003",

            "criteria":
                "(iii), (v), (vi)",

            "history":
                """
Matobo Hills imwe yenzvimbo dzenhaka dzakakosha zvikuru muZimbabwe.
Matombo egranite akapa vanhu nzvimbo dzekugara nekuzvivanza kwemakore
akawanda zvikuru.

Archaeological evidence inodzokera kuStone Age.
Hunter-gatherer communities vakashandisa mapako nemarock shelters
uye vakasiya mifananidzo yakawanda pamabwe.

Mapoka evarimi akazotevera akashandisawo nzvimbo iyi.
Matobo yakazobatanawo zvakanyanya nenhoroondo yeNdebele.

Saka nzvimbo iyi inochengeta nyaya dzemakore nemapoka evanhu akasiyana.
""",

            "culture":
                """
Matobo haisi nzvimbo yekare chete.
Ichiri cultural uye spiritual landscape inorarama.

Nzvimbo dzinoyera, shrines, oral traditions nemadzitateguru
zvichiri kukosha kum communities.

Mwari religious tradition netsika dzekukumbira mvura zvakare
zvine hukama neMatobo.

Nzvimbo iyi ine hukama hwakasimba nenhoroondo yeNdebele,
kusanganisira ndangariro dzaMambo Mzilikazi.

Kuchengetedza Matobo zvinoreva kuchengetedza zvivakwa nezvinhu
zvayo pamwe netsika dzichiri kurarama.
""",

            "features": [

                "Granite kopjes, balancing rocks nemipata inoshamisa.",

                "Mapako nemarock shelters akagadzirwa nezvisikwa.",

                "Huwandu hukuru hweprehistoric rock paintings.",

                "Paintings dzinoratidza vanhu, mhuka, kuvhima nezvimwe zviitiko.",

                "Archaeological deposits dzinobatsira kunzwisisa hupenyu hwekare.",

                "Nzvimbo dzinoyera dzichiri kukosha kum communities.",

                "Landscape ine hukama hwakadzama nenhoroondo yeZimbabwe neNdebele.",
            ],

            "unesco":
                """
Matobo Hills yakanyoreswa paUNESCO World Heritage List muna 2003
se cultural landscape pasi pecriteria (iii), (v) ne(vi).

UNESCO inocherechedza kuwanda kwe rock art, hukama hurefu pakati
pevanhu nenzvimbo uye spiritual traditions dzichiri kurarama.
""",

            "protection": [

                "Usabata rock paintings nekuti mafuta ari pamaoko anogona kudzikuvara.",

                "Usanyorovesa paintings kuti colours dzinyanye kuoneka.",

                "Usa trace mifananidzo nechalk, penzura kana paint.",

                "Shandisa nzira dzakatenderwa uye gara kuseri kwemiganhu.",

                "Usabvisa matombo kana archaeological material.",

                "Remekedza nzvimbo dzinoyera nemirayiridzo yevatungamiriri.",

                "Dzivisa graffiti, moto, marara uye kukwira pamatombo ane paintings.",
            ],

            "facts": [

                "Matobo ine imwe yehuwandu hukuru hwe rock art muSouthern Africa.",

                "Mamwe marock shelters ane layers dzemifananidzo dzemakore akasiyana.",

                "Granite shelters dzakabatsira kuchengetedza paintings.",

                "Matobo ichiri spiritual landscape inorarama.",

                "Nzvimbo iyi inobatanidza nature, archaeology, history, spirituality neart.",
            ],

            "significance":
                """
Matobo inoratidza kuti nhaka inogona kuva yekare uye ichiri kurarama.
Mapako, rock art, archaeology, oral history netsika dzinoyera
zvinoita kuti ive chikamu chakakosha chenhaka yeZimbabwe.
""",
        },
    },


    "Great Zimbabwe": {

        "emoji":
            "🏛️",

        "English": {

            "name":
                "Great Zimbabwe",

            "subtitle":
                "The monumental stone capital whose name became the name of a nation.",

            "location":
                "Masvingo Province, south-eastern Zimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(i), (iii), (vi)",

            "history":
                """
Great Zimbabwe developed into a major political, economic and cultural
centre between roughly the eleventh and fifteenth centuries.

The city was built and occupied by ancestors of Shona-speaking communities.
Its growth demonstrates the existence of a powerful and highly organized
African society with skilled builders, craftspeople, traders and leaders.

Great Zimbabwe participated in long-distance commercial networks linking
the Zimbabwe Plateau with other parts of Africa and ultimately the
Indian Ocean world.

Its scale, wealth and monumental architecture made it one of the most
important pre-colonial urban centres in southern Africa.
""",

            "culture":
                """
Great Zimbabwe is deeply connected to Zimbabwean identity and to the
history of Shona-speaking communities.

Leadership, cattle wealth, spirituality, craft production and trade were
important parts of the society that developed around the city.

The name Zimbabwe is commonly associated with Shona expressions connected
with houses or buildings of stone.

The site's legacy became so powerful that the independent nation adopted
the name Zimbabwe.

The Zimbabwe Bird, inspired by soapstone bird sculptures found at the site,
also became a national symbol.
""",

            "features": [

                "The Hill Complex, constructed among natural granite boulders.",

                "The Great Enclosure, surrounded by an enormous dry-stone wall.",

                "The famous Conical Tower within the Great Enclosure.",

                "The Valley Ruins, containing numerous stone enclosures.",

                "Sophisticated dry-stone masonry constructed without mortar.",

                "Carved soapstone Zimbabwe Birds.",

                "Evidence of local craft industries and long-distance trade.",

                "Decorative stone patterns built into sections of the walls.",
            ],

            "unesco":
                """
Great Zimbabwe National Monument was inscribed on the UNESCO World
Heritage List in 1986 under criteria (i), (iii) and (vi).

UNESCO recognizes its remarkable architectural achievement, its exceptional
testimony to an important African civilization and its powerful historic
and symbolic importance.
""",

            "protection": [

                "Never climb ancient walls.",

                "Do not sit or lean on dry-stone structures.",

                "Do not remove stones, pottery, beads or archaeological objects.",

                "Stay on designated visitor routes.",

                "Do not carve or scratch names into stone surfaces.",

                "Follow guides and respect restricted areas.",

                "Protect the setting as well as individual walls and artifacts.",
            ],

            "facts": [

                "Modern Zimbabwe takes its name from Great Zimbabwe.",

                "Its monumental walls were built without mortar.",

                "The Great Enclosure is one of the most famous pre-colonial stone structures in sub-Saharan Africa.",

                "Zimbabwe Bird sculptures were carved from soapstone.",

                "The Zimbabwe Bird later became an important national emblem.",

                "Archaeological finds show participation in wide trade networks.",

                "The site provides strong evidence of sophisticated African architecture and state organization.",
            ],

            "significance":
                """
Great Zimbabwe is powerful evidence of African political organization,
architecture, craftsmanship and trade.

It is also important because modern archaeological research corrected
old colonial-era claims that attempted to deny African authorship of
the monument.

Great Zimbabwe stands as both an archaeological achievement and
a major national symbol.
""",
        },


        "isiNdebele": {

            "name":
                "IGreat Zimbabwe",

            "subtitle":
                "Inhloko-dolobha enkulu yamatshe eyapha ilizwe igama lalo.",

            "location":
                "EMasvingo Province, eningizimu-mpumalanga yeZimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(i), (iii), (vi)",

            "history":
                """
IGreat Zimbabwe yakhula yaba yindawo enkulu yezombusazwe,
ezomnotho lamasiko phakathi kwekhulu le-11 lele-15.

Yakhiwa futhi yahlalwa ngokhokho bemiphakathi ekhuluma isiShona.

Ukukhula kwayo kutshengisa ukuthi kwakukhona umbuso waseAfrica
owawulabakhi abalolwazi, abenza imisebenzi yezandla, abahwebi
kanye labakhokheli.

IGreat Zimbabwe yayixhumene lokuhweba okude okwakuxhumanisa
iZimbabwe Plateau lezinye indawo zeAfrica kanye lezindlela
zokuhweba zeIndian Ocean.
""",

            "culture":
                """
IGreat Zimbabwe ixhumene kakhulu lobuwena beZimbabwe kanye
lomlando wemiphakathi ekhuluma isiShona.

Ubukhokheli, inkomo, okomoya, ubuciko kanye lokuhweba kwakuyingxenye
eqakathekileyo yempilo.

Igama elithi Zimbabwe lixhunyaniswa lamazwi esiShona aphathelane
lezindlu kumbe izakhiwo zamatshe.

Ilizwe laseZimbabwe lathatha igama lalo kule ndawo.

IZimbabwe Bird eyatholakala lapha yaba luphawu oluqakathekileyo lwesizwe.
""",

            "features": [

                "I-Hill Complex eyakhiwe phakathi kwamadwala egranite.",

                "I-Great Enclosure elodonga olukhulu lwamatshe.",

                "I-Conical Tower edumileyo.",

                "I-Valley Ruins elezakhiwo zamatshe ezinengi.",

                "Imiduli eyakhiwe ngamatshe ngaphandle kwe-mortar.",

                "IZimbabwe Birds ezibazwe ngesoapstone.",

                "Ubufakazi bobuciko bendawo kanye lokuhweba okude.",

                "Amaphetheni amahle akhiwe emidulini.",
            ],

            "unesco":
                """
IGreat Zimbabwe National Monument yabhaliswa ku-UNESCO World Heritage
List ngo-1986 ngaphansi kwemigomo (i), (iii) kanye (vi).

I-UNESCO iqaphela ubuciko bokwakha, ubufakazi bempucuko enkulu yaseAfrica
kanye lokubaluleka kwendawo emlandweni.
""",

            "protection": [

                "Ungagibeli emidulini yakudala.",

                "Ungahlali kumbe uncike emidulini.",

                "Ungasusi amatshe, pottery, ubuhlalu kumbe izinto zakudala.",

                "Hamba ngemizila yezivakashi.",

                "Ungaqophi amagama ematsheni.",

                "Landela imithetho yabakhokheli.",

                "Hlonipha izindawo ezingavunyelwanga ukungena kuzo.",
            ],

            "facts": [

                "Ilizwe laseZimbabwe lathatha igama lalo eGreat Zimbabwe.",

                "Imiduli emikhulu yakhiwa ngaphandle kwe-mortar.",

                "IGreat Enclosure ingenye yezakhiwo ezidume kakhulu eAfrica.",

                "IZimbabwe Birds zabazwa ngesoapstone.",

                "Inyoni yeZimbabwe yaba luphawu lwesizwe.",

                "Izinto ezatholakala lapha zitshengisa ukuhweba okude.",

                "Indawo itshengisa ubuciko obukhulu bokwakha baseAfrica.",
            ],

            "significance":
                """
IGreat Zimbabwe iyibufakazi bokuthi imiphakathi yaseAfrica yayilobukhokheli,
ubuciko bokwakha, imisebenzi yezandla kanye lokuhweba okuphucukileyo.

Iqakathekile futhi ngoba ubufakazi bezinto zakudala baphikisa imibono
yakudala eyayizama ukuphika ukuthi yakhiwa ngabantu baseAfrica.
""",
        },


        "Shona": {

            "name":
                "Great Zimbabwe",

            "subtitle":
                "Guta guru rematombo rakazopa nyika zita rayo.",

            "location":
                "Masvingo Province, kumaodzanyemba-kumabvazuva kweZimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(i), (iii), (vi)",

            "history":
                """
Great Zimbabwe yakakura kuva political, economic uye cultural centre
huru pakati pezvinenge zana remakore rechi11 nerechi15.

Yakavakwa nekugarwa nemadzitateguru evanhu vanotaura Shona.

Kukura kweguta kunoratidza nzanga yeAfrica yaive nehutungamiri,
vavaki vane hunyanzvi, craftspeople uye vatengesi.

Great Zimbabwe yaive chikamu che long-distance trade networks
dzakabatanidza Zimbabwe Plateau nedzimwe nzvimbo dzeAfrica
uye Indian Ocean world.
""",

            "culture":
                """
Great Zimbabwe yakabatana zvakadzama neZimbabwean identity
uye nhoroondo yevanhu vanotaura Shona.

Hutungamiri, mombe, spirituality, craft production uye trade
zvaive zvakakosha muupenyu hwenharaunda.

Zita rekuti Zimbabwe rinowanzobatanidzwa nemashoko echiShona
ane chekuita nedzimba kana zvivakwa zvematombo.

Nyika yakazvimirira yakatora zita rekuti Zimbabwe.

Zimbabwe Bird yakawanikwa panzvimbo iyi yakazovawo chiratidzo
chakakosha chenyika.
""",

            "features": [

                "Hill Complex yakavakwa pakati pematombo makuru egranite.",

                "Great Enclosure ine madziro makuru edry-stone.",

                "Conical Tower inozivikanwa zvikuru.",

                "Valley Ruins ine zvivakwa zvakawanda zvematombo.",

                "Dry-stone masonry yakavakwa pasina mortar.",

                "Zimbabwe Birds dzakavezwa musoapstone.",

                "Evidence yemabasa emaoko nekutengeserana kure.",

                "Decorative patterns dziri pamadziro.",
            ],

            "unesco":
                """
Great Zimbabwe National Monument yakanyoreswa paUNESCO World Heritage
List muna 1986 pasi pecriteria (i), (iii) ne(vi).

UNESCO inocherechedza architectural achievement yayo,
humbowo hwebudiriro huru yeAfrica uye kukosha kwayo munhoroondo.
""",

            "protection": [

                "Usakwira pamadziro ekare.",

                "Usagara kana kuzembera pamadziro.",

                "Usabvisa matombo, pottery, beads kana archaeological material.",

                "Shandisa visitor paths dzakatemerwa.",

                "Usakwenya kana kuveza mazita pamatombo.",

                "Tevera mirayiridzo yemaguides.",

                "Remekedza nzvimbo dzakarambidzwa.",
            ],

            "facts": [

                "Zimbabwe yemazuva ano yakatora zita rayo kuGreat Zimbabwe.",

                "Madziro makuru akavakwa pasina mortar.",

                "Great Enclosure ndeimwe yezvivakwa zvematombo zvinozivikanwa zvikuru muAfrica.",

                "Zimbabwe Birds dzakavezwa musoapstone.",

                "Zimbabwe Bird yakazova national symbol.",

                "Archaeology inoratidza long-distance trade.",

                "Nzvimbo iyi inoratidza advanced African architecture nepolitical organization.",
            ],

            "significance":
                """
Great Zimbabwe ihumbowo hwakasimba hweAfrican statecraft,
architecture, craftsmanship uye trade.

Archaeology yemazuva ano yakagadzirisawo pfungwa dzekare dzaiedza
kuramba kuti monument iyi yakavakwa nevanhu veAfrica.

Nhasi inzvimbo yakakosha munhoroondo uye national identity.
""",
        },
    },


    "Khami Ruins": {

        "emoji":
            "🧱",

        "English": {

            "name":
                "Khami Ruins",

            "subtitle":
                "A terraced stone city of the Torwa era, rich in decorative masonry and trade history.",

            "location":
                "Near Bulawayo, western Zimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(iii), (iv)",

            "history":
                """
Khami became an important political centre after the decline of
Great Zimbabwe.

It became the capital of the Torwa state, especially from the
fifteenth century into the seventeenth century.

Its rulers controlled an important political and economic centre
in south-western Zimbabwe.

Archaeology shows that Khami participated in regional and
long-distance trading systems.

Imported ceramics and other prestige goods have been found alongside
local material culture.

Khami therefore demonstrates the continuation and transformation of
the wider Zimbabwe stone-building tradition.
""",

            "culture":
                """
Khami reflects the political authority, household organization,
craftsmanship and trading connections of communities in south-western
Zimbabwe.

Its architecture shows clear links with the broader Zimbabwe cultural
tradition, but Khami's builders developed distinctive ways of using
terraces and retaining walls.

The site demonstrates that cultural traditions can continue while
architecture and political systems change over time.
""",

            "features": [

                "Large stone-faced terraces built into the natural landscape.",

                "Raised platforms associated with important occupation areas.",

                "Decorative dry-stone wall patterns.",

                "Retaining walls constructed using carefully laid stone.",

                "The Hill Complex and other major architectural platforms.",

                "Evidence of regional and long-distance trade.",

                "Imported ceramics and other prestige goods.",

                "An architectural tradition related to Great Zimbabwe but expressed through extensive terracing.",
            ],

            "unesco":
                """
Khami Ruins National Monument was inscribed on the UNESCO World
Heritage List in 1986 under criteria (iii) and (iv).

UNESCO recognizes Khami as exceptional testimony to an important
cultural tradition and as an outstanding architectural ensemble
representing an important stage in southern African history.
""",

            "protection": [

                "Never climb or walk along fragile terrace walls.",

                "Stay on designated visitor paths.",

                "Do not remove pottery, beads, stones or archaeological objects.",

                "Do not rearrange loose stones.",

                "Avoid actions that increase erosion around terraces.",

                "Do not scratch or write on decorative stonework.",

                "Follow site instructions designed to protect unstable structures.",
            ],

            "facts": [

                "Khami became prominent after Great Zimbabwe declined.",

                "It is closely associated with the Torwa state.",

                "Its terraces make it visually different from Great Zimbabwe's best-known freestanding walls.",

                "Decorative wall patterns are an important feature of the site.",

                "Imported goods show Khami's participation in wider trade networks.",

                "Khami demonstrates change and innovation within the Zimbabwe stone-building tradition.",
            ],

            "significance":
                """
Khami shows that Zimbabwe's stone-building tradition did not simply
disappear when Great Zimbabwe declined.

The tradition continued, developed and changed.

Khami's terraces, decorative masonry and archaeological evidence show
political organization, skilled architecture and participation in
regional and long-distance trade.
""",
        },


        "isiNdebele": {

            "name":
                "Amanxiwa eKhami",

            "subtitle":
                "Idolobho lamatshe elamathala eTorwa, elicebile ngobuciko bamatshe kanye lomlando wokuhweba.",

            "location":
                "Eduze leBulawayo, entshonalanga yeZimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(iii), (iv)",

            "history":
                """
IKhami yakhula yaba yindawo enkulu ngemva kokwehla kweGreat Zimbabwe.

Yaba yinhloko yombuso weTorwa ikakhulu kusukela ngekhulu le-15
kusiya kwele-17.

Ababusi bayo babelawula indawo eqakathekileyo kwezombusazwe
lezomnotho eNingizimu-Ntshonalanga yeZimbabwe.

Ubufakazi bezinto zakudala butshengisa ukuthi iKhami yayixhumene
lokuhweba okuseduze kanye lokukude.

Izinto ezavela kwamanye amazwe zitholakale kanye lezinto ezenziwa
ngabantu bendawo.

IKhami ngakho itshengisa ukuqhubeka kanye lokuguquka kwesiko
lokwakha ngamatshe eZimbabwe.
""",

            "culture":
                """
IKhami itshengisa amandla ezombusazwe, ukuhleleka kwemizi,
ubuciko kanye lokuxhumana kwezokuhweba.

Izakhiwo zayo zixhumene lesiko elikhulu lokwakha ngamatshe eZimbabwe
kodwa abakhi beKhami basebenzisa amathala lemiduli yokubamba umhlabathi
ngendlela evelele kakhulu.

Lokhu kutshengisa ukuthi amasiko angaqhubeka kodwa indlela yokwakha
iguquke ngesikhathi.
""",

            "features": [

                "Amathala amakhulu alemiduli yamatshe.",

                "Amapulatifomu aphakemeyo akhiwe ehambisana lendawo.",

                "Amaphetheni amahle e-dry-stone masonry.",

                "Imiduli yokubamba umhlabathi.",

                "I-Hill Complex lamanye amapulatifomu amakhulu.",

                "Ubufakazi bokuhweba kwesigaba lesikude.",

                "Ceramics kanye lezinto ezavela kwamanye amazwe.",

                "Isiko lokwakha elixhumene leGreat Zimbabwe kodwa elisebenzisa amathala kakhulu.",
            ],

            "unesco":
                """
IKhami Ruins National Monument yabhaliswa ku-UNESCO World Heritage
List ngo-1986 ngaphansi kwemigomo (iii) kanye (iv).

I-UNESCO iyibona njengobufakazi obukhulu besiko kanye lesibonelo
esihle seqoqo lezakhiwo lesigaba esiqakathekileyo emlandweni
weSouthern Africa.
""",

            "protection": [

                "Ungagibeli kumbe uhambe phezu kwemiduli yamathala.",

                "Hamba ngemizila evunyelweyo.",

                "Ungasusi pottery, ubuhlalu, amatshe kumbe izinto zakudala.",

                "Ungahlele kabutsha amatshe aphumileyo.",

                "Gwema ukwenza izinto ezenza umhlabathi uguguleke.",

                "Ungaqophi kumbe ubhale emidulini.",

                "Landela iziqondiso zokuvikela izakhiwo.",
            ],

            "facts": [

                "IKhami yakhula ngemva kokwehla kweGreat Zimbabwe.",

                "Ixhumene kakhulu lombuso weTorwa.",

                "Amathala ayo ayenza yehluke kakhulu eGreat Zimbabwe.",

                "Imiduli ehlotshisiwe ingenye yezinto ezidume kakhulu.",

                "Izinto ezavela kwamanye amazwe zitshengisa ukuhweba okude.",

                "IKhami itshengisa ukuguquka kwesiko lokwakha ngamatshe.",
            ],

            "significance":
                """
IKhami itshengisa ukuthi isiko lokwakha ngamatshe eZimbabwe
aliqedanga ngesikhathi iGreat Zimbabwe isehla.

Laqhubeka futhi laguquka.

Amathala, ubuciko bemiduli kanye lobufakazi bokuhweba kutshengisa
ukusungula, ubukhokheli kanye lamakhono amakhulu okwakha.
""",
        },


        "Shona": {

            "name":
                "Khami Ruins",

            "subtitle":
                "Guta rematombo rine terraces renguva yeTorwa, richiratidza decorative masonry nenhoroondo yekutengeserana.",

            "location":
                "Pedyo neBulawayo, kumadokero kweZimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(iii), (iv)",

            "history":
                """
Khami yakasimukira mushure mekuderera kweGreat Zimbabwe.

Yakava capital yeTorwa state, kunyanya kubva muzana remakore
rechi15 kusvika muzana remakore rechi17.

Vatongi vayo vaive nesimba mune zvematongerwo enyika nehupfumi
kumaodzanyemba-kumadokero kweZimbabwe.

Archaeological evidence inoratidza kuti Khami yaive mu regional
uye long-distance trade.

Imported ceramics nezvimwe prestige goods zvakawanikwa pamwe
nezvinhu zvakagadzirwa munharaunda.

Khami saka inoratidza kuenderera uye kushanduka kweZimbabwe
stone-building tradition.
""",

            "culture":
                """
Khami inoratidza political authority, household organization,
craftsmanship uye trading connections.

Architecture yayo ine hukama ne broader Zimbabwe cultural tradition
asi vakavaka Khami vakashandisa terraces neretaining walls
zvakanyanya.

Izvi zvinoratidza kuti tsika inogona kuenderera mberi asi nzira
dzekuvaka dzichishanduka.
""",

            "features": [

                "Stone-faced terraces dzakakura.",

                "Raised platforms dzakavakwa dzichitevera terrain.",

                "Decorative dry-stone wall patterns.",

                "Retaining walls dzakavakwa nehunyanzvi.",

                "Hill Complex nemamwe mapuratifomu makuru.",

                "Evidence ye regional ne long-distance trade.",

                "Imported ceramics nezvimwe prestige goods.",

                "Architecture ine hukama neGreat Zimbabwe asi ine extensive terracing.",
            ],

            "unesco":
                """
Khami Ruins National Monument yakanyoreswa paUNESCO World Heritage
List muna 1986 pasi pecriteria (iii) ne(iv).

UNESCO inoiona sehumbowo hwakasarudzika hwecultural tradition
uye architectural ensemble yakakosha munhoroondo yeSouthern Africa.
""",

            "protection": [

                "Usakwira kana kufamba pamusoro pemadziro e terraces.",

                "Shandisa designated visitor paths.",

                "Usabvisa pottery, beads, stones kana archaeological objects.",

                "Usarongazve loose stones.",

                "Dzivisa zvinhu zvinoita kuti erosion iwedzere.",

                "Usakwenya kana kunyora pamadziro.",

                "Tevera site protection instructions.",
            ],

            "facts": [

                "Khami yakasimukira mushure mekuderera kweGreat Zimbabwe.",

                "Yakabatana zvikuru neTorwa state.",

                "Terraces dzayo dzinoipa appearance yakasiyana neGreat Zimbabwe.",

                "Decorative wall patterns chinhu chakakosha paKhami.",

                "Imported goods dzinoratidza wider trading connections.",

                "Khami inoratidza innovation muZimbabwe stone-building tradition.",
            ],

            "significance":
                """
Khami inoratidza kuti stone-building tradition yeZimbabwe yakaramba
ichienderera kunyange Great Zimbabwe yaderera.

Terraces, decorative masonry uye archaeological evidence zvinoratidza
innovation, political organization uye trade connections.
""",
        },
    },
}


# ------------------------------------------------------------
# QUIZ
# ------------------------------------------------------------

QUIZ = {

    "English": [

        {
            "q":
                "Which ROBO GUIDE heritage site is especially famous for a very high concentration of rock art?",

            "options":
                [
                    "Khami Ruins",
                    "Matobo Hills",
                    "Great Zimbabwe",
                    "Victoria Falls",
                ],

            "answer":
                1,

            "why":
                "Matobo Hills has an exceptional concentration of prehistoric rock paintings preserved in caves and rock shelters.",
        },

        {
            "q":
                "In which year was Matobo Hills inscribed on the UNESCO World Heritage List?",

            "options":
                [
                    "1980",
                    "1986",
                    "2003",
                    "2015",
                ],

            "answer":
                2,

            "why":
                "Matobo Hills was inscribed in 2003 under UNESCO cultural criteria (iii), (v) and (vi).",
        },

        {
            "q":
                "Who built Great Zimbabwe?",

            "options":
                [
                    "Roman soldiers",
                    "Ancestors of Shona-speaking African communities",
                    "Portuguese explorers",
                    "European colonists",
                ],

            "answer":
                1,

            "why":
                "Modern archaeology demonstrates that Great Zimbabwe was built by African communities, particularly ancestors of Shona-speaking peoples.",
        },

        {
            "q":
                "Which famous feature stands within the Great Enclosure?",

            "options":
                [
                    "Conical Tower",
                    "Khami Terrace",
                    "Matobo Cave",
                    "Victoria Falls Tower",
                ],

            "answer":
                0,

            "why":
                "The Conical Tower is one of the best-known architectural features inside the Great Enclosure.",
        },

        {
            "q":
                "How were Great Zimbabwe's monumental stone walls constructed?",

            "options":
                [
                    "With steel reinforcement",
                    "With fired brick and cement",
                    "Using dry-stone masonry without mortar",
                    "Using concrete blocks",
                ],

            "answer":
                2,

            "why":
                "The builders carefully selected and stacked stone without mortar, demonstrating exceptional construction skill.",
        },

        {
            "q":
                "The famous Zimbabwe Birds are associated with which heritage site?",

            "options":
                [
                    "Khami Ruins",
                    "Matobo Hills",
                    "Great Zimbabwe",
                    "Mana Pools",
                ],

            "answer":
                2,

            "why":
                "Carved soapstone Zimbabwe Birds were found at Great Zimbabwe and later became important national symbols.",
        },

        {
            "q":
                "Khami is especially associated with which historic state?",

            "options":
                [
                    "Torwa State",
                    "Roman Empire",
                    "Mali Empire",
                    "Aztec Empire",
                ],

            "answer":
                0,

            "why":
                "Khami became the capital and an important political centre of the Torwa state after Great Zimbabwe declined.",
        },

        {
            "q":
                "Which architectural feature is especially characteristic of Khami?",

            "options":
                [
                    "Extensive stone-faced terraces",
                    "Glass towers",
                    "Pyramids",
                    "Steel bridges",
                ],

            "answer":
                0,

            "why":
                "Khami is especially famous for stone-faced terraces, retaining walls and decorative dry-stone patterns.",
        },

        {
            "q":
                "What is the safest behaviour near prehistoric rock paintings?",

            "options":
                [
                    "Wet them so the colours become brighter",
                    "Trace them using chalk",
                    "Do not touch them",
                    "Rub dust from the surface",
                ],

            "answer":
                2,

            "why":
                "Touching, wetting or tracing rock art can damage fragile surfaces and pigments. Visitors should observe without contact.",
        },

        {
            "q":
                "Why is evidence of long-distance trade important at Great Zimbabwe and Khami?",

            "options":
                [
                    "It shows that the sites were built recently",
                    "It shows links with wider African and Indian Ocean exchange networks",
                    "It proves nobody lived at the sites",
                    "It explains Matobo rock paintings",
                ],

            "answer":
                1,

            "why":
                "Imported objects and other archaeological evidence demonstrate that these centres participated in wide commercial networks.",
        },

        {
            "q":
                "Which site became a major centre after Great Zimbabwe declined?",

            "options":
                [
                    "Khami",
                    "Matobo Cave",
                    "Mana Pools",
                    "Victoria Falls",
                ],

            "answer":
                0,

            "why":
                "Khami rose to political importance after Great Zimbabwe declined and became closely associated with the Torwa state.",
        },

        {
            "q":
                "What should a visitor do when the ROBO GUIDE IR boundary warning activates?",

            "options":
                [
                    "Step back behind the protected boundary",
                    "Ignore the buzzer",
                    "Touch the exhibit quickly",
                    "Disconnect the sensor",
                ],

            "answer":
                0,

            "why":
                "The IR and buzzer system is designed to encourage visitors to step back before approaching protected heritage too closely.",
        },
    ],


    "isiNdebele": [

        {
            "q":
                "Yiphi indawo yeROBO GUIDE edume kakhulu ngobunengi bemidwebo emadwaleni?",

            "options":
                [
                    "IKhami Ruins",
                    "IMatobo Hills",
                    "IGreat Zimbabwe",
                    "IVictoria Falls",
                ],

            "answer":
                1,

            "why":
                "IMatobo Hills ilobunengi obumangalisayo bemidwebo yakudala emigedeni lezindawo zokukhosela.",
        },

        {
            "q":
                "IMatobo Hills yabhaliswa nini kuUNESCO World Heritage List?",

            "options":
                [
                    "1980",
                    "1986",
                    "2003",
                    "2015",
                ],

            "answer":
                2,

            "why":
                "IMatobo Hills yabhaliswa ngo-2003 ngaphansi kwemigomo (iii), (v) kanye (vi).",
        },

        {
            "q":
                "Ngubani owakha iGreat Zimbabwe?",

            "options":
                [
                    "AmaRoma",
                    "Okhokho bemiphakathi yaseAfrica ekhuluma isiShona",
                    "AmaPutukezi",
                    "Abakoloni baseEurope",
                ],

            "answer":
                1,

            "why":
                "Ubufakazi bezinto zakudala butshengisa ukuthi iGreat Zimbabwe yakhiwa yimiphakathi yaseAfrica, ikakhulu okhokho babantu abakhuluma isiShona.",
        },

        {
            "q":
                "Yisiphi isakhiwo esidumileyo esingaphakathi kweGreat Enclosure?",

            "options":
                [
                    "IConical Tower",
                    "IKhami Terrace",
                    "Umgeda weMatobo",
                    "IVictoria Falls Tower",
                ],

            "answer":
                0,

            "why":
                "IConical Tower ingenye yezinto ezaziwa kakhulu ngaphakathi kweGreat Enclosure.",
        },

        {
            "q":
                "Imiduli emikhulu yeGreat Zimbabwe yakhiwa njani?",

            "options":
                [
                    "Ngensimbi",
                    "Ngezitina lesamende",
                    "Ngamatshe ngaphandle kwe-mortar",
                    "Ngeconcrete",
                ],

            "answer":
                2,

            "why":
                "Abakhi babeka amatshe ngobuciko ngaphandle kwe-mortar.",
        },

        {
            "q":
                "IZimbabwe Birds zihlotshaniswa kakhulu layiphi indawo?",

            "options":
                [
                    "IKhami",
                    "IMatobo",
                    "IGreat Zimbabwe",
                    "IMana Pools",
                ],

            "answer":
                2,

            "why":
                "IZimbabwe Birds ezibazwe ngesoapstone zatholakala eGreat Zimbabwe futhi zaba luphawu lwesizwe.",
        },

        {
            "q":
                "IKhami ihlotshaniswa kakhulu lawuphi umbuso?",

            "options":
                [
                    "ITorwa",
                    "IRoma",
                    "IMali",
                    "IAztec",
                ],

            "answer":
                0,

            "why":
                "IKhami yaba yinhloko kanye lendawo enkulu yombuso weTorwa ngemva kokwehla kweGreat Zimbabwe.",
        },

        {
            "q":
                "Yisiphi isici esidume kakhulu ezakhiweni zeKhami?",

            "options":
                [
                    "Amathala amanengi alemiduli yamatshe",
                    "Amaphiramidi",
                    "Izakhiwo zengilazi",
                    "Amabholoho ensimbi",
                ],

            "answer":
                0,

            "why":
                "IKhami idume ngamathala, retaining walls kanye lamaphetheni amahle akhiwe ngamatshe.",
        },

        {
            "q":
                "Kumele wenzeni eduze komdwebo wakudala edwaleni?",

            "options":
                [
                    "Uwumanzise",
                    "Uwucupe ngechalk",
                    "Ungawuthinti",
                    "Uwuhlikihle",
                ],

            "answer":
                2,

            "why":
                "Ukuthinta, ukumanzisa loba ukucupha imidwebo kungayonakalisa. Bukela ngaphandle kokuthinta.",
        },

        {
            "q":
                "Kungani ubufakazi bokuhweba okude buqakathekile eGreat Zimbabwe laseKhami?",

            "options":
                [
                    "Butshengisa ukuthi izindawo zintsha",
                    "Butshengisa ukuxhumana lezindlela ezinkulu zokuhweba",
                    "Butshengisa ukuthi abantu babengahlali lapho",
                    "Buchaza imidwebo yeMatobo",
                ],

            "answer":
                1,

            "why":
                "Izinto ezavela kude zitshengisa ukuxhumana lezindlela ezinkulu zokuhweba eAfrica kanye leIndian Ocean.",
        },

        {
            "q":
                "Yiphi indawo eyakhula kakhulu ngemva kokwehla kweGreat Zimbabwe?",

            "options":
                [
                    "IKhami",
                    "IMatobo Cave",
                    "IMana Pools",
                    "IVictoria Falls",
                ],

            "answer":
                0,

            "why":
                "IKhami yakhula yaba yindawo enkulu yezombusazwe ngemva kokwehla kweGreat Zimbabwe.",
        },

        {
            "q":
                "Isivakashi kumele senzeni nxa iIR warning yeROBO GUIDE ikhala?",

            "options":
                [
                    "Sihlehle sibuyele ngemva komngcele",
                    "Singayinaki",
                    "Sithinte umbukiso masinyane",
                    "Sikhiphe isensor",
                ],

            "answer":
                0,

            "why":
                "Isixwayiso senzelwe ukukhuthaza isivakashi ukuthi sihlehle sivikele amagugu.",
        },
    ],


    "Shona": [

        {
            "q":
                "Ndeipi nzvimbo yeROBO GUIDE inonyanya kuzivikanwa nekuwanda kwe rock art?",

            "options":
                [
                    "Khami Ruins",
                    "Matobo Hills",
                    "Great Zimbabwe",
                    "Victoria Falls",
                ],

            "answer":
                1,

            "why":
                "Matobo Hills ine huwandu hukuru hwe prehistoric rock paintings mumapako nemarock shelters.",
        },

        {
            "q":
                "Matobo Hills yakanyoreswa riini paUNESCO World Heritage List?",

            "options":
                [
                    "1980",
                    "1986",
                    "2003",
                    "2015",
                ],

            "answer":
                2,

            "why":
                "Matobo Hills yakanyoreswa muna 2003 pasi pecriteria (iii), (v) ne(vi).",
        },

        {
            "q":
                "Ndiani akavaka Great Zimbabwe?",

            "options":
                [
                    "Roman soldiers",
                    "Madzitateguru eAfrican communities aitaura Shona",
                    "Portuguese explorers",
                    "European colonists",
                ],

            "answer":
                1,

            "why":
                "Archaeology inoratidza kuti Great Zimbabwe yakavakwa neAfrican communities, kunyanya madzitateguru evanhu vanotaura Shona.",
        },

        {
            "q":
                "Ndechipi chinhu chinozivikanwa chiri mukati meGreat Enclosure?",

            "options":
                [
                    "Conical Tower",
                    "Khami Terrace",
                    "Matobo Cave",
                    "Victoria Falls Tower",
                ],

            "answer":
                0,

            "why":
                "Conical Tower ndeimwe yezviratidzo zvinozivikanwa zvikuru mukati meGreat Enclosure.",
        },

        {
            "q":
                "Madziro makuru eGreat Zimbabwe akavakwa nenzira ipi?",

            "options":
                [
                    "Steel reinforcement",
                    "Brick necement",
                    "Dry-stone masonry pasina mortar",
                    "Concrete blocks",
                ],

            "answer":
                2,

            "why":
                "Matombo akaiswa nehunyanzvi pasina mortar.",
        },

        {
            "q":
                "Zimbabwe Birds dzinonyanya kubatanidzwa nenzvimbo ipi?",

            "options":
                [
                    "Khami",
                    "Matobo",
                    "Great Zimbabwe",
                    "Mana Pools",
                ],

            "answer":
                2,

            "why":
                "Zimbabwe Birds dzakavezwa musoapstone dzakawanikwa kuGreat Zimbabwe uye dzakazova national symbols.",
        },

        {
            "q":
                "Khami inonyanya kubatanidzwa neipi historical state?",

            "options":
                [
                    "Torwa",
                    "Roman",
                    "Mali",
                    "Aztec",
                ],

            "answer":
                0,

            "why":
                "Khami yakava capital uye political centre yakakosha yeTorwa state.",
        },

        {
            "q":
                "Ndechipi architectural feature chinonyanya kusiyanisa Khami?",

            "options":
                [
                    "Stone-faced terraces dzakawanda",
                    "Pyramids",
                    "Glass towers",
                    "Steel bridges",
                ],

            "answer":
                0,

            "why":
                "Khami inozivikanwa nema terraces, retaining walls uye decorative stone patterns.",
        },

        {
            "q":
                "Mushanyi anofanira kuita sei pedyo ne ancient rock art?",

            "options":
                [
                    "Kuinyorovesa",
                    "Ku trace nechalk",
                    "Kusai bata",
                    "Kuikwesha",
                ],

            "answer":
                2,

            "why":
                "Kubata, kunyorovesa kana tracing kunogona kukuvadza pigments nesurface.",
        },

        {
            "q":
                "Sei long-distance trade evidence yakakosha paGreat Zimbabwe neKhami?",

            "options":
                [
                    "Inoratidza kuti nzvimbo itsva",
                    "Inoratidza wider African neIndian Ocean trade networks",
                    "Inoratidza kuti hapana aigara ipapo",
                    "Inotsanangura Matobo paintings",
                ],

            "answer":
                1,

            "why":
                "Imported goods nedzimwe archaeological finds zvinoratidza kubatana kwecentres idzi ne wider exchange networks.",
        },

        {
            "q":
                "Ndeipi nzvimbo yakasimukira mushure mekuderera kweGreat Zimbabwe?",

            "options":
                [
                    "Khami",
                    "Matobo Cave",
                    "Mana Pools",
                    "Victoria Falls",
                ],

            "answer":
                0,

            "why":
                "Khami yakasimukira kuva political centre yakakosha mushure mekuderera kweGreat Zimbabwe.",
        },

        {
            "q":
                "Mushanyi anofanira kuita sei kana IR warning yeROBO GUIDE yarira?",

            "options":
                [
                    "Kudzokera kuseri kwemuganhu wakachengetedzwa",
                    "Kuregeredza buzzer",
                    "Kubata exhibit nekukurumidza",
                    "Kubvisa sensor",
                ],

            "answer":
                0,

            "why":
                "IR nebuzzer zvinokurudzira mushanyi kudzokera shure kuitira kudzivirira sensitive heritage.",
        },
    ],
}


# ------------------------------------------------------------
# HERITAGE ASSISTANT KNOWLEDGE BASE
# ------------------------------------------------------------

KB = {

    "English": {

        "matobo_history":
            """
Matobo Hills is an ancient cultural landscape containing evidence of
human occupation stretching far back into the Stone Age.

Hunter-gatherer communities left an extraordinary record through rock
paintings. Later agricultural communities also occupied the area.

Matobo additionally carries strong Ndebele historical associations and
continues to have spiritual importance today.
""",

        "matobo_rock":
            """
Matobo Hills has one of the highest concentrations of rock art in
southern Africa.

Paintings occur in caves and rock shelters and commonly portray people,
wildlife, hunting, movement and other aspects of life.

The paintings are valuable both as art and as archaeological evidence
that helps researchers interpret earlier communities.
""",

        "matobo_caves":
            """
Matobo's granite landscape created many natural caves and rock shelters.

These shelters provided protection for people and also helped preserve
rock paintings and archaeological deposits from direct weathering.

This natural protection is one reason Matobo contains such a rich
archaeological record.
""",

        "matobo_spiritual":
            """
Matobo is a living sacred landscape.

Shrines, sacred hills, oral traditions, ancestral associations,
rain-making practices and the Mwari religious tradition remain important.

This means conservation should respect both physical archaeological
heritage and living community beliefs.
""",

        "matobo_unesco":
            """
Matobo Hills was inscribed on the UNESCO World Heritage List in 2003
under cultural criteria (iii), (v) and (vi).

UNESCO recognizes its outstanding rock art, the long interaction between
people and landscape and its continuing religious significance.
""",

        "great_history":
            """
Great Zimbabwe flourished mainly between roughly the eleventh and
fifteenth centuries.

It became a major political, economic and cultural centre.

Its scale, stone architecture, craft production, cattle wealth and trade
connections demonstrate the sophistication of the society that lived there.
""",

        "great_builders":
            """
Great Zimbabwe was built by African communities, particularly ancestors
of Shona-speaking peoples.

Modern archaeology has firmly rejected older colonial-era theories that
attempted to attribute Great Zimbabwe to outsiders.
""",

        "great_architecture":
            """
Great Zimbabwe is famous for sophisticated dry-stone masonry built
without mortar.

Its major architectural areas include the Hill Complex, Great Enclosure
and Valley Ruins.

The Great Enclosure contains enormous curved stone walls, internal
passages and the famous Conical Tower.
""",

        "great_birds":
            """
The Zimbabwe Birds are carved soapstone bird sculptures associated with
Great Zimbabwe.

They probably had important elite or spiritual significance.

The bird image later became one of Zimbabwe's strongest national symbols
and appears on the country's flag and national emblem.
""",

        "great_trade":
            """
Great Zimbabwe participated in important long-distance trade networks.

Archaeological finds demonstrate connections with wider African and
Indian Ocean exchange systems.

Regional products such as gold moved through commercial networks while
imported goods reached communities on the Zimbabwe Plateau.
""",

        "great_unesco":
            """
Great Zimbabwe National Monument was inscribed on the UNESCO World
Heritage List in 1986 under criteria (i), (iii) and (vi).

UNESCO recognizes its outstanding architecture, testimony to a major
African civilization and exceptional historic and symbolic significance.
""",

        "khami_history":
            """
Khami rose to prominence after the decline of Great Zimbabwe.

It became the capital of the Torwa state and was especially important
from the fifteenth into the seventeenth century.

Khami demonstrates a later phase of the Zimbabwe stone-building
and political tradition.
""",

        "khami_torwa":
            """
Khami is strongly associated with the Torwa state.

Torwa rulers controlled an important political and economic centre in
south-western Zimbabwe after the decline of Great Zimbabwe.

Khami therefore helps explain how political power shifted and developed
in the region.
""",

        "khami_architecture":
            """
Khami is especially known for stone-faced terraces, retaining walls
and decorative dry-stone patterns.

Its builders adapted architecture to the natural terrain by constructing
raised platforms.

The style is related to Great Zimbabwe but Khami places much stronger
emphasis on extensive terracing.
""",

        "khami_trade":
            """
Khami participated in regional and long-distance trade.

Imported ceramics and other prestige objects discovered by archaeologists
show that Khami's elite had access to wider exchange networks.

Local cultural traditions continued while external trade connections
remained important.
""",

        "khami_unesco":
            """
Khami Ruins National Monument was inscribed on the UNESCO World Heritage
List in 1986 under criteria (iii) and (iv).

UNESCO recognizes its cultural testimony and outstanding architectural
ensemble.
""",

        "conservation":
            """
ROBO GUIDE promotes preventive heritage conservation.

Visitors should not touch rock art, climb ancient walls, remove artifacts,
scratch stone, create graffiti or enter protected areas.

Visitors should remain on designated paths, respect sacred places and
follow heritage guides.

The physical ROBO GUIDE prototype demonstrates preventive conservation
using an IR protected-boundary sensor and buzzer warning.
""",

        "comparison":
            """
Great Zimbabwe and Khami belong to related Zimbabwe stone-building
traditions, but they are not identical.

Great Zimbabwe is earlier and is especially famous for monumental
freestanding dry-stone architecture such as the Great Enclosure.

Khami became important later and is particularly recognizable for
extensive terraces, retaining walls and decorative masonry.

Both demonstrate skilled construction, organized political societies
and participation in long-distance trade.
""",

        "all_sites":
            """
The three ROBO GUIDE heritage sites tell complementary stories.

Matobo Hills is a living granite cultural landscape famous for rock art,
archaeology, caves and sacred traditions.

Great Zimbabwe is a monumental medieval stone centre associated with
Shona history, political organization and long-distance trade.

Khami is a later Torwa-era stone city distinguished by terraces,
decorative masonry and trading connections.

Together they demonstrate the extraordinary diversity and depth of
Zimbabwe's cultural heritage.
""",
    },


    "isiNdebele": {

        "matobo_history":
            """
IMatobo Hills yindawo yamasiko yakudala elobufakazi bempilo yabantu
obubuyela eStone Age.

Abazingeli labaqoqi batshiya imidwebo emangalisayo emadwaleni.
Abalimi abalandelayo labo basebenzisa indawo.

IMatobo iphinde ixhumane lomlando wamaNdebele futhi isaqakathekile
ngokomoya lamuhla.
""",

        "matobo_rock":
            """
IMatobo ilobunengi obukhulu bemidwebo emadwaleni eSouthern Africa.

Imidwebo itholakala emigedeni lezindawo zokukhosela futhi itshengisa
abantu, izinyamazana, ukuzingela kanye lezinye izenzo zempilo yakudala.

Imidwebo iqakathekile njengobuciko futhi njengobufakazi bezinto zakudala.
""",

        "matobo_caves":
            """
Amadwala egranite eMatobo adala imigede lezindawo zokukhosela eziningi.

Lezindawo zavikela abantu futhi zanceda ukugcina imidwebo kanye
lezinto zakudala esimeni sezulu.

Yikho iMatobo igcina ubufakazi obunengi kangaka.
""",

        "matobo_spiritual":
            """
IMatobo yindawo engcwele ephilayo.

Izindawo zokukhulekela, amagquma angcwele, izindaba zomlomo,
ubudlelwano labokhokho, ukucela izulu kanye lenkolelo kaMwari
kusaqakathekile.

Ukuvikelwa kumele kuhloniphe izinto zakudala kanye lamasiko aphilayo.
""",

        "matobo_unesco":
            """
IMatobo Hills yabhaliswa kuUNESCO World Heritage List ngo-2003
ngaphansi kwemigomo (iii), (v) kanye (vi).

I-UNESCO iqaphela imidwebo emadwaleni, ubudlelwano phakathi kwabantu
lendawo kanye lokubaluleka kwayo ngokomoya.
""",

        "great_history":
            """
IGreat Zimbabwe yachuma phakathi kwekhulu le-11 lele-15.

Yaba yindawo enkulu yezombusazwe, ezomnotho lamasiko.

Izakhiwo zamatshe, ubuciko, inkomo kanye lokuhweba kutshengisa
umphakathi waseAfrica owawuphucukile.
""",

        "great_builders":
            """
IGreat Zimbabwe yakhiwa yimiphakathi yaseAfrica, ikakhulu okhokho
babantu abakhuluma isiShona.

Ubufakazi bezinto zakudala buyayiphika imibono yakudala eyayithi
indawo yakhiwa ngabantu bangaphandle.
""",

        "great_architecture":
            """
IGreat Zimbabwe idume ngemiduli eyakhiwe ngamatshe ngaphandle kwe-mortar.

Izingxenye ezinkulu yiHill Complex, Great Enclosure kanye leValley Ruins.

IGreat Enclosure ilodonga olukhulu, imizila kanye leConical Tower.
""",

        "great_birds":
            """
IZimbabwe Birds yizinyoni ezibazwe ngesoapstone ezatholakala
eGreat Zimbabwe.

Kungenzeka ukuthi zazilokubaluleka kwezokhokheli kumbe ngokomoya.

Inyoni yeZimbabwe yacina isiba luphawu olukhulu lwesizwe.
""",

        "great_trade":
            """
IGreat Zimbabwe yayixhumene lokuhweba okude.

Izinto ezatholakala khona zitshengisa ukuxhumana lezindlela zokuhweba
zaseAfrica kanye leIndian Ocean.

Lokhu kutshengisa ukuthi iGreat Zimbabwe yayingeyona indawo evalekileyo.
""",

        "great_unesco":
            """
IGreat Zimbabwe National Monument yabhaliswa kuUNESCO World Heritage
List ngo-1986 ngaphansi kwemigomo (i), (iii) kanye (vi).
""",

        "khami_history":
            """
IKhami yakhula ngemva kokwehla kweGreat Zimbabwe.

Yaba yinhloko yombuso weTorwa futhi yaqakatheka kakhulu kusukela
ngekhulu le-15 kusiya kwele-17.

Imele isigaba esalandela ekwakhiweni kwamatshe eZimbabwe.
""",

        "khami_torwa":
            """
IKhami ixhumene kakhulu lombuso weTorwa.

Ababusi beTorwa babelawula indawo enkulu yezombusazwe lezomnotho
eNingizimu-Ntshonalanga yeZimbabwe.

IKhami isinceda ukuqonda ukuguquka kwamandla kwezombusazwe.
""",

        "khami_architecture":
            """
IKhami idume ngamathala alemiduli yamatshe, retaining walls kanye
lamaphetheni amahle e-dry-stone.

Abakhi bayo bakha amapulatifomu ahambisana lendawo yemvelo.

Isiko lixhumene leGreat Zimbabwe kodwa iKhami isebenzisa amathala kakhulu.
""",

        "khami_trade":
            """
IKhami yayixhumene lokuhweba okuseduze kanye lokukude.

Ceramics kanye lezinto ezivela kwamanye amazwe zatholakala ngabavubukuli.

Lokhu kutshengisa ukuxhumana kweKhami lezindlela ezinkulu zokuhweba.
""",

        "khami_unesco":
            """
IKhami Ruins National Monument yabhaliswa kuUNESCO World Heritage
List ngo-1986 ngaphansi kwemigomo (iii) kanye (iv).
""",

        "conservation":
            """
I-ROBO GUIDE ikhuthaza ukuvikelwa kwamagugu kusenesikhathi.

Ungathinti imidwebo emadwaleni, ungagibeli imiduli yakudala,
ungasusi izinto zakudala futhi ungabhali ematsheni.

Hamba ngemizila evunyelweyo futhi uhloniphe izindawo ezingcwele.

Iprototype yeROBO GUIDE isebenzisa iIR sensor le-buzzer ukukhuthaza
izivakashi ukuthi zingaweli umngcele ovikelweyo.
""",

        "comparison":
            """
IGreat Zimbabwe leKhami zixhumene lesiko lokwakha ngamatshe
eZimbabwe kodwa azifanani.

IGreat Zimbabwe indala futhi idume ngemiduli emikhulu efana leGreat Enclosure.

IKhami yalandela futhi idume ngamathala, retaining walls kanye
ledecorative stonework.

Zombili zitshengisa amakhono okuwakha, ubukhokheli kanye lokuhweba.
""",

        "all_sites":
            """
Izindawo ezintathu zeROBO GUIDE zilandisa izindaba ezitshiyeneyo.

IMatobo yindawo yegranite edume ngemidwebo, imigede kanye lamasiko angcwele.

IGreat Zimbabwe yindawo enkulu yamatshe ehlotshaniswa lomlando wabantu
abakhuluma isiShona, ubukhokheli kanye lokuhweba.

IKhami yidolobho leTorwa elidume ngamathala lemiduli ehlotshisiwe.

Zonke ndawonye zitshengisa ubukhulu bamagugu amasiko eZimbabwe.
""",
    },


    "Shona": {

        "matobo_history":
            """
Matobo Hills inzvimbo yekare yetsika ine archaeological evidence
inodzokera kuStone Age.

Hunter-gatherer communities vakasiya rock paintings dzakawanda.
Mapoka evarimi akazotevera akashandisawo nzvimbo.

Matobo yakazobatanawo zvakanyanya nenhoroondo yeNdebele
uye ichiri spiritual landscape inokosha.
""",

        "matobo_rock":
            """
Matobo ine imwe yehuwandu hukuru hwe rock art muSouthern Africa.

Paintings dziri mumapako nemarock shelters uye dzinoratidza vanhu,
mhuka, kuvhima uye mamwe maitiro ehupenyu.

Dzine kukosha seart uye se archaeological evidence.
""",

        "matobo_caves":
            """
Granite landscape yeMatobo yakagadzira mapako nemarock shelters akawanda.

Aya akapa vanhu shelter uye akabatsira kuchengetedza paintings
nearchaeological deposits kubva kumamiriro ekunze.

Izvi ndizvo zvimwe zvinoita kuti Matobo ive neheritage yakawanda.
""",

        "matobo_spiritual":
            """
Matobo inzvimbo inoyera ichiri kurarama.

Shrines, sacred hills, oral traditions, madzitateguru,
rain-making practices uye Mwari religious tradition zvichiri kukosha.

Conservation inofanira kuremekedza physical heritage pamwe netsika
dzinorarama.
""",

        "matobo_unesco":
            """
Matobo Hills yakanyoreswa paUNESCO World Heritage List muna 2003
pasi pecriteria (iii), (v) ne(vi).

UNESCO inocherechedza rock art yayo, hukama hurefu pakati pevanhu
nenzvimbo uye continuing spiritual significance.
""",

        "great_history":
            """
Great Zimbabwe yakabudirira zvikuru pakati pezvinenge zana remakore
rechi11 nerechi15.

Yakava political, economic uye cultural centre huru.

Architecture, crafts, cattle wealth uye trade zvinoratidza
sophisticated African society.
""",

        "great_builders":
            """
Great Zimbabwe yakavakwa neAfrican communities, kunyanya
madzitateguru evanhu vanotaura Shona.

Archaeological evidence yemazuva ano inoramba pfungwa dzekare
dzaiti monument yakavakwa nevatorwa.
""",

        "great_architecture":
            """
Great Zimbabwe inozivikanwa nedry-stone masonry yakavakwa pasina mortar.

Nzvimbo huru dzinosanganisira Hill Complex, Great Enclosure
uye Valley Ruins.

Great Enclosure ine madziro makuru, passages uye Conical Tower.
""",

        "great_birds":
            """
Zimbabwe Birds ishiri dzakavezwa musoapstone dzakawanikwa
kuGreat Zimbabwe.

Dzaigona kunge dzine elite kana spiritual meaning.

Zimbabwe Bird yakazova chimwe chezviratidzo zvikuru zvenyika.
""",

        "great_trade":
            """
Great Zimbabwe yaive mu long-distance trade.

Archaeological finds dzinoratidza kubatana neAfrican uye Indian Ocean
exchange networks.

Izvi zvinoratidza kuti Great Zimbabwe yaive chikamu che wider economy.
""",

        "great_unesco":
            """
Great Zimbabwe National Monument yakanyoreswa paUNESCO World Heritage
List muna 1986 pasi pecriteria (i), (iii) ne(vi).
""",

        "khami_history":
            """
Khami yakasimukira mushure mekuderera kweGreat Zimbabwe.

Yakava capital yeTorwa state uye yaive yakakosha zvikuru kubva
muzana remakore rechi15 kusvika rechi17.

Inomiririra later stage yeZimbabwe stone-building tradition.
""",

        "khami_torwa":
            """
Khami yakabatana zvakanyanya neTorwa state.

Vatongi veTorwa vaive nepolitical neeconomic centre yakakosha
kumaodzanyemba-kumadokero kweZimbabwe.

Khami inobatsira kutsanangura kushanduka kwepolitical power.
""",

        "khami_architecture":
            """
Khami inozivikanwa nema stone-faced terraces, retaining walls
uye decorative dry-stone patterns.

Architecture yayo yakagadziridzwa kuti ienderane neterrain.

Ine hukama neGreat Zimbabwe asi terracing yakanyanya kuoneka paKhami.
""",

        "khami_trade":
            """
Khami yaive mu regional ne long-distance trade.

Imported ceramics nezvimwe prestige goods zvakawanikwa nearchaeologists.

Izvi zvinoratidza wider commercial connections.
""",

        "khami_unesco":
            """
Khami Ruins National Monument yakanyoreswa paUNESCO World Heritage
List muna 1986 pasi pecriteria (iii) ne(iv).
""",

        "conservation":
            """
ROBO GUIDE inokurudzira preventive heritage conservation.

Usabata rock art, usakwira ancient walls, usabvisa artifacts,
usakwenya matombo uye usapinda munzvimbo dzakarambidzwa.

Shandisa designated paths uye remekedza sacred places.

Physical ROBO GUIDE prototype inoshandisa IR sensor nebuzzer
kuyambira mushanyi kana ayambuka protected boundary.
""",

        "comparison":
            """
Great Zimbabwe neKhami zviri muZimbabwe stone-building tradition
asi hazvina kufanana.

Great Zimbabwe yakatanga uye inozivikanwa nemadziro makuru
akaita seGreat Enclosure.

Khami yakazotevera uye inozivikanwa nema terraces,
retaining walls uye decorative stonework.

Dzose dzinoratidza skilled architecture, political organization
uye long-distance trade.
""",

        "all_sites":
            """
Nzvimbo nhatu dzeROBO GUIDE dzinotaura nyaya dzakasiyana
asi dzinobatsirana.

Matobo inzvimbo yegranite ine rock art, archaeology, mapako
uye sacred traditions.

Great Zimbabwe iguta guru rematombo rakabatana neShona history,
statecraft uye trade.

Khami iguta reTorwa rakazotevera rinozivikanwa nema terraces
uye decorative masonry.

Pamwe chete dzinoratidza hupfumi hwenhaka yeZimbabwe.
""",
    },
}


# ------------------------------------------------------------
# HELPER FUNCTIONS
# ------------------------------------------------------------

def tr(key):

    return UI[
        st.session_state.lang
    ][key]


def go(page):

    st.session_state.page = page

    st.rerun()


def reset_quiz():

    st.session_state.quiz_index = 0

    st.session_state.quiz_score = 0

    st.session_state.quiz_points = 0

    st.session_state.quiz_answered = False

    st.session_state.quiz_feedback = None

    st.session_state.quiz_finished = False


def normalize(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    return text.strip()


def contains_any(text, words):

    return any(
        word in text
        for word in words
    )


def assistant_answer(question):

    q = normalize(question)

    lang = st.session_state.lang

    kb = KB[lang]


    # --------------------------------------------------------
    # COMPARISON QUESTIONS
    # --------------------------------------------------------

    comparison_words = [

        "compare",
        "comparison",
        "difference",
        "different",
        "similar",
        "similarity",

        "qhathanisa",
        "umehluko",
        "fanana",

        "enzanisa",
        "musiyano",
        "zvakafanana",
    ]


    if contains_any(
        q,
        comparison_words
    ):

        great = (
            "great zimbabwe" in q
            or
            "great" in q
        )

        khami = (
            "khami" in q
        )

        matobo = (
            "matobo" in q
        )


        if great and khami and not matobo:

            return kb[
                "comparison"
            ]


        if (
            sum(
                [
                    great,
                    khami,
                    matobo
                ]
            )
            >= 2
        ):

            return kb[
                "all_sites"
            ]


    # --------------------------------------------------------
    # CONSERVATION
    # --------------------------------------------------------

    conservation_words = [

        "protect",
        "protection",
        "conservation",
        "conserve",
        "preserve",
        "preservation",
        "damage",
        "touch",
        "visitor",
        "boundary",
        "sensor",
        "buzzer",
        "warning",
        "ir sensor",

        "vikela",
        "ukuvikela",
        "thinta",
        "umngcele",

        "chengetedza",
        "kuchengetedza",
        "bata",
        "muganhu",
        "yambiro",
    ]


    if contains_any(
        q,
        conservation_words
    ):

        return kb[
            "conservation"
        ]


    # --------------------------------------------------------
    # MATOBO
    # --------------------------------------------------------

    matobo_trigger = (

        "matobo" in q

        or

        contains_any(
            q,
            [
                "rock art",
                "rock painting",
                "rock paintings",
                "cave painting",
                "cave paintings",
                "imidwebo",
                "mapako",
                "imigede",
            ]
        )
    )


    if matobo_trigger:

        if contains_any(
            q,
            [
                "unesco",
                "world heritage",
                "inscribed",
                "inscription",
                "criteria",
                "bhaliswa",
                "nyoreswa",
            ]
        ):

            return kb[
                "matobo_unesco"
            ]


        if contains_any(
            q,
            [
                "cave",
                "caves",
                "shelter",
                "shelters",
                "umgede",
                "imigede",
                "pako",
                "mapako",
            ]
        ):

            return kb[
                "matobo_caves"
            ]


        if contains_any(
            q,
            [
                "rock art",
                "painting",
                "paintings",
                "imidwebo",
                "umdwebo",
                "mifananidzo",
            ]
        ):

            return kb[
                "matobo_rock"
            ]


        if contains_any(
            q,
            [
                "sacred",
                "spiritual",
                "spirit",
                "religion",
                "mwari",
                "shrine",
                "ancestor",
                "ancestors",

                "okungcwele",
                "amadlozi",

                "mweya",
                "madzitateguru",
                "inoyera",
            ]
        ):

            return kb[
                "matobo_spiritual"
            ]


        return kb[
            "matobo_history"
        ]


    # --------------------------------------------------------
    # GREAT ZIMBABWE
    # --------------------------------------------------------

    great_trigger = contains_any(

        q,

        [
            "great zimbabwe",
            "great enclosure",
            "conical tower",
            "zimbabwe bird",
            "zimbabwe birds",
        ]
    )


    if great_trigger:

        if contains_any(
            q,
            [
                "who built",
                "built by",
                "builder",
                "builders",
                "build",

                "ngubani",
                "owakha",

                "ndiani",
                "akavaka",
                "vakavaka",
            ]
        ):

            return kb[
                "great_builders"
            ]


        if contains_any(
            q,
            [
                "bird",
                "birds",
                "inyoni",
                "izinyoni",
                "shiri",
            ]
        ):

            return kb[
                "great_birds"
            ]


        if contains_any(
            q,
            [
                "trade",
                "trading",
                "gold",
                "import",
                "imports",
                "commerce",

                "ukuhweba",

                "kutengeserana",
            ]
        ):

            return kb[
                "great_trade"
            ]


        if contains_any(
            q,
            [
                "architecture",
                "wall",
                "walls",
                "enclosure",
                "tower",
                "stone",
                "masonry",
                "mortar",

                "udonga",
                "imiduli",
                "izakhiwo",

                "madziro",
                "zvivakwa",
                "matombo",
            ]
        ):

            return kb[
                "great_architecture"
            ]


        if contains_any(
            q,
            [
                "unesco",
                "world heritage",
                "inscribed",
                "criteria",
                "bhaliswa",
                "nyoreswa",
            ]
        ):

            return kb[
                "great_unesco"
            ]


        return kb[
            "great_history"
        ]


    # --------------------------------------------------------
    # KHAMI
    # --------------------------------------------------------

    if (
        "khami" in q
        or
        "torwa" in q
    ):

        if contains_any(
            q,
            [
                "torwa",
                "state",
                "kingdom",
                "ruler",
                "rulers",
                "government",
                "umbuso",
                "hurumende",
            ]
        ):

            return kb[
                "khami_torwa"
            ]


        if contains_any(
            q,
            [
                "trade",
                "trading",
                "ceramic",
                "ceramics",
                "import",
                "imports",

                "ukuhweba",

                "kutengeserana",
            ]
        ):

            return kb[
                "khami_trade"
            ]


        if contains_any(
            q,
            [
                "terrace",
                "terraces",
                "architecture",
                "wall",
                "walls",
                "decorative",
                "stonework",
                "masonry",

                "amathala",
                "imiduli",
                "izakhiwo",

                "madziro",
                "matombo",
            ]
        ):

            return kb[
                "khami_architecture"
            ]


        if contains_any(
            q,
            [
                "unesco",
                "world heritage",
                "inscribed",
                "criteria",
                "bhaliswa",
                "nyoreswa",
            ]
        ):

            return kb[
                "khami_unesco"
            ]


        return kb[
            "khami_history"
        ]


    # --------------------------------------------------------
    # GENERAL TOPIC ROUTING
    # --------------------------------------------------------

    if contains_any(
        q,
        [
            "who built",
            "builder",
            "builders",
            "built by",
            "ngubani owakha",
            "ndiani akavaka",
        ]
    ):

        return kb[
            "great_builders"
        ]


    if contains_any(
        q,
        [
            "zimbabwe bird",
            "birds",
            "bird",
            "izinyoni",
            "inyoni",
            "shiri",
        ]
    ):

        return kb[
            "great_birds"
        ]


    if contains_any(
        q,
        [
            "torwa",
            "terrace",
            "terraces",
            "amathala",
        ]
    ):

        return (
            kb["khami_torwa"]
            +
            "\n\n"
            +
            kb["khami_architecture"]
        )


    if contains_any(
        q,
        [
            "rock art",
            "rock painting",
            "paintings",
            "cave",
            "caves",
            "imidwebo",
            "imigede",
            "mapako",
        ]
    ):

        return kb[
            "matobo_rock"
        ]


    if contains_any(
        q,
        [
            "trade",
            "trading",
            "commerce",
            "kutengeserana",
            "ukuhweba",
        ]
    ):

        return (
            kb["great_trade"]
            +
            "\n\n"
            +
            kb["khami_trade"]
        )


    if contains_any(
        q,
        [
            "unesco",
            "world heritage",
        ]
    ):

        return (
            kb["great_unesco"]
            +
            "\n\n"
            +
            kb["khami_unesco"]
            +
            "\n\n"
            +
            kb["matobo_unesco"]
        )


    if contains_any(
        q,
        [
            "three sites",
            "all sites",
            "heritage sites",
            "zimbabwe heritage",

            "izindawo",
            "amagugu",

            "nzvimbo",
            "nhaka",
        ]
    ):

        return kb[
            "all_sites"
        ]


    return tr(
        "no_answer"
    )


# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

with st.sidebar:

    st.markdown(
        f"""
        <div class="brand">

            <div class="brand-logo">
                🤖🗿
            </div>

            <h2>
                ROBO GUIDE
            </h2>

            <p>
                {tr("tagline")}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    previous_language = (
        st.session_state.lang
    )


    selected_language = st.selectbox(

        tr(
            "language"
        ),

        [
            "English",
            "isiNdebele",
            "Shona"
        ],

        index=
            [
                "English",
                "isiNdebele",
                "Shona"
            ].index(
                previous_language
            )
    )


    if (
        selected_language
        !=
        previous_language
    ):

        st.session_state.lang = (
            selected_language
        )

        reset_quiz()

        st.session_state.chat = []

        st.rerun()


    st.markdown(
        "### "
        +
        tr(
            "navigation"
        )
    )


    NAVIGATION = [

        (
            "Home",
            "🏠",
            tr("home")
        ),

        (
            "Matobo Hills",
            "🪨",
            tr("matobo")
        ),

        (
            "Great Zimbabwe",
            "🏛️",
            tr("great")
        ),

        (
            "Khami Ruins",
            "🧱",
            tr("khami")
        ),

        (
            "Heritage Challenge",
            "🏆",
            tr("quiz")
        ),

        (
            "Heritage Assistant",
            "💬",
            tr("assistant")
        ),

        (
            "Robot + Website",
            "🤖",
            tr("prototype")
        ),
    ]


    for (
        target,
        icon,
        label
    ) in NAVIGATION:

        active = (
            st.session_state.page
            ==
            target
        )


        if st.button(

            f"{icon}  {label}",

            key=
                f"nav_{target}",

            use_container_width=True,

            type=
                "primary"
                if active
                else
                "secondary"
        ):

            go(
                target
            )


    st.markdown(
        "---"
    )


    st.caption(
        "🏆 WRO 2026 Zimbabwe National Finals"
    )

    st.caption(
        "🤖 Theme: Robots Meet Culture"
    )

    st.caption(
        "🇿🇼 Learn • Respect • Protect"
    )


# ------------------------------------------------------------
# HOME PAGE
# ------------------------------------------------------------

def home_page():

    st.markdown(

        f"""
        <div class="hero">

            <div class="kicker">
                {tr("tagline")}
            </div>

            <h1>
                ROBO GUIDE
            </h1>

            <h2>
                {tr("hero")}
            </h2>

            <p>
                {tr("hero_text")}
            </p>

            <div>

                <span class="badge">
                    🌍 English
                </span>

                <span class="badge">
                    🗣️ isiNdebele
                </span>

                <span class="badge">
                    💬 Shona
                </span>

                <span class="badge">
                    📡 IR Protection
                </span>

                <span class="badge">
                    🔔 Smart Warning
                </span>

                <span class="badge">
                    🏆 Gamified Learning
                </span>

            </div>

        </div>
        """,

        unsafe_allow_html=True
    )


    col1, col2, col3 = (
        st.columns(
            3
        )
    )


    with col1:

        st.markdown(

            """
            <div class="stat">

                <div class="stat-number">
                    3
                </div>

                <div class="stat-label">
                    Zimbabwe heritage experiences
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    with col2:

        st.markdown(

            """
            <div class="stat">

                <div class="stat-number">
                    3
                </div>

                <div class="stat-label">
                    Visitor languages
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    with col3:

        st.markdown(

            """
            <div class="stat">

                <div class="stat-number">
                    1
                </div>

                <div class="stat-label">
                    Connected robot + digital journey
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    st.markdown(

        f"""
        <div class="section-title">
            {tr("explore")}
        </div>

        <div class="section-sub">
            {tr("explore_sub")}
        </div>
        """,

        unsafe_allow_html=True
    )


    cards = st.columns(
        3
    )


    summary = {

        "English": {

            "Matobo Hills":
                "Rock art • sacred landscape • caves • granite hills",

            "Great Zimbabwe":
                "Great Enclosure • Zimbabwe Birds • stone architecture • trade",

            "Khami Ruins":
                "Terraces • Torwa history • decorative stonework • trade",
        },

        "isiNdebele": {

            "Matobo Hills":
                "Imidwebo emadwaleni • izindawo ezingcwele • imigede • amagquma",

            "Great Zimbabwe":
                "Great Enclosure • Zimbabwe Birds • izakhiwo zamatshe • ukuhweba",

            "Khami Ruins":
                "Amathala • umlando weTorwa • ubuciko bamatshe • ukuhweba",
        },

        "Shona": {

            "Matobo Hills":
                "Rock art • nzvimbo dzinoyera • mapako • zvikomo zvegranite",

            "Great Zimbabwe":
                "Great Enclosure • Zimbabwe Birds • stone architecture • trade",

            "Khami Ruins":
                "Terraces • Torwa history • decorative stonework • trade",
        },
    }


    for column, site_key in zip(

        cards,

        [
            "Matobo Hills",
            "Great Zimbabwe",
            "Khami Ruins",
        ]
    ):

        site = SITES[
            site_key
        ][
            st.session_state.lang
        ]


        with column:

            st.markdown(

                f"""
                <div class="card">

                    <div class="site-icon">
                        {SITES[site_key]["emoji"]}
                    </div>

                    <h3>
                        {site["name"]}
                    </h3>

                    <p>
                        {
                            summary[
                                st.session_state.lang
                            ][
                                site_key
                            ]
                        }
                    </p>

                    <p>
                        <b>UNESCO:</b>
                        {site["inscribed"]}
                        •
                        {site["criteria"]}
                    </p>

                </div>
                """,

                unsafe_allow_html=True
            )


            if st.button(

                f'{tr("open")} →',

                key=
                    f"open_{site_key}",

                use_container_width=True
            ):

                go(
                    site_key
                )


    st.markdown(

        f"""
        <div class="section-title">
            {tr("why")}
        </div>

        <div class="section-sub">
            {tr("why_text")}
        </div>
        """,

        unsafe_allow_html=True
    )


    c1, c2, c3, c4 = (
        st.columns(
            4
        )
    )


    mini_cards = [

        (
            c1,
            "📚",
            tr("learn"),
            tr("learn_text")
        ),

        (
            c2,
            "🎮",
            tr("play"),
            tr("play_text")
        ),

        (
            c3,
            "🛡️",
            tr("protect"),
            tr("protect_text")
        ),

        (
            c4,
            "🔗",
            tr("connect"),
            tr("connect_text")
        ),
    ]


    for (
        column,
        icon,
        title,
        text
    ) in mini_cards:

        with column:

            st.markdown(

                f"""
                <div class="card">

                    <div class="site-icon">
                        {icon}
                    </div>

                    <h4>
                        {title}
                    </h4>

                    <p>
                        {text}
                    </p>

                </div>
                """,

                unsafe_allow_html=True
            )


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    a, b, c = (
        st.columns(
            3
        )
    )


    with a:

        if st.button(

            "🏆 "
            +
            tr("challenge"),

            type="primary",

            use_container_width=True
        ):

            go(
                "Heritage Challenge"
            )


    with b:

        if st.button(

            "💬 "
            +
            tr("ask"),

            use_container_width=True
        ):

            go(
                "Heritage Assistant"
            )


    with c:

        if st.button(

            "🤖 "
            +
            tr("robot"),

            use_container_width=True
        ):

            go(
                "Robot + Website"
            )


# ------------------------------------------------------------
# HERITAGE SITE PAGE
# ------------------------------------------------------------

def site_page(
    site_key
):

    site = SITES[
        site_key
    ][
        st.session_state.lang
    ]


    st.markdown(

        f"""
        <div class="hero">

            <div class="kicker">
                ROBO GUIDE • Zimbabwe Heritage
            </div>

            <h1 style="font-size:3.4rem">

                {
                    SITES[
                        site_key
                    ]["emoji"]
                }

                {site["name"]}

            </h1>

            <p>
                {site["subtitle"]}
            </p>

        </div>
        """,

        unsafe_allow_html=True
    )


    col1, col2, col3 = (
        st.columns(
            3
        )
    )


    with col1:

        st.markdown(

            f"""
            <div class="stat">

                <div class="stat-number">
                    {site["inscribed"]}
                </div>

                <div class="stat-label">
                    {tr("inscription")}
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    with col2:

        st.markdown(

            f"""
            <div class="stat">

                <div class="stat-number">
                    {site["criteria"]}
                </div>

                <div class="stat-label">
                    {tr("criteria")}
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    with col3:

        st.markdown(

            f"""
            <div class="stat">

                <div
                    class="stat-number"
                    style="font-size:16px"
                >
                    {site["location"]}
                </div>

                <div class="stat-label">
                    {tr("location")}
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    left, right = (
        st.columns(
            [
                1.25,
                1
            ]
        )
    )


    with left:

        st.markdown(
            "### 📜 "
            +
            tr("history")
        )

        st.write(
            site[
                "history"
            ]
        )


        st.markdown(
            "### 👥 "
            +
            tr("culture")
        )

        st.write(
            site[
                "culture"
            ]
        )


    with right:

        st.markdown(
            "### ✨ "
            +
            tr("features")
        )


        for item in site[
            "features"
        ]:

            st.markdown(
                "◆ "
                +
                item
            )


    st.markdown(

        f"""
        <div class="unesco">

            <b>
                🌐 {tr("unesco")}
            </b>

            <br><br>

            {
                site["unesco"]
            }

        </div>
        """,

        unsafe_allow_html=True
    )


    p1, p2 = (
        st.columns(
            2
        )
    )


    with p1:

        st.markdown(
            "### 🛡️ "
            +
            tr("protection")
        )


        for rule in site[
            "protection"
        ]:

            st.markdown(

                f"""
                <div class="greenbox">
                    ✓ {rule}
                </div>
                """,

                unsafe_allow_html=True
            )


    with p2:

        st.markdown(
            "### 💡 "
            +
            tr("facts")
        )


        for fact in site[
            "facts"
        ]:

            st.markdown(

                f"""
                <div class="goldbox">
                    ★ {fact}
                </div>
                """,

                unsafe_allow_html=True
            )


    st.markdown(
        "### 🌟 "
        +
        tr("significance")
    )


    st.info(
        site[
            "significance"
        ],
        icon="🌍"
    )


    c1, c2, c3 = (
        st.columns(
            3
        )
    )


    with c1:

        if st.button(

            tr("back"),

            use_container_width=True
        ):

            go(
                "Home"
            )


    with c2:

        if st.button(

            "🏆 "
            +
            tr("challenge"),

            use_container_width=True
        ):

            go(
                "Heritage Challenge"
            )


    with c3:

        if st.button(

            "💬 "
            +
            tr("ask"),

            use_container_width=True
        ):

            go(
                "Heritage Assistant"
            )


# ------------------------------------------------------------
# HERITAGE QUIZ PAGE
# ------------------------------------------------------------

def quiz_page():

    questions = QUIZ[
        st.session_state.lang
    ]


    total = len(
        questions
    )


    st.markdown(

        f"""
        <div class="hero">

            <div class="kicker">
                ROBO GUIDE • Learn By Playing
            </div>

            <h1 style="font-size:3.3rem">
                🏆 {tr("quiz_title")}
            </h1>

            <p>
                {tr("quiz_intro")}
            </p>

        </div>
        """,

        unsafe_allow_html=True
    )


    if (
        st.session_state.quiz_finished
    ):

        percentage = round(

            (
                st.session_state.quiz_score
                /
                total
            )
            *
            100
        )


        guardian = (
            percentage
            >=
            80
        )


        achievement_title = (

            tr("guardian")

            if guardian

            else

            tr("guide")
        )


        achievement_desc = (

            tr("guardian_desc")

            if guardian

            else

            tr("guide_desc")
        )


        icon = (

            "🛡️🏆"

            if guardian

            else

            "🧭🏅"
        )


        st.markdown(

            f"""
            <div class="achievement">

                <div class="achievement-icon">
                    {icon}
                </div>

                <div
                    style="
                        text-transform:uppercase;
                        font-size:13px;
                        letter-spacing:2px;
                    "
                >
                    {tr("achievement")}
                </div>

                <h2>
                    {achievement_title}
                </h2>

                <p>
                    {achievement_desc}
                </p>

                <h3>

                    {
                        st.session_state.quiz_score
                    }
                    /
                    {total}

                    •

                    {percentage}%

                    •

                    {
                        st.session_state.quiz_points
                    }

                    Heritage Points

                </h3>

            </div>
            """,

            unsafe_allow_html=True
        )


        st.balloons()


        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )


        col1, col2 = (
            st.columns(
                2
            )
        )


        with col1:

            if st.button(

                "🔁 "
                +
                tr("replay"),

                type="primary",

                use_container_width=True
            ):

                reset_quiz()

                st.rerun()


        with col2:

            if st.button(

                "📚 "
                +
                tr("explore"),

                use_container_width=True
            ):

                go(
                    "Home"
                )


        return


    index = (
        st.session_state.quiz_index
    )


    question = questions[
        index
    ]


    st.progress(

        index
        /
        total
    )


    m1, m2, m3 = (
        st.columns(
            3
        )
    )


    m1.metric(

        tr("question"),

        f"{index + 1}/{total}"
    )


    m2.metric(

        tr("score"),

        f'{st.session_state.quiz_score}/{total}'
    )


    m3.metric(

        tr("points"),

        st.session_state.quiz_points
    )


    st.markdown(

        '<div class="quizbox">',

        unsafe_allow_html=True
    )


    st.markdown(

        f"""
        ### {index + 1}. {question["q"]}
        """
    )


    if (
        st.session_state.lang
        ==
        "English"
    ):

        choose_label = (
            "Choose one answer"
        )


    elif (
        st.session_state.lang
        ==
        "isiNdebele"
    ):

        choose_label = (
            "Khetha impendulo eyodwa"
        )


    else:

        choose_label = (
            "Sarudza mhinduro imwe"
        )


    selected = st.radio(

        choose_label,

        options=
            list(
                range(
                    len(
                        question[
                            "options"
                        ]
                    )
                )
            ),

        format_func=
            lambda x:
                question[
                    "options"
                ][x],

        index=None,

        key=
            f'quiz_{
                st.session_state.lang
            }_{index}',

        disabled=
            st.session_state.quiz_answered
    )


    if not (
        st.session_state.quiz_answered
    ):

        if st.button(

            "✅ "
            +
            tr("submit"),

            type="primary",

            use_container_width=True,

            disabled=
                selected
                is
                None
        ):

            st.session_state.quiz_answered = (
                True
            )


            if (
                selected
                ==
                question[
                    "answer"
                ]
            ):

                st.session_state.quiz_score += 1

                st.session_state.quiz_points += 100

                st.session_state.quiz_feedback = (
                    "correct"
                )


            else:

                # Give some participation points
                # to keep the challenge positive and gamified.

                st.session_state.quiz_points += 20

                st.session_state.quiz_feedback = (
                    "incorrect"
                )


            st.rerun()


    else:

        if (
            st.session_state.quiz_feedback
            ==
            "correct"
        ):

            st.success(

                "🎉 "
                +
                tr("correct")
                +
                "  +100 Heritage Points"
                +
                "\n\n"
                +
                question["why"]
            )


        else:

            correct_answer = (

                question[
                    "options"
                ][
                    question[
                        "answer"
                    ]
                ]
            )


            st.error(

                "💡 "
                +
                tr("incorrect")
                +
                "  +20 Participation Points"
                +
                "\n\n"
                +
                "**✓ "
                +
                correct_answer
                +
                "**"
                +
                "\n\n"
                +
                question["why"]
            )


        if (
            index
            ==
            total - 1
        ):

            next_text = (
                tr("finish")
            )


        else:

            next_text = (
                tr("next")
            )


        if st.button(

            next_text,

            type="primary",

            use_container_width=True
        ):

            if (
                index
                ==
                total - 1
            ):

                st.session_state.quiz_finished = (
                    True
                )


            else:

                st.session_state.quiz_index += 1

                st.session_state.quiz_answered = (
                    False
                )

                st.session_state.quiz_feedback = (
                    None
                )


            st.rerun()


    st.markdown(

        "</div>",

        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# HERITAGE ASSISTANT PAGE
# ------------------------------------------------------------

def assistant_page():

    st.markdown(

        f"""
        <div class="hero">

            <div class="kicker">
                ROBO GUIDE • Free Rule-Based Heritage Intelligence
            </div>

            <h1 style="font-size:3.2rem">
                💬 {tr("assistant_title")}
            </h1>

            <p>
                {tr("assistant_intro")}
            </p>

        </div>
        """,

        unsafe_allow_html=True
    )


    SUGGESTIONS = {

        "English": [

            "Who built Great Zimbabwe?",

            "Why are Matobo caves important?",

            "Tell me about rock art at Matobo.",

            "What are the Zimbabwe Birds?",

            "What is the Great Enclosure?",

            "Tell me about the Torwa state at Khami.",

            "Why does Khami have terraces?",

            "How did Great Zimbabwe trade?",

            "Compare Great Zimbabwe and Khami.",

            "How should visitors protect rock art?",

            "When did Khami become important?",

            "What does UNESCO recognize at Matobo?",
        ],


        "isiNdebele": [

            "Ngubani owakha iGreat Zimbabwe?",

            "Kungani imigede yeMatobo iqakathekile?",

            "Ngitshele ngemidwebo yeMatobo.",

            "Yini iZimbabwe Birds?",

            "Yini iGreat Enclosure?",

            "Ngitshele ngombuso weTorwa eKhami.",

            "Kungani iKhami ilamathala?",

            "IGreat Zimbabwe yayihweba njani?",

            "Qhathanisa iGreat Zimbabwe leKhami.",

            "Izivakashi zingayivikela njani imidwebo?",

            "IKhami yaba yiqakathekile nini?",

            "IUNESCO iqaphelani eMatobo?",
        ],


        "Shona": [

            "Ndiani akavaka Great Zimbabwe?",

            "Sei mapako eMatobo akakosha?",

            "Ndiudze nezve rock art yeMatobo.",

            "Zimbabwe Birds chii?",

            "Great Enclosure chii?",

            "Ndiudze nezveTorwa paKhami.",

            "Sei Khami iine terraces?",

            "Great Zimbabwe yaitengesa sei?",

            "Enzanisa Great Zimbabwe neKhami.",

            "Vashanyi vangachengetedza sei rock art?",

            "Khami yakatanga kukosha riini?",

            "UNESCO inocherechedzei paMatobo?",
        ],
    }


    st.markdown(

        "**"
        +
        tr("try_question")
        +
        ":**"
    )


    suggestion_columns = (
        st.columns(
            3
        )
    )


    for i, prompt in enumerate(

        SUGGESTIONS[
            st.session_state.lang
        ]
    ):

        column = (
            suggestion_columns[
                i % 3
            ]
        )


        with column:

            if st.button(

                prompt,

                key=
                    f"suggestion_{i}",

                use_container_width=True
            ):

                reply = (
                    assistant_answer(
                        prompt
                    )
                )


                st.session_state.chat.append(

                    (
                        prompt,
                        reply
                    )
                )


                st.rerun()


    st.markdown(
        "---"
    )


    # Only display latest eight exchanges
    # to keep the page readable.

    for (
        question,
        answer
    ) in st.session_state.chat[-8:]:


        st.markdown(

            f"""
            <div class="chat-user">

                <b>
                    👤 Visitor
                </b>

                <br>

                {escape(question)}

            </div>
            """,

            unsafe_allow_html=True
        )


        st.markdown(

            f"""
            <div class="chat-bot">

                <b>
                    🤖 ROBO GUIDE
                </b>

                <br>

                {
                    escape(
                        answer
                    ).replace(
                        chr(10),
                        "<br>"
                    )
                }

            </div>
            """,

            unsafe_allow_html=True
        )


    with st.form(

        "heritage_assistant_form",

        clear_on_submit=True
    ):

        user_question = (
            st.text_input(

                "Question",

                placeholder=
                    tr(
                        "assistant_placeholder"
                    ),

                label_visibility=
                    "collapsed"
            )
        )


        send = (
            st.form_submit_button(

                "🤖 "
                +
                tr("ask"),

                type="primary",

                use_container_width=True
            )
        )


        if (
            send
            and
            user_question.strip()
        ):

            reply = (
                assistant_answer(
                    user_question
                )
            )


            st.session_state.chat.append(

                (
                    user_question.strip(),
                    reply
                )
            )


            st.rerun()


    if (
        st.session_state.chat
    ):

        if st.button(

            "🧹 "
            +
            tr("clear")
        ):

            st.session_state.chat = []

            st.rerun()


    st.caption(
        "✅ No paid API • ✅ No API key • ✅ Rule-based knowledge engine contained entirely inside app.py"
    )


# ------------------------------------------------------------
# ROBOT + WEBSITE PAGE
# ------------------------------------------------------------

def prototype_page():

    st.markdown(

        f"""
        <div class="hero">

            <div class="kicker">
                ROBO GUIDE • Physical + Digital Heritage System
            </div>

            <h1 style="font-size:3.2rem">
                🤖 {tr("prototype_title")}
            </h1>

            <p>
                {tr("prototype_intro")}
            </p>

        </div>
        """,

        unsafe_allow_html=True
    )


    st.markdown(

        "### 🔄 "
        +
        tr("flow")
    )


    FLOW = {

        "English":
            """
Visitor approaches the ROBO GUIDE exhibit
→ OLED gives multilingual heritage education
→ visitor scans the QR code
→ ROBO GUIDE website opens
→ visitor explores detailed heritage content
→ IR sensor watches the protected boundary
→ buzzer warns if the boundary is crossed
→ laptop records boundary events
→ dashboard identifies patterns and trends
→ heritage managers can improve visitor education and protection.
""",

        "isiNdebele":
            """
Isivakashi siyasondela kuROBO GUIDE
→ OLED inika ulwazi ngezindimi ezintathu
→ isivakashi siskena iQR
→ iwebhusayithi yeROBO GUIDE iyavuleka
→ isivakashi sihlola ulwazi olujulileyo
→ IR sensor iqapha umngcele ovikelweyo
→ buzzer iyaxwayisa nxa umngcele uweqiwa
→ ikhompyutha iyarekhoda izehlakalo
→ ideshibhodi itshengisa imikhuba
→ abaphathi bangathuthukisa imfundo lokuvikela.
""",

        "Shona":
            """
Mushanyi anosvika paROBO GUIDE
→ OLED inopa multilingual heritage education
→ mushanyi anoskena QR
→ ROBO GUIDE webhusaiti inovhurika
→ mushanyi anoongorora detailed heritage content
→ IR sensor inotarisa protected boundary
→ buzzer inoyambira kana muganhu wayambukwa
→ laptop inorekodha boundary events
→ dashboard inoratidza patterns nema trends
→ heritage managers vanogona kuvandudza visitor education nekuchengetedza.
""",
    }


    st.markdown(

        f"""
        <div class="unesco">

            {
                FLOW[
                    st.session_state.lang
                ]
            }

        </div>
        """,

        unsafe_allow_html=True
    )


    FEATURES = [

        (
            "🖥️",
            tr("oled"),
            tr("oled_text")
        ),

        (
            "📱",
            tr("qr"),
            tr("qr_text")
        ),

        (
            "🧭",
            tr("visitor"),
            tr("visitor_text")
        ),

        (
            "📡",
            tr("ir"),
            tr("ir_text")
        ),

        (
            "🔔",
            tr("buzzer"),
            tr("buzzer_text")
        ),

        (
            "📊",
            tr("dashboard"),
            tr("dashboard_text")
        ),
    ]


    for start in range(

        0,
        len(FEATURES),
        2
    ):

        col1, col2 = (
            st.columns(
                2
            )
        )


        pair = FEATURES[
            start:
            start + 2
        ]


        for column, feature in zip(

            [
                col1,
                col2
            ],

            pair
        ):

            icon, title, text = (
                feature
            )


            with column:

                st.markdown(

                    f"""
                    <div class="card">

                        <div class="site-icon">
                            {icon}
                        </div>

                        <h3>
                            {title}
                        </h3>

                        <p>
                            {text}
                        </p>

                    </div>
                    """,

                    unsafe_allow_html=True
                )


        st.markdown(

            "<br>",

            unsafe_allow_html=True
        )


    DASHBOARD_TITLE = {

        "English":
            "What the ROBO GUIDE laptop dashboard can analyse",

        "isiNdebele":
            "Okungahlaziywa yideshibhodi yeROBO GUIDE",

        "Shona":
            "Zvinogona kuongororwa neROBO GUIDE laptop dashboard",
    }


    st.markdown(

        "### 📈 "
        +
        DASHBOARD_TITLE[
            st.session_state.lang
        ]
    )


    LABELS = {

        "English": [

            "Boundary crossings today",

            "Busiest warning hour",

            "Repeat warnings",

            "7-day crossing trend",
        ],

        "isiNdebele": [

            "Ukweqa umngcele lamuhla",

            "Ihora lezixwayiso ezinengi",

            "Izixwayiso eziphindayo",

            "Umkhuba wezinsuku eziyisikhombisa",
        ],

        "Shona": [

            "Boundary crossings nhasi",

            "Nguva ine warnings dzakawanda",

            "Repeat warnings",

            "7-day crossing trend",
        ],
    }


    d1, d2, d3, d4 = (
        st.columns(
            4
        )
    )


    values = [

        "12",

        "13:00",

        "3",

        "↓ 18%",
    ]


    for (
        column,
        label,
        value
    ) in zip(

        [
            d1,
            d2,
            d3,
            d4
        ],

        LABELS[
            st.session_state.lang
        ],

        values
    ):

        with column:

            st.metric(

                label,

                value
            )


    EXPLANATION = {

        "English":
            """
WRO demonstration message: the IR sensor does not replace heritage staff.
It acts as a low-cost educational and preventive layer.

The physical prototype can warn a visitor immediately, while the management
dashboard can convert repeated boundary events into useful information.

For example, if most warnings occur between 13:00 and 14:00, managers could
increase visitor education, change signs, reposition a barrier or provide
additional supervision during that period.
""",

        "isiNdebele":
            """
Umlayezo weWRO: iIR sensor ayithathi indawo yabasebenzi bamagugu.
Iyindlela engabizi kakhulu yokufundisa kanye lokuvikela.

Iprototype ingaxwayisa isivakashi masinyane, kuthi ideshibhodi
iguqule izehlakalo zokweqa umngcele zibe lulwazi olunceda abaphathi.

Nxa izixwayiso ezinengi zenzeka ngesikhathi esithile, abaphathi bangangeza
izibonakaliso, imfundo, izithiyo kumbe ukuqapha ngalesosikhathi.
""",

        "Shona":
            """
Mharidzo yeWRO: IR sensor haitsivi heritage staff.
Iyo low-cost educational uye preventive layer.

Prototype inogona kuyambira mushanyi pakarepo, uku dashboard
ichishandura repeated boundary events kuita useful management information.

Kana warnings dzakawanda dzichiitika panguva imwe chete zuva rega rega,
mamaneja vanogona kuwedzera visitor education, signage, barriers
kana supervision panguva iyoyo.
""",
    }


    st.info(

        EXPLANATION[
            st.session_state.lang
        ],

        icon="💡"
    )


    st.markdown(
        "### 🧠 ROBO GUIDE System Logic"
    )


    system_col1, system_col2 = (
        st.columns(
            2
        )
    )


    with system_col1:

        st.markdown(
            """
            <div class="greenbox">

            <b>Physical ROBO GUIDE</b><br><br>

            👁 IR sensor detects visitor movement<br><br>

            🔔 Buzzer provides immediate warning<br><br>

            🖥 OLED provides multilingual education<br><br>

            📱 QR sends the visitor to the website

            </div>
            """,
            unsafe_allow_html=True
        )


    with system_col2:

        st.markdown(
            """
            <div class="goldbox">

            <b>Digital ROBO GUIDE</b><br><br>

            🌍 Detailed heritage exploration<br><br>

            🗣 English • isiNdebele • Shona<br><br>

            🏆 Interactive Heritage Challenge<br><br>

            💬 Rule-based Heritage Assistant<br><br>

            📊 Heritage management interpretation

            </div>
            """,
            unsafe_allow_html=True
        )


# ------------------------------------------------------------
# PAGE ROUTING
# ------------------------------------------------------------

current_page = (
    st.session_state.page
)


if (
    current_page
    ==
    "Home"
):

    home_page()


elif (
    current_page
    in
    [
        "Matobo Hills",
        "Great Zimbabwe",
        "Khami Ruins",
    ]
):

    site_page(
        current_page
    )


elif (
    current_page
    ==
    "Heritage Challenge"
):

    quiz_page()


elif (
    current_page
    ==
    "Heritage Assistant"
):

    assistant_page()


elif (
    current_page
    ==
    "Robot + Website"
):

    prototype_page()


else:

    st.session_state.page = (
        "Home"
    )

    st.rerun()


# ------------------------------------------------------------
# FINAL FOOTER
# ------------------------------------------------------------

st.markdown(

    f"""
    <div class="footer">

        <b>
            {tr("footer")}
        </b>

        <br><br>

        ROBO GUIDE combines cultural education,
        multilingual communication,
        interactive learning and
        preventive heritage-protection technology.

        <br>

        Built as a single-file Streamlit experience
        for the WRO 2026 Zimbabwe National Finals.

    </div>
    """,

    unsafe_allow_html=True
)
import streamlit as st
import re
from html import escape

st.set_page_config(
    page_title="ROBO GUIDE | Zimbabwe Heritage Explorer",
    page_icon="🗿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# ROBO GUIDE
# WRO 2026 Zimbabwe National Finals
# Theme: Robots Meet Culture
# ============================================================

# ------------------------------------------------------------
# DESIGN
# ------------------------------------------------------------

st.markdown(
    """
<style>

:root {
    --green: #08683A;
    --deepgreen: #034725;
    --gold: #E5B72E;
    --lightgold: #FFF7DA;
    --cream: #FFFDF5;
    --text: #183126;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%,
        rgba(229,183,46,0.10), transparent 22%),
        radial-gradient(circle at 90% 20%,
        rgba(8,104,58,0.08), transparent 25%),
        linear-gradient(180deg,#fffdf7,#f5faf6);
}

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #033d22 0%,
            #086238 60%,
            #034326 100%
        );
    border-right: 3px solid #E5B72E;
}

[data-testid="stSidebar"] * {
    color:white;
}

.brand {
    text-align:center;
    padding:20px 10px;
    margin-bottom:16px;

    border-radius:22px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,.12),
            rgba(229,183,46,.08)
        );

    border:1px solid rgba(229,183,46,.45);
}

.brand-logo {
    font-size:46px;
}

.brand h2 {
    margin:2px 0;
    color:white;
    letter-spacing:2px;
}

.brand p {
    color:#FFE899;
    font-size:13px;
}

.hero {

    border-radius:30px;

    padding:42px;

    margin-bottom:26px;

    color:white;

    position:relative;

    overflow:hidden;

    background:

        linear-gradient(
            120deg,
            rgba(3,65,35,.98),
            rgba(9,119,63,.94)
        );

    border:1px solid rgba(229,183,46,.6);

    box-shadow:
        0 20px 50px
        rgba(0,70,38,.18);
}

.hero:after {

    content:"";

    position:absolute;

    width:320px;
    height:320px;

    border-radius:50%;

    right:-110px;
    top:-100px;

    border:
        35px solid
        rgba(229,183,46,.18);

    box-shadow:
        0 0 0 30px
        rgba(255,255,255,.03);
}

.kicker {

    color:#F6D35C;

    font-size:13px;

    font-weight:800;

    letter-spacing:2px;

    text-transform:uppercase;
}

.hero h1 {

    margin:6px 0;

    font-size:
        clamp(
            2.7rem,
            6vw,
            5.2rem
        );

    line-height:1;

    color:white;
}

.hero h2 {

    color:#F8D766;

    margin-top:5px;
}

.hero p {

    max-width:900px;

    line-height:1.7;

    font-size:1.08rem;

    color:#F4FFF8;
}

.badge {

    display:inline-block;

    background:
        rgba(255,255,255,.10);

    border:
        1px solid
        rgba(255,255,255,.20);

    padding:
        7px 12px;

    border-radius:100px;

    margin:
        4px 4px 0 0;

    font-size:13px;
}

.section-title {

    font-size:30px;

    font-weight:850;

    color:#034725;

    margin-top:24px;
}

.section-sub {

    color:#65746A;

    line-height:1.6;

    margin-bottom:18px;
}

.card {

    background:
        rgba(255,255,255,.96);

    border:
        1px solid
        #E0EAE3;

    border-top:
        4px solid
        #E5B72E;

    border-radius:20px;

    padding:22px;

    min-height:220px;

    box-shadow:
        0 10px 25px
        rgba(31,70,45,.07);
}

.card h3 {

    color:#034725;

    margin-top:5px;
}

.card h4 {

    color:#034725;
}

.card p {

    line-height:1.6;

    color:#435349;
}

.site-icon {
    font-size:36px;
}

.stat {

    background:white;

    border:
        1px solid
        #E2EAE4;

    border-radius:17px;

    padding:
        16px;

    box-shadow:
        0 8px 20px
        rgba(30,60,40,.05);
}

.stat-number {

    color:#08683A;

    font-size:24px;

    font-weight:850;
}

.stat-label {

    font-size:13px;

    color:#68786E;
}

.goldbox {

    background:#FFF8E0;

    border:
        1px solid
        #EAD17A;

    padding:16px;

    border-radius:16px;

    margin:
        10px 0;
}

.greenbox {

    background:#F1FAF5;

    border:
        1px solid
        #CAE3D3;

    border-left:
        5px solid
        #08683A;

    padding:16px;

    border-radius:16px;

    margin:
        10px 0;
}

.unesco {

    background:
        linear-gradient(
            90deg,
            #08683A,
            #0E7946
        );

    border-left:
        6px solid
        #E5B72E;

    color:white;

    border-radius:17px;

    padding:20px;

    margin:
        18px 0;
}

.quizbox {

    background:white;

    border:
        1px solid
        #DFE8E1;

    border-radius:22px;

    padding:24px;

    box-shadow:
        0 10px 26px
        rgba(25,65,40,.07);
}

.achievement {

    text-align:center;

    padding:32px;

    border-radius:25px;

    background:
        linear-gradient(
            135deg,
            #033D22,
            #087343
        );

    color:white;

    border:
        2px solid
        #E5B72E;

    box-shadow:
        0 18px 40px
        rgba(0,85,45,.20);
}

.achievement h2 {

    color:#F6D35C;

    margin:
        7px 0;
}

.achievement-icon {
    font-size:58px;
}

.chat-user {

    max-width:82%;

    margin:
        8px 0 8px auto;

    background:#E8F5ED;

    border:
        1px solid
        #CEE5D5;

    padding:
        13px 15px;

    border-radius:
        18px 18px 4px 18px;
}

.chat-bot {

    max-width:90%;

    margin:
        8px auto 8px 0;

    background:#FFF7DE;

    border:
        1px solid
        #EBD482;

    padding:
        13px 15px;

    border-radius:
        18px 18px 18px 4px;
}

.footer {

    margin-top:40px;

    padding-top:24px;

    border-top:
        1px solid
        #DAE5DC;

    text-align:center;

    font-size:13px;

    color:#66766C;
}

div.stButton > button {

    border-radius:13px;

    border:
        1px solid
        #08703E;

    font-weight:700;

    transition:.2s;
}

div.stButton > button:hover {

    transform:
        translateY(-1px);

    border-color:
        #E5B72E;

    box-shadow:
        0 6px 15px
        rgba(0,90,45,.13);
}

div.stButton > button[kind="primary"] {

    background:
        linear-gradient(
            90deg,
            #08683A,
            #0C7C46
        );

    color:white;
}

.stProgress > div > div > div > div {

    background:
        #08683A;
}

[data-testid="stMetric"] {

    background:white;

    border:
        1px solid
        #E2EAE4;

    padding:
        10px;

    border-radius:
        14px;
}

</style>
""",
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# SESSION STATE
# ------------------------------------------------------------

DEFAULTS = {

    "page":
        "Home",

    "lang":
        "English",

    "quiz_index":
        0,

    "quiz_score":
        0,

    "quiz_points":
        0,

    "quiz_answered":
        False,

    "quiz_feedback":
        None,

    "quiz_finished":
        False,

    "chat":
        [],
}

for key, value in DEFAULTS.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ------------------------------------------------------------
# INTERFACE TRANSLATIONS
# ------------------------------------------------------------

UI = {

    "English": {

        "tagline":
            "Robots Meet Culture • WRO 2026 Zimbabwe",

        "language":
            "Language",

        "navigation":
            "Explore ROBO GUIDE",

        "home":
            "Home",

        "matobo":
            "Matobo Hills",

        "great":
            "Great Zimbabwe",

        "khami":
            "Khami Ruins",

        "quiz":
            "Heritage Challenge",

        "assistant":
            "Heritage Assistant",

        "prototype":
            "Robot + Website",

        "hero":
            "Meet Zimbabwe through technology.",

        "hero_text":
            "ROBO GUIDE connects a physical heritage-protection prototype with a multilingual digital guide, helping visitors learn, explore and protect Zimbabwe's cultural treasures.",

        "explore":
            "Explore Zimbabwe's heritage",

        "explore_sub":
            "Choose a heritage site and discover its history, people, architecture, stories and protection needs.",

        "open":
            "Open site guide",

        "history":
            "History",

        "culture":
            "Culture & People",

        "features":
            "Major Features",

        "unesco":
            "UNESCO World Heritage",

        "protection":
            "Protect This Heritage",

        "facts":
            "Interesting Facts",

        "significance":
            "Why It Matters",

        "location":
            "Location",

        "inscription":
            "UNESCO inscription",

        "criteria":
            "UNESCO criteria",

        "why":
            "Why ROBO GUIDE?",

        "why_text":
            "Culture is strongest when people understand it, experience it and help protect it. ROBO GUIDE turns heritage learning into an interactive visitor journey while demonstrating how affordable robotics can support respectful visitor behaviour.",

        "learn":
            "Learn",

        "learn_text":
            "Detailed heritage guides and learning in three languages.",

        "play":
            "Play",

        "play_text":
            "Earn Heritage Points through an interactive gamified challenge.",

        "protect":
            "Protect",

        "protect_text":
            "Use technology to encourage safe behaviour near sensitive heritage.",

        "connect":
            "Connect",

        "connect_text":
            "Link the physical prototype to deeper learning through QR access.",

        "challenge":
            "Take the Heritage Challenge",

        "ask":
            "Ask ROBO GUIDE",

        "robot":
            "Explore Robot Integration",

        "back":
            "← Back to Home",

        "quiz_title":
            "Heritage Challenge",

        "quiz_intro":
            "Test what you have learned about Zimbabwe's heritage. Correct answers earn Heritage Points and every answer includes an explanation.",

        "question":
            "Question",

        "score":
            "Score",

        "points":
            "Heritage Points",

        "submit":
            "Check Answer",

        "next":
            "Next Question →",

        "finish":
            "See My Achievement",

        "correct":
            "Correct!",

        "incorrect":
            "Not quite.",

        "replay":
            "Play Again",

        "achievement":
            "Achievement Unlocked",

        "guide":
            "Heritage Guide",

        "guardian":
            "Heritage Guardian",

        "guide_desc":
            "You have built a strong foundation. Keep exploring Zimbabwe's heritage and share what you learn.",

        "guardian_desc":
            "Outstanding work! You demonstrated excellent heritage knowledge and a strong conservation mindset.",

        "assistant_title":
            "ROBO GUIDE Heritage Assistant",

        "assistant_intro":
            "Ask detailed questions about Matobo Hills, Great Zimbabwe or Khami Ruins — including history, dates, builders, caves, rock art, architecture, artifacts, trade, culture, UNESCO, conservation or comparisons.",

        "assistant_placeholder":
            "Example: Who built Great Zimbabwe?",

        "try_question":
            "Try a question",

        "clear":
            "Clear Conversation",

        "no_answer":
            "I can answer questions about Matobo Hills, Great Zimbabwe and Khami Ruins. Try asking about history, builders, dates, caves, rock art, architecture, artifacts, trade, culture, UNESCO status, conservation, significance or comparisons.",

        "prototype_title":
            "How ROBO GUIDE Connects the Robot and Website",

        "prototype_intro":
            "ROBO GUIDE is one connected visitor-learning system. The physical prototype provides immediate guidance and protection while the website delivers deeper multilingual heritage education and data interpretation.",

        "flow":
            "Visitor Journey",

        "oled":
            "Multilingual OLED Education",

        "oled_text":
            "The physical prototype displays short heritage messages in English, isiNdebele and Shona so visitors can learn in a language they understand.",

        "qr":
            "QR Access",

        "qr_text":
            "A QR code on the physical ROBO GUIDE prototype opens this website, moving visitors from short exhibit messages into a detailed interactive heritage guide.",

        "visitor":
            "Visitor Guidance",

        "visitor_text":
            "ROBO GUIDE teaches respectful visitor behaviour such as staying behind protected boundaries, not touching rock art or stone structures, following site rules and respecting sacred places.",

        "ir":
            "IR Protected-Boundary Monitoring",

        "ir_text":
            "An infrared sensor detects when a visitor crosses the demonstration heritage-protection boundary. It provides a low-cost example of preventive conservation technology.",

        "buzzer":
            "Buzzer Warning",

        "buzzer_text":
            "When the protected boundary is crossed, the buzzer immediately warns the visitor to step back without requiring physical contact.",

        "dashboard":
            "Laptop Management Dashboard",

        "dashboard_text":
            "Boundary-crossing events can be recorded and analysed by time, frequency and trend. This can help identify high-risk periods and improve visitor education, staffing or protection measures.",

        "footer":
            "ROBO GUIDE • WRO 2026 Zimbabwe National Finals • Robots Meet Culture • Learn • Respect • Protect",
    },


    "isiNdebele": {

        "tagline":
            "Amarobhothi Ahlangana Lamasiko • WRO 2026 Zimbabwe",

        "language":
            "Ulimi",

        "navigation":
            "Hlola i-ROBO GUIDE",

        "home":
            "Ikhaya",

        "matobo":
            "Amagquma eMatobo",

        "great":
            "IGreat Zimbabwe",

        "khami":
            "Amanxiwa eKhami",

        "quiz":
            "Inselele Yamagugu",

        "assistant":
            "Umsizi Wamagugu",

        "prototype":
            "Irobhothi + Iwebhusayithi",

        "hero":
            "Hlangana leZimbabwe ngobuchwepheshe.",

        "hero_text":
            "I-ROBO GUIDE ixhumanisa irobhothi lokuvikela amagugu lomhlahlandlela wedijithali osebenza ngezindimi ezintathu, ukuze izivakashi zifunde, zihlole njalo zivikele amagugu amasiko eZimbabwe.",

        "explore":
            "Hlola amagugu eZimbabwe",

        "explore_sub":
            "Khetha indawo yamagugu ufunde ngomlando, abantu, izakhiwo, izindaba kanye lendlela yokuyivikela.",

        "open":
            "Vula umhlahlandlela",

        "history":
            "Umlando",

        "culture":
            "Amasiko Labantu",

        "features":
            "Izinto Eziqakathekileyo",

        "unesco":
            "Amagugu Omhlaba e-UNESCO",

        "protection":
            "Vikela Amagugu La",

        "facts":
            "Amaqiniso Athakazelisayo",

        "significance":
            "Kungani Kuqakathekile",

        "location":
            "Indawo",

        "inscription":
            "Ukubhaliswa yi-UNESCO",

        "criteria":
            "Imigomo ye-UNESCO",

        "why":
            "Kungani i-ROBO GUIDE?",

        "why_text":
            "Amasiko aqina nxa abantu bewazwisisa, bewabona njalo besiza ukuwavikela. I-ROBO GUIDE yenza ukufunda amagugu kube ngumsebenzi osebenzisanayo futhi iveze indlela amarobhothi anganceda ngayo ekuvikeleni indawo.",

        "learn":
            "Funda",

        "learn_text":
            "Imihlahlandlela ejulileyo yamagugu ngezindimi ezintathu.",

        "play":
            "Dlala",

        "play_text":
            "Thola amaHeritage Points ngokuphendula imibuzo.",

        "protect":
            "Vikela",

        "protect_text":
            "Sebenzisa ubuchwepheshe ukukhuthaza ukuziphatha okuphephileyo.",

        "connect":
            "Xhumanisa",

        "connect_text":
            "Xhumanisa irobhothi lolwazi olujulileyo ngeQR.",

        "challenge":
            "Yenza Inselele Yamagugu",

        "ask":
            "Buza i-ROBO GUIDE",

        "robot":
            "Bona Ukuxhumana Kwerobhothi",

        "back":
            "← Buyela Ekhaya",

        "quiz_title":
            "Inselele Yamagugu",

        "quiz_intro":
            "Hlola ulwazi lwakho ngamagugu eZimbabwe. Impendulo elungileyo iletha amaHeritage Points futhi yonke impendulo ilencazelo.",

        "question":
            "Umbuzo",

        "score":
            "Amaphuzu",

        "points":
            "AmaHeritage Points",

        "submit":
            "Hlola Impendulo",

        "next":
            "Umbuzo Olandelayo →",

        "finish":
            "Bona Umklomelo",

        "correct":
            "Kulungile!",

        "incorrect":
            "Akukabi yikho.",

        "replay":
            "Dlala Futhi",

        "achievement":
            "Umklomelo Uvuliwe",

        "guide":
            "Heritage Guide",

        "guardian":
            "Heritage Guardian",

        "guide_desc":
            "Usulolwazi oluqinileyo. Qhubeka uhlola amagugu eZimbabwe njalo wabelane ngalokho okufundayo.",

        "guardian_desc":
            "Umsebenzi omuhle kakhulu! Utshengise ulwazi olukhulu kanye lomqondo oqinileyo wokuvikela amagugu.",

        "assistant_title":
            "Umsizi Wamagugu we-ROBO GUIDE",

        "assistant_intro":
            "Buza ngeMatobo Hills, Great Zimbabwe kumbe Khami Ruins — umlando, izinsuku, abakhi, imigede, imidwebo emadwaleni, izakhiwo, izinto zakudala, ukuhweba, amasiko, UNESCO, ukuvikelwa kumbe ukuqhathanisa.",

        "assistant_placeholder":
            "Isibonelo: Ngubani owakha iGreat Zimbabwe?",

        "try_question":
            "Zama umbuzo",

        "clear":
            "Sula Ingxoxo",

        "no_answer":
            "Nginganceda ngezindawo ezintathu zeROBO GUIDE. Buza ngomlando, abakhi, izinsuku, imigede, imidwebo, izakhiwo, izinto zakudala, ukuhweba, amasiko, UNESCO, ukuvikelwa kumbe ukuqhathanisa.",

        "prototype_title":
            "Indlela i-ROBO GUIDE Exhumanisa Ngayo Irobhothi Lewebhusayithi",

        "prototype_intro":
            "I-ROBO GUIDE iyisistimu eyodwa yokufundisa izivakashi. Irobhothi linika ulwazi lokuvikela masinyane kuthi iwebhusayithi inike ulwazi olujulileyo ngezindimi ezintathu.",

        "flow":
            "Uhambo Lwesivakashi",

        "oled":
            "Imfundo ye-OLED Ngezindimi Ezintathu",

        "oled_text":
            "Iprototype iveza imilayezo emifitshane ngesiNgisi, isiNdebele kanye lesiShona ukuze izivakashi zifunde ngolimi eziluzwisisayo.",

        "qr":
            "Ukungena nge-QR",

        "qr_text":
            "Ikhodi yeQR embukisweni ivula iwebhusayithi yeROBO GUIDE, isusa isivakashi emlayezweni omfitshane isise emhlahlandleleni ogcweleyo.",

        "visitor":
            "Ukuqondisa Izivakashi",

        "visitor_text":
            "I-ROBO GUIDE ifundisa ukuziphatha okuhloniphayo: hlala ngaphandle kwemingcele evikelweyo, ungathinti imidwebo kumbe izakhiwo zamatshe njalo uhloniphe izindawo ezingcwele.",

        "ir":
            "Ukuqapha Umngcele nge-IR",

        "ir_text":
            "I-infrared sensor ibona nxa isivakashi siwela umngcele wokuvikela, itshengisa indlela ubuchwepheshe obunganceda ngayo ekuvikelweni kwamagugu.",

        "buzzer":
            "Isixwayiso se-Buzzer",

        "buzzer_text":
            "Nxa umngcele oweqiwa i-buzzer inika isixwayiso masinyane, ikhuthaze isivakashi ukuthi sihlehle.",

        "dashboard":
            "Ideshibhodi Yokuphatha Kukhompyutha",

        "dashboard_text":
            "Izehlakalo zokweqa umngcele zingarekhodwa futhi zihlaziywe ngesikhathi, ngobunengi kanye lemikhuba ukuze abaphathi bathuthukise ukuvikelwa.",

        "footer":
            "ROBO GUIDE • WRO 2026 Zimbabwe National Finals • Robots Meet Culture • Funda • Hlonipha • Vikela",
    },


    "Shona": {

        "tagline":
            "Marobhoti Anosangana Netsika • WRO 2026 Zimbabwe",

        "language":
            "Mutauro",

        "navigation":
            "Ongorora ROBO GUIDE",

        "home":
            "Kumba",

        "matobo":
            "Matobo Hills",

        "great":
            "Great Zimbabwe",

        "khami":
            "Khami Ruins",

        "quiz":
            "Heritage Challenge",

        "assistant":
            "Mubatsiri weNhaka",

        "prototype":
            "Robhoti + Webhusaiti",

        "hero":
            "Sangana neZimbabwe kuburikidza netekinoroji.",

        "hero_text":
            "ROBO GUIDE inobatanidza prototype yerobhoti rekuchengetedza nhaka nemutungamiriri wedhijitari wemitauro mitatu, ichibatsira vashanyi kudzidza, kuongorora uye kuchengetedza pfuma yetsika yeZimbabwe.",

        "explore":
            "Ongorora nhaka yeZimbabwe",

        "explore_sub":
            "Sarudza nzvimbo kuti uzive nhoroondo, vanhu, zvivakwa, nyaya uye nzira dzekuichengetedza.",

        "open":
            "Vhura Mutungamiriri",

        "history":
            "Nhoroondo",

        "culture":
            "Tsika Nevanhu",

        "features":
            "Zvinhu Zvikuru",

        "unesco":
            "UNESCO World Heritage",

        "protection":
            "Chengetedza Nhaka Iyi",

        "facts":
            "Mashoko Anonakidza",

        "significance":
            "Kukosha Kwayo",

        "location":
            "Nzvimbo",

        "inscription":
            "Kunyoreswa neUNESCO",

        "criteria":
            "Mitemo yeUNESCO",

        "why":
            "Sei ROBO GUIDE?",

        "why_text":
            "Tsika dzinosimba kana vanhu vachidzinzwisisa, vachidziona uye vachibatsira kudzichengetedza. ROBO GUIDE inoita kuti kudzidza nhaka kuve chiitiko chinodyidzana uye inoratidza mashandisirwo etekinoroji mukuchengetedza nzvimbo.",

        "learn":
            "Dzidza",

        "learn_text":
            "Mitungamiriri yakadzama yenzvimbo dzenhaka mumitauro mitatu.",

        "play":
            "Tamba",

        "play_text":
            "Wana Heritage Points kuburikidza nemibvunzo inodyidzana.",

        "protect":
            "Chengetedza",

        "protect_text":
            "Shandisa tekinoroji kukurudzira maitiro anoremekedza nhaka.",

        "connect":
            "Batanidza",

        "connect_text":
            "QR inobatanidza physical prototype neruzivo rwakadzama.",

        "challenge":
            "Tora Heritage Challenge",

        "ask":
            "Bvunza ROBO GUIDE",

        "robot":
            "Ona Kubatana Kwerobhoti",

        "back":
            "← Dzokera Kumba",

        "quiz_title":
            "Heritage Challenge",

        "quiz_intro":
            "Edza ruzivo rwako rwenhaka yeZimbabwe. Mhinduro dzakarurama dzinokupa Heritage Points uye mhinduro dzese dzine tsananguro.",

        "question":
            "Mubvunzo",

        "score":
            "Zvawawana",

        "points":
            "Heritage Points",

        "submit":
            "Tarisa Mhinduro",

        "next":
            "Mubvunzo Unotevera →",

        "finish":
            "Ona Mubairo",

        "correct":
            "Zvakarurama!",

        "incorrect":
            "Hazvisati zvanyatsonaka.",

        "replay":
            "Tamba Zvakare",

        "achievement":
            "Mubairo Wavhurwa",

        "guide":
            "Heritage Guide",

        "guardian":
            "Heritage Guardian",

        "guide_desc":
            "Wava neruzivo rwakanaka. Ramba uchiongorora nhaka yeZimbabwe uye ugovane zvaunodzidza.",

        "guardian_desc":
            "Basa rakanaka zvikuru! Waratidza ruzivo rwakadzama uye pfungwa yakasimba yekuchengetedza nhaka.",

        "assistant_title":
            "ROBO GUIDE Heritage Assistant",

        "assistant_intro":
            "Bvunza nezveMatobo Hills, Great Zimbabwe kana Khami Ruins — nhoroondo, mazuva, vavaki, mapako, rock art, architecture, artifacts, trade, tsika, UNESCO, conservation kana comparisons.",

        "assistant_placeholder":
            "Semuenzaniso: Ndiani akavaka Great Zimbabwe?",

        "try_question":
            "Edza mubvunzo",

        "clear":
            "Bvisa Hurukuro",

        "no_answer":
            "Ndinogona kubatsira nezvenzvimbo nhatu dzeROBO GUIDE. Bvunza nezvenhoroondo, vavaki, mazuva, mapako, rock art, architecture, artifacts, trade, tsika, UNESCO, conservation kana comparisons.",

        "prototype_title":
            "Maitiro ROBO GUIDE Anobatanidza Robhoti Newebhusaiti",

        "prototype_intro":
            "ROBO GUIDE ihurongwa humwe hwekudzidzisa vashanyi. Prototype inopa yambiro nekudzidzisa ipapo, uku webhusaiti ichipa ruzivo rwakadzama rwemitauro mitatu.",

        "flow":
            "Rwendo Rwemushanyi",

        "oled":
            "Dzidzo yeOLED Yemitauro Mitatu",

        "oled_text":
            "Prototype inoratidza mashoko mapfupi muEnglish, isiNdebele neShona kuitira kuti vashanyi vadzidze nemutauro wavanonzwisisa.",

        "qr":
            "QR Access",

        "qr_text":
            "QR code iri paprototype inovhura ROBO GUIDE webhusaiti, ichiendesa mushanyi kubva pamashoko mapfupi kuenda kumutungamiriri wakadzama.",

        "visitor":
            "Kutungamirira Vashanyi",

        "visitor_text":
            "ROBO GUIDE inodzidzisa maitiro anoremekedza nhaka: gara kunze kwemiganhu yakachengetedzwa, usabata rock art kana ancient stonework uye remekedza nzvimbo dzinoyera.",

        "ir":
            "IR Protected-Boundary Monitoring",

        "ir_text":
            "Infrared sensor inoona kana mushanyi ayambuka muganhu wekuchengetedza, ichiratidza kuti tekinoroji inogona kubatsira sei mukudzivirira kukuvara.",

        "buzzer":
            "Yambiro yeBuzzer",

        "buzzer_text":
            "Kana muganhu wayambukwa buzzer inopa yambiro ipapo uye inokurudzira mushanyi kudzokera shure.",

        "dashboard":
            "Laptop Management Dashboard",

        "dashboard_text":
            "Boundary-crossing events dzinogona kurekodhwa nekuongororwa nenguva, frequency uye trend kuti mamaneja avandudze visitor education nekuchengetedza.",

        "footer":
            "ROBO GUIDE • WRO 2026 Zimbabwe National Finals • Robots Meet Culture • Dzidza • Remekedza • Chengetedza",
    },
}


# ------------------------------------------------------------
# HERITAGE SITE CONTENT
# ------------------------------------------------------------

SITES = {

    "Matobo Hills": {

        "emoji":
            "🪨",

        "English": {

            "name":
                "Matobo Hills",

            "subtitle":
                "A living cultural landscape of granite hills, sacred places, caves and extraordinary rock art.",

            "location":
                "Matabeleland South, south of Bulawayo, Zimbabwe",

            "inscribed":
                "2003",

            "criteria":
                "(iii), (v), (vi)",

            "history":
                """
Matobo Hills is one of Zimbabwe's most remarkable cultural landscapes.
Its granite formations have provided shelter, food, spiritual meaning and
strategic refuge to people for thousands of years.

Archaeological evidence in the hills reaches far back into the Stone Age.
Hunter-gatherer communities used the caves and rock shelters and left behind
a remarkable artistic record in the form of paintings.

Later farming communities occupied the wider landscape, while Matobo also
became closely connected with Ndebele history during the nineteenth century.

The landscape therefore records many different periods of Zimbabwean history
rather than representing only one community or one time.
""",

            "culture":
                """
Matobo remains a living cultural and spiritual landscape.

Sacred hills, shrines, oral traditions and ancestral associations remain
important to communities around the area. The Mwari religious tradition,
rain-making beliefs and respect for sacred places contribute to the continuing
cultural significance of Matobo.

The hills are also strongly connected to Ndebele history, including memories
of King Mzilikazi and important nineteenth-century events.

This means that protecting Matobo requires protecting both physical heritage
and living traditions.
""",

            "features": [

                "Granite kopjes, balancing rocks and dramatic valleys created through long geological weathering.",

                "Natural caves and rock shelters that protected people and preserved archaeological evidence.",

                "A very high concentration of prehistoric rock paintings.",

                "Paintings showing humans, animals, hunting, movement and aspects of past social and spiritual life.",

                "Archaeological deposits that help researchers understand changing human occupation over thousands of years.",

                "Sacred hills and shrines that remain culturally important to surrounding communities.",

                "A landscape strongly associated with Zimbabwean and Ndebele history.",
            ],

            "unesco":
                """
Matobo Hills was inscribed on the UNESCO World Heritage List in 2003
as a cultural landscape under criteria (iii), (v) and (vi).

UNESCO recognizes its exceptional concentration of rock art, the very long
relationship between communities and the landscape, and the continuing
importance of powerful religious traditions associated with the hills.
""",

            "protection": [

                "Never touch rock paintings because oils and moisture from human hands can damage fragile surfaces.",

                "Never wet paintings to make their colours appear stronger.",

                "Do not trace paintings using chalk, pencil, paint or any other material.",

                "Stay behind barriers and use approved visitor paths.",

                "Do not remove stones, pottery fragments or archaeological material.",

                "Respect sacred areas and instructions given by local custodians and heritage guides.",

                "Avoid graffiti, fire, littering and climbing over sensitive painted surfaces.",
            ],

            "facts": [

                "Matobo has one of the highest concentrations of rock art in southern Africa.",

                "Some rock shelters contain several layers of paintings created during different periods.",

                "Granite shelters helped preserve both paintings and archaeological deposits.",

                "Matobo is not simply an archaeological site — it remains a living spiritual landscape.",

                "The landscape combines natural beauty with archaeology, history, belief and art.",
            ],

            "significance":
                """
Matobo demonstrates that heritage can be both ancient and living.
Its caves, paintings, archaeology, oral history and sacred landscape allow
visitors to understand how generations of people interacted with the same
environment in very different ways.
""",
        },


        "isiNdebele": {

            "name":
                "Amagquma eMatobo",

            "subtitle":
                "Indawo yamasiko ephilayo elamagquma egranite, izindawo ezingcwele, imigede kanye lemidwebo emangalisayo emadwaleni.",

            "location":
                "EMatabeleland South, eningizimu yeBulawayo, eZimbabwe",

            "inscribed":
                "2003",

            "criteria":
                "(iii), (v), (vi)",

            "history":
                """
IMatobo ingenye yezindawo zamasiko eziqakathekileyo kakhulu eZimbabwe.
Amadwala ayo egranite anike abantu indawo yokukhosela kanye lendawo
yokuphila okweminyaka eminengi.

Ubufakazi bezinto zakudala bubuyela eStone Age.
Abazingeli labaqoqi basebenzisa imigede lezindawo zokukhosela
futhi batshiya imidwebo emangalisayo emadwaleni.

Abalimi abalandelayo labo bahlala endaweni le.
IMatobo yabuye yaba yindawo eqakathekileyo emlandweni wamaNdebele.

Ngakho iMatobo igcina umlando wezikhathi lemiphakathi etshiyeneyo.
""",

            "culture":
                """
IMatobo iseyindawo ephilayo yamasiko lokomoya.

Amagquma angcwele, izindawo zokukhulekela, izindaba zomlomo kanye
lobudlelwano labokhokho kusaqakathekile emiphakathini.

Inkolelo kaMwari kanye lamasiko ahlobene lokucela izulu lawo ayingxenye
yokubaluleka kwendawo.

IMatobo iphinde ixhumane kakhulu lomlando wamaNdebele, okuhlanganisa
inkumbulo yeNkosi uMzilikazi.

Ukuvikela iMatobo yikho ukuvikela kokubili izinto ezibonakalayo
kanye lamasiko aphilayo.
""",

            "features": [

                "Amagquma egranite, amatshe azilinganisileyo kanye lezihotsha ezinhle.",

                "Imigede lezindawo zemvelo zokukhosela.",

                "Imidwebo eminengi kakhulu yakudala emadwaleni.",

                "Imidwebo yabantu, izinyamazana, ukuzingela kanye lezinye izenzo.",

                "Ubufakazi bezinto zakudala obunceda ukufunda impilo yabantu bakudala.",

                "Izindawo ezingcwele ezisaqakathekile emphakathini.",

                "Indawo exhumene kakhulu lomlando wamaNdebele.",
            ],

            "unesco":
                """
IMatobo Hills yabhaliswa ku-UNESCO World Heritage List ngo-2003
njengendawo yamasiko ngaphansi kwemigomo (iii), (v) kanye (vi).

I-UNESCO iqaphela ubunengi bemidwebo emadwaleni, ubudlelwano obude
phakathi kwabantu lendawo, kanye lokuqhubeka kwamasiko okomoya.
""",

            "protection": [

                "Ungathinti imidwebo emadwaleni ngoba amafutha asezandleni angayonakalisa.",

                "Ungamanzisi imidwebo ukuze imibala ibonakale kakhulu.",

                "Ungayicuphi ngechalk, ipensela loba upende.",

                "Hamba ngemizila evunyelweyo njalo uhlale ngemva kwemingcele.",

                "Ungasusi amatshe kumbe ezinye izinto zakudala.",

                "Hlonipha izindawo ezingcwele kanye lemithetho yendawo.",

                "Gwema ingcekeza, umlilo, graffiti kanye lokugibela phezu kwamatshe avikelweyo.",
            ],

            "facts": [

                "IMatobo ilobunengi obukhulu bemidwebo emadwaleni eSouthern Africa.",

                "Ezinye indawo zilezigaba eziningi zemidwebo ezenziwa ngezikhathi ezitshiyeneyo.",

                "Imigede yegranite yanceda ukugcina imidwebo.",

                "IMatobo ayisiyo archaeological site kuphela — iyindawo ephilayo ngokomoya.",

                "Indawo ixhumanisa ubuhle bemvelo, umlando, amasiko kanye lobuciko.",
            ],

            "significance":
                """
IMatobo itshengisa ukuthi amagugu angaba madala kodwa aqhubeke ephila.
Imigede, imidwebo, izinto zakudala, izindaba zabantu kanye lezindawo
ezingcwele kwenza iMatobo ibe yingxenye eqakathekileyo yobuwena beZimbabwe.
""",
        },


        "Shona": {

            "name":
                "Matobo Hills",

            "subtitle":
                "Nzvimbo yetsika inorarama ine zvikomo zvegranite, nzvimbo dzinoyera, mapako uye rock art inoshamisa.",

            "location":
                "Matabeleland South, kumaodzanyemba kweBulawayo, Zimbabwe",

            "inscribed":
                "2003",

            "criteria":
                "(iii), (v), (vi)",

            "history":
                """
Matobo Hills imwe yenzvimbo dzenhaka dzakakosha zvikuru muZimbabwe.
Matombo egranite akapa vanhu nzvimbo dzekugara nekuzvivanza kwemakore
akawanda zvikuru.

Archaeological evidence inodzokera kuStone Age.
Hunter-gatherer communities vakashandisa mapako nemarock shelters
uye vakasiya mifananidzo yakawanda pamabwe.

Mapoka evarimi akazotevera akashandisawo nzvimbo iyi.
Matobo yakazobatanawo zvakanyanya nenhoroondo yeNdebele.

Saka nzvimbo iyi inochengeta nyaya dzemakore nemapoka evanhu akasiyana.
""",

            "culture":
                """
Matobo haisi nzvimbo yekare chete.
Ichiri cultural uye spiritual landscape inorarama.

Nzvimbo dzinoyera, shrines, oral traditions nemadzitateguru
zvichiri kukosha kum communities.

Mwari religious tradition netsika dzekukumbira mvura zvakare
zvine hukama neMatobo.

Nzvimbo iyi ine hukama hwakasimba nenhoroondo yeNdebele,
kusanganisira ndangariro dzaMambo Mzilikazi.

Kuchengetedza Matobo zvinoreva kuchengetedza zvivakwa nezvinhu
zvayo pamwe netsika dzichiri kurarama.
""",

            "features": [

                "Granite kopjes, balancing rocks nemipata inoshamisa.",

                "Mapako nemarock shelters akagadzirwa nezvisikwa.",

                "Huwandu hukuru hweprehistoric rock paintings.",

                "Paintings dzinoratidza vanhu, mhuka, kuvhima nezvimwe zviitiko.",

                "Archaeological deposits dzinobatsira kunzwisisa hupenyu hwekare.",

                "Nzvimbo dzinoyera dzichiri kukosha kum communities.",

                "Landscape ine hukama hwakadzama nenhoroondo yeZimbabwe neNdebele.",
            ],

            "unesco":
                """
Matobo Hills yakanyoreswa paUNESCO World Heritage List muna 2003
se cultural landscape pasi pecriteria (iii), (v) ne(vi).

UNESCO inocherechedza kuwanda kwe rock art, hukama hurefu pakati
pevanhu nenzvimbo uye spiritual traditions dzichiri kurarama.
""",

            "protection": [

                "Usabata rock paintings nekuti mafuta ari pamaoko anogona kudzikuvara.",

                "Usanyorovesa paintings kuti colours dzinyanye kuoneka.",

                "Usa trace mifananidzo nechalk, penzura kana paint.",

                "Shandisa nzira dzakatenderwa uye gara kuseri kwemiganhu.",

                "Usabvisa matombo kana archaeological material.",

                "Remekedza nzvimbo dzinoyera nemirayiridzo yevatungamiriri.",

                "Dzivisa graffiti, moto, marara uye kukwira pamatombo ane paintings.",
            ],

            "facts": [

                "Matobo ine imwe yehuwandu hukuru hwe rock art muSouthern Africa.",

                "Mamwe marock shelters ane layers dzemifananidzo dzemakore akasiyana.",

                "Granite shelters dzakabatsira kuchengetedza paintings.",

                "Matobo ichiri spiritual landscape inorarama.",

                "Nzvimbo iyi inobatanidza nature, archaeology, history, spirituality neart.",
            ],

            "significance":
                """
Matobo inoratidza kuti nhaka inogona kuva yekare uye ichiri kurarama.
Mapako, rock art, archaeology, oral history netsika dzinoyera
zvinoita kuti ive chikamu chakakosha chenhaka yeZimbabwe.
""",
        },
    },


    "Great Zimbabwe": {

        "emoji":
            "🏛️",

        "English": {

            "name":
                "Great Zimbabwe",

            "subtitle":
                "The monumental stone capital whose name became the name of a nation.",

            "location":
                "Masvingo Province, south-eastern Zimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(i), (iii), (vi)",

            "history":
                """
Great Zimbabwe developed into a major political, economic and cultural
centre between roughly the eleventh and fifteenth centuries.

The city was built and occupied by ancestors of Shona-speaking communities.
Its growth demonstrates the existence of a powerful and highly organized
African society with skilled builders, craftspeople, traders and leaders.

Great Zimbabwe participated in long-distance commercial networks linking
the Zimbabwe Plateau with other parts of Africa and ultimately the
Indian Ocean world.

Its scale, wealth and monumental architecture made it one of the most
important pre-colonial urban centres in southern Africa.
""",

            "culture":
                """
Great Zimbabwe is deeply connected to Zimbabwean identity and to the
history of Shona-speaking communities.

Leadership, cattle wealth, spirituality, craft production and trade were
important parts of the society that developed around the city.

The name Zimbabwe is commonly associated with Shona expressions connected
with houses or buildings of stone.

The site's legacy became so powerful that the independent nation adopted
the name Zimbabwe.

The Zimbabwe Bird, inspired by soapstone bird sculptures found at the site,
also became a national symbol.
""",

            "features": [

                "The Hill Complex, constructed among natural granite boulders.",

                "The Great Enclosure, surrounded by an enormous dry-stone wall.",

                "The famous Conical Tower within the Great Enclosure.",

                "The Valley Ruins, containing numerous stone enclosures.",

                "Sophisticated dry-stone masonry constructed without mortar.",

                "Carved soapstone Zimbabwe Birds.",

                "Evidence of local craft industries and long-distance trade.",

                "Decorative stone patterns built into sections of the walls.",
            ],

            "unesco":
                """
Great Zimbabwe National Monument was inscribed on the UNESCO World
Heritage List in 1986 under criteria (i), (iii) and (vi).

UNESCO recognizes its remarkable architectural achievement, its exceptional
testimony to an important African civilization and its powerful historic
and symbolic importance.
""",

            "protection": [

                "Never climb ancient walls.",

                "Do not sit or lean on dry-stone structures.",

                "Do not remove stones, pottery, beads or archaeological objects.",

                "Stay on designated visitor routes.",

                "Do not carve or scratch names into stone surfaces.",

                "Follow guides and respect restricted areas.",

                "Protect the setting as well as individual walls and artifacts.",
            ],

            "facts": [

                "Modern Zimbabwe takes its name from Great Zimbabwe.",

                "Its monumental walls were built without mortar.",

                "The Great Enclosure is one of the most famous pre-colonial stone structures in sub-Saharan Africa.",

                "Zimbabwe Bird sculptures were carved from soapstone.",

                "The Zimbabwe Bird later became an important national emblem.",

                "Archaeological finds show participation in wide trade networks.",

                "The site provides strong evidence of sophisticated African architecture and state organization.",
            ],

            "significance":
                """
Great Zimbabwe is powerful evidence of African political organization,
architecture, craftsmanship and trade.

It is also important because modern archaeological research corrected
old colonial-era claims that attempted to deny African authorship of
the monument.

Great Zimbabwe stands as both an archaeological achievement and
a major national symbol.
""",
        },


        "isiNdebele": {

            "name":
                "IGreat Zimbabwe",

            "subtitle":
                "Inhloko-dolobha enkulu yamatshe eyapha ilizwe igama lalo.",

            "location":
                "EMasvingo Province, eningizimu-mpumalanga yeZimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(i), (iii), (vi)",

            "history":
                """
IGreat Zimbabwe yakhula yaba yindawo enkulu yezombusazwe,
ezomnotho lamasiko phakathi kwekhulu le-11 lele-15.

Yakhiwa futhi yahlalwa ngokhokho bemiphakathi ekhuluma isiShona.

Ukukhula kwayo kutshengisa ukuthi kwakukhona umbuso waseAfrica
owawulabakhi abalolwazi, abenza imisebenzi yezandla, abahwebi
kanye labakhokheli.

IGreat Zimbabwe yayixhumene lokuhweba okude okwakuxhumanisa
iZimbabwe Plateau lezinye indawo zeAfrica kanye lezindlela
zokuhweba zeIndian Ocean.
""",

            "culture":
                """
IGreat Zimbabwe ixhumene kakhulu lobuwena beZimbabwe kanye
lomlando wemiphakathi ekhuluma isiShona.

Ubukhokheli, inkomo, okomoya, ubuciko kanye lokuhweba kwakuyingxenye
eqakathekileyo yempilo.

Igama elithi Zimbabwe lixhunyaniswa lamazwi esiShona aphathelane
lezindlu kumbe izakhiwo zamatshe.

Ilizwe laseZimbabwe lathatha igama lalo kule ndawo.

IZimbabwe Bird eyatholakala lapha yaba luphawu oluqakathekileyo lwesizwe.
""",

            "features": [

                "I-Hill Complex eyakhiwe phakathi kwamadwala egranite.",

                "I-Great Enclosure elodonga olukhulu lwamatshe.",

                "I-Conical Tower edumileyo.",

                "I-Valley Ruins elezakhiwo zamatshe ezinengi.",

                "Imiduli eyakhiwe ngamatshe ngaphandle kwe-mortar.",

                "IZimbabwe Birds ezibazwe ngesoapstone.",

                "Ubufakazi bobuciko bendawo kanye lokuhweba okude.",

                "Amaphetheni amahle akhiwe emidulini.",
            ],

            "unesco":
                """
IGreat Zimbabwe National Monument yabhaliswa ku-UNESCO World Heritage
List ngo-1986 ngaphansi kwemigomo (i), (iii) kanye (vi).

I-UNESCO iqaphela ubuciko bokwakha, ubufakazi bempucuko enkulu yaseAfrica
kanye lokubaluleka kwendawo emlandweni.
""",

            "protection": [

                "Ungagibeli emidulini yakudala.",

                "Ungahlali kumbe uncike emidulini.",

                "Ungasusi amatshe, pottery, ubuhlalu kumbe izinto zakudala.",

                "Hamba ngemizila yezivakashi.",

                "Ungaqophi amagama ematsheni.",

                "Landela imithetho yabakhokheli.",

                "Hlonipha izindawo ezingavunyelwanga ukungena kuzo.",
            ],

            "facts": [

                "Ilizwe laseZimbabwe lathatha igama lalo eGreat Zimbabwe.",

                "Imiduli emikhulu yakhiwa ngaphandle kwe-mortar.",

                "IGreat Enclosure ingenye yezakhiwo ezidume kakhulu eAfrica.",

                "IZimbabwe Birds zabazwa ngesoapstone.",

                "Inyoni yeZimbabwe yaba luphawu lwesizwe.",

                "Izinto ezatholakala lapha zitshengisa ukuhweba okude.",

                "Indawo itshengisa ubuciko obukhulu bokwakha baseAfrica.",
            ],

            "significance":
                """
IGreat Zimbabwe iyibufakazi bokuthi imiphakathi yaseAfrica yayilobukhokheli,
ubuciko bokwakha, imisebenzi yezandla kanye lokuhweba okuphucukileyo.

Iqakathekile futhi ngoba ubufakazi bezinto zakudala baphikisa imibono
yakudala eyayizama ukuphika ukuthi yakhiwa ngabantu baseAfrica.
""",
        },


        "Shona": {

            "name":
                "Great Zimbabwe",

            "subtitle":
                "Guta guru rematombo rakazopa nyika zita rayo.",

            "location":
                "Masvingo Province, kumaodzanyemba-kumabvazuva kweZimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(i), (iii), (vi)",

            "history":
                """
Great Zimbabwe yakakura kuva political, economic uye cultural centre
huru pakati pezvinenge zana remakore rechi11 nerechi15.

Yakavakwa nekugarwa nemadzitateguru evanhu vanotaura Shona.

Kukura kweguta kunoratidza nzanga yeAfrica yaive nehutungamiri,
vavaki vane hunyanzvi, craftspeople uye vatengesi.

Great Zimbabwe yaive chikamu che long-distance trade networks
dzakabatanidza Zimbabwe Plateau nedzimwe nzvimbo dzeAfrica
uye Indian Ocean world.
""",

            "culture":
                """
Great Zimbabwe yakabatana zvakadzama neZimbabwean identity
uye nhoroondo yevanhu vanotaura Shona.

Hutungamiri, mombe, spirituality, craft production uye trade
zvaive zvakakosha muupenyu hwenharaunda.

Zita rekuti Zimbabwe rinowanzobatanidzwa nemashoko echiShona
ane chekuita nedzimba kana zvivakwa zvematombo.

Nyika yakazvimirira yakatora zita rekuti Zimbabwe.

Zimbabwe Bird yakawanikwa panzvimbo iyi yakazovawo chiratidzo
chakakosha chenyika.
""",

            "features": [

                "Hill Complex yakavakwa pakati pematombo makuru egranite.",

                "Great Enclosure ine madziro makuru edry-stone.",

                "Conical Tower inozivikanwa zvikuru.",

                "Valley Ruins ine zvivakwa zvakawanda zvematombo.",

                "Dry-stone masonry yakavakwa pasina mortar.",

                "Zimbabwe Birds dzakavezwa musoapstone.",

                "Evidence yemabasa emaoko nekutengeserana kure.",

                "Decorative patterns dziri pamadziro.",
            ],

            "unesco":
                """
Great Zimbabwe National Monument yakanyoreswa paUNESCO World Heritage
List muna 1986 pasi pecriteria (i), (iii) ne(vi).

UNESCO inocherechedza architectural achievement yayo,
humbowo hwebudiriro huru yeAfrica uye kukosha kwayo munhoroondo.
""",

            "protection": [

                "Usakwira pamadziro ekare.",

                "Usagara kana kuzembera pamadziro.",

                "Usabvisa matombo, pottery, beads kana archaeological material.",

                "Shandisa visitor paths dzakatemerwa.",

                "Usakwenya kana kuveza mazita pamatombo.",

                "Tevera mirayiridzo yemaguides.",

                "Remekedza nzvimbo dzakarambidzwa.",
            ],

            "facts": [

                "Zimbabwe yemazuva ano yakatora zita rayo kuGreat Zimbabwe.",

                "Madziro makuru akavakwa pasina mortar.",

                "Great Enclosure ndeimwe yezvivakwa zvematombo zvinozivikanwa zvikuru muAfrica.",

                "Zimbabwe Birds dzakavezwa musoapstone.",

                "Zimbabwe Bird yakazova national symbol.",

                "Archaeology inoratidza long-distance trade.",

                "Nzvimbo iyi inoratidza advanced African architecture nepolitical organization.",
            ],

            "significance":
                """
Great Zimbabwe ihumbowo hwakasimba hweAfrican statecraft,
architecture, craftsmanship uye trade.

Archaeology yemazuva ano yakagadzirisawo pfungwa dzekare dzaiedza
kuramba kuti monument iyi yakavakwa nevanhu veAfrica.

Nhasi inzvimbo yakakosha munhoroondo uye national identity.
""",
        },
    },


    "Khami Ruins": {

        "emoji":
            "🧱",

        "English": {

            "name":
                "Khami Ruins",

            "subtitle":
                "A terraced stone city of the Torwa era, rich in decorative masonry and trade history.",

            "location":
                "Near Bulawayo, western Zimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(iii), (iv)",

            "history":
                """
Khami became an important political centre after the decline of
Great Zimbabwe.

It became the capital of the Torwa state, especially from the
fifteenth century into the seventeenth century.

Its rulers controlled an important political and economic centre
in south-western Zimbabwe.

Archaeology shows that Khami participated in regional and
long-distance trading systems.

Imported ceramics and other prestige goods have been found alongside
local material culture.

Khami therefore demonstrates the continuation and transformation of
the wider Zimbabwe stone-building tradition.
""",

            "culture":
                """
Khami reflects the political authority, household organization,
craftsmanship and trading connections of communities in south-western
Zimbabwe.

Its architecture shows clear links with the broader Zimbabwe cultural
tradition, but Khami's builders developed distinctive ways of using
terraces and retaining walls.

The site demonstrates that cultural traditions can continue while
architecture and political systems change over time.
""",

            "features": [

                "Large stone-faced terraces built into the natural landscape.",

                "Raised platforms associated with important occupation areas.",

                "Decorative dry-stone wall patterns.",

                "Retaining walls constructed using carefully laid stone.",

                "The Hill Complex and other major architectural platforms.",

                "Evidence of regional and long-distance trade.",

                "Imported ceramics and other prestige goods.",

                "An architectural tradition related to Great Zimbabwe but expressed through extensive terracing.",
            ],

            "unesco":
                """
Khami Ruins National Monument was inscribed on the UNESCO World
Heritage List in 1986 under criteria (iii) and (iv).

UNESCO recognizes Khami as exceptional testimony to an important
cultural tradition and as an outstanding architectural ensemble
representing an important stage in southern African history.
""",

            "protection": [

                "Never climb or walk along fragile terrace walls.",

                "Stay on designated visitor paths.",

                "Do not remove pottery, beads, stones or archaeological objects.",

                "Do not rearrange loose stones.",

                "Avoid actions that increase erosion around terraces.",

                "Do not scratch or write on decorative stonework.",

                "Follow site instructions designed to protect unstable structures.",
            ],

            "facts": [

                "Khami became prominent after Great Zimbabwe declined.",

                "It is closely associated with the Torwa state.",

                "Its terraces make it visually different from Great Zimbabwe's best-known freestanding walls.",

                "Decorative wall patterns are an important feature of the site.",

                "Imported goods show Khami's participation in wider trade networks.",

                "Khami demonstrates change and innovation within the Zimbabwe stone-building tradition.",
            ],

            "significance":
                """
Khami shows that Zimbabwe's stone-building tradition did not simply
disappear when Great Zimbabwe declined.

The tradition continued, developed and changed.

Khami's terraces, decorative masonry and archaeological evidence show
political organization, skilled architecture and participation in
regional and long-distance trade.
""",
        },


        "isiNdebele": {

            "name":
                "Amanxiwa eKhami",

            "subtitle":
                "Idolobho lamatshe elamathala eTorwa, elicebile ngobuciko bamatshe kanye lomlando wokuhweba.",

            "location":
                "Eduze leBulawayo, entshonalanga yeZimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(iii), (iv)",

            "history":
                """
IKhami yakhula yaba yindawo enkulu ngemva kokwehla kweGreat Zimbabwe.

Yaba yinhloko yombuso weTorwa ikakhulu kusukela ngekhulu le-15
kusiya kwele-17.

Ababusi bayo babelawula indawo eqakathekileyo kwezombusazwe
lezomnotho eNingizimu-Ntshonalanga yeZimbabwe.

Ubufakazi bezinto zakudala butshengisa ukuthi iKhami yayixhumene
lokuhweba okuseduze kanye lokukude.

Izinto ezavela kwamanye amazwe zitholakale kanye lezinto ezenziwa
ngabantu bendawo.

IKhami ngakho itshengisa ukuqhubeka kanye lokuguquka kwesiko
lokwakha ngamatshe eZimbabwe.
""",

            "culture":
                """
IKhami itshengisa amandla ezombusazwe, ukuhleleka kwemizi,
ubuciko kanye lokuxhumana kwezokuhweba.

Izakhiwo zayo zixhumene lesiko elikhulu lokwakha ngamatshe eZimbabwe
kodwa abakhi beKhami basebenzisa amathala lemiduli yokubamba umhlabathi
ngendlela evelele kakhulu.

Lokhu kutshengisa ukuthi amasiko angaqhubeka kodwa indlela yokwakha
iguquke ngesikhathi.
""",

            "features": [

                "Amathala amakhulu alemiduli yamatshe.",

                "Amapulatifomu aphakemeyo akhiwe ehambisana lendawo.",

                "Amaphetheni amahle e-dry-stone masonry.",

                "Imiduli yokubamba umhlabathi.",

                "I-Hill Complex lamanye amapulatifomu amakhulu.",

                "Ubufakazi bokuhweba kwesigaba lesikude.",

                "Ceramics kanye lezinto ezavela kwamanye amazwe.",

                "Isiko lokwakha elixhumene leGreat Zimbabwe kodwa elisebenzisa amathala kakhulu.",
            ],

            "unesco":
                """
IKhami Ruins National Monument yabhaliswa ku-UNESCO World Heritage
List ngo-1986 ngaphansi kwemigomo (iii) kanye (iv).

I-UNESCO iyibona njengobufakazi obukhulu besiko kanye lesibonelo
esihle seqoqo lezakhiwo lesigaba esiqakathekileyo emlandweni
weSouthern Africa.
""",

            "protection": [

                "Ungagibeli kumbe uhambe phezu kwemiduli yamathala.",

                "Hamba ngemizila evunyelweyo.",

                "Ungasusi pottery, ubuhlalu, amatshe kumbe izinto zakudala.",

                "Ungahlele kabutsha amatshe aphumileyo.",

                "Gwema ukwenza izinto ezenza umhlabathi uguguleke.",

                "Ungaqophi kumbe ubhale emidulini.",

                "Landela iziqondiso zokuvikela izakhiwo.",
            ],

            "facts": [

                "IKhami yakhula ngemva kokwehla kweGreat Zimbabwe.",

                "Ixhumene kakhulu lombuso weTorwa.",

                "Amathala ayo ayenza yehluke kakhulu eGreat Zimbabwe.",

                "Imiduli ehlotshisiwe ingenye yezinto ezidume kakhulu.",

                "Izinto ezavela kwamanye amazwe zitshengisa ukuhweba okude.",

                "IKhami itshengisa ukuguquka kwesiko lokwakha ngamatshe.",
            ],

            "significance":
                """
IKhami itshengisa ukuthi isiko lokwakha ngamatshe eZimbabwe
aliqedanga ngesikhathi iGreat Zimbabwe isehla.

Laqhubeka futhi laguquka.

Amathala, ubuciko bemiduli kanye lobufakazi bokuhweba kutshengisa
ukusungula, ubukhokheli kanye lamakhono amakhulu okwakha.
""",
        },


        "Shona": {

            "name":
                "Khami Ruins",

            "subtitle":
                "Guta rematombo rine terraces renguva yeTorwa, richiratidza decorative masonry nenhoroondo yekutengeserana.",

            "location":
                "Pedyo neBulawayo, kumadokero kweZimbabwe",

            "inscribed":
                "1986",

            "criteria":
                "(iii), (iv)",

            "history":
                """
Khami yakasimukira mushure mekuderera kweGreat Zimbabwe.

Yakava capital yeTorwa state, kunyanya kubva muzana remakore
rechi15 kusvika muzana remakore rechi17.

Vatongi vayo vaive nesimba mune zvematongerwo enyika nehupfumi
kumaodzanyemba-kumadokero kweZimbabwe.

Archaeological evidence inoratidza kuti Khami yaive mu regional
uye long-distance trade.

Imported ceramics nezvimwe prestige goods zvakawanikwa pamwe
nezvinhu zvakagadzirwa munharaunda.

Khami saka inoratidza kuenderera uye kushanduka kweZimbabwe
stone-building tradition.
""",

            "culture":
                """
Khami inoratidza political authority, household organization,
craftsmanship uye trading connections.

Architecture yayo ine hukama ne broader Zimbabwe cultural tradition
asi vakavaka Khami vakashandisa terraces neretaining walls
zvakanyanya.

Izvi zvinoratidza kuti tsika inogona kuenderera mberi asi nzira
dzekuvaka dzichishanduka.
""",

            "features": [

                "Stone-faced terraces dzakakura.",

                "Raised platforms dzakavakwa dzichitevera terrain.",

                "Decorative dry-stone wall patterns.",

                "Retaining walls dzakavakwa nehunyanzvi.",

                "Hill Complex nemamwe mapuratifomu makuru.",

                "Evidence ye regional ne long-distance trade.",

                "Imported ceramics nezvimwe prestige goods.",

                "Architecture ine hukama neGreat Zimbabwe asi ine extensive terracing.",
            ],

            "unesco":
                """
Khami Ruins National Monument yakanyoreswa paUNESCO World Heritage
List muna 1986 pasi pecriteria (iii) ne(iv).

UNESCO inoiona sehumbowo hwakasarudzika hwecultural tradition
uye architectural ensemble yakakosha munhoroondo yeSouthern Africa.
""",

            "protection": [

                "Usakwira kana kufamba pamusoro pemadziro e terraces.",

                "Shandisa designated visitor paths.",

                "Usabvisa pottery, beads, stones kana archaeological objects.",

                "Usarongazve loose stones.",

                "Dzivisa zvinhu zvinoita kuti erosion iwedzere.",

                "Usakwenya kana kunyora pamadziro.",

                "Tevera site protection instructions.",
            ],

            "facts": [

                "Khami yakasimukira mushure mekuderera kweGreat Zimbabwe.",

                "Yakabatana zvikuru neTorwa state.",

                "Terraces dzayo dzinoipa appearance yakasiyana neGreat Zimbabwe.",

                "Decorative wall patterns chinhu chakakosha paKhami.",

                "Imported goods dzinoratidza wider trading connections.",

                "Khami inoratidza innovation muZimbabwe stone-building tradition.",
            ],

            "significance":
                """
Khami inoratidza kuti stone-building tradition yeZimbabwe yakaramba
ichienderera kunyange Great Zimbabwe yaderera.

Terraces, decorative masonry uye archaeological evidence zvinoratidza
innovation, political organization uye trade connections.
""",
        },
    },
}


# ------------------------------------------------------------
# QUIZ
# ------------------------------------------------------------

QUIZ = {

    "English": [

        {
            "q":
                "Which ROBO GUIDE heritage site is especially famous for a very high concentration of rock art?",

            "options":
                [
                    "Khami Ruins",
                    "Matobo Hills",
                    "Great Zimbabwe",
                    "Victoria Falls",
                ],

            "answer":
                1,

            "why":
                "Matobo Hills has an exceptional concentration of prehistoric rock paintings preserved in caves and rock shelters.",
        },

        {
            "q":
                "In which year was Matobo Hills inscribed on the UNESCO World Heritage List?",

            "options":
                [
                    "1980",
                    "1986",
                    "2003",
                    "2015",
                ],

            "answer":
                2,

            "why":
                "Matobo Hills was inscribed in 2003 under UNESCO cultural criteria (iii), (v) and (vi).",
        },

        {
            "q":
                "Who built Great Zimbabwe?",

            "options":
                [
                    "Roman soldiers",
                    "Ancestors of Shona-speaking African communities",
                    "Portuguese explorers",
                    "European colonists",
                ],

            "answer":
                1,

            "why":
                "Modern archaeology demonstrates that Great Zimbabwe was built by African communities, particularly ancestors of Shona-speaking peoples.",
        },

        {
            "q":
                "Which famous feature stands within the Great Enclosure?",

            "options":
                [
                    "Conical Tower",
                    "Khami Terrace",
                    "Matobo Cave",
                    "Victoria Falls Tower",
                ],

            "answer":
                0,

            "why":
                "The Conical Tower is one of the best-known architectural features inside the Great Enclosure.",
        },

        {
            "q":
                "How were Great Zimbabwe's monumental stone walls constructed?",

            "options":
                [
                    "With steel reinforcement",
                    "With fired brick and cement",
                    "Using dry-stone masonry without mortar",
                    "Using concrete blocks",
                ],

            "answer":
                2,

            "why":
                "The builders carefully selected and stacked stone without mortar, demonstrating exceptional construction skill.",
        },

        {
            "q":
                "The famous Zimbabwe Birds are associated with which heritage site?",

            "options":
                [
                    "Khami Ruins",
                    "Matobo Hills",
                    "Great Zimbabwe",
                    "Mana Pools",
                ],

            "answer":
                2,

            "why":
                "Carved soapstone Zimbabwe Birds were found at Great Zimbabwe and later became important national symbols.",
        },

        {
            "q":
                "Khami is especially associated with which historic state?",

            "options":
                [
                    "Torwa State",
                    "Roman Empire",
                    "Mali Empire",
                    "Aztec Empire",
                ],

            "answer":
                0,

            "why":
                "Khami became the capital and an important political centre of the Torwa state after Great Zimbabwe declined.",
        },

        {
            "q":
                "Which architectural feature is especially characteristic of Khami?",

            "options":
                [
                    "Extensive stone-faced terraces",
                    "Glass towers",
                    "Pyramids",
                    "Steel bridges",
                ],

            "answer":
                0,

            "why":
                "Khami is especially famous for stone-faced terraces, retaining walls and decorative dry-stone patterns.",
        },

        {
            "q":
                "What is the safest behaviour near prehistoric rock paintings?",

            "options":
                [
                    "Wet them so the colours become brighter",
                    "Trace them using chalk",
                    "Do not touch them",
                    "Rub dust from the surface",
                ],

            "answer":
                2,

            "why":
                "Touching, wetting or tracing rock art can damage fragile surfaces and pigments. Visitors should observe without contact.",
        },

        {
            "q":
                "Why is evidence of long-distance trade important at Great Zimbabwe and Khami?",

            "options":
                [
                    "It shows that the sites were built recently",
                    "It shows links with wider African and Indian Ocean exchange networks",
                    "It proves nobody lived at the sites",
                    "It explains Matobo rock paintings",
                ],

            "answer":
                1,

            "why":
                "Imported objects and other archaeological evidence demonstrate that these centres participated in wide commercial networks.",
        },

        {
            "q":
                "Which site became a major centre after Great Zimbabwe declined?",

            "options":
                [
                    "Khami",
                    "Matobo Cave",
                    "Mana Pools",
                    "Victoria Falls",
                ],

            "answer":
                0,

            "why":
                "Khami rose to political importance after Great Zimbabwe declined and became closely associated with the Torwa state.",
        },

        {
            "q":
                "What should a visitor do when the ROBO GUIDE IR boundary warning activates?",

            "options":
                [
                    "Step back behind the protected boundary",
                    "Ignore the buzzer",
                    "Touch the exhibit quickly",
                    "Disconnect the sensor",
                ],

            "answer":
                0,

            "why":
                "The IR and buzzer system is designed to encourage visitors to step back before approaching protected heritage too closely.",
        },
    ],


    "isiNdebele": [

        {
            "q":
                "Yiphi indawo yeROBO GUIDE edume kakhulu ngobunengi bemidwebo emadwaleni?",

            "options":
                [
                    "IKhami Ruins",
                    "IMatobo Hills",
                    "IGreat Zimbabwe",
                    "IVictoria Falls",
                ],

            "answer":
                1,

            "why":
                "IMatobo Hills ilobunengi obumangalisayo bemidwebo yakudala emigedeni lezindawo zokukhosela.",
        },

        {
            "q":
                "IMatobo Hills yabhaliswa nini kuUNESCO World Heritage List?",

            "options":
                [
                    "1980",
                    "1986",
                    "2003",
                    "2015",
                ],

            "answer":
                2,

            "why":
                "IMatobo Hills yabhaliswa ngo-2003 ngaphansi kwemigomo (iii), (v) kanye (vi).",
        },

        {
            "q":
                "Ngubani owakha iGreat Zimbabwe?",

            "options":
                [
                    "AmaRoma",
                    "Okhokho bemiphakathi yaseAfrica ekhuluma isiShona",
                    "AmaPutukezi",
                    "Abakoloni baseEurope",
                ],

            "answer":
                1,

            "why":
                "Ubufakazi bezinto zakudala butshengisa ukuthi iGreat Zimbabwe yakhiwa yimiphakathi yaseAfrica, ikakhulu okhokho babantu abakhuluma isiShona.",
        },

        {
            "q":
                "Yisiphi isakhiwo esidumileyo esingaphakathi kweGreat Enclosure?",

            "options":
                [
                    "IConical Tower",
                    "IKhami Terrace",
                    "Umgeda weMatobo",
                    "IVictoria Falls Tower",
                ],

            "answer":
                0,

            "why":
                "IConical Tower ingenye yezinto ezaziwa kakhulu ngaphakathi kweGreat Enclosure.",
        },

        {
            "q":
                "Imiduli emikhulu yeGreat Zimbabwe yakhiwa njani?",

            "options":
                [
                    "Ngensimbi",
                    "Ngezitina lesamende",
                    "Ngamatshe ngaphandle kwe-mortar",
                    "Ngeconcrete",
                ],

            "answer":
                2,

            "why":
                "Abakhi babeka amatshe ngobuciko ngaphandle kwe-mortar.",
        },

        {
            "q":
                "IZimbabwe Birds zihlotshaniswa kakhulu layiphi indawo?",

            "options":
                [
                    "IKhami",
                    "IMatobo",
                    "IGreat Zimbabwe",
                    "IMana Pools",
                ],

            "answer":
                2,

            "why":
                "IZimbabwe Birds ezibazwe ngesoapstone zatholakala eGreat Zimbabwe futhi zaba luphawu lwesizwe.",
        },

        {
            "q":
                "IKhami ihlotshaniswa kakhulu lawuphi umbuso?",

            "options":
                [
                    "ITorwa",
                    "IRoma",
                    "IMali",
                    "IAztec",
                ],

            "answer":
                0,

            "why":
                "IKhami yaba yinhloko kanye lendawo enkulu yombuso weTorwa ngemva kokwehla kweGreat Zimbabwe.",
        },

        {
            "q":
                "Yisiphi isici esidume kakhulu ezakhiweni zeKhami?",

            "options":
                [
                    "Amathala amanengi alemiduli yamatshe",
                    "Amaphiramidi",
                    "Izakhiwo zengilazi",
                    "Amabholoho ensimbi",
                ],

            "answer":
                0,

            "why":
                "IKhami idume ngamathala, retaining walls kanye lamaphetheni amahle akhiwe ngamatshe.",
        },

        {
            "q":
                "Kumele wenzeni eduze komdwebo wakudala edwaleni?",

            "options":
                [
                    "Uwumanzise",
                    "Uwucupe ngechalk",
                    "Ungawuthinti",
                    "Uwuhlikihle",
                ],

            "answer":
                2,

            "why":
                "Ukuthinta, ukumanzisa loba ukucupha imidwebo kungayonakalisa. Bukela ngaphandle kokuthinta.",
        },

        {
            "q":
                "Kungani ubufakazi bokuhweba okude buqakathekile eGreat Zimbabwe laseKhami?",

            "options":
                [
                    "Butshengisa ukuthi izindawo zintsha",
                    "Butshengisa ukuxhumana lezindlela ezinkulu zokuhweba",
                    "Butshengisa ukuthi abantu babengahlali lapho",
                    "Buchaza imidwebo yeMatobo",
                ],

            "answer":
                1,

            "why":
                "Izinto ezavela kude zitshengisa ukuxhumana lezindlela ezinkulu zokuhweba eAfrica kanye leIndian Ocean.",
        },

        {
            "q":
                "Yiphi indawo eyakhula kakhulu ngemva kokwehla kweGreat Zimbabwe?",

            "options":
                [
                    "IKhami",
                    "IMatobo Cave",
                    "IMana Pools",
                    "IVictoria Falls",
                ],

            "answer":
                0,

            "why":
                "IKhami yakhula yaba yindawo enkulu yezombusazwe ngemva kokwehla kweGreat Zimbabwe.",
        },

        {
            "q":
                "Isivakashi kumele senzeni nxa iIR warning yeROBO GUIDE ikhala?",

            "options":
                [
                    "Sihlehle sibuyele ngemva komngcele",
                    "Singayinaki",
                    "Sithinte umbukiso masinyane",
                    "Sikhiphe isensor",
                ],

            "answer":
                0,

            "why":
                "Isixwayiso senzelwe ukukhuthaza isivakashi ukuthi sihlehle sivikele amagugu.",
        },
    ],


    "Shona": [

        {
            "q":
                "Ndeipi nzvimbo yeROBO GUIDE inonyanya kuzivikanwa nekuwanda kwe rock art?",

            "options":
                [
                    "Khami Ruins",
                    "Matobo Hills",
                    "Great Zimbabwe",
                    "Victoria Falls",
                ],

            "answer":
                1,

            "why":
                "Matobo Hills ine huwandu hukuru hwe prehistoric rock paintings mumapako nemarock shelters.",
        },

        {
            "q":
                "Matobo Hills yakanyoreswa riini paUNESCO World Heritage List?",

            "options":
                [
                    "1980",
                    "1986",
                    "2003",
                    "2015",
                ],

            "answer":
                2,

            "why":
                "Matobo Hills yakanyoreswa muna 2003 pasi pecriteria (iii), (v) ne(vi).",
        },

        {
            "q":
                "Ndiani akavaka Great Zimbabwe?",

            "options":
                [
                    "Roman soldiers",
                    "Madzitateguru eAfrican communities aitaura Shona",
                    "Portuguese explorers",
                    "European colonists",
                ],

            "answer":
                1,

            "why":
                "Archaeology inoratidza kuti Great Zimbabwe yakavakwa neAfrican communities, kunyanya madzitateguru evanhu vanotaura Shona.",
        },

        {
            "q":
                "Ndechipi chinhu chinozivikanwa chiri mukati meGreat Enclosure?",

            "options":
                [
                    "Conical Tower",
                    "Khami Terrace",
                    "Matobo Cave",
                    "Victoria Falls Tower",
                ],

            "answer":
                0,

            "why":
                "Conical Tower ndeimwe yezviratidzo zvinozivikanwa zvikuru mukati meGreat Enclosure.",
        },

        {
            "q":
                "Madziro makuru eGreat Zimbabwe akavakwa nenzira ipi?",

            "options":
                [
                    "Steel reinforcement",
                    "Brick necement",
                    "Dry-stone masonry pasina mortar",
                    "Concrete blocks",
                ],

            "answer":
                2,

            "why":
                "Matombo akaiswa nehunyanzvi pasina mortar.",
        },

        {
            "q":
                "Zimbabwe Birds dzinonyanya kubatanidzwa nenzvimbo ipi?",

            "options":
                [
                    "Khami",
                    "Matobo",
                    "Great Zimbabwe",
                    "Mana Pools",
                ],

            "answer":
                2,

            "why":
                "Zimbabwe Birds dzakavezwa musoapstone dzakawanikwa kuGreat Zimbabwe uye dzakazova national symbols.",
        },

        {
            "q":
                "Khami inonyanya kubatanidzwa neipi historical state?",

            "options":
                [
                    "Torwa",
                    "Roman",
                    "Mali",
                    "Aztec",
                ],

            "answer":
                0,

            "why":
                "Khami yakava capital uye political centre yakakosha yeTorwa state.",
        },

        {
            "q":
                "Ndechipi architectural feature chinonyanya kusiyanisa Khami?",

            "options":
                [
                    "Stone-faced terraces dzakawanda",
                    "Pyramids",
                    "Glass towers",
                    "Steel bridges",
                ],

            "answer":
                0,

            "why":
                "Khami inozivikanwa nema terraces, retaining walls uye decorative stone patterns.",
        },

        {
            "q":
                "Mushanyi anofanira kuita sei pedyo ne ancient rock art?",

            "options":
                [
                    "Kuinyorovesa",
                    "Ku trace nechalk",
                    "Kusai bata",
                    "Kuikwesha",
                ],

            "answer":
                2,

            "why":
                "Kubata, kunyorovesa kana tracing kunogona kukuvadza pigments nesurface.",
        },

        {
            "q":
                "Sei long-distance trade evidence yakakosha paGreat Zimbabwe neKhami?",

            "options":
                [
                    "Inoratidza kuti nzvimbo itsva",
                    "Inoratidza wider African neIndian Ocean trade networks",
                    "Inoratidza kuti hapana aigara ipapo",
                    "Inotsanangura Matobo paintings",
                ],

            "answer":
                1,

            "why":
                "Imported goods nedzimwe archaeological finds zvinoratidza kubatana kwecentres idzi ne wider exchange networks.",
        },

        {
            "q":
                "Ndeipi nzvimbo yakasimukira mushure mekuderera kweGreat Zimbabwe?",

            "options":
                [
                    "Khami",
                    "Matobo Cave",
                    "Mana Pools",
                    "Victoria Falls",
                ],

            "answer":
                0,

            "why":
                "Khami yakasimukira kuva political centre yakakosha mushure mekuderera kweGreat Zimbabwe.",
        },

        {
            "q":
                "Mushanyi anofanira kuita sei kana IR warning yeROBO GUIDE yarira?",

            "options":
                [
                    "Kudzokera kuseri kwemuganhu wakachengetedzwa",
                    "Kuregeredza buzzer",
                    "Kubata exhibit nekukurumidza",
                    "Kubvisa sensor",
                ],

            "answer":
                0,

            "why":
                "IR nebuzzer zvinokurudzira mushanyi kudzokera shure kuitira kudzivirira sensitive heritage.",
        },
    ],
}


# ------------------------------------------------------------
# HERITAGE ASSISTANT KNOWLEDGE BASE
# ------------------------------------------------------------

KB = {

    "English": {

        "matobo_history":
            """
Matobo Hills is an ancient cultural landscape containing evidence of
human occupation stretching far back into the Stone Age.

Hunter-gatherer communities left an extraordinary record through rock
paintings. Later agricultural communities also occupied the area.

Matobo additionally carries strong Ndebele historical associations and
continues to have spiritual importance today.
""",

        "matobo_rock":
            """
Matobo Hills has one of the highest concentrations of rock art in
southern Africa.

Paintings occur in caves and rock shelters and commonly portray people,
wildlife, hunting, movement and other aspects of life.

The paintings are valuable both as art and as archaeological evidence
that helps researchers interpret earlier communities.
""",

        "matobo_caves":
            """
Matobo's granite landscape created many natural caves and rock shelters.

These shelters provided protection for people and also helped preserve
rock paintings and archaeological deposits from direct weathering.

This natural protection is one reason Matobo contains such a rich
archaeological record.
""",

        "matobo_spiritual":
            """
Matobo is a living sacred landscape.

Shrines, sacred hills, oral traditions, ancestral associations,
rain-making practices and the Mwari religious tradition remain important.

This means conservation should respect both physical archaeological
heritage and living community beliefs.
""",

        "matobo_unesco":
            """
Matobo Hills was inscribed on the UNESCO World Heritage List in 2003
under cultural criteria (iii), (v) and (vi).

UNESCO recognizes its outstanding rock art, the long interaction between
people and landscape and its continuing religious significance.
""",

        "great_history":
            """
Great Zimbabwe flourished mainly between roughly the eleventh and
fifteenth centuries.

It became a major political, economic and cultural centre.

Its scale, stone architecture, craft production, cattle wealth and trade
connections demonstrate the sophistication of the society that lived there.
""",

        "great_builders":
            """
Great Zimbabwe was built by African communities, particularly ancestors
of Shona-speaking peoples.

Modern archaeology has firmly rejected older colonial-era theories that
attempted to attribute Great Zimbabwe to outsiders.
""",

        "great_architecture":
            """
Great Zimbabwe is famous for sophisticated dry-stone masonry built
without mortar.

Its major architectural areas include the Hill Complex, Great Enclosure
and Valley Ruins.

The Great Enclosure contains enormous curved stone walls, internal
passages and the famous Conical Tower.
""",

        "great_birds":
            """
The Zimbabwe Birds are carved soapstone bird sculptures associated with
Great Zimbabwe.

They probably had important elite or spiritual significance.

The bird image later became one of Zimbabwe's strongest national symbols
and appears on the country's flag and national emblem.
""",

        "great_trade":
            """
Great Zimbabwe participated in important long-distance trade networks.

Archaeological finds demonstrate connections with wider African and
Indian Ocean exchange systems.

Regional products such as gold moved through commercial networks while
imported goods reached communities on the Zimbabwe Plateau.
""",

        "great_unesco":
            """
Great Zimbabwe National Monument was inscribed on the UNESCO World
Heritage List in 1986 under criteria (i), (iii) and (vi).

UNESCO recognizes its outstanding architecture, testimony to a major
African civilization and exceptional historic and symbolic significance.
""",

        "khami_history":
            """
Khami rose to prominence after the decline of Great Zimbabwe.

It became the capital of the Torwa state and was especially important
from the fifteenth into the seventeenth century.

Khami demonstrates a later phase of the Zimbabwe stone-building
and political tradition.
""",

        "khami_torwa":
            """
Khami is strongly associated with the Torwa state.

Torwa rulers controlled an important political and economic centre in
south-western Zimbabwe after the decline of Great Zimbabwe.

Khami therefore helps explain how political power shifted and developed
in the region.
""",

        "khami_architecture":
            """
Khami is especially known for stone-faced terraces, retaining walls
and decorative dry-stone patterns.

Its builders adapted architecture to the natural terrain by constructing
raised platforms.

The style is related to Great Zimbabwe but Khami places much stronger
emphasis on extensive terracing.
""",

        "khami_trade":
            """
Khami participated in regional and long-distance trade.

Imported ceramics and other prestige objects discovered by archaeologists
show that Khami's elite had access to wider exchange networks.

Local cultural traditions continued while external trade connections
remained important.
""",

        "khami_unesco":
            """
Khami Ruins National Monument was inscribed on the UNESCO World Heritage
List in 1986 under criteria (iii) and (iv).

UNESCO recognizes its cultural testimony and outstanding architectural
ensemble.
""",

        "conservation":
            """
ROBO GUIDE promotes preventive heritage conservation.

Visitors should not touch rock art, climb ancient walls, remove artifacts,
scratch stone, create graffiti or enter protected areas.

Visitors should remain on designated paths, respect sacred places and
follow heritage guides.

The physical ROBO GUIDE prototype demonstrates preventive conservation
using an IR protected-boundary sensor and buzzer warning.
""",

        "comparison":
            """
Great Zimbabwe and Khami belong to related Zimbabwe stone-building
traditions, but they are not identical.

Great Zimbabwe is earlier and is especially famous for monumental
freestanding dry-stone architecture such as the Great Enclosure.

Khami became important later and is particularly recognizable for
extensive terraces, retaining walls and decorative masonry.

Both demonstrate skilled construction, organized political societies
and participation in long-distance trade.
""",

        "all_sites":
            """
The three ROBO GUIDE heritage sites tell complementary stories.

Matobo Hills is a living granite cultural landscape famous for rock art,
archaeology, caves and sacred traditions.

Great Zimbabwe is a monumental medieval stone centre associated with
Shona history, political organization and long-distance trade.

Khami is a later Torwa-era stone city distinguished by terraces,
decorative masonry and trading connections.

Together they demonstrate the extraordinary diversity and depth of
Zimbabwe's cultural heritage.
""",
    },


    "isiNdebele": {

        "matobo_history":
            """
IMatobo Hills yindawo yamasiko yakudala elobufakazi bempilo yabantu
obubuyela eStone Age.

Abazingeli labaqoqi batshiya imidwebo emangalisayo emadwaleni.
Abalimi abalandelayo labo basebenzisa indawo.

IMatobo iphinde ixhumane lomlando wamaNdebele futhi isaqakathekile
ngokomoya lamuhla.
""",

        "matobo_rock":
            """
IMatobo ilobunengi obukhulu bemidwebo emadwaleni eSouthern Africa.

Imidwebo itholakala emigedeni lezindawo zokukhosela futhi itshengisa
abantu, izinyamazana, ukuzingela kanye lezinye izenzo zempilo yakudala.

Imidwebo iqakathekile njengobuciko futhi njengobufakazi bezinto zakudala.
""",

        "matobo_caves":
            """
Amadwala egranite eMatobo adala imigede lezindawo zokukhosela eziningi.

Lezindawo zavikela abantu futhi zanceda ukugcina imidwebo kanye
lezinto zakudala esimeni sezulu.

Yikho iMatobo igcina ubufakazi obunengi kangaka.
""",

        "matobo_spiritual":
            """
IMatobo yindawo engcwele ephilayo.

Izindawo zokukhulekela, amagquma angcwele, izindaba zomlomo,
ubudlelwano labokhokho, ukucela izulu kanye lenkolelo kaMwari
kusaqakathekile.

Ukuvikelwa kumele kuhloniphe izinto zakudala kanye lamasiko aphilayo.
""",

        "matobo_unesco":
            """
IMatobo Hills yabhaliswa kuUNESCO World Heritage List ngo-2003
ngaphansi kwemigomo (iii), (v) kanye (vi).

I-UNESCO iqaphela imidwebo emadwaleni, ubudlelwano phakathi kwabantu
lendawo kanye lokubaluleka kwayo ngokomoya.
""",

        "great_history":
            """
IGreat Zimbabwe yachuma phakathi kwekhulu le-11 lele-15.

Yaba yindawo enkulu yezombusazwe, ezomnotho lamasiko.

Izakhiwo zamatshe, ubuciko, inkomo kanye lokuhweba kutshengisa
umphakathi waseAfrica owawuphucukile.
""",

        "great_builders":
            """
IGreat Zimbabwe yakhiwa yimiphakathi yaseAfrica, ikakhulu okhokho
babantu abakhuluma isiShona.

Ubufakazi bezinto zakudala buyayiphika imibono yakudala eyayithi
indawo yakhiwa ngabantu bangaphandle.
""",

        "great_architecture":
            """
IGreat Zimbabwe idume ngemiduli eyakhiwe ngamatshe ngaphandle kwe-mortar.

Izingxenye ezinkulu yiHill Complex, Great Enclosure kanye leValley Ruins.

IGreat Enclosure ilodonga olukhulu, imizila kanye leConical Tower.
""",

        "great_birds":
            """
IZimbabwe Birds yizinyoni ezibazwe ngesoapstone ezatholakala
eGreat Zimbabwe.

Kungenzeka ukuthi zazilokubaluleka kwezokhokheli kumbe ngokomoya.

Inyoni yeZimbabwe yacina isiba luphawu olukhulu lwesizwe.
""",

        "great_trade":
            """
IGreat Zimbabwe yayixhumene lokuhweba okude.

Izinto ezatholakala khona zitshengisa ukuxhumana lezindlela zokuhweba
zaseAfrica kanye leIndian Ocean.

Lokhu kutshengisa ukuthi iGreat Zimbabwe yayingeyona indawo evalekileyo.
""",

        "great_unesco":
            """
IGreat Zimbabwe National Monument yabhaliswa kuUNESCO World Heritage
List ngo-1986 ngaphansi kwemigomo (i), (iii) kanye (vi).
""",

        "khami_history":
            """
IKhami yakhula ngemva kokwehla kweGreat Zimbabwe.

Yaba yinhloko yombuso weTorwa futhi yaqakatheka kakhulu kusukela
ngekhulu le-15 kusiya kwele-17.

Imele isigaba esalandela ekwakhiweni kwamatshe eZimbabwe.
""",

        "khami_torwa":
            """
IKhami ixhumene kakhulu lombuso weTorwa.

Ababusi beTorwa babelawula indawo enkulu yezombusazwe lezomnotho
eNingizimu-Ntshonalanga yeZimbabwe.

IKhami isinceda ukuqonda ukuguquka kwamandla kwezombusazwe.
""",

        "khami_architecture":
            """
IKhami idume ngamathala alemiduli yamatshe, retaining walls kanye
lamaphetheni amahle e-dry-stone.

Abakhi bayo bakha amapulatifomu ahambisana lendawo yemvelo.

Isiko lixhumene leGreat Zimbabwe kodwa iKhami isebenzisa amathala kakhulu.
""",

        "khami_trade":
            """
IKhami yayixhumene lokuhweba okuseduze kanye lokukude.

Ceramics kanye lezinto ezivela kwamanye amazwe zatholakala ngabavubukuli.

Lokhu kutshengisa ukuxhumana kweKhami lezindlela ezinkulu zokuhweba.
""",

        "khami_unesco":
            """
IKhami Ruins National Monument yabhaliswa kuUNESCO World Heritage
List ngo-1986 ngaphansi kwemigomo (iii) kanye (iv).
""",

        "conservation":
            """
I-ROBO GUIDE ikhuthaza ukuvikelwa kwamagugu kusenesikhathi.

Ungathinti imidwebo emadwaleni, ungagibeli imiduli yakudala,
ungasusi izinto zakudala futhi ungabhali ematsheni.

Hamba ngemizila evunyelweyo futhi uhloniphe izindawo ezingcwele.

Iprototype yeROBO GUIDE isebenzisa iIR sensor le-buzzer ukukhuthaza
izivakashi ukuthi zingaweli umngcele ovikelweyo.
""",

        "comparison":
            """
IGreat Zimbabwe leKhami zixhumene lesiko lokwakha ngamatshe
eZimbabwe kodwa azifanani.

IGreat Zimbabwe indala futhi idume ngemiduli emikhulu efana leGreat Enclosure.

IKhami yalandela futhi idume ngamathala, retaining walls kanye
ledecorative stonework.

Zombili zitshengisa amakhono okuwakha, ubukhokheli kanye lokuhweba.
""",

        "all_sites":
            """
Izindawo ezintathu zeROBO GUIDE zilandisa izindaba ezitshiyeneyo.

IMatobo yindawo yegranite edume ngemidwebo, imigede kanye lamasiko angcwele.

IGreat Zimbabwe yindawo enkulu yamatshe ehlotshaniswa lomlando wabantu
abakhuluma isiShona, ubukhokheli kanye lokuhweba.

IKhami yidolobho leTorwa elidume ngamathala lemiduli ehlotshisiwe.

Zonke ndawonye zitshengisa ubukhulu bamagugu amasiko eZimbabwe.
""",
    },


    "Shona": {

        "matobo_history":
            """
Matobo Hills inzvimbo yekare yetsika ine archaeological evidence
inodzokera kuStone Age.

Hunter-gatherer communities vakasiya rock paintings dzakawanda.
Mapoka evarimi akazotevera akashandisawo nzvimbo.

Matobo yakazobatanawo zvakanyanya nenhoroondo yeNdebele
uye ichiri spiritual landscape inokosha.
""",

        "matobo_rock":
            """
Matobo ine imwe yehuwandu hukuru hwe rock art muSouthern Africa.

Paintings dziri mumapako nemarock shelters uye dzinoratidza vanhu,
mhuka, kuvhima uye mamwe maitiro ehupenyu.

Dzine kukosha seart uye se archaeological evidence.
""",

        "matobo_caves":
            """
Granite landscape yeMatobo yakagadzira mapako nemarock shelters akawanda.

Aya akapa vanhu shelter uye akabatsira kuchengetedza paintings
nearchaeological deposits kubva kumamiriro ekunze.

Izvi ndizvo zvimwe zvinoita kuti Matobo ive neheritage yakawanda.
""",

        "matobo_spiritual":
            """
Matobo inzvimbo inoyera ichiri kurarama.

Shrines, sacred hills, oral traditions, madzitateguru,
rain-making practices uye Mwari religious tradition zvichiri kukosha.

Conservation inofanira kuremekedza physical heritage pamwe netsika
dzinorarama.
""",

        "matobo_unesco":
            """
Matobo Hills yakanyoreswa paUNESCO World Heritage List muna 2003
pasi pecriteria (iii), (v) ne(vi).

UNESCO inocherechedza rock art yayo, hukama hurefu pakati pevanhu
nenzvimbo uye continuing spiritual significance.
""",

        "great_history":
            """
Great Zimbabwe yakabudirira zvikuru pakati pezvinenge zana remakore
rechi11 nerechi15.

Yakava political, economic uye cultural centre huru.

Architecture, crafts, cattle wealth uye trade zvinoratidza
sophisticated African society.
""",

        "great_builders":
            """
Great Zimbabwe yakavakwa neAfrican communities, kunyanya
madzitateguru evanhu vanotaura Shona.

Archaeological evidence yemazuva ano inoramba pfungwa dzekare
dzaiti monument yakavakwa nevatorwa.
""",

        "great_architecture":
            """
Great Zimbabwe inozivikanwa nedry-stone masonry yakavakwa pasina mortar.

Nzvimbo huru dzinosanganisira Hill Complex, Great Enclosure
uye Valley Ruins.

Great Enclosure ine madziro makuru, passages uye Conical Tower.
""",

        "great_birds":
            """
Zimbabwe Birds ishiri dzakavezwa musoapstone dzakawanikwa
kuGreat Zimbabwe.

Dzaigona kunge dzine elite kana spiritual meaning.

Zimbabwe Bird yakazova chimwe chezviratidzo zvikuru zvenyika.
""",

        "great_trade":
            """
Great Zimbabwe yaive mu long-distance trade.

Archaeological finds dzinoratidza kubatana neAfrican uye Indian Ocean
exchange networks.

Izvi zvinoratidza kuti Great Zimbabwe yaive chikamu che wider economy.
""",

        "great_unesco":
            """
Great Zimbabwe National Monument yakanyoreswa paUNESCO World Heritage
List muna 1986 pasi pecriteria (i), (iii) ne(vi).
""",

        "khami_history":
            """
Khami yakasimukira mushure mekuderera kweGreat Zimbabwe.

Yakava capital yeTorwa state uye yaive yakakosha zvikuru kubva
muzana remakore rechi15 kusvika rechi17.

Inomiririra later stage yeZimbabwe stone-building tradition.
""",

        "khami_torwa":
            """
Khami yakabatana zvakanyanya neTorwa state.

Vatongi veTorwa vaive nepolitical neeconomic centre yakakosha
kumaodzanyemba-kumadokero kweZimbabwe.

Khami inobatsira kutsanangura kushanduka kwepolitical power.
""",

        "khami_architecture":
            """
Khami inozivikanwa nema stone-faced terraces, retaining walls
uye decorative dry-stone patterns.

Architecture yayo yakagadziridzwa kuti ienderane neterrain.

Ine hukama neGreat Zimbabwe asi terracing yakanyanya kuoneka paKhami.
""",

        "khami_trade":
            """
Khami yaive mu regional ne long-distance trade.

Imported ceramics nezvimwe prestige goods zvakawanikwa nearchaeologists.

Izvi zvinoratidza wider commercial connections.
""",

        "khami_unesco":
            """
Khami Ruins National Monument yakanyoreswa paUNESCO World Heritage
List muna 1986 pasi pecriteria (iii) ne(iv).
""",

        "conservation":
            """
ROBO GUIDE inokurudzira preventive heritage conservation.

Usabata rock art, usakwira ancient walls, usabvisa artifacts,
usakwenya matombo uye usapinda munzvimbo dzakarambidzwa.

Shandisa designated paths uye remekedza sacred places.

Physical ROBO GUIDE prototype inoshandisa IR sensor nebuzzer
kuyambira mushanyi kana ayambuka protected boundary.
""",

        "comparison":
            """
Great Zimbabwe neKhami zviri muZimbabwe stone-building tradition
asi hazvina kufanana.

Great Zimbabwe yakatanga uye inozivikanwa nemadziro makuru
akaita seGreat Enclosure.

Khami yakazotevera uye inozivikanwa nema terraces,
retaining walls uye decorative stonework.

Dzose dzinoratidza skilled architecture, political organization
uye long-distance trade.
""",

        "all_sites":
            """
Nzvimbo nhatu dzeROBO GUIDE dzinotaura nyaya dzakasiyana
asi dzinobatsirana.

Matobo inzvimbo yegranite ine rock art, archaeology, mapako
uye sacred traditions.

Great Zimbabwe iguta guru rematombo rakabatana neShona history,
statecraft uye trade.

Khami iguta reTorwa rakazotevera rinozivikanwa nema terraces
uye decorative masonry.

Pamwe chete dzinoratidza hupfumi hwenhaka yeZimbabwe.
""",
    },
}


# ------------------------------------------------------------
# HELPER FUNCTIONS
# ------------------------------------------------------------

def tr(key):

    return UI[
        st.session_state.lang
    ][key]


def go(page):

    st.session_state.page = page

    st.rerun()


def reset_quiz():

    st.session_state.quiz_index = 0

    st.session_state.quiz_score = 0

    st.session_state.quiz_points = 0

    st.session_state.quiz_answered = False

    st.session_state.quiz_feedback = None

    st.session_state.quiz_finished = False


def normalize(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    return text.strip()


def contains_any(text, words):

    return any(
        word in text
        for word in words
    )


def assistant_answer(question):

    q = normalize(question)

    lang = st.session_state.lang

    kb = KB[lang]


    # --------------------------------------------------------
    # COMPARISON QUESTIONS
    # --------------------------------------------------------

    comparison_words = [

        "compare",
        "comparison",
        "difference",
        "different",
        "similar",
        "similarity",

        "qhathanisa",
        "umehluko",
        "fanana",

        "enzanisa",
        "musiyano",
        "zvakafanana",
    ]


    if contains_any(
        q,
        comparison_words
    ):

        great = (
            "great zimbabwe" in q
            or
            "great" in q
        )

        khami = (
            "khami" in q
        )

        matobo = (
            "matobo" in q
        )


        if great and khami and not matobo:

            return kb[
                "comparison"
            ]


        if (
            sum(
                [
                    great,
                    khami,
                    matobo
                ]
            )
            >= 2
        ):

            return kb[
                "all_sites"
            ]


    # --------------------------------------------------------
    # CONSERVATION
    # --------------------------------------------------------

    conservation_words = [

        "protect",
        "protection",
        "conservation",
        "conserve",
        "preserve",
        "preservation",
        "damage",
        "touch",
        "visitor",
        "boundary",
        "sensor",
        "buzzer",
        "warning",
        "ir sensor",

        "vikela",
        "ukuvikela",
        "thinta",
        "umngcele",

        "chengetedza",
        "kuchengetedza",
        "bata",
        "muganhu",
        "yambiro",
    ]


    if contains_any(
        q,
        conservation_words
    ):

        return kb[
            "conservation"
        ]


    # --------------------------------------------------------
    # MATOBO
    # --------------------------------------------------------

    matobo_trigger = (

        "matobo" in q

        or

        contains_any(
            q,
            [
                "rock art",
                "rock painting",
                "rock paintings",
                "cave painting",
                "cave paintings",
                "imidwebo",
                "mapako",
                "imigede",
            ]
        )
    )


    if matobo_trigger:

        if contains_any(
            q,
            [
                "unesco",
                "world heritage",
                "inscribed",
                "inscription",
                "criteria",
                "bhaliswa",
                "nyoreswa",
            ]
        ):

            return kb[
                "matobo_unesco"
            ]


        if contains_any(
            q,
            [
                "cave",
                "caves",
                "shelter",
                "shelters",
                "umgede",
                "imigede",
                "pako",
                "mapako",
            ]
        ):

            return kb[
                "matobo_caves"
            ]


        if contains_any(
            q,
            [
                "rock art",
                "painting",
                "paintings",
                "imidwebo",
                "umdwebo",
                "mifananidzo",
            ]
        ):

            return kb[
                "matobo_rock"
            ]


        if contains_any(
            q,
            [
                "sacred",
                "spiritual",
                "spirit",
                "religion",
                "mwari",
                "shrine",
                "ancestor",
                "ancestors",

                "okungcwele",
                "amadlozi",

                "mweya",
                "madzitateguru",
                "inoyera",
            ]
        ):

            return kb[
                "matobo_spiritual"
            ]


        return kb[
            "matobo_history"
        ]


    # --------------------------------------------------------
    # GREAT ZIMBABWE
    # --------------------------------------------------------

    great_trigger = contains_any(

        q,

        [
            "great zimbabwe",
            "great enclosure",
            "conical tower",
            "zimbabwe bird",
            "zimbabwe birds",
        ]
    )


    if great_trigger:

        if contains_any(
            q,
            [
                "who built",
                "built by",
                "builder",
                "builders",
                "build",

                "ngubani",
                "owakha",

                "ndiani",
                "akavaka",
                "vakavaka",
            ]
        ):

            return kb[
                "great_builders"
            ]


        if contains_any(
            q,
            [
                "bird",
                "birds",
                "inyoni",
                "izinyoni",
                "shiri",
            ]
        ):

            return kb[
                "great_birds"
            ]


        if contains_any(
            q,
            [
                "trade",
                "trading",
                "gold",
                "import",
                "imports",
                "commerce",

                "ukuhweba",

                "kutengeserana",
            ]
        ):

            return kb[
                "great_trade"
            ]


        if contains_any(
            q,
            [
                "architecture",
                "wall",
                "walls",
                "enclosure",
                "tower",
                "stone",
                "masonry",
                "mortar",

                "udonga",
                "imiduli",
                "izakhiwo",

                "madziro",
                "zvivakwa",
                "matombo",
            ]
        ):

            return kb[
                "great_architecture"
            ]


        if contains_any(
            q,
            [
                "unesco",
                "world heritage",
                "inscribed",
                "criteria",
                "bhaliswa",
                "nyoreswa",
            ]
        ):

            return kb[
                "great_unesco"
            ]


        return kb[
            "great_history"
        ]


    # --------------------------------------------------------
    # KHAMI
    # --------------------------------------------------------

    if (
        "khami" in q
        or
        "torwa" in q
    ):

        if contains_any(
            q,
            [
                "torwa",
                "state",
                "kingdom",
                "ruler",
                "rulers",
                "government",
                "umbuso",
                "hurumende",
            ]
        ):

            return kb[
                "khami_torwa"
            ]


        if contains_any(
            q,
            [
                "trade",
                "trading",
                "ceramic",
                "ceramics",
                "import",
                "imports",

                "ukuhweba",

                "kutengeserana",
            ]
        ):

            return kb[
                "khami_trade"
            ]


        if contains_any(
            q,
            [
                "terrace",
                "terraces",
                "architecture",
                "wall",
                "walls",
                "decorative",
                "stonework",
                "masonry",

                "amathala",
                "imiduli",
                "izakhiwo",

                "madziro",
                "matombo",
            ]
        ):

            return kb[
                "khami_architecture"
            ]


        if contains_any(
            q,
            [
                "unesco",
                "world heritage",
                "inscribed",
                "criteria",
                "bhaliswa",
                "nyoreswa",
            ]
        ):

            return kb[
                "khami_unesco"
            ]


        return kb[
            "khami_history"
        ]


    # --------------------------------------------------------
    # GENERAL TOPIC ROUTING
    # --------------------------------------------------------

    if contains_any(
        q,
        [
            "who built",
            "builder",
            "builders",
            "built by",
            "ngubani owakha",
            "ndiani akavaka",
        ]
    ):

        return kb[
            "great_builders"
        ]


    if contains_any(
        q,
        [
            "zimbabwe bird",
            "birds",
            "bird",
            "izinyoni",
            "inyoni",
            "shiri",
        ]
    ):

        return kb[
            "great_birds"
        ]


    if contains_any(
        q,
        [
            "torwa",
            "terrace",
            "terraces",
            "amathala",
        ]
    ):

        return (
            kb["khami_torwa"]
            +
            "\n\n"
            +
            kb["khami_architecture"]
        )


    if contains_any(
        q,
        [
            "rock art",
            "rock painting",
            "paintings",
            "cave",
            "caves",
            "imidwebo",
            "imigede",
            "mapako",
        ]
    ):

        return kb[
            "matobo_rock"
        ]


    if contains_any(
        q,
        [
            "trade",
            "trading",
            "commerce",
            "kutengeserana",
            "ukuhweba",
        ]
    ):

        return (
            kb["great_trade"]
            +
            "\n\n"
            +
            kb["khami_trade"]
        )


    if contains_any(
        q,
        [
            "unesco",
            "world heritage",
        ]
    ):

        return (
            kb["great_unesco"]
            +
            "\n\n"
            +
            kb["khami_unesco"]
            +
            "\n\n"
            +
            kb["matobo_unesco"]
        )


    if contains_any(
        q,
        [
            "three sites",
            "all sites",
            "heritage sites",
            "zimbabwe heritage",

            "izindawo",
            "amagugu",

            "nzvimbo",
            "nhaka",
        ]
    ):

        return kb[
            "all_sites"
        ]


    return tr(
        "no_answer"
    )


# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

with st.sidebar:

    st.markdown(
        f"""
        <div class="brand">

            <div class="brand-logo">
                🤖🗿
            </div>

            <h2>
                ROBO GUIDE
            </h2>

            <p>
                {tr("tagline")}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    previous_language = (
        st.session_state.lang
    )


    selected_language = st.selectbox(

        tr(
            "language"
        ),

        [
            "English",
            "isiNdebele",
            "Shona"
        ],

        index=
            [
                "English",
                "isiNdebele",
                "Shona"
            ].index(
                previous_language
            )
    )


    if (
        selected_language
        !=
        previous_language
    ):

        st.session_state.lang = (
            selected_language
        )

        reset_quiz()

        st.session_state.chat = []

        st.rerun()


    st.markdown(
        "### "
        +
        tr(
            "navigation"
        )
    )


    NAVIGATION = [

        (
            "Home",
            "🏠",
            tr("home")
        ),

        (
            "Matobo Hills",
            "🪨",
            tr("matobo")
        ),

        (
            "Great Zimbabwe",
            "🏛️",
            tr("great")
        ),

        (
            "Khami Ruins",
            "🧱",
            tr("khami")
        ),

        (
            "Heritage Challenge",
            "🏆",
            tr("quiz")
        ),

        (
            "Heritage Assistant",
            "💬",
            tr("assistant")
        ),

        (
            "Robot + Website",
            "🤖",
            tr("prototype")
        ),
    ]


    for (
        target,
        icon,
        label
    ) in NAVIGATION:

        active = (
            st.session_state.page
            ==
            target
        )


        if st.button(

            f"{icon}  {label}",

            key=
                f"nav_{target}",

            use_container_width=True,

            type=
                "primary"
                if active
                else
                "secondary"
        ):

            go(
                target
            )


    st.markdown(
        "---"
    )


    st.caption(
        "🏆 WRO 2026 Zimbabwe National Finals"
    )

    st.caption(
        "🤖 Theme: Robots Meet Culture"
    )

    st.caption(
        "🇿🇼 Learn • Respect • Protect"
    )


# ------------------------------------------------------------
# HOME PAGE
# ------------------------------------------------------------

def home_page():

    st.markdown(

        f"""
        <div class="hero">

            <div class="kicker">
                {tr("tagline")}
            </div>

            <h1>
                ROBO GUIDE
            </h1>

            <h2>
                {tr("hero")}
            </h2>

            <p>
                {tr("hero_text")}
            </p>

            <div>

                <span class="badge">
                    🌍 English
                </span>

                <span class="badge">
                    🗣️ isiNdebele
                </span>

                <span class="badge">
                    💬 Shona
                </span>

                <span class="badge">
                    📡 IR Protection
                </span>

                <span class="badge">
                    🔔 Smart Warning
                </span>

                <span class="badge">
                    🏆 Gamified Learning
                </span>

            </div>

        </div>
        """,

        unsafe_allow_html=True
    )


    col1, col2, col3 = (
        st.columns(
            3
        )
    )


    with col1:

        st.markdown(

            """
            <div class="stat">

                <div class="stat-number">
                    3
                </div>

                <div class="stat-label">
                    Zimbabwe heritage experiences
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    with col2:

        st.markdown(

            """
            <div class="stat">

                <div class="stat-number">
                    3
                </div>

                <div class="stat-label">
                    Visitor languages
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    with col3:

        st.markdown(

            """
            <div class="stat">

                <div class="stat-number">
                    1
                </div>

                <div class="stat-label">
                    Connected robot + digital journey
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    st.markdown(

        f"""
        <div class="section-title">
            {tr("explore")}
        </div>

        <div class="section-sub">
            {tr("explore_sub")}
        </div>
        """,

        unsafe_allow_html=True
    )


    cards = st.columns(
        3
    )


    summary = {

        "English": {

            "Matobo Hills":
                "Rock art • sacred landscape • caves • granite hills",

            "Great Zimbabwe":
                "Great Enclosure • Zimbabwe Birds • stone architecture • trade",

            "Khami Ruins":
                "Terraces • Torwa history • decorative stonework • trade",
        },

        "isiNdebele": {

            "Matobo Hills":
                "Imidwebo emadwaleni • izindawo ezingcwele • imigede • amagquma",

            "Great Zimbabwe":
                "Great Enclosure • Zimbabwe Birds • izakhiwo zamatshe • ukuhweba",

            "Khami Ruins":
                "Amathala • umlando weTorwa • ubuciko bamatshe • ukuhweba",
        },

        "Shona": {

            "Matobo Hills":
                "Rock art • nzvimbo dzinoyera • mapako • zvikomo zvegranite",

            "Great Zimbabwe":
                "Great Enclosure • Zimbabwe Birds • stone architecture • trade",

            "Khami Ruins":
                "Terraces • Torwa history • decorative stonework • trade",
        },
    }


    for column, site_key in zip(

        cards,

        [
            "Matobo Hills",
            "Great Zimbabwe",
            "Khami Ruins",
        ]
    ):

        site = SITES[
            site_key
        ][
            st.session_state.lang
        ]


        with column:

            st.markdown(

                f"""
                <div class="card">

                    <div class="site-icon">
                        {SITES[site_key]["emoji"]}
                    </div>

                    <h3>
                        {site["name"]}
                    </h3>

                    <p>
                        {
                            summary[
                                st.session_state.lang
                            ][
                                site_key
                            ]
                        }
                    </p>

                    <p>
                        <b>UNESCO:</b>
                        {site["inscribed"]}
                        •
                        {site["criteria"]}
                    </p>

                </div>
                """,

                unsafe_allow_html=True
            )


            if st.button(

                f'{tr("open")} →',

                key=
                    f"open_{site_key}",

                use_container_width=True
            ):

                go(
                    site_key
                )


    st.markdown(

        f"""
        <div class="section-title">
            {tr("why")}
        </div>

        <div class="section-sub">
            {tr("why_text")}
        </div>
        """,

        unsafe_allow_html=True
    )


    c1, c2, c3, c4 = (
        st.columns(
            4
        )
    )


    mini_cards = [

        (
            c1,
            "📚",
            tr("learn"),
            tr("learn_text")
        ),

        (
            c2,
            "🎮",
            tr("play"),
            tr("play_text")
        ),

        (
            c3,
            "🛡️",
            tr("protect"),
            tr("protect_text")
        ),

        (
            c4,
            "🔗",
            tr("connect"),
            tr("connect_text")
        ),
    ]


    for (
        column,
        icon,
        title,
        text
    ) in mini_cards:

        with column:

            st.markdown(

                f"""
                <div class="card">

                    <div class="site-icon">
                        {icon}
                    </div>

                    <h4>
                        {title}
                    </h4>

                    <p>
                        {text}
                    </p>

                </div>
                """,

                unsafe_allow_html=True
            )


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    a, b, c = (
        st.columns(
            3
        )
    )


    with a:

        if st.button(

            "🏆 "
            +
            tr("challenge"),

            type="primary",

            use_container_width=True
        ):

            go(
                "Heritage Challenge"
            )


    with b:

        if st.button(

            "💬 "
            +
            tr("ask"),

            use_container_width=True
        ):

            go(
                "Heritage Assistant"
            )


    with c:

        if st.button(

            "🤖 "
            +
            tr("robot"),

            use_container_width=True
        ):

            go(
                "Robot + Website"
            )


# ------------------------------------------------------------
# HERITAGE SITE PAGE
# ------------------------------------------------------------

def site_page(
    site_key
):

    site = SITES[
        site_key
    ][
        st.session_state.lang
    ]


    st.markdown(

        f"""
        <div class="hero">

            <div class="kicker">
                ROBO GUIDE • Zimbabwe Heritage
            </div>

            <h1 style="font-size:3.4rem">

                {
                    SITES[
                        site_key
                    ]["emoji"]
                }

                {site["name"]}

            </h1>

            <p>
                {site["subtitle"]}
            </p>

        </div>
        """,

        unsafe_allow_html=True
    )


    col1, col2, col3 = (
        st.columns(
            3
        )
    )


    with col1:

        st.markdown(

            f"""
            <div class="stat">

                <div class="stat-number">
                    {site["inscribed"]}
                </div>

                <div class="stat-label">
                    {tr("inscription")}
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    with col2:

        st.markdown(

            f"""
            <div class="stat">

                <div class="stat-number">
                    {site["criteria"]}
                </div>

                <div class="stat-label">
                    {tr("criteria")}
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    with col3:

        st.markdown(

            f"""
            <div class="stat">

                <div
                    class="stat-number"
                    style="font-size:16px"
                >
                    {site["location"]}
                </div>

                <div class="stat-label">
                    {tr("location")}
                </div>

            </div>
            """,

            unsafe_allow_html=True
        )


    left, right = (
        st.columns(
            [
                1.25,
                1
            ]
        )
    )


    with left:

        st.markdown(
            "### 📜 "
            +
            tr("history")
        )

        st.write(
            site[
                "history"
            ]
        )


        st.markdown(
            "### 👥 "
            +
            tr("culture")
        )

        st.write(
            site[
                "culture"
            ]
        )


    with right:

        st.markdown(
            "### ✨ "
            +
            tr("features")
        )


        for item in site[
            "features"
        ]:

            st.markdown(
                "◆ "
                +
                item
            )


    st.markdown(

        f"""
        <div class="unesco">

            <b>
                🌐 {tr("unesco")}
            </b>

            <br><br>

            {
                site["unesco"]
            }

        </div>
        """,

        unsafe_allow_html=True
    )


    p1, p2 = (
        st.columns(
            2
        )
    )


    with p1:

        st.markdown(
            "### 🛡️ "
            +
            tr("protection")
        )


        for rule in site[
            "protection"
        ]:

            st.markdown(

                f"""
                <div class="greenbox">
                    ✓ {rule}
                </div>
                """,

                unsafe_allow_html=True
            )


    with p2:

        st.markdown(
            "### 💡 "
            +
            tr("facts")
        )


        for fact in site[
            "facts"
        ]:

            st.markdown(

                f"""
                <div class="goldbox">
                    ★ {fact}
                </div>
                """,

                unsafe_allow_html=True
            )


    st.markdown(
        "### 🌟 "
        +
        tr("significance")
    )


    st.info(
        site[
            "significance"
        ],
        icon="🌍"
    )


    c1, c2, c3 = (
        st.columns(
            3
        )
    )


    with c1:

        if st.button(

            tr("back"),

            use_container_width=True
        ):

            go(
                "Home"
            )


    with c2:

        if st.button(

            "🏆 "
            +
            tr("challenge"),

            use_container_width=True
        ):

            go(
                "Heritage Challenge"
            )


    with c3:

        if st.button(

            "💬 "
            +
            tr("ask"),

            use_container_width=True
        ):

            go(
                "Heritage Assistant"
            )


# ------------------------------------------------------------
# HERITAGE QUIZ PAGE
# ------------------------------------------------------------

def quiz_page():

    questions = QUIZ[
        st.session_state.lang
    ]


    total = len(
        questions
    )


    st.markdown(

        f"""
        <div class="hero">

            <div class="kicker">
                ROBO GUIDE • Learn By Playing
            </div>

            <h1 style="font-size:3.3rem">
                🏆 {tr("quiz_title")}
            </h1>

            <p>
                {tr("quiz_intro")}
            </p>

        </div>
        """,

        unsafe_allow_html=True
    )


    if (
        st.session_state.quiz_finished
    ):

        percentage = round(

            (
                st.session_state.quiz_score
                /
                total
            )
            *
            100
        )


        guardian = (
            percentage
            >=
            80
        )


        achievement_title = (

            tr("guardian")

            if guardian

            else

            tr("guide")
        )


        achievement_desc = (

            tr("guardian_desc")

            if guardian

            else

            tr("guide_desc")
        )


        icon = (

            "🛡️🏆"

            if guardian

            else

            "🧭🏅"
        )


        st.markdown(

            f"""
            <div class="achievement">

                <div class="achievement-icon">
                    {icon}
                </div>

                <div
                    style="
                        text-transform:uppercase;
                        font-size:13px;
                        letter-spacing:2px;
                    "
                >
                    {tr("achievement")}
                </div>

                <h2>
                    {achievement_title}
                </h2>

                <p>
                    {achievement_desc}
                </p>

                <h3>

                    {
                        st.session_state.quiz_score
                    }
                    /
                    {total}

                    •

                    {percentage}%

                    •

                    {
                        st.session_state.quiz_points
                    }

                    Heritage Points

                </h3>

            </div>
            """,

            unsafe_allow_html=True
        )


        st.balloons()


        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )


        col1, col2 = (
            st.columns(
                2
            )
        )


        with col1:

            if st.button(

                "🔁 "
                +
                tr("replay"),

                type="primary",

                use_container_width=True
            ):

                reset_quiz()

                st.rerun()


        with col2:

            if st.button(

                "📚 "
                +
                tr("explore"),

                use_container_width=True
            ):

                go(
                    "Home"
                )


        return


    index = (
        st.session_state.quiz_index
    )


    question = questions[
        index
    ]


    st.progress(

        index
        /
        total
    )


    m1, m2, m3 = (
        st.columns(
            3
        )
    )


    m1.metric(

        tr("question"),

        f"{index + 1}/{total}"
    )


    m2.metric(

        tr("score"),

        f'{st.session_state.quiz_score}/{total}'
    )


    m3.metric(

        tr("points"),

        st.session_state.quiz_points
    )


    st.markdown(

        '<div class="quizbox">',

        unsafe_allow_html=True
    )


    st.markdown(

        f"""
        ### {index + 1}. {question["q"]}
        """
    )


    if (
        st.session_state.lang
        ==
        "English"
    ):

        choose_label = (
            "Choose one answer"
        )


    elif (
        st.session_state.lang
        ==
        "isiNdebele"
    ):

        choose_label = (
            "Khetha impendulo eyodwa"
        )


    else:

        choose_label = (
            "Sarudza mhinduro imwe"
        )


    selected = st.radio(

        choose_label,

        options=
            list(
                range(
                    len(
                        question[
                            "options"
                        ]
                    )
                )
            ),

        format_func=
            lambda x:
                question[
                    "options"
                ][x],

        index=None,

        key=
            f'quiz_{
                st.session_state.lang
            }_{index}',

        disabled=
            st.session_state.quiz_answered
    )


    if not (
        st.session_state.quiz_answered
    ):

        if st.button(

            "✅ "
            +
            tr("submit"),

            type="primary",

            use_container_width=True,

            disabled=
                selected
                is
                None
        ):

            st.session_state.quiz_answered = (
                True
            )


            if (
                selected
                ==
                question[
                    "answer"
                ]
            ):

                st.session_state.quiz_score += 1

                st.session_state.quiz_points += 100

                st.session_state.quiz_feedback = (
                    "correct"
                )


            else:

                # Give some participation points
                # to keep the challenge positive and gamified.

                st.session_state.quiz_points += 20

                st.session_state.quiz_feedback = (
                    "incorrect"
                )


            st.rerun()


    else:

        if (
            st.session_state.quiz_feedback
            ==
            "correct"
        ):

            st.success(

                "🎉 "
                +
                tr("correct")
                +
                "  +100 Heritage Points"
                +
                "\n\n"
                +
                question["why"]
            )


        else:

            correct_answer = (

                question[
                    "options"
                ][
                    question[
                        "answer"
                    ]
                ]
            )


            st.error(

                "💡 "
                +
                tr("incorrect")
                +
                "  +20 Participation Points"
                +
                "\n\n"
                +
                "**✓ "
                +
                correct_answer
                +
                "**"
                +
                "\n\n"
                +
                question["why"]
            )


        if (
            index
            ==
            total - 1
        ):

            next_text = (
                tr("finish")
            )


        else:

            next_text = (
                tr("next")
            )


        if st.button(

            next_text,

            type="primary",

            use_container_width=True
        ):

            if (
                index
                ==
                total - 1
            ):

                st.session_state.quiz_finished = (
                    True
                )


            else:

                st.session_state.quiz_index += 1

                st.session_state.quiz_answered = (
                    False
                )

                st.session_state.quiz_feedback = (
                    None
                )


            st.rerun()


    st.markdown(

        "</div>",

        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# HERITAGE ASSISTANT PAGE
# ------------------------------------------------------------

def assistant_page():

    st.markdown(

        f"""
        <div class="hero">

            <div class="kicker">
                ROBO GUIDE • Free Rule-Based Heritage Intelligence
            </div>

            <h1 style="font-size:3.2rem">
                💬 {tr("assistant_title")}
            </h1>

            <p>
                {tr("assistant_intro")}
            </p>

        </div>
        """,

        unsafe_allow_html=True
    )


    SUGGESTIONS = {

        "English": [

            "Who built Great Zimbabwe?",

            "Why are Matobo caves important?",

            "Tell me about rock art at Matobo.",

            "What are the Zimbabwe Birds?",

            "What is the Great Enclosure?",

            "Tell me about the Torwa state at Khami.",

            "Why does Khami have terraces?",

            "How did Great Zimbabwe trade?",

            "Compare Great Zimbabwe and Khami.",

            "How should visitors protect rock art?",

            "When did Khami become important?",

            "What does UNESCO recognize at Matobo?",
        ],


        "isiNdebele": [

            "Ngubani owakha iGreat Zimbabwe?",

            "Kungani imigede yeMatobo iqakathekile?",

            "Ngitshele ngemidwebo yeMatobo.",

            "Yini iZimbabwe Birds?",

            "Yini iGreat Enclosure?",

            "Ngitshele ngombuso weTorwa eKhami.",

            "Kungani iKhami ilamathala?",

            "IGreat Zimbabwe yayihweba njani?",

            "Qhathanisa iGreat Zimbabwe leKhami.",

            "Izivakashi zingayivikela njani imidwebo?",

            "IKhami yaba yiqakathekile nini?",

            "IUNESCO iqaphelani eMatobo?",
        ],


        "Shona": [

            "Ndiani akavaka Great Zimbabwe?",

            "Sei mapako eMatobo akakosha?",

            "Ndiudze nezve rock art yeMatobo.",

            "Zimbabwe Birds chii?",

            "Great Enclosure chii?",

            "Ndiudze nezveTorwa paKhami.",

            "Sei Khami iine terraces?",

            "Great Zimbabwe yaitengesa sei?",

            "Enzanisa Great Zimbabwe neKhami.",

            "Vashanyi vangachengetedza sei rock art?",

            "Khami yakatanga kukosha riini?",

            "UNESCO inocherechedzei paMatobo?",
        ],
    }


    st.markdown(

        "**"
        +
        tr("try_question")
        +
        ":**"
    )


    suggestion_columns = (
        st.columns(
            3
        )
    )


    for i, prompt in enumerate(

        SUGGESTIONS[
            st.session_state.lang
        ]
    ):

        column = (
            suggestion_columns[
                i % 3
            ]
        )


        with column:

            if st.button(

                prompt,

                key=
                    f"suggestion_{i}",

                use_container_width=True
            ):

                reply = (
                    assistant_answer(
                        prompt
                    )
                )


                st.session_state.chat.append(

                    (
                        prompt,
                        reply
                    )
                )


                st.rerun()


    st.markdown(
        "---"
    )


    # Only display latest eight exchanges
    # to keep the page readable.

    for (
        question,
        answer
    ) in st.session_state.chat[-8:]:


        st.markdown(

            f"""
            <div class="chat-user">

                <b>
                    👤 Visitor
                </b>

                <br>

                {escape(question)}

            </div>
            """,

            unsafe_allow_html=True
        )


        st.markdown(

            f"""
            <div class="chat-bot">

                <b>
                    🤖 ROBO GUIDE
                </b>

                <br>

                {
                    escape(
                        answer
                    ).replace(
                        chr(10),
                        "<br>"
                    )
                }

            </div>
            """,

            unsafe_allow_html=True
        )


    with st.form(

        "heritage_assistant_form",

        clear_on_submit=True
    ):

        user_question = (
            st.text_input(

                "Question",

                placeholder=
                    tr(
                        "assistant_placeholder"
                    ),

                label_visibility=
                    "collapsed"
            )
        )


        send = (
            st.form_submit_button(

                "🤖 "
                +
                tr("ask"),

                type="primary",

                use_container_width=True
            )
        )


        if (
            send
            and
            user_question.strip()
        ):

            reply = (
                assistant_answer(
                    user_question
                )
            )


            st.session_state.chat.append(

                (
                    user_question.strip(),
                    reply
                )
            )


            st.rerun()


    if (
        st.session_state.chat
    ):

        if st.button(

            "🧹 "
            +
            tr("clear")
        ):

            st.session_state.chat = []

            st.rerun()


    st.caption(
        "✅ No paid API • ✅ No API key • ✅ Rule-based knowledge engine contained entirely inside app.py"
    )


# ------------------------------------------------------------
# ROBOT + WEBSITE PAGE
# ------------------------------------------------------------

def prototype_page():

    st.markdown(

        f"""
        <div class="hero">

            <div class="kicker">
                ROBO GUIDE • Physical + Digital Heritage System
            </div>

            <h1 style="font-size:3.2rem">
                🤖 {tr("prototype_title")}
            </h1>

            <p>
                {tr("prototype_intro")}
            </p>

        </div>
        """,

        unsafe_allow_html=True
    )


    st.markdown(

        "### 🔄 "
        +
        tr("flow")
    )


    FLOW = {

        "English":
            """
Visitor approaches the ROBO GUIDE exhibit
→ OLED gives multilingual heritage education
→ visitor scans the QR code
→ ROBO GUIDE website opens
→ visitor explores detailed heritage content
→ IR sensor watches the protected boundary
→ buzzer warns if the boundary is crossed
→ laptop records boundary events
→ dashboard identifies patterns and trends
→ heritage managers can improve visitor education and protection.
""",

        "isiNdebele":
            """
Isivakashi siyasondela kuROBO GUIDE
→ OLED inika ulwazi ngezindimi ezintathu
→ isivakashi siskena iQR
→ iwebhusayithi yeROBO GUIDE iyavuleka
→ isivakashi sihlola ulwazi olujulileyo
→ IR sensor iqapha umngcele ovikelweyo
→ buzzer iyaxwayisa nxa umngcele uweqiwa
→ ikhompyutha iyarekhoda izehlakalo
→ ideshibhodi itshengisa imikhuba
→ abaphathi bangathuthukisa imfundo lokuvikela.
""",

        "Shona":
            """
Mushanyi anosvika paROBO GUIDE
→ OLED inopa multilingual heritage education
→ mushanyi anoskena QR
→ ROBO GUIDE webhusaiti inovhurika
→ mushanyi anoongorora detailed heritage content
→ IR sensor inotarisa protected boundary
→ buzzer inoyambira kana muganhu wayambukwa
→ laptop inorekodha boundary events
→ dashboard inoratidza patterns nema trends
→ heritage managers vanogona kuvandudza visitor education nekuchengetedza.
""",
    }


    st.markdown(

        f"""
        <div class="unesco">

            {
                FLOW[
                    st.session_state.lang
                ]
            }

        </div>
        """,

        unsafe_allow_html=True
    )


    FEATURES = [

        (
            "🖥️",
            tr("oled"),
            tr("oled_text")
        ),

        (
            "📱",
            tr("qr"),
            tr("qr_text")
        ),

        (
            "🧭",
            tr("visitor"),
            tr("visitor_text")
        ),

        (
            "📡",
            tr("ir"),
            tr("ir_text")
        ),

        (
            "🔔",
            tr("buzzer"),
            tr("buzzer_text")
        ),

        (
            "📊",
            tr("dashboard"),
            tr("dashboard_text")
        ),
    ]


    for start in range(

        0,
        len(FEATURES),
        2
    ):

        col1, col2 = (
            st.columns(
                2
            )
        )


        pair = FEATURES[
            start:
            start + 2
        ]


        for column, feature in zip(

            [
                col1,
                col2
            ],

            pair
        ):

            icon, title, text = (
                feature
            )


            with column:

                st.markdown(

                    f"""
                    <div class="card">

                        <div class="site-icon">
                            {icon}
                        </div>

                        <h3>
                            {title}
                        </h3>

                        <p>
                            {text}
                        </p>

                    </div>
                    """,

                    unsafe_allow_html=True
                )


        st.markdown(

            "<br>",

            unsafe_allow_html=True
        )


    DASHBOARD_TITLE = {

        "English":
            "What the ROBO GUIDE laptop dashboard can analyse",

        "isiNdebele":
            "Okungahlaziywa yideshibhodi yeROBO GUIDE",

        "Shona":
            "Zvinogona kuongororwa neROBO GUIDE laptop dashboard",
    }


    st.markdown(

        "### 📈 "
        +
        DASHBOARD_TITLE[
            st.session_state.lang
        ]
    )


    LABELS = {

        "English": [

            "Boundary crossings today",

            "Busiest warning hour",

            "Repeat warnings",

            "7-day crossing trend",
        ],

        "isiNdebele": [

            "Ukweqa umngcele lamuhla",

            "Ihora lezixwayiso ezinengi",

            "Izixwayiso eziphindayo",

            "Umkhuba wezinsuku eziyisikhombisa",
        ],

        "Shona": [

            "Boundary crossings nhasi",

            "Nguva ine warnings dzakawanda",

            "Repeat warnings",

            "7-day crossing trend",
        ],
    }


    d1, d2, d3, d4 = (
        st.columns(
            4
        )
    )


    values = [

        "12",

        "13:00",

        "3",

        "↓ 18%",
    ]


    for (
        column,
        label,
        value
    ) in zip(

        [
            d1,
            d2,
            d3,
            d4
        ],

        LABELS[
            st.session_state.lang
        ],

        values
    ):

        with column:

            st.metric(

                label,

                value
            )


    EXPLANATION = {

        "English":
            """
WRO demonstration message: the IR sensor does not replace heritage staff.
It acts as a low-cost educational and preventive layer.

The physical prototype can warn a visitor immediately, while the management
dashboard can convert repeated boundary events into useful information.

For example, if most warnings occur between 13:00 and 14:00, managers could
increase visitor education, change signs, reposition a barrier or provide
additional supervision during that period.
""",

        "isiNdebele":
            """
Umlayezo weWRO: iIR sensor ayithathi indawo yabasebenzi bamagugu.
Iyindlela engabizi kakhulu yokufundisa kanye lokuvikela.

Iprototype ingaxwayisa isivakashi masinyane, kuthi ideshibhodi
iguqule izehlakalo zokweqa umngcele zibe lulwazi olunceda abaphathi.

Nxa izixwayiso ezinengi zenzeka ngesikhathi esithile, abaphathi bangangeza
izibonakaliso, imfundo, izithiyo kumbe ukuqapha ngalesosikhathi.
""",

        "Shona":
            """
Mharidzo yeWRO: IR sensor haitsivi heritage staff.
Iyo low-cost educational uye preventive layer.

Prototype inogona kuyambira mushanyi pakarepo, uku dashboard
ichishandura repeated boundary events kuita useful management information.

Kana warnings dzakawanda dzichiitika panguva imwe chete zuva rega rega,
mamaneja vanogona kuwedzera visitor education, signage, barriers
kana supervision panguva iyoyo.
""",
    }


    st.info(

        EXPLANATION[
            st.session_state.lang
        ],

        icon="💡"
    )


    st.markdown(
        "### 🧠 ROBO GUIDE System Logic"
    )


    system_col1, system_col2 = (
        st.columns(
            2
        )
    )


    with system_col1:

        st.markdown(
            """
            <div class="greenbox">

            <b>Physical ROBO GUIDE</b><br><br>

            👁 IR sensor detects visitor movement<br><br>

            🔔 Buzzer provides immediate warning<br><br>

            🖥 OLED provides multilingual education<br><br>

            📱 QR sends the visitor to the website

            </div>
            """,
            unsafe_allow_html=True
        )


    with system_col2:

        st.markdown(
            """
            <div class="goldbox">

            <b>Digital ROBO GUIDE</b><br><br>

            🌍 Detailed heritage exploration<br><br>

            🗣 English • isiNdebele • Shona<br><br>

            🏆 Interactive Heritage Challenge<br><br>

            💬 Rule-based Heritage Assistant<br><br>

            📊 Heritage management interpretation

            </div>
            """,
            unsafe_allow_html=True
        )


# ------------------------------------------------------------
# PAGE ROUTING
# ------------------------------------------------------------

current_page = (
    st.session_state.page
)


if (
    current_page
    ==
    "Home"
):

    home_page()


elif (
    current_page
    in
    [
        "Matobo Hills",
        "Great Zimbabwe",
        "Khami Ruins",
    ]
):

    site_page(
        current_page
    )


elif (
    current_page
    ==
    "Heritage Challenge"
):

    quiz_page()


elif (
    current_page
    ==
    "Heritage Assistant"
):

    assistant_page()


elif (
    current_page
    ==
    "Robot + Website"
):

    prototype_page()


else:

    st.session_state.page = (
        "Home"
    )

    st.rerun()


# ------------------------------------------------------------
# FINAL FOOTER
# ------------------------------------------------------------

st.markdown(

    f"""
    <div class="footer">

        <b>
            {tr("footer")}
        </b>

        <br><br>

        ROBO GUIDE combines cultural education,
        multilingual communication,
        interactive learning and
        preventive heritage-protection technology.

        <br>

        Built as a single-file Streamlit experience
        for the WRO 2026 Zimbabwe National Finals.

    </div>
    """,

    unsafe_allow_html=True
)
v
