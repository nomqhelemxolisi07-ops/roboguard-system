import streamlit as st
import re
from html import escape

st.set_page_config(
    page_title="ROBO GUIDE | Zimbabwe Heritage Explorer",
    page_icon="🗿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# ROBO GUIDE — WRO 2026 Zimbabwe National Finals
# Theme: Robots Meet Culture
# Single-file Streamlit application
# =========================================================

# -----------------------------
# Theme / CSS
# -----------------------------
st.markdown(
    """
    <style>
    :root {
        --rg-green: #7A5A3A;
        --rg-deep: #4B382A;
        --rg-gold: #B98B4A;
        --rg-cream: #F3EBDD;
        --rg-ink: #302820;
        --rg-muted: #746B61;
        --rg-card: rgba(255,255,255,.94);
    }

    .stApp {
        background:
            radial-gradient(circle at 8% 8%, rgba(185,139,74,.10), transparent 20%),
            radial-gradient(circle at 92% 18%, rgba(122,90,58,.09), transparent 22%),
            linear-gradient(180deg, #F8F3EA 0%, #EFE6D8 55%, #F8F3EA 100%);
        color: var(--rg-ink);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #3B3027 0%, #4A3A2D 55%, #2F2822 100%);
        border-right: 3px solid var(--rg-gold);
    }

    [data-testid="stSidebar"] * { color: #FFFFFF; }
    [data-testid="stSidebar"] .stRadio label,
    [data-testid="stSidebar"] .stSelectbox label { color: #FFFFFF !important; }

    .rg-brand {
        border: 1px solid rgba(230,179,37,.45);
        background: linear-gradient(135deg, rgba(255,255,255,.12), rgba(230,179,37,.07));
        border-radius: 20px;
        padding: 18px 16px;
        margin-bottom: 14px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,.10);
    }
    .rg-brand h2 { margin: 0; color: #fff; letter-spacing: 1.4px; }
    .rg-brand p { margin: 4px 0 0; color: #F7E9B1; font-size: .88rem; }

    .rg-hero {
        position: relative;
        overflow: hidden;
        border-radius: 28px;
        padding: 38px 38px 34px 38px;
        margin: 6px 0 24px 0;
        color: white;
        background:
            linear-gradient(110deg, rgba(72,54,40,.98), rgba(118,83,50,.94)),
            repeating-linear-gradient(45deg, rgba(255,255,255,.03) 0 8px, transparent 8px 16px);
        border: 1px solid rgba(230,179,37,.65);
        box-shadow: 0 16px 42px rgba(6,70,42,.18);
    }
    .rg-hero:after {
        content: "";
        position: absolute;
        width: 260px;
        height: 260px;
        border-radius: 50%;
        right: -75px;
        top: -85px;
        border: 28px solid rgba(230,179,37,.19);
        box-shadow: 0 0 0 26px rgba(255,255,255,.04);
    }
    .rg-kicker {
        color: #E4C794;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: .78rem;
    }
    .rg-hero h1 {
        margin: 7px 0 6px 0;
        font-size: clamp(2.2rem, 5vw, 4.4rem);
        line-height: .98;
        letter-spacing: -1.5px;
    }
    .rg-hero p {
        max-width: 850px;
        font-size: 1.08rem;
        line-height: 1.7;
        color: #F4FBF7;
        margin-bottom: 0;
    }
    .rg-badges { margin-top: 18px; }
    .rg-badge {
        display: inline-block;
        background: rgba(255,255,255,.10);
        border: 1px solid rgba(255,255,255,.19);
        padding: 7px 11px;
        border-radius: 999px;
        margin: 4px 5px 0 0;
        font-size: .82rem;
    }

    .rg-section-title {
        font-size: 1.8rem;
        font-weight: 850;
        color: var(--rg-deep);
        margin: 8px 0 3px 0;
    }
    .rg-section-sub {
        color: var(--rg-muted);
        margin: 0 0 18px 0;
        line-height: 1.6;
    }

    .rg-card {
        background: var(--rg-card);
        border: 1px solid #E5ECE7;
        border-top: 4px solid var(--rg-gold);
        border-radius: 20px;
        padding: 21px;
        height: 100%;
        box-shadow: 0 9px 24px rgba(34,67,48,.07);
    }
    .rg-card h3, .rg-card h4 { color: var(--rg-deep); margin-top: 0; }
    .rg-card p { color: #435449; line-height: 1.65; }
    .rg-site-icon { font-size: 2rem; margin-bottom: 5px; }

    .rg-stat {
        background: linear-gradient(180deg, #FFFFFF, #FBFCFA);
        border: 1px solid #E4EBE6;
        border-radius: 18px;
        padding: 15px 16px;
        box-shadow: 0 7px 20px rgba(33,63,45,.05);
    }
    .rg-stat .n { font-size: 1.45rem; font-weight: 850; color: var(--rg-green); }
    .rg-stat .l { color: var(--rg-muted); font-size: .83rem; margin-top: 2px; }

    .rg-strip {
        background: linear-gradient(90deg, #5E4633, #7A5A3A);
        color: #fff;
        border-left: 6px solid var(--rg-gold);
        border-radius: 17px;
        padding: 17px 20px;
        margin: 16px 0;
    }

    .rg-callout {
        background: #FFF9E6;
        border: 1px solid #F2DA89;
        border-radius: 16px;
        padding: 15px 17px;
        color: #574818;
        margin: 12px 0;
    }

    .rg-protect {
        background: #F3EEE6;
        border: 1px solid #D8CCBC;
        border-left: 5px solid var(--rg-green);
        border-radius: 15px;
        padding: 15px 17px;
        margin: 10px 0;
    }

    .rg-quizbox {
        background: #FFFFFF;
        border: 1px solid #E2E9E4;
        border-radius: 22px;
        padding: 20px;
        box-shadow: 0 10px 25px rgba(28,65,44,.07);
    }

    .rg-achievement {
        text-align: center;
        border-radius: 24px;
        background: linear-gradient(135deg, #3B3027, #6B4E35);
        color: white;
        padding: 28px;
        border: 2px solid var(--rg-gold);
        box-shadow: 0 14px 35px rgba(11,107,58,.18);
    }
    .rg-achievement .trophy { font-size: 3.4rem; }
    .rg-achievement h2 { margin: 5px 0; color: #F7D45F; }

    .rg-chat-user {
        margin: 8px 0 8px auto;
        max-width: 84%;
        background: #EEE7DE;
        border: 1px solid #D9CCBD;
        border-radius: 18px 18px 4px 18px;
        padding: 12px 14px;
    }
    .rg-chat-bot {
        margin: 8px auto 8px 0;
        max-width: 90%;
        background: #FFF8E5;
        border: 1px solid #ECD98F;
        border-radius: 18px 18px 18px 4px;
        padding: 12px 14px;
    }

    .rg-footer {
        margin-top: 38px;
        padding: 23px 10px 10px;
        border-top: 1px solid #DCE5DE;
        text-align: center;
        color: #66766B;
        font-size: .86rem;
    }

    div.stButton > button {
        border-radius: 12px;
        border: 1px solid #0B6B3A;
        font-weight: 750;
        transition: .18s ease;
    }
    div.stButton > button:hover {
        border-color: #E6B325;
        transform: translateY(-1px);
        box-shadow: 0 6px 15px rgba(11,107,58,.12);
    }
    div.stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #0B6B3A, #0D7B45);
        color: #fff;
    }

    .stProgress > div > div > div > div { background-color: #0B6B3A; }
    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #E5ECE7;
        padding: 10px 12px;
        border-radius: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Session state
# -----------------------------
DEFAULTS = {
    "page": "Home",
    "lang": "English",
    "quiz_index": 0,
    "quiz_score": 0,
    "quiz_points": 0,
    "quiz_answered": False,
    "quiz_selected": None,
    "quiz_feedback": None,
    "quiz_finished": False,
    "chat": [],
}
for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -----------------------------
# Translation strings
# -----------------------------
UI = {
    "English": {
        "tagline": "Robots Meet Culture • WRO 2026 Zimbabwe",
        "nav": "Explore ROBO GUIDE",
        "language": "Language",
        "home": "Home",
        "matobo": "Matobo Hills",
        "great": "Great Zimbabwe",
        "khami": "Khami Ruins",
        "quiz": "Heritage Challenge",
        "assistant": "Heritage Assistant",
        "prototype": "Heritage Explorer",
        "hero_title": "Meet Zimbabwe through technology.",
        "hero_text": "ROBO GUIDE is a multilingual digital heritage guide that helps visitors discover, understand and respect Zimbabwe's cultural treasures.",
        "explore": "Explore the heritage sites",
        "explore_sub": "Choose a site to discover its people, history, architecture, stories and protection needs.",
        "open": "Open site guide",
        "challenge_cta": "Take the Heritage Challenge",
        "assistant_cta": "Ask ROBO GUIDE",
        "prototype_cta": "See how the robot connects",
        "why": "Why ROBO GUIDE?",
        "why_text": "Culture is strongest when people can understand it, experience it and help protect it. ROBO GUIDE turns heritage learning into an interactive visitor journey while showing how low-cost robotics can support respectful site behaviour.",
        "learn": "Learn",
        "learn_d": "Three rich site guides, multilingual explanations and memorable facts.",
        "play": "Play",
        "play_d": "A gamified challenge with points, progress, feedback and achievements.",
        "protect": "Protect",
        "protect_d": "Learn simple visitor behaviours that help protect fragile heritage for future generations.",
        "connect": "Connect",
        "connect_d": "Use the website on a phone, tablet or computer to explore Zimbabwean heritage anywhere.",
        "history": "History",
        "culture": "Culture & people",
        "features": "Major features",
        "unesco": "UNESCO World Heritage",
        "protection": "Protect this heritage",
        "facts": "Interesting facts",
        "quick": "Quick facts",
        "inscribed": "UNESCO inscription",
        "criteria": "UNESCO criteria",
        "location": "Location",
        "significance": "Why it matters",
        "back": "← Back to Home",
        "quiz_title": "Heritage Challenge",
        "quiz_intro": "Test what you have learned. Every correct answer earns Heritage Points. Instant feedback explains the answer before you continue.",
        "question": "Question",
        "of": "of",
        "score": "Score",
        "points": "Heritage Points",
        "submit": "Check answer",
        "next": "Next question →",
        "finish": "See achievement",
        "correct": "Correct!",
        "incorrect": "Not quite.",
        "reset": "Play again",
        "achievement": "Achievement unlocked",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "guide_desc": "You have built a strong foundation. Keep exploring Zimbabwe's heritage and share what you learn.",
        "guardian_desc": "Outstanding work! You showed excellent knowledge and a strong heritage-protection mindset.",
        "assistant_title": "ROBO GUIDE Heritage Assistant",
        "assistant_intro": "Ask about Matobo Hills, Great Zimbabwe or Khami Ruins — history, dates, builders, rock art, caves, architecture, trade, culture, UNESCO, conservation, artifacts, significance or comparisons.",
        "assistant_placeholder": "e.g. Who built Great Zimbabwe? Compare Khami and Great Zimbabwe.",
        "ask": "Ask ROBO GUIDE",
        "suggested": "Try a question",
        "clear_chat": "Clear conversation",
        "no_answer": "I can help with the three ROBO GUIDE heritage sites. Ask about history, builders, dates, caves, rock art, architecture, artifacts, trade, culture, UNESCO status, conservation, significance, or compare the sites.",
        "prototype_title": "How ROBO GUIDE connects the robot and website",
        "prototype_intro": "The project is one visitor-learning system: the physical prototype responds at the heritage display while the website provides deeper exploration, multilingual learning and event analysis.",
        "flow": "Visitor journey",
        "oled": "Multilingual OLED education",
        "oled_d": "The prototype displays short heritage messages in English, isiNdebele and Shona so visitors can learn in a language they understand.",
        "qr": "QR access",
        "qr_d": "A QR code on the exhibit opens this ROBO GUIDE website, moving the visitor from a short physical message to a detailed digital guide.",
        "visitor": "Visitor guidance",
        "visitor_d": "ROBO GUIDE explains respectful behaviour: stay behind protected boundaries, avoid touching rock art or stonework, follow site rules and learn before interacting.",
        "ir": "IR protected-boundary monitoring",
        "ir_d": "An infrared sensor detects when a visitor crosses the demonstration protection boundary, showing how technology can support preventive heritage conservation.",
        "buzzer": "Buzzer warning",
        "buzzer_d": "When the protected boundary is crossed, the buzzer gives an immediate non-contact warning, encouraging the visitor to step back.",
        "dashboard": "Laptop management dashboard",
        "dashboard_d": "Boundary-crossing events can be recorded on the laptop and analysed by time, frequency and trend. This helps demonstrate how site managers could identify high-risk periods and improve visitor education or protection measures.",
        "footer": "ROBO GUIDE • WRO 2026 Zimbabwe National Finals • Robots Meet Culture • Learn • Respect • Protect",
    },
    "isiNdebele": {
        "tagline": "Amarobhothi Ahlangana Lamasiko • WRO 2026 Zimbabwe",
        "nav": "Hlola i-ROBO GUIDE",
        "language": "Ulimi",
        "home": "Ikhaya",
        "matobo": "Amagquma eMatobo",
        "great": "IGreat Zimbabwe",
        "khami": "Amanxiwa eKhami",
        "quiz": "Inselele Yamagugu",
        "assistant": "Umsizi Wamagugu",
        "prototype": "Ukuhlola Amagugu",
        "hero_title": "Hlangana leZimbabwe ngobuchwepheshe.",
        "hero_text": "I-ROBO GUIDE ixhumanisa irobhothi lokuvikela amagugu lomhlahlandlela wedijithali osebenza ngezindimi ezintathu, ukuze izivakashi zifunde, zihlole futhi zivikele amagugu amasiko eZimbabwe.",
        "explore": "Hlola izindawo zamagugu",
        "explore_sub": "Khetha indawo ufunde ngabantu, umlando, izakhiwo, izindaba kanye lendlela yokuyivikela.",
        "open": "Vula umhlahlandlela",
        "challenge_cta": "Yenza Inselele Yamagugu",
        "assistant_cta": "Buza i-ROBO GUIDE",
        "prototype_cta": "Bona ukuxhumana kwerobhothi",
        "why": "Kungani i-ROBO GUIDE?",
        "why_text": "Amasiko aqina nxa abantu bewazwisisa, bewabona njalo besiza ukuwavikela. I-ROBO GUIDE yenza ukufunda amagugu kube ngumsebenzi osebenzisanayo futhi iveze indlela amarobhothi anganceda ngayo ekuvikeleni indawo.",
        "learn": "Funda",
        "learn_d": "Imihlahlandlela emithathu ejulileyo, izindimi ezintathu kanye lamaqiniso akhumbulekayo.",
        "play": "Dlala",
        "play_d": "Inselele elamaphuzu, inqubekela phambili, impendulo esheshayo kanye lemiklomelo.",
        "protect": "Vikela",
        "protect_d": "Funda indlela yokuvakasha ehlonipha futhi evikela amagugu ezizukulwaneni ezizayo.",
        "connect": "Xhumanisa",
        "connect_d": "I-QR ixhumanisa irobhothi lomhlahlandlela wedijithali.",
        "history": "Umlando",
        "culture": "Amasiko labantu",
        "features": "Izinto eziqakathekileyo",
        "unesco": "Amagugu Omhlaba e-UNESCO",
        "protection": "Vikela amagugu la",
        "facts": "Amaqiniso athakazelisayo",
        "quick": "Amaqiniso amafitshane",
        "inscribed": "Ukubhaliswa yi-UNESCO",
        "criteria": "Imigomo ye-UNESCO",
        "location": "Indawo",
        "significance": "Kungani kuqakathekile",
        "back": "← Buyela Ekhaya",
        "quiz_title": "Inselele Yamagugu",
        "quiz_intro": "Hlola ulwazi lwakho. Impendulo ngayinye elungileyo iletha amaHeritage Points, njalo uthola incazelo masinyane.",
        "question": "Umbuzo",
        "of": "ku",
        "score": "Amaphuzu",
        "points": "AmaHeritage Points",
        "submit": "Hlola impendulo",
        "next": "Umbuzo olandelayo →",
        "finish": "Bona umklomelo",
        "correct": "Kulungile!",
        "incorrect": "Akukabi yikho.",
        "reset": "Dlala futhi",
        "achievement": "Umklomelo uvuliwe",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "guide_desc": "Usulolwazi oluqinileyo. Qhubeka uhlola amagugu eZimbabwe futhi wabelane ngalokho okufundayo.",
        "guardian_desc": "Umsebenzi omuhle kakhulu! Utshengise ulwazi olukhulu kanye lomqondo oqinileyo wokuvikela amagugu.",
        "assistant_title": "Umsizi Wamagugu we-ROBO GUIDE",
        "assistant_intro": "Buza ngeMatobo, Great Zimbabwe kumbe Khami — umlando, izinsuku, abakhi, imidwebo emadwaleni, imigede, izakhiwo, ukuhweba, amasiko, UNESCO, ukuvikelwa, izinto zakudala, ukubaluleka kumbe ukuqhathanisa.",
        "assistant_placeholder": "isb. Ngubani owakha iGreat Zimbabwe? Qhathanisa iKhami leGreat Zimbabwe.",
        "ask": "Buza i-ROBO GUIDE",
        "suggested": "Zama umbuzo",
        "clear_chat": "Sula ingxoxo",
        "no_answer": "Nginganceda ngezindawo ezintathu ze-ROBO GUIDE. Buza ngomlando, abakhi, izinsuku, imigede, imidwebo, izakhiwo, izinto zakudala, ukuhweba, amasiko, UNESCO, ukuvikelwa, ukubaluleka kumbe ukuqhathanisa.",
        "prototype_title": "Indlela i-ROBO GUIDE exhumanisa ngayo irobhothi lewebhusayithi",
        "prototype_intro": "Iprojekthi iyisistimu eyodwa yokufundisa izivakashi: irobhothi lisebenza embukisweni kuthi iwebhusayithi inike ulwazi olujulileyo, izindimi ezintathu kanye lokuhlaziya izehlakalo.",
        "flow": "Uhambo lwesivakashi",
        "oled": "Imfundo ye-OLED ngezindimi ezintathu",
        "oled_d": "Iprototype iveza imilayezo emifitshane ngesiNgisi, isiNdebele kanye lesiShona ukuze izivakashi zifunde ngolimi eziluzwisisayo.",
        "qr": "Ukungena nge-QR",
        "qr_d": "Ikhodi ye-QR embukisweni ivula iwebhusayithi ye-ROBO GUIDE, isusa isivakashi emlayezweni omfitshane isise emhlahlandleleni ogcweleyo.",
        "visitor": "Ukuqondisa izivakashi",
        "visitor_d": "I-ROBO GUIDE ichaza ukuziphatha okuhloniphayo: hlala ngaphandle kwemingcele evikelweyo, ungathinti imidwebo kumbe amatshe, landela imithetho yendawo futhi ufunde ngaphambi kokusebenzisana layo.",
        "ir": "Ukuqapha umngcele nge-IR",
        "ir_d": "I-infrared sensor ibona nxa isivakashi siwela umngcele wokuvikela, itshengisa indlela ubuchwepheshe obunganceda ngayo ukuvikelwa kwamagugu.",
        "buzzer": "Isixwayiso se-buzzer",
        "buzzer_d": "Nxa umngcele oweqiwa, i-buzzer inika isixwayiso masinyane ngaphandle kokuthinta umuntu, imkhuthaze ukuthi ahlehle.",
        "dashboard": "Ideshibhodi yokuphatha kukhompyutha",
        "dashboard_d": "Izehlakalo zokweqa umngcele zingarekhodwa kukhompyutha zihlaziywe ngesikhathi, ngobunengi kanye lemikhuba. Lokhu kunganceda abaphathi babone izikhathi eziyingozi futhi bathuthukise imfundo lezindlela zokuvikela.",
        "footer": "ROBO GUIDE • WRO 2026 Zimbabwe National Finals • Robots Meet Culture • Funda • Hlonipha • Vikela",
    },
    "Shona": {
        "tagline": "Marobhoti Anosangana Netsika • WRO 2026 Zimbabwe",
        "nav": "Ongorora ROBO GUIDE",
        "language": "Mutauro",
        "home": "Kumba",
        "matobo": "Matobo Hills",
        "great": "Great Zimbabwe",
        "khami": "Khami Ruins",
        "quiz": "Heritage Challenge",
        "assistant": "Mubatsiri weNhaka",
        "prototype": "Kuongorora Nhaka",
        "hero_title": "Sangana neZimbabwe kuburikidza netekinoroji.",
        "hero_text": "ROBO GUIDE mutungamiriri wedhijitari wemitauro mitatu unobatsira vashanyi kudzidza, kuongorora uye kuremekedza pfuma yetsika yeZimbabwe.",
        "explore": "Ongorora nzvimbo dzenhaka",
        "explore_sub": "Sarudza nzvimbo kuti uzive vanhu, nhoroondo, zvivakwa, nyaya uye nzira dzekuichengetedza.",
        "open": "Vhura mutungamiriri",
        "challenge_cta": "Tora Heritage Challenge",
        "assistant_cta": "Bvunza ROBO GUIDE",
        "prototype_cta": "Ona kubatana kwerobhoti",
        "why": "Sei ROBO GUIDE?",
        "why_text": "Tsika dzinosimba kana vanhu vachidzinzwisisa, vachidziona uye vachibatsira kudzichengetedza. ROBO GUIDE inoita kuti kudzidza nhaka kuve chiitiko chinodyidzana uye inoratidza mashandisirwo emarobhoti asingadhuri mukuchengetedza nzvimbo.",
        "learn": "Dzidza",
        "learn_d": "Mitungamiriri mitatu yakadzama, mitauro mitatu uye mashoko anoyeukwa.",
        "play": "Tamba",
        "play_d": "Mutambo une mapoinzi, kufambira mberi, mhinduro yepakarepo uye mibairo.",
        "protect": "Chengetedza",
        "protect_d": "Dzidza maitiro ekushanya anoremekedza uye anochengetedza nhaka yezvizvarwa zvinotevera.",
        "connect": "Batanidza",
        "connect_d": "Shandisa webhusaiti pafoni, tablet kana komputa kuti uongorore nhaka yeZimbabwe.",
        "history": "Nhoroondo",
        "culture": "Tsika nevanhu",
        "features": "Zvinhu zvikuru",
        "unesco": "UNESCO World Heritage",
        "protection": "Chengetedza nhaka iyi",
        "facts": "Mashoko anonakidza",
        "quick": "Mashoko mapfupi",
        "inscribed": "Kunyoreswa neUNESCO",
        "criteria": "Mitemo yeUNESCO",
        "location": "Nzvimbo",
        "significance": "Kukosha kwayo",
        "back": "← Dzokera Kumba",
        "quiz_title": "Heritage Challenge",
        "quiz_intro": "Edza ruzivo rwako. Mhinduro yega yega yakarurama inokupa Heritage Points uye unowana tsananguro pakarepo.",
        "question": "Mubvunzo",
        "of": "pa",
        "score": "Zvawawana",
        "points": "Heritage Points",
        "submit": "Tarisa mhinduro",
        "next": "Mubvunzo unotevera →",
        "finish": "Ona mubairo",
        "correct": "Zvakarurama!",
        "incorrect": "Hazvisati zvanyatsonaka.",
        "reset": "Tamba zvakare",
        "achievement": "Mubairo wavhurwa",
        "guide": "Heritage Guide",
        "guardian": "Heritage Guardian",
        "guide_desc": "Wava neruzivo rwakanaka. Ramba uchiongorora nhaka yeZimbabwe uye ugovane zvaunodzidza.",
        "guardian_desc": "Basa rakanaka zvikuru! Waratidza ruzivo rwakadzama uye pfungwa yakasimba yekuchengetedza nhaka.",
        "assistant_title": "ROBO GUIDE Heritage Assistant",
        "assistant_intro": "Bvunza nezveMatobo Hills, Great Zimbabwe kana Khami Ruins — nhoroondo, mazuva, vavaki, rock art, mapako, architecture, kutengeserana, tsika, UNESCO, conservation, artifacts, kukosha kana kuenzanisa.",
        "assistant_placeholder": "semuenzaniso: Ndiani akavaka Great Zimbabwe? Enzanisa Khami neGreat Zimbabwe.",
        "ask": "Bvunza ROBO GUIDE",
        "suggested": "Edza mubvunzo",
        "clear_chat": "Bvisa hurukuro",
        "no_answer": "Ndinogona kubatsira nezvenzvimbo nhatu dzeROBO GUIDE. Bvunza nezvenhoroondo, vavaki, mazuva, mapako, rock art, architecture, artifacts, kutengeserana, tsika, UNESCO, conservation, kukosha kana kuenzanisa.",
        "prototype_title": "Maitiro ROBO GUIDE anobatanidza robhoti newebhusaiti",
        "prototype_intro": "Projekiti iyi ihurongwa humwe hwekudzidzisa vashanyi: prototype inopindura pachiratidziro chenhaka, uku webhusaiti ichipa ruzivo rwakadzama, mitauro mitatu uye kuongorora zviitiko.",
        "flow": "Rwendo rwemushanyi",
        "oled": "Dzidzo yeOLED yemitauro mitatu",
        "oled_d": "Prototype inoratidza mashoko mapfupi enhaka muEnglish, isiNdebele neShona kuitira kuti vashanyi vadzidze nemutauro wavanonzwisisa.",
        "qr": "QR access",
        "qr_d": "QR code iri pachiratidziro inovhura ROBO GUIDE webhusaiti, ichibvisa mushanyi pamashoko mapfupi ichimuendesa kumutungamiriri wakadzama.",
        "visitor": "Kutungamirira vashanyi",
        "visitor_d": "ROBO GUIDE inotsanangura maitiro anoremekedza nhaka: gara kunze kwemiganhu yakachengetedzwa, usabata rock art kana stonework, tevera mitemo yenzvimbo uye dzidza usati wabata chero chinhu.",
        "ir": "IR protected-boundary monitoring",
        "ir_d": "Infrared sensor inoona kana mushanyi ayambuka muganhu wekuchengetedza, ichiratidza kuti tekinoroji inogona kubatsira sei mukudzivirira kukuvara kwenhaka.",
        "buzzer": "Yambiro yebuzzer",
        "buzzer_d": "Kana muganhu wayambukwa, buzzer inopa yambiro ipapo pasina kubata munhu, ichikurudzira mushanyi kudzokera shure.",
        "dashboard": "Laptop management dashboard",
        "dashboard_d": "Zviitiko zvekuyambuka muganhu zvinogona kurekodhwa palaptop zvoongororwa nenguva, huwandu uye trend. Izvi zvinoratidza kuti mamaneja enzvimbo angaziva sei nguva dzine njodzi uye kuvandudza dzidzo kana nzira dzekuchengetedza.",
        "footer": "ROBO GUIDE • WRO 2026 Zimbabwe National Finals • Robots Meet Culture • Dzidza • Remekedza • Chengetedza",
    },
}

# -----------------------------
# Heritage content
# -----------------------------
SITES = {
    "Matobo Hills": {
        "emoji": "🪨",
        "English": {
            "name": "Matobo Hills",
            "subtitle": "A living cultural landscape of granite hills, sacred places, caves and extraordinary rock art.",
            "location": "Matabeleland South, south of Bulawayo, Zimbabwe",
            "inscribed": "2003",
            "criteria": "(iii), (v), (vi)",
            "history": "Matobo is an ancient cultural landscape shaped by both nature and people. The granite terrain contains archaeological evidence reaching far back into the Stone Age. Hunter-gatherer communities left a remarkable record of their lives in rock paintings, while later farming communities, Ndebele history and continuing spiritual traditions added new layers of meaning to the landscape.",
            "culture": "Matobo remains important to local communities as a spiritual and cultural landscape. Shrines, sacred hills and oral traditions connect people to ancestors, rain-making traditions and the Mwari religious tradition. Ndebele history is also closely connected to the area, including the memory of King Mzilikazi and major events of the nineteenth century.",
            "features": [
                "Granite kopjes, balancing rocks and dramatic valleys formed by long geological weathering.",
                "Caves and rock shelters containing a very high concentration of prehistoric paintings.",
                "Rock art showing people, animals, hunting, movement, ritual and aspects of past ways of life.",
                "Important archaeological deposits that help researchers study changing human occupation over long periods.",
                "Sacred places and living cultural traditions that continue to give the landscape meaning today.",
            ],
            "unesco": "UNESCO inscribed Matobo Hills in 2003 as a cultural landscape under criteria (iii), (v) and (vi). UNESCO highlights the exceptional concentration of rock art, the long interaction between communities and the landscape, and the continuing importance of powerful religious traditions associated with Matobo.",
            "protection": [
                "Never touch, trace, wet, chalk or paint over rock art; oils and moisture can damage fragile surfaces.",
                "Stay on approved paths and behind barriers around sensitive caves, shrines and archaeological areas.",
                "Do not remove stones, pottery fragments, plants or any archaeological material.",
                "Respect sacred places, local customs, guides and restrictions on photography or access where they apply.",
                "Avoid litter, fire, graffiti and climbing on protected painted surfaces.",
            ],
            "facts": [
                "Matobo is renowned for one of the highest concentrations of rock art in southern Africa.",
                "Some shelters preserve many layers of paintings, showing that people returned to these places over long periods.",
                "The hills are not only an archaeological landscape; they remain culturally and spiritually meaningful to communities today.",
                "The smooth granite forms create natural shelters that helped preserve archaeological material and paintings.",
            ],
            "significance": "Matobo links archaeology, art, spirituality, oral history and a spectacular granite landscape. It teaches that heritage can be both ancient and living at the same time.",
        },
        "isiNdebele": {
            "name": "Amagquma eMatobo",
            "subtitle": "Indawo yamasiko ephilayo elamagquma egranite, izindawo ezingcwele, imigede kanye lemidwebo emangalisayo emadwaleni.",
            "location": "EMatabeleland South, eningizimu yeBulawayo, eZimbabwe",
            "inscribed": "2003",
            "criteria": "(iii), (v), (vi)",
            "history": "IMatobo yindawo yamasiko yakudala eyakhiwe yimvelo kanye labantu. Amadwala egranite aqukethe ubufakazi bezinto zakudala obubuyela eStone Age. Abazingeli labaqoqi batshiya imidwebo emadwaleni, kwathi abalimi abalandelayo, umlando wamaNdebele kanye lamasiko okomoya aqhubekayo kwengeza ezinye incazelo kule ndawo.",
            "culture": "IMatobo isaqakathekile emiphakathini njengendawo yomoya lamasiko. Izindawo ezingcwele, amagquma kanye lendaba zomlomo zixhumanisa abantu labokhokho, imikhuba yokucela izulu kanye lenkolelo kaMwari. Umlando wamaNdebele lawo uxhumene kakhulu leMatobo, uhlanganisa inkumbulo yeNkosi uMzilikazi kanye lezehlakalo zekhulu le-19.",
            "features": [
                "Amagquma egranite, amatshe azilinganisileyo kanye lezihotsha ezidalwe yisikhathi eside sokuguguleka.",
                "Imigede lezindawo zokukhosela ezilemifanekiso eminengi yakudala emadwaleni.",
                "Imidwebo etshengisa abantu, izinyamazana, ukuzingela, ukuhamba kanye leminye imikhuba yakudala.",
                "Ubufakazi bezinto zakudala obunceda ukufunda ngempilo yabantu ezikhathini ezitshiyeneyo.",
                "Izindawo ezingcwele kanye lamasiko aphilayo aqhubeka enika indawo incazelo lamuhla.",
            ],
            "unesco": "I-UNESCO yabhalisa iMatobo Hills ngo-2003 njengendawo yamasiko ngaphansi kwemigomo (iii), (v) kanye (vi), igcizelela ubunengi bemidwebo emadwaleni, ubudlelwano obude phakathi kwabantu lendawo kanye lokuqhubeka kwamasiko okomoya.",
            "protection": [
                "Ungathinti, ungacuphi, ungamanzisi loba upende phezu kwemidwebo emadwaleni.",
                "Hamba ngemizila evunyelweyo futhi uhlale ngaphandle kwezindawo ezivalelweyo.",
                "Ungasusi amatshe, izingcezu zebumba, izihlahla loba izinto zakudala.",
                "Hlonipha izindawo ezingcwele, amasiko omphakathi kanye lemithetho yabakhokheli bendawo.",
                "Gwema ukulahla ingcekeza, umlilo, ukubhala emadwaleni kanye lokugibela phezu kwemidwebo.",
            ],
            "facts": [
                "IMatobo ilezinye zezibalo eziphakeme kakhulu zemidwebo emadwaleni eSouthern Africa.",
                "Ezinye indawo zokukhosela zilezigaba eziningi zemidwebo ezitshengisa ukusetshenziswa kwazo isikhathi eside.",
                "IMatobo ayisiyo ndawo yezinto zakudala kuphela; iseyindawo ephilayo ngokwesiko langokomoya.",
                "Amadwala egranite adala indawo zokukhosela ezanceda ukugcina imidwebo lezinto zakudala.",
            ],
            "significance": "IMatobo ixhumanisa izinto zakudala, ubuciko, okomoya, umlando womlomo kanye lendawo enhle yegranite. Ifundisa ukuthi amagugu angaba madala kodwa aqhubeke ephila.",
        },
        "Shona": {
            "name": "Matobo Hills",
            "subtitle": "Nzvimbo yetsika inorarama ine zvikomo zvegranite, nzvimbo dzinoyera, mapako uye rock art inoshamisa.",
            "location": "Matabeleland South, kumaodzanyemba kweBulawayo, Zimbabwe",
            "inscribed": "2003",
            "criteria": "(iii), (v), (vi)",
            "history": "Matobo inzvimbo yekare yetsika yakagadzirwa nezvisikwa pamwe nevanhu. Matombo egranite ane humbowo hwevanhu hunodzokera kuStone Age. Hunter-gatherer communities vakasiya rock paintings, uye mapoka evarimi akazotevera, nhoroondo yeNdebele pamwe netsika dzemweya dzichiri kurarama zvakawedzera zvinoreva nzvimbo iyi.",
            "culture": "Matobo ichiri yakakosha kum communities senzvimbo yemweya netsika. Nzvimbo dzinoyera, zvikomo uye oral traditions zvinobatanidza vanhu nemadzitateguru, tsika dzekukumbira mvura uye Mwari religious tradition. Nhoroondo yeNdebele yakabatana zvikuru nenzvimbo iyi, kusanganisira ndangariro dzaMambo Mzilikazi nezviitiko zvikuru zvezana remakore rechi19.",
            "features": [
                "Granite kopjes, balancing rocks nemipata yakagadzirwa nekushanduka kwedombo kwenguva refu.",
                "Mapako nemarock shelters ane rock paintings dzakawanda zvikuru.",
                "Rock art inoratidza vanhu, mhuka, kuvhima, kufamba uye zvimwe zvehupenyu hwekare.",
                "Archaeological deposits dzinobatsira kunzwisisa kugara kwevanhu mumakore akawanda.",
                "Nzvimbo dzinoyera uye tsika dzichiri kurarama dzinoramba dzichipa nzvimbo iyi kukosha.",
            ],
            "unesco": "UNESCO yakanyoresa Matobo Hills muna 2003 se cultural landscape pasi pecriteria (iii), (v) ne(vi), ichisimbisa kuwanda kwe rock art, hukama hurefu pakati pevanhu nenzvimbo uye kukosha kwetsika dzemweya dzichiri kurarama.",
            "protection": [
                "Usabata, kutevedzera, kunyorovesa kana kupenda pamusoro pe rock art.",
                "Shandisa nzira dzakatenderwa uye gara kuseri kwemiganhu yenzvimbo dzine ngozi.",
                "Usabvisa matombo, zvidimbu zvehari, zvirimwa kana zvinhu zve archaeology.",
                "Remekedza nzvimbo dzinoyera, tsika dzemunharaunda uye mirayiro yevatungamiriri.",
                "Dzivisa marara, moto, graffiti uye kukwira pamatombo ane mifananidzo.",
            ],
            "facts": [
                "Matobo ine imwe yehuwandu hukuru hwe rock art muSouthern Africa.",
                "Mamwe marock shelters ane layers dzemifananidzo dzinoratidza kushandiswa kwenguva refu.",
                "Matobo haisi archaeological landscape chete; ichiri nzvimbo ine kukosha kwetsika nemweya.",
                "Granite forms dzakagadzira shelters dzakabatsira kuchengetedza paintings nezvimwe zvinhu zvekare.",
            ],
            "significance": "Matobo inobatanidza archaeology, art, spirituality, oral history uye granite landscape inoshamisa. Inodzidzisa kuti nhaka inogona kuva yekare uye ichiri kurarama panguva imwe chete.",
        },
    },
    "Great Zimbabwe": {
        "emoji": "🏛️",
        "English": {
            "name": "Great Zimbabwe",
            "subtitle": "The monumental stone capital whose name became the name of a nation.",
            "location": "Masvingo Province, south-eastern Zimbabwe",
            "inscribed": "1986",
            "criteria": "(i), (iii), (vi)",
            "history": "Great Zimbabwe developed into a major political, economic and cultural centre between roughly the eleventh and fifteenth centuries. It was built and occupied by ancestors of Shona-speaking communities and became the centre of a powerful state connected to long-distance trade. Its stone architecture, cattle wealth, craft production and imported goods point to an influential society linked to Indian Ocean trade networks.",
            "culture": "The site is deeply connected to Zimbabwean identity and to the history of Shona-speaking peoples. Leadership, spirituality, cattle, craft skills and control of trade were important to the society that flourished here. The name Zimbabwe is commonly linked to Shona expressions referring to houses or buildings of stone, and the site's legacy became a powerful national symbol.",
            "features": [
                "The Hill Complex, built among granite boulders and associated with long occupation and important ritual or elite activity.",
                "The Great Enclosure, famous for its massive dry-stone outer wall, internal passages and Conical Tower.",
                "The Valley Ruins, a broad area of stone enclosures that reflects residential and political expansion.",
                "Dry-stone masonry constructed without mortar, using carefully shaped and stacked granite blocks.",
                "Zimbabwe Birds: carved soapstone birds found at the site; the bird motif later became an important national emblem.",
                "Evidence of local crafts and long-distance trade, including imported objects linked to wider African and Indian Ocean networks.",
            ],
            "unesco": "UNESCO inscribed Great Zimbabwe National Monument in 1986 under criteria (i), (iii) and (vi). It is recognized for the achievement of its stone architecture, its exceptional testimony to a major African civilization, and its strong historical and symbolic importance.",
            "protection": [
                "Do not climb, sit or lean on ancient dry-stone walls; movement can loosen carefully balanced masonry.",
                "Never remove stones, pottery, beads or other archaeological material.",
                "Stay on marked routes, especially where walls or paths are fragile.",
                "Do not scratch, carve or write on stone surfaces.",
                "Respect guides, cultural interpretation and all restricted or sacred areas.",
            ],
            "facts": [
                "Great Zimbabwe gave modern Zimbabwe its name and one of its most recognizable national symbols.",
                "Its monumental walls were built without mortar, relying on skilled stone selection and construction.",
                "The Great Enclosure is one of the most iconic surviving pre-colonial stone structures in sub-Saharan Africa.",
                "Finds from the site demonstrate participation in trade networks extending far beyond the Zimbabwe Plateau.",
            ],
            "significance": "Great Zimbabwe is evidence of complex African statecraft, architecture, trade and cultural achievement. It is central to national identity and challenges outdated claims that denied African authorship of sophisticated monuments.",
        },
        "isiNdebele": {
            "name": "IGreat Zimbabwe",
            "subtitle": "Inhloko-dolobha yamatshe enkulu eyapha ilizwe igama lalo.",
            "location": "EMasvingo Province, eningizimu-mpumalanga yeZimbabwe",
            "inscribed": "1986",
            "criteria": "(i), (iii), (vi)",
            "history": "IGreat Zimbabwe yakhula yaba yindawo enkulu yezombusazwe, ezomnotho lamasiko phakathi kwekhulu le-11 lele-15. Yakhiwa futhi yahlalwa ngokhokho bemiphakathi ekhuluma isiShona, yaba yinhloko yombuso olamandla owawuxhumene lokuhweba okude. Izakhiwo zamatshe, inkomo, ubuciko kanye lezinto ezivela kwamanye amazwe kutshengisa umphakathi owawuxhumene lezindlela zokuhweba ze-Indian Ocean.",
            "culture": "Indawo ixhumene kakhulu lobuwena beZimbabwe kanye lomlando wabantu abakhuluma isiShona. Ubukhokheli, okomoya, inkomo, amakhono ezandla kanye lokulawula ukuhweba kwakubalulekile emphakathini walapha. Igama elithi Zimbabwe lixhunyaniswa lamazwi esiShona aphathelane lezindlu zamatshe, kanti ilifa lendawo laba luphawu olukhulu lwesizwe.",
            "features": [
                "I-Hill Complex eyakhiwe phakathi kwamadwala amakhulu futhi ehlotshaniswa lokuhlala isikhathi eside.",
                "I-Great Enclosure edume ngodonga lwayo olukhulu olwakhiwe ngaphandle kwe-mortar, imizila yangaphakathi kanye leConical Tower.",
                "I-Valley Ruins, indawo ebanzi yezakhiwo zamatshe etshengisa ukukhula kwendawo yokuhlala lombuso.",
                "Ukwakhiwa kwamatshe ngaphandle kodaka, kusetshenziswa amatshe egranite akhethwe futhi abekwa ngobuciko.",
                "IZimbabwe Birds: izinyoni eziqoshwe ngesoapstone ezatholakala lapha, zaba luphawu oluqakathekileyo lwesizwe.",
                "Ubufakazi bobuciko bendawo kanye lokuhweba lamazwe akude.",
            ],
            "unesco": "I-UNESCO yabhalisa iGreat Zimbabwe National Monument ngo-1986 ngaphansi kwemigomo (i), (iii) kanye (vi), iqaphela ubuciko bokwakha ngamatshe, ubufakazi bempucuko enkulu yaseAfrica kanye lokubaluleka kwayo emlandweni.",
            "protection": [
                "Ungagibeli, ungahlali loba uncike emidulini yakudala; lokhu kungakhulula amatshe.",
                "Ungasusi amatshe, izitsha zobumba, ubuhlalu loba ezinye izinto zakudala.",
                "Hamba ngemizila ephawuliweyo, ikakhulu lapho izindonga zibuthakathaka.",
                "Ungabhali loba uqophe phezu kwamatshe.",
                "Hlonipha abakhokheli kanye lezindawo ezinqatshelweyo kumbe ezingcwele.",
            ],
            "facts": [
                "IGreat Zimbabwe yapha iZimbabwe yanamuhla igama layo kanye lolunye uphawu lwayo oludume kakhulu.",
                "Imiduli yayo emikhulu yakhiwa ngaphandle kwe-mortar.",
                "IGreat Enclosure ingenye yezakhiwo zamatshe zangaphambi kobukoloni ezidume kakhulu eSub-Saharan Africa.",
                "Izinto ezatholakala lapha zitshengisa ukuhweba okwakufinyelela kude ngaphandle kweZimbabwe Plateau.",
            ],
            "significance": "IGreat Zimbabwe iyibufakazi bobukhokheli, ubuciko bokwakha, ukuhweba kanye lempucuko yaseAfrica. Iqakathekile ekubunjweni kobuwena besizwe futhi iphikisa imibono yakudala eyayiphika ukuthi yakhiwa ngabantu baseAfrica.",
        },
        "Shona": {
            "name": "Great Zimbabwe",
            "subtitle": "Guta guru rematombo rakapa nyika zita rayo.",
            "location": "Masvingo Province, kumaodzanyemba-kumabvazuva kweZimbabwe",
            "inscribed": "1986",
            "criteria": "(i), (iii), (vi)",
            "history": "Great Zimbabwe yakakura kuva muzinda mukuru wezvematongerwo enyika, hupfumi netsika pakati pezvinenge zana remakore rechi11 nerechi15. Yakavakwa nekugarwa nemadzitateguru evanhu vanotaura Shona uye yakava pakati pehurumende yakasimba yakabatana nekutengeserana kure. Zvivakwa zvematombo, mombe, mabasa emaoko nezvinhu zvakabva kunze zvinoratidza nzanga yaive chikamu cheIndian Ocean trade networks.",
            "culture": "Nzvimbo iyi yakabatana zvakadzama neZimbabwean identity uye nhoroondo yevanhu vanotaura Shona. Hutungamiri, spirituality, mombe, mabasa emaoko uye kutonga trade zvaikosha munzanga yaigara pano. Zita rekuti Zimbabwe rinowanzobatanidzwa nemashoko echiShona anoreva dzimba kana zvivakwa zvematombo, uye nhaka yenzvimbo yakava chiratidzo chikuru chenyika.",
            "features": [
                "Hill Complex yakavakwa pakati pematombo makuru uye ine humbowo hwekugara kwenguva refu.",
                "Great Enclosure ine madziro makuru edry-stone, nzira dzemukati uye Conical Tower.",
                "Valley Ruins, nzvimbo yakafara yezvivakwa zvematombo inoratidza kukura kwekugara nehutongi.",
                "Dry-stone masonry yakavakwa pasina mortar, matombo egranite achisarudzwa nekuiswa nehunyanzvi.",
                "Zimbabwe Birds: shiri dzakavezwa musoapstone dzakawanikwa panzvimbo iyi uye dzakazova chiratidzo chenyika.",
                "Humbowo hwemabasa emaoko emuno uye kutengeserana kure.",
            ],
            "unesco": "UNESCO yakanyoresa Great Zimbabwe National Monument muna 1986 pasi pecriteria (i), (iii) ne(vi), ichiremekedza hunyanzvi hwezvivakwa zvematombo, humbowo hwebudiriro huru yeAfrica uye kukosha kwayo munhoroondo nechiratidzo chenyika.",
            "protection": [
                "Usakwira, kugara kana kuzembera pamadziro ekare; izvi zvinogona kusunungura matombo.",
                "Usabvisa matombo, pottery, beads kana zvimwe zvinhu zve archaeology.",
                "Ramba uri munzira dzakatemerwa, kunyanya pane madziro asina kusimba.",
                "Usakwenya, kuveza kana kunyora pamatombo.",
                "Remekedza guides uye nzvimbo dzakarambidzwa kana dzinoyera.",
            ],
            "facts": [
                "Great Zimbabwe yakapa Zimbabwe yemazuva ano zita rayo uye chiratidzo chayo chine mukurumbira.",
                "Madziro makuru akavakwa pasina mortar, achivimba nehunyanzvi hwekuisa matombo.",
                "Great Enclosure ndeimwe yezvivakwa zvikuru zvematombo zvakapona kubva pre-colonial sub-Saharan Africa.",
                "Zvakawanikwa zvinoratidza trade networks dzaisvika kure kupfuura Zimbabwe Plateau.",
            ],
            "significance": "Great Zimbabwe ihumbowo hweAfrican statecraft, architecture, trade uye cultural achievement. Inokosha zvikuru kuZimbabwean identity uye inoramba pfungwa dzekare dzairamba African authorship yezvivakwa zvakaoma.",
        },
    },
    "Khami Ruins": {
        "emoji": "🧱",
        "English": {
            "name": "Khami Ruins",
            "subtitle": "A terraced stone city of the Torwa era, rich in decorative masonry and trade history.",
            "location": "Near Bulawayo, western Zimbabwe",
            "inscribed": "1986",
            "criteria": "(iii), (iv)",
            "history": "Khami rose to prominence after the decline of Great Zimbabwe and became the capital of the Torwa state, especially from the fifteenth century into the seventeenth century. Its rulers participated in regional and long-distance trade, and archaeology has revealed imported goods alongside local material culture. Khami represents an important later development of the Zimbabwe stone-building tradition.",
            "culture": "Khami reflects the political authority, household organization, craftsmanship and trading connections of communities in south-western Zimbabwe. Its architecture shows continuity with the wider Zimbabwe cultural tradition while introducing a distinctive emphasis on terraced platforms and decorative retaining walls.",
            "features": [
                "Stone-faced terraces built into the landscape, creating raised platforms for elite occupation and structures.",
                "Decorative dry-stone wall patterns, including courses and designs that produce striking visual effects.",
                "The Hill Complex and other platforms that show sophisticated adaptation of architecture to the natural terrain.",
                "Archaeological evidence of long-distance trade, including imported ceramics and other prestige goods.",
                "A building tradition related to Great Zimbabwe but expressed through more extensive terracing and retaining walls.",
            ],
            "unesco": "UNESCO inscribed Khami Ruins National Monument in 1986 under criteria (iii) and (iv). It recognizes Khami as exceptional testimony to a cultural tradition and an outstanding example of an architectural ensemble representing an important stage in southern African history.",
            "protection": [
                "Do not climb or walk on fragile terrace walls; pressure can cause stone movement or collapse.",
                "Keep vegetation, litter and fire away from archaeological structures and follow site instructions.",
                "Never remove pottery, beads, stones or other objects, even if they appear loose.",
                "Stay on designated paths to reduce erosion around terraces and excavated areas.",
                "Do not scratch, rearrange or rebuild ancient stonework.",
            ],
            "facts": [
                "Khami became an important political centre after Great Zimbabwe's decline.",
                "It is strongly associated with the Torwa state and the later Zimbabwe cultural tradition.",
                "Its extensive terracing distinguishes it visually from Great Zimbabwe's best-known monumental walls.",
                "Imported objects found through archaeology show that Khami was connected to wider trade networks.",
            ],
            "significance": "Khami shows that the Zimbabwe stone-building tradition continued and changed over time. Its terraces, decorative masonry and trade evidence reveal innovation rather than simple imitation of Great Zimbabwe.",
        },
        "isiNdebele": {
            "name": "Amanxiwa eKhami",
            "subtitle": "Idolobho lamatshe elamathala eTorwa, elicebile ngobuciko bamatshe kanye lomlando wokuhweba.",
            "location": "Eduze leBulawayo, entshonalanga yeZimbabwe",
            "inscribed": "1986",
            "criteria": "(iii), (iv)",
            "history": "IKhami yakhula ngemva kokwehla kweGreat Zimbabwe yaba yinhloko yombuso weTorwa, ikakhulu kusukela ngekhulu le-15 kusiya kwele-17. Ababusi bayo babexhumene lokuhweba kwesigaba lesikude, futhi izinto zakudala zembula izinto ezavela kwamanye amazwe kanye lezinto zomphakathi wendawo. IKhami iyisigaba esiqakathekileyo esalandela isiko lokwakha ngamatshe eZimbabwe.",
            "culture": "IKhami itshengisa amandla ezombusazwe, ukuhleleka kwemizi, ubuciko kanye lokuxhumana kwezokuhweba kwemiphakathi yaseNingizimu-Ntshonalanga yeZimbabwe. Izakhiwo zayo ziqhubekisa isiko leZimbabwe kodwa zigcizelela amathala aphakemeyo kanye lemiduli yokubamba umhlabathi ehlotshisiwe.",
            "features": [
                "Amathala alemiduli yamatshe akhiwe ehambisana lendawo, adala izindawo eziphakemeyo.",
                "Imiduli yamatshe ehlotshiswe ngamaphetheni ahlukileyo.",
                "I-Hill Complex lamanye amapulatifomu atshengisa ubuciko bokuhlanganisa izakhiwo lendawo yemvelo.",
                "Ubufakazi bokuhweba okude, obuhlanganisa ceramics ezavela kwamanye amazwe.",
                "Isiko lokwakha elixhumene leGreat Zimbabwe kodwa elisebenzisa amathala lemiduli yokubamba umhlabathi kakhulu.",
            ],
            "unesco": "I-UNESCO yabhalisa iKhami Ruins National Monument ngo-1986 ngaphansi kwemigomo (iii) kanye (iv), iyibona njengobufakazi obukhulu besiko kanye lesibonelo esiphakemeyo seqoqo lezakhiwo lesigaba esiqakathekileyo emlandweni weSouthern Africa.",
            "protection": [
                "Ungagibeli loba uhambe phezu kwemiduli yamathala ebuthakathaka.",
                "Gcina izihlahla, ingcekeza lomlilo kude lezakhiwo futhi ulandele imithetho yendawo.",
                "Ungasusi izitsha zobumba, ubuhlalu, amatshe loba ezinye izinto.",
                "Hamba ngemizila ebekiweyo ukuze unciphise ukuguguleka komhlabathi.",
                "Ungakwenyi, uhlele kabutsha loba wakhe kabutsha amatshe amadala.",
            ],
            "facts": [
                "IKhami yaba yindawo enkulu yezombusazwe ngemva kokwehla kweGreat Zimbabwe.",
                "Ixhumene kakhulu lombuso weTorwa kanye lesiko leZimbabwe elalandelayo.",
                "Amathala ayo amanengi ayenza ibonakale ihlukile emidulini edume kakhulu yeGreat Zimbabwe.",
                "Izinto ezavela kwamanye amazwe zitshengisa ukuthi iKhami yayixhumene lezindlela ezinkulu zokuhweba.",
            ],
            "significance": "IKhami itshengisa ukuthi isiko lokwakha ngamatshe eZimbabwe laqhubeka futhi laguquka. Amathala ayo, ubuciko bemiduli kanye lobufakazi bokuhweba kutshengisa ukusungula, hatshi ukukopa iGreat Zimbabwe kuphela.",
        },
        "Shona": {
            "name": "Khami Ruins",
            "subtitle": "Guta rematombo rine terraces renguva yeTorwa, richiratidza decorative masonry nenhoroondo yekutengeserana.",
            "location": "Pedyo neBulawayo, kumadokero kweZimbabwe",
            "inscribed": "1986",
            "criteria": "(iii), (iv)",
            "history": "Khami yakasimukira mushure mekuderera kweGreat Zimbabwe ikava guta guru reTorwa state, kunyanya kubva muzana remakore rechi15 kusvika rechi17. Vatongi vayo vaive mu regional ne long-distance trade, uye archaeology yakawana zvinhu zvakabva kunze pamwe nezvemuno. Khami inomiririra chikamu chakakosha chakazotevera muZimbabwe stone-building tradition.",
            "culture": "Khami inoratidza political authority, kurongeka kwemisha, craftsmanship uye trading connections dzemunharaunda dzekumaodzanyemba-kumadokero kweZimbabwe. Architecture yayo inoenderera neZimbabwe cultural tradition asi ine emphasis yakasiyana pamapuratifomu e terraces nemadziro ekutsigira akashongedzwa.",
            "features": [
                "Stone-faced terraces dzakavakwa dzichitevera terrain, dzichiita mapuratifomu akakwirira.",
                "Decorative dry-stone wall patterns ane maitiro akasiyana anopa runako rwakanyanya.",
                "Hill Complex nemamwe mapuratifomu anoratidza kugadziriswa kwearchitecture zvinoenderana nenzvimbo.",
                "Archaeological evidence ye long-distance trade, kusanganisira imported ceramics nezvimwe zvinhu zvinokosha.",
                "Building tradition ine hukama neGreat Zimbabwe asi ine terraces nem retaining walls zvakawanda.",
            ],
            "unesco": "UNESCO yakanyoresa Khami Ruins National Monument muna 1986 pasi pecriteria (iii) ne(iv), ichiona Khami sehumbowo hwakasarudzika hwetsika uye muenzaniso wakanaka we architectural ensemble yechikamu chakakosha munhoroondo yeSouthern Africa.",
            "protection": [
                "Usakwira kana kufamba pamusoro pemadziro e terraces asina kusimba.",
                "Chengetedza vegetation, marara nemoto kure nezvivakwa uye tevera mirayiro yenzvimbo.",
                "Usabvisa pottery, beads, matombo kana zvimwe zvinhu kunyange zviri loose.",
                "Shandisa designated paths kuderedza erosion pamativi e terraces.",
                "Usakwenya, kurongazve kana kuvakazve ancient stonework.",
            ],
            "facts": [
                "Khami yakava political centre yakakosha mushure mekuderera kweGreat Zimbabwe.",
                "Yakabatana zvikuru neTorwa state uye later Zimbabwe cultural tradition.",
                "Terracing yayo yakawanda inoipa chitarisiko chakasiyana nemadziro anonyanya kuzivikanwa eGreat Zimbabwe.",
                "Imported objects dzakawanikwa nearchaeology dzinoratidza kubatana ne trade networks dzakakura.",
            ],
            "significance": "Khami inoratidza kuti Zimbabwe stone-building tradition yakaramba ichienderera uye ichichinja. Terraces, decorative masonry uye trade evidence zvinoratidza innovation, kwete kungotevedzera Great Zimbabwe.",
        },
    },
}

# -----------------------------
# Quiz bank — fully translated
# -----------------------------
QUIZ = {
    "English": [
        {"q": "Which ROBO GUIDE site is especially famous for a very high concentration of rock art?", "options": ["Khami Ruins", "Matobo Hills", "Great Zimbabwe", "Victoria Falls"], "answer": 1, "why": "Matobo Hills contains an exceptional concentration of prehistoric rock paintings in caves and shelters."},
        {"q": "In which year was Matobo Hills inscribed on the UNESCO World Heritage List?", "options": ["1980", "1986", "2003", "2010"], "answer": 2, "why": "Matobo Hills was inscribed in 2003 under cultural criteria (iii), (v) and (vi)."},
        {"q": "Which feature is found at Great Zimbabwe?", "options": ["Conical Tower", "Victoria Falls bridge", "Stone Age cave paintings only", "Modern concrete terraces"], "answer": 0, "why": "The Conical Tower stands inside the Great Enclosure and is one of Great Zimbabwe's most recognizable features."},
        {"q": "What construction technique is strongly associated with Great Zimbabwe's monumental walls?", "options": ["Dry-stone masonry without mortar", "Reinforced concrete", "Fired brick and cement", "Steel-frame construction"], "answer": 0, "why": "The walls use carefully selected and stacked stone without mortar — evidence of remarkable building skill."},
        {"q": "The carved Zimbabwe Birds are most strongly associated with which site?", "options": ["Matobo Hills", "Khami Ruins", "Great Zimbabwe", "Mana Pools"], "answer": 2, "why": "Soapstone Zimbabwe Birds were found at Great Zimbabwe and the bird became a major national emblem."},
        {"q": "Khami is especially associated with which historical state?", "options": ["Torwa", "Roman", "Mali", "Aztec"], "answer": 0, "why": "Khami became an important centre and capital of the Torwa state after Great Zimbabwe declined."},
        {"q": "Which architectural feature visually distinguishes Khami?", "options": ["Extensive stone-faced terraces", "Pyramids", "Mud skyscrapers", "Roman arches"], "answer": 0, "why": "Khami is famous for terraced platforms and decorative retaining walls adapted to the landscape."},
        {"q": "What is the safest behaviour near ancient rock art?", "options": ["Wet it to make colours brighter", "Trace it with chalk", "Do not touch it", "Rub the surface clean"], "answer": 2, "why": "Touching, wetting or tracing rock art can damage fragile surfaces and pigments. Observe without contact."},
        {"q": "Why is long-distance trade important to understanding Great Zimbabwe and Khami?", "options": ["It proves the sites were modern", "It shows links to wider regional and overseas exchange networks", "It means nobody lived there", "It explains the rock paintings"], "answer": 1, "why": "Imported goods and trade evidence show that these centres participated in broad African and Indian Ocean exchange networks."},
        {"q": "What should a visitor do near a protected heritage area?", "options": ["Respect the marked boundary and follow site guidance", "Climb over the barrier", "Touch the exhibit quickly", "Remove a small souvenir"], "answer": 0, "why": "Marked boundaries and visitor guidance help protect sensitive heritage from accidental damage."},
    ],
    "isiNdebele": [
        {"q": "Yiphi indawo ye-ROBO GUIDE edume kakhulu ngobunengi bemidwebo emadwaleni?", "options": ["IKhami Ruins", "IMatobo Hills", "IGreat Zimbabwe", "IVictoria Falls"], "answer": 1, "why": "IMatobo Hills ilobunengi obumangalisayo bemidwebo yakudala emigedeni lezindawo zokukhosela."},
        {"q": "IMatobo Hills yabhaliswa nini ku-UNESCO World Heritage List?", "options": ["1980", "1986", "2003", "2010"], "answer": 2, "why": "IMatobo Hills yabhaliswa ngo-2003 ngaphansi kwemigomo (iii), (v) kanye (vi)."},
        {"q": "Yisiphi isici esitholakala eGreat Zimbabwe?", "options": ["IConical Tower", "Ibholoho leVictoria Falls", "Imidwebo yemigede kuphela", "Amathala econcrete"], "answer": 0, "why": "IConical Tower ingaphakathi kweGreat Enclosure futhi ingenye yezinto ezaziwa kakhulu eGreat Zimbabwe."},
        {"q": "Imiduli emikhulu yeGreat Zimbabwe yakhiwa njani?", "options": ["Ngamatshe ngaphandle kwe-mortar", "Ngeconcrete elensimbi", "Ngezitina lesamende", "Ngensimbi kuphela"], "answer": 0, "why": "Amatshe akhethwa futhi abekwa ngobuciko ngaphandle kodaka lwe-mortar."},
        {"q": "IZimbabwe Birds ezibazwe ngesoapstone zihlotshaniswa kakhulu layiphi indawo?", "options": ["IMatobo", "IKhami", "IGreat Zimbabwe", "IMana Pools"], "answer": 2, "why": "IZimbabwe Birds zatholakala eGreat Zimbabwe futhi inyoni yaba luphawu olukhulu lwesizwe."},
        {"q": "IKhami ihlotshaniswa kakhulu lawuphi umbuso wakudala?", "options": ["ITorwa", "IRoma", "IMali", "IAztec"], "answer": 0, "why": "IKhami yaba yindawo enkulu yombuso weTorwa ngemva kokwehla kweGreat Zimbabwe."},
        {"q": "Yini ebonakala kakhulu ezakhiweni zeKhami?", "options": ["Amathala amanengi ahlanganiswe lamatshe", "Amaphiramidi", "Izindlu ezinde zodaka", "Ama-arches eRoma"], "answer": 0, "why": "IKhami idume ngamathala aphakemeyo lemiduli yokubamba umhlabathi ehlotshisiwe."},
        {"q": "Kumele wenzeni eduze komdwebo wakudala edwaleni?", "options": ["Uwumanzise", "Uwucupe ngechalk", "Ungawuthinti", "Uwuhlikihle"], "answer": 2, "why": "Ukuthinta, ukumanzisa loba ukucupha imidwebo kungayonakalisa. Bukela ngaphandle kokuthinta."},
        {"q": "Kungani ubufakazi bokuhweba okude buqakathekile eGreat Zimbabwe laseKhami?", "options": ["Butshengisa ukuthi izindawo zintsha", "Butshengisa ukuxhumana lezindlela zokuhweba ezibanzi", "Butshengisa ukuthi akulamuntu owake wahlala khona", "Buchaza imidwebo yemigede"], "answer": 1, "why": "Izinto ezivela kude zitshengisa ukuxhumana lezindlela ezinkulu zokuhweba eAfrica kanye le-Indian Ocean."},
        {"q": "Isivakashi kumele senzeni nxa i-IR warning ye-ROBO GUIDE ikhala?", "options": ["Sihlehle sibuyele ngemva komngcele", "Singayinaki", "Sithinte umbukiso masinyane", "Sikhiphe isensor"], "answer": 0, "why": "Isixwayiso sikhuthaza isivakashi ukuthi sihlehle ukuze sivikele amagugu."},
    ],
    "Shona": [
        {"q": "Ndeipi nzvimbo yeROBO GUIDE inonyanya kuzivikanwa nekuwanda kwe rock art?", "options": ["Khami Ruins", "Matobo Hills", "Great Zimbabwe", "Victoria Falls"], "answer": 1, "why": "Matobo Hills ine huwandu hwakanyanya hwe prehistoric rock paintings mumapako nemarock shelters."},
        {"q": "Matobo Hills yakanyoreswa riini paUNESCO World Heritage List?", "options": ["1980", "1986", "2003", "2010"], "answer": 2, "why": "Matobo Hills yakanyoreswa muna 2003 pasi pecriteria (iii), (v) ne(vi)."},
        {"q": "Ndechipi chinhu chinowanikwa kuGreat Zimbabwe?", "options": ["Conical Tower", "Victoria Falls bridge", "Rock paintings chete", "Concrete terraces"], "answer": 0, "why": "Conical Tower iri mukati meGreat Enclosure uye ndeimwe yezviratidzo zvinozivikanwa zveGreat Zimbabwe."},
        {"q": "Madziro makuru eGreat Zimbabwe akavakwa nenzira ipi?", "options": ["Dry-stone masonry pasina mortar", "Reinforced concrete", "Brick necement", "Steel frame"], "answer": 0, "why": "Matombo akasarudzwa nekuiswa nehunyanzvi pasina mortar."},
        {"q": "Zimbabwe Birds dzakavezwa musoapstone dzinonyanya kubatanidzwa nenzvimbo ipi?", "options": ["Matobo", "Khami", "Great Zimbabwe", "Mana Pools"], "answer": 2, "why": "Zimbabwe Birds dzakawanikwa kuGreat Zimbabwe uye shiri yakazova chiratidzo chikuru chenyika."},
        {"q": "Khami inonyanya kubatanidzwa neipi historical state?", "options": ["Torwa", "Roman", "Mali", "Aztec"], "answer": 0, "why": "Khami yakava centre yakakosha yeTorwa state mushure mekuderera kweGreat Zimbabwe."},
        {"q": "Ndechipi architectural feature chinonyanya kusiyanisa Khami?", "options": ["Stone-faced terraces dzakawanda", "Pyramids", "Mud skyscrapers", "Roman arches"], "answer": 0, "why": "Khami inozivikanwa nema terraced platforms nemadziro ekutsigira akashongedzwa."},
        {"q": "Mushanyi anofanira kuita sei pedyo ne ancient rock art?", "options": ["Kuinyorovesa", "Ku tracing nechalk", "Kusai bata", "Kukwesha pamusoro"], "answer": 2, "why": "Kubata, kunyorovesa kana tracing kunogona kukuvadza pigments nesurface. Tarisa pasina contact."},
        {"q": "Sei long-distance trade evidence yakakosha paGreat Zimbabwe neKhami?", "options": ["Inoratidza kuti nzvimbo itsva", "Inoratidza kubatana ne wider exchange networks", "Inoratidza kuti hapana aigara ipapo", "Inotsanangura rock paintings"], "answer": 1, "why": "Imported goods dzinoratidza kubatana kwecentres idzi neAfrican neIndian Ocean trade networks."},
        {"q": "Mushanyi anofanira kuita sei pedyo nenzvimbo yenhaka yakachengetedzwa?", "options": ["Kuremekedza muganhu wakatarwa uye kutevera mirayiridzo", "Kukwira pamusoro pebarrier", "Kubata exhibit nekukurumidza", "Kutora chinhu chidiki sechirangaridzo"], "answer": 0, "why": "Miganhu yakatarwa nemirayiridzo yevashanyi zvinobatsira kudzivirira kukuvadzwa kwenhaka."},
    ],
}

# -----------------------------
# Rule-based assistant knowledge
# -----------------------------
ASSISTANT_KB = {
    "English": {
        "matobo_history": "Matobo Hills is an ancient cultural landscape. Archaeology and rock paintings preserve evidence of Stone Age hunter-gatherer life, later farming communities and long cultural continuity. It also carries major Ndebele historical and spiritual associations.",
        "matobo_rockart": "Matobo Hills has one of southern Africa's highest concentrations of rock art. Paintings occur in caves and rock shelters and often show humans, animals, hunting and other activities. Their value is both artistic and archaeological because they help reconstruct past lifeways.",
        "matobo_caves": "Matobo's granite landscape creates many natural caves and rock shelters. These shelters protected paintings and archaeological deposits from weather, which is one reason the area preserves such a rich record of past human activity.",
        "matobo_spiritual": "Matobo is a living sacred landscape. Shrines, oral traditions, ancestral associations, rain-making traditions and the Mwari religious tradition remain important. Heritage protection therefore includes respect for living beliefs, not only the physical rocks and paintings.",
        "matobo_unesco": "Matobo Hills was inscribed by UNESCO in 2003 under cultural criteria (iii), (v) and (vi), recognizing its rock art, long interaction between people and landscape, and continuing religious significance.",
        "great_history": "Great Zimbabwe flourished mainly between about the 11th and 15th centuries. It became a major political, economic and cultural centre and was built by ancestors of Shona-speaking communities. Its scale reflects organized leadership, specialist skills and a prosperous society.",
        "great_builders": "Great Zimbabwe was built by African communities — ancestors of Shona-speaking peoples. Modern archaeology rejects old colonial claims that tried to attribute the monument to outsiders.",
        "great_architecture": "Great Zimbabwe is famous for sophisticated dry-stone masonry built without mortar. Major zones include the Hill Complex, Great Enclosure and Valley Ruins. The Great Enclosure contains massive curved walls, passages and the well-known Conical Tower.",
        "great_birds": "The Zimbabwe Birds are carved soapstone bird sculptures found at Great Zimbabwe. They probably carried elite or spiritual meaning. Their image later became one of Zimbabwe's strongest national symbols and appears on the national flag and emblem.",
        "great_trade": "Great Zimbabwe participated in long-distance trade. Archaeological finds include local craft products and imported goods that link the centre to wider African and Indian Ocean exchange networks. Gold and other regional products were important within these systems.",
        "great_unesco": "Great Zimbabwe National Monument was inscribed by UNESCO in 1986 under criteria (i), (iii) and (vi). UNESCO recognizes its architectural achievement, testimony to a major African civilization and powerful historical significance.",
        "khami_history": "Khami became prominent after Great Zimbabwe declined and served as the capital of the Torwa state, especially from the 15th into the 17th century. It represents a later phase of the broader Zimbabwe cultural and stone-building tradition.",
        "khami_architecture": "Khami is especially known for stone-faced terraces, retaining walls and decorative dry-stone patterns. Its builders adapted platforms to the landscape, producing an architectural style related to Great Zimbabwe but visually distinct.",
        "khami_trade": "Khami participated in regional and long-distance trade. Imported ceramics and other prestige goods found archaeologically show that its elite had access to wider exchange networks while maintaining strong local cultural traditions.",
        "khami_torwa": "Khami is strongly associated with the Torwa state. The Torwa rulers controlled an important political and economic centre in south-western Zimbabwe after Great Zimbabwe's decline.",
        "khami_unesco": "Khami Ruins National Monument was inscribed by UNESCO in 1986 under criteria (iii) and (iv), recognizing its cultural testimony and outstanding architectural ensemble.",
        "conservation": "ROBO GUIDE promotes responsible heritage visits: do not touch rock art, do not climb ancient walls, do not remove artifacts, remain on designated paths, avoid graffiti and litter, and respect sacred or restricted places.",
        "comparison_gz_khami": "Great Zimbabwe and Khami belong to related Zimbabwe stone-building traditions, but they are not identical. Great Zimbabwe is earlier and is famous for monumental freestanding dry-stone walls such as the Great Enclosure; Khami rose later and is especially known for extensive terraced platforms, retaining walls and decorative masonry. Both show political organization, skilled construction and long-distance trade.",
        "comparison_all": "Matobo, Great Zimbabwe and Khami tell different but complementary stories. Matobo is a living granite cultural landscape famous for rock art, archaeology and sacred traditions. Great Zimbabwe is a monumental medieval stone centre tied to Shona history, statecraft and long-distance trade. Khami is a later Torwa-era stone city distinguished by terraces and decorative masonry. Together they show the depth and diversity of Zimbabwean heritage.",
    },
    "isiNdebele": {
        "matobo_history": "IMatobo Hills yindawo yamasiko yakudala. Izinto zakudala lemidwebo emadwaleni kugcina ubufakazi bempilo yeStone Age, imiphakathi yabalimi eyalandelayo kanye lomlando omude. Indawo ilobudlelwano obukhulu lomlando wamaNdebele kanye lokomoya.",
        "matobo_rockart": "IMatobo ilobunengi obukhulu bemidwebo emadwaleni eSouthern Africa. Imidwebo isemigedeni lezindawo zokukhosela futhi itshengisa abantu, izinyamazana, ukuzingela kanye lezinye izenzo zakudala.",
        "matobo_caves": "Amadwala egranite eMatobo adala imigede lezindawo zokukhosela eziningi. Lezindawo zanceda ukuvikela imidwebo kanye lobufakazi bezinto zakudala esimeni sezulu.",
        "matobo_spiritual": "IMatobo yindawo engcwele ephilayo. Izindawo zokukhulekela, izindaba zomlomo, ubudlelwano labokhokho, ukucela izulu kanye lenkolelo kaMwari kusaqakathekile.",
        "matobo_unesco": "IMatobo Hills yabhaliswa yi-UNESCO ngo-2003 ngaphansi kwemigomo (iii), (v) kanye (vi).",
        "great_history": "IGreat Zimbabwe yachuma kakhulu phakathi kwekhulu le-11 lele-15. Yaba yindawo enkulu yezombusazwe, ezomnotho lamasiko, yakhiwa ngokhokho bemiphakathi ekhuluma isiShona.",
        "great_builders": "IGreat Zimbabwe yakhiwa yimiphakathi yaseAfrica — okhokho babantu abakhuluma isiShona. Ubufakazi bezinto zakudala buyayiphika imibono yakudala eyayithi yakhiwa ngabantu bangaphandle.",
        "great_architecture": "IGreat Zimbabwe idume ngokwakhiwa ngamatshe ngaphandle kwe-mortar. Izingxenye ezinkulu yiHill Complex, Great Enclosure kanye leValley Ruins. IGreat Enclosure ilodonga olukhulu, imizila kanye leConical Tower.",
        "great_birds": "IZimbabwe Birds yizinyoni ezibazwe ngesoapstone ezatholakala eGreat Zimbabwe. Zaba luphawu olukhulu lwesizwe seZimbabwe.",
        "great_trade": "IGreat Zimbabwe yayixhumene lokuhweba okude. Izinto ezatholakala khona zitshengisa ukuxhumana lezindlela zokuhweba zaseAfrica kanye le-Indian Ocean.",
        "great_unesco": "IGreat Zimbabwe National Monument yabhaliswa yi-UNESCO ngo-1986 ngaphansi kwemigomo (i), (iii) kanye (vi).",
        "khami_history": "IKhami yakhula ngemva kokwehla kweGreat Zimbabwe yaba yinhloko yombuso weTorwa kusukela ikakhulu ngekhulu le-15 kusiya kwele-17.",
        "khami_architecture": "IKhami idume ngamathala alemiduli yamatshe, retaining walls kanye lamaphetheni amahle e-dry-stone. Lokhu kuyenza yehluke ngokubukeka eGreat Zimbabwe.",
        "khami_trade": "IKhami yayixhumene lokuhweba kwesigaba lesikude. Izinto ezavela kwamanye amazwe ezatholakala ngabavubukuli zitshengisa lobu budlelwano.",
        "khami_torwa": "IKhami ihlotshaniswa kakhulu lombuso weTorwa, owawulendawo eqakathekileyo yezombusazwe lezomnotho eNingizimu-Ntshonalanga yeZimbabwe.",
        "khami_unesco": "IKhami Ruins National Monument yabhaliswa yi-UNESCO ngo-1986 ngaphansi kwemigomo (iii) kanye (iv).",
        "conservation": "I-ROBO GUIDE ikhuthaza ukuvakasha okuhlonipha amagugu: ungathinti imidwebo, ungagibeli imiduli, ungasusi izinto zakudala, hamba ngemizila evunyelweyo, ungabhali emadwaleni futhi uhloniphe izindawo ezingcwele.",
        "comparison_gz_khami": "IGreat Zimbabwe leKhami zixhumene lesiko lokwakha ngamatshe eZimbabwe kodwa azifanani. IGreat Zimbabwe indala futhi idume ngemiduli emikhulu efana leGreat Enclosure; iKhami yalandela futhi idume ngamathala, retaining walls kanye lobuciko bemiduli. Zombili zitshengisa ubukhokheli, amakhono okuwakha kanye lokuhweba okude.",
        "comparison_all": "IMatobo, Great Zimbabwe leKhami zilandisa izindaba ezitshiyeneyo. IMatobo yindawo yamasiko ephilayo edume ngemidwebo, izinto zakudala kanye lezindawo ezingcwele. IGreat Zimbabwe yindawo enkulu yamatshe ehlotshaniswa lomlando wamaShona, ubukhokheli lokuhweba. IKhami yidolobho leTorwa elidume ngamathala lemiduli ehlotshisiwe.",
    },
    "Shona": {
        "matobo_history": "Matobo Hills inzvimbo yekare yetsika. Archaeology ne rock paintings zvinochengeta humbowo hweStone Age hunter-gatherers, mapoka evarimi akazotevera uye kuenderera kwetsika. Inewo hukama hwakasimba nenhoroondo yeNdebele netsika dzemweya.",
        "matobo_rockart": "Matobo ine imwe yehuwandu hukuru hwe rock art muSouthern Africa. Paintings dziri mumapako nemarock shelters uye dzinoratidza vanhu, mhuka, kuvhima nezvimwe zviitiko zvekare.",
        "matobo_caves": "Granite landscape yeMatobo inogadzira mapako nemarock shelters akawanda. Aya akabatsira kuchengetedza paintings ne archaeological deposits kubva kumamiriro ekunze.",
        "matobo_spiritual": "Matobo inzvimbo inoyera ichiri kurarama. Shrines, oral traditions, madzitateguru, tsika dzekukumbira mvura uye Mwari religious tradition zvichiri kukosha.",
        "matobo_unesco": "Matobo Hills yakanyoreswa neUNESCO muna 2003 pasi pecriteria (iii), (v) ne(vi).",
        "great_history": "Great Zimbabwe yakanyanya kubudirira pakati pezvinenge zana remakore rechi11 nerechi15. Yakava centre huru yezvematongerwo enyika, hupfumi netsika uye yakavakwa nemadzitateguru evanhu vanotaura Shona.",
        "great_builders": "Great Zimbabwe yakavakwa neAfrican communities — madzitateguru evanhu vanotaura Shona. Archaeology yemazuva ano inoramba pfungwa dzekare dzaiti yakavakwa nevatorwa.",
        "great_architecture": "Great Zimbabwe inozivikanwa nedry-stone masonry pasina mortar. Nzvimbo huru dzinosanganisira Hill Complex, Great Enclosure neValley Ruins. Great Enclosure ine madziro makuru, passages neConical Tower.",
        "great_birds": "Zimbabwe Birds ishiri dzakavezwa musoapstone dzakawanikwa kuGreat Zimbabwe. Dzakatova chiratidzo chakakosha chenyika yeZimbabwe.",
        "great_trade": "Great Zimbabwe yaive mu long-distance trade. Zvakawanikwa ne archaeology zvinoratidza kubatana neAfrican neIndian Ocean exchange networks.",
        "great_unesco": "Great Zimbabwe National Monument yakanyoreswa neUNESCO muna 1986 pasi pecriteria (i), (iii) ne(vi).",
        "khami_history": "Khami yakasimukira mushure mekuderera kweGreat Zimbabwe ikava capital yeTorwa state, kunyanya kubva muzana remakore rechi15 kusvika rechi17.",
        "khami_architecture": "Khami inozivikanwa nema stone-faced terraces, retaining walls uye decorative dry-stone patterns. Izvi zvinoipa style yakasiyana neGreat Zimbabwe.",
        "khami_trade": "Khami yaive mu regional ne long-distance trade. Imported ceramics nezvimwe prestige goods zvinoratidza kubatana kwayo ne wider exchange networks.",
        "khami_torwa": "Khami yakabatana zvikuru neTorwa state, yaive political ne economic centre yakakosha kumaodzanyemba-kumadokero kweZimbabwe.",
        "khami_unesco": "Khami Ruins National Monument yakanyoreswa neUNESCO muna 1986 pasi pecriteria (iii) ne(iv).",
        "conservation": "ROBO GUIDE inokurudzira kushanya kunoremekedza nhaka: usabata rock art, usakwira madziro ekare, usabvisa artifacts, shandisa designated paths, usaite graffiti kana kurasa marara uye remekedza nzvimbo dzinoyera.",
        "comparison_gz_khami": "Great Zimbabwe neKhami zviri muZimbabwe stone-building tradition asi hazvina kufanana. Great Zimbabwe yakatanga uye inozivikanwa nemadziro makuru akaita seGreat Enclosure; Khami yakazotevera uye inonyanya kuzivikanwa nema terraces, retaining walls ne decorative masonry. Dzose dzinoratidza political organization, building skill ne long-distance trade.",
        "comparison_all": "Matobo, Great Zimbabwe neKhami dzinotaura nyaya dzakasiyana dzinowirirana. Matobo inzvimbo yegranite inorarama netsika, yakakurumbira ne rock art, archaeology ne sacred traditions. Great Zimbabwe iguta guru rematombo rakabatana neShona history, statecraft ne trade. Khami iguta reTorwa rakazotevera, rinozivikanwa nema terraces ne decorative masonry.",
    },
}

# -----------------------------
# Helpers
# -----------------------------
def tr(key):
    return UI[st.session_state.lang][key]


def go(page):
    st.session_state.page = page
    st.rerun()


def normalize(text):
    return re.sub(r"[^a-z0-9\s]", " ", text.lower()).strip()


def any_phrase(text, phrases):
    return any(p in text for p in phrases)


def assistant_answer(question, lang):
    q = normalize(question)
    kb = ASSISTANT_KB[lang]

    # comparison intent first
    compare_words = ["compare", "difference", "similar", "qhathanisa", "umehluko", "fanana", "enzanisa", "musiyano", "zvakafanana"]
    if any_phrase(q, compare_words):
        has_great = any_phrase(q, ["great zimbabwe", "great"])
        has_khami = "khami" in q
        has_matobo = "matobo" in q
        if has_great and has_khami and not has_matobo:
            return kb["comparison_gz_khami"]
        if sum([has_great, has_khami, has_matobo]) >= 2:
            return kb["comparison_all"]

    # global conservation
    if any_phrase(q, ["protect", "protection", "conservation", "preserve", "damage", "touch", "visitor", "vikela", "ukuvikela", "thinta", "chengetedza", "kuchengetedza", "bata", "muganhu"]):
        return kb["conservation"]

    # Matobo intents
    if "matobo" in q or any_phrase(q, ["rock art", "rock painting", "cave painting", "umdwembo", "imidwebo", "mapako", "mifananidzo yematombo"]):
        if any_phrase(q, ["unesco", "world heritage", "inscribed", "criteria", "bhaliswa", "nyoreswa"]):
            return kb["matobo_unesco"]
        if any_phrase(q, ["cave", "shelter", "umgede", "imigede", "pako", "mapako"]):
            return kb["matobo_caves"]
        if any_phrase(q, ["rock art", "painting", "paintings", "imidwebo", "umdwebo", "mifananidzo"]):
            return kb["matobo_rockart"]
        if any_phrase(q, ["spirit", "sacred", "religion", "mwari", "shrine", "ancestor", "okungcwele", "amadlozi", "inhlanganiso", "mweya", "madzitateguru", "inoyera"]):
            return kb["matobo_spiritual"]
        return kb["matobo_history"]

    # Great Zimbabwe intents
    if any_phrase(q, ["great zimbabwe", "great enclosure", "conical tower", "zimbabwe bird", "zimbabwe birds"]):
        if any_phrase(q, ["who built", "builder", "built by", "ngubani", "owakha", "ndiani", "akavaka", "vakavaka"]):
            return kb["great_builders"]
        if any_phrase(q, ["bird", "birds", "inyoni", "izinyoni", "shiri"]):
            return kb["great_birds"]
        if any_phrase(q, ["trade", "trading", "gold", "import", "kutengeserana", "ukuhweba"]):
            return kb["great_trade"]
        if any_phrase(q, ["wall", "architecture", "enclosure", "tower", "masonry", "stone", "udonga", "imiduli", "izakhiwo", "madziro", "zvivakwa", "matombo"]):
            return kb["great_architecture"]
        if any_phrase(q, ["unesco", "world heritage", "inscribed", "criteria", "bhaliswa", "nyoreswa"]):
            return kb["great_unesco"]
        return kb["great_history"]

    # Khami intents
    if "khami" in q or "torwa" in q:
        if any_phrase(q, ["torwa", "ruler", "state", "kingdom", "umbuso", "hurumende"]):
            return kb["khami_torwa"]
        if any_phrase(q, ["trade", "trading", "import", "ceramic", "kutengeserana", "ukuhweba"]):
            return kb["khami_trade"]
        if any_phrase(q, ["terrace", "terraces", "architecture", "wall", "decorative", "stonework", "masonry", "amathala", "imiduli", "izakhiwo", "madziro", "matombo"]):
            return kb["khami_architecture"]
        if any_phrase(q, ["unesco", "world heritage", "inscribed", "criteria", "bhaliswa", "nyoreswa"]):
            return kb["khami_unesco"]
        return kb["khami_history"]

    # topic without explicit site — route to comparative / relevant answers
    if any_phrase(q, ["builder", "built", "who built", "ngubani owakha", "ndiani akavaka"]):
        return kb["great_builders"]
    if any_phrase(q, ["bird", "birds", "zimbabwe bird", "inyoni", "shiri"]):
        return kb["great_birds"]
    if any_phrase(q, ["terrace", "torwa", "amathala"]):
        return kb["khami_architecture"] + " " + kb["khami_torwa"]
    if any_phrase(q, ["rock art", "painting", "cave", "imidwebo", "imigede", "mapako"]):
        return kb["matobo_rockart"]
    if any_phrase(q, ["trade", "trading", "kutengeserana", "ukuhweba"]):
        return kb["great_trade"] + " " + kb["khami_trade"]
    if any_phrase(q, ["unesco", "world heritage"]):
        return kb["comparison_all"] + " " + kb["great_unesco"] + " " + kb["khami_unesco"] + " " + kb["matobo_unesco"]

    return UI[lang]["no_answer"]


def render_list(items, icon="◆"):
    for item in items:
        st.markdown(f"{icon} {item}")


def reset_quiz():
    st.session_state.quiz_index = 0
    st.session_state.quiz_score = 0
    st.session_state.quiz_points = 0
    st.session_state.quiz_answered = False
    st.session_state.quiz_selected = None
    st.session_state.quiz_feedback = None
    st.session_state.quiz_finished = False

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown(
        f"""
        <div class="rg-brand">
            <div style="font-size:2.3rem">🤖🗿</div>
            <h2>ROBO GUIDE</h2>
            <p>{tr('tagline')}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    old_lang = st.session_state.lang
    new_lang = st.selectbox(
        tr("language"),
        ["English", "isiNdebele", "Shona"],
        index=["English", "isiNdebele", "Shona"].index(old_lang),
        key="language_selector",
    )
    if new_lang != old_lang:
        st.session_state.lang = new_lang
        reset_quiz()
        st.session_state.chat = []
        st.rerun()

    st.markdown(f"### {tr('nav')}")
    nav_items = [
        ("Home", "🏠", tr("home")),
        ("Matobo Hills", "🪨", tr("matobo")),
        ("Great Zimbabwe", "🏛️", tr("great")),
        ("Khami Ruins", "🧱", tr("khami")),
        ("Heritage Challenge", "🏆", tr("quiz")),
        ("Heritage Assistant", "💬", tr("assistant")),
    ]
    for target, icon, label in nav_items:
        active = st.session_state.page == target
        if st.button(f"{icon}  {label}", key=f"nav_{target}", use_container_width=True, type="primary" if active else "secondary"):
            go(target)

    st.markdown("---")
    st.caption("WRO 2026 • Zimbabwe National Finals")
    st.caption("Theme: Robots Meet Culture")

# -----------------------------
# Page: Home
# -----------------------------
def page_home():
    st.markdown(
        f"""
        <div class="rg-hero">
            <div class="rg-kicker">{tr('tagline')}</div>
            <h1>ROBO GUIDE</h1>
            <h2 style="margin:4px 0 9px;color:#E4C794">{tr('hero_title')}</h2>
            <p>{tr('hero_text')}</p>
            <div class="rg-badges">
                <span class="rg-badge">🌍 English</span>
                <span class="rg-badge">🗣️ isiNdebele</span>
                <span class="rg-badge">💬 Shona</span>
                <span class="rg-badge">🏆 Heritage Challenge</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="rg-stat"><div class="n">3</div><div class="l">UNESCO heritage experiences</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="rg-stat"><div class="n">3</div><div class="l">Visitor languages</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="rg-stat"><div class="n">1</div><div class="l">Interactive heritage learning</div></div>', unsafe_allow_html=True)

    st.markdown(f'<div class="rg-section-title">{tr("explore")}</div><div class="rg-section-sub">{tr("explore_sub")}</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    site_summaries = {
        "Matobo Hills": {
            "English": "Rock art • sacred landscape • caves • granite hills",
            "isiNdebele": "Imidwebo emadwaleni • indawo engcwele • imigede • amagquma",
            "Shona": "Rock art • nzvimbo dzinoyera • mapako • zvikomo zvegranite",
        },
        "Great Zimbabwe": {
            "English": "Great Enclosure • Zimbabwe Birds • stone architecture • trade",
            "isiNdebele": "Great Enclosure • Zimbabwe Birds • izakhiwo zamatshe • ukuhweba",
            "Shona": "Great Enclosure • Zimbabwe Birds • stone architecture • trade",
        },
        "Khami Ruins": {
            "English": "Terraces • Torwa history • decorative stonework • trade",
            "isiNdebele": "Amathala • umlando weTorwa • ubuciko bamatshe • ukuhweba",
            "Shona": "Terraces • nhoroondo yeTorwa • decorative stonework • trade",
        },
    }
    for col, site in zip(cols, ["Matobo Hills", "Great Zimbabwe", "Khami Ruins"]):
        s = SITES[site][st.session_state.lang]
        with col:
            st.markdown(
                f"""
                <div class="rg-card">
                    <div class="rg-site-icon">{SITES[site]['emoji']}</div>
                    <h3>{s['name']}</h3>
                    <p>{site_summaries[site][st.session_state.lang]}</p>
                    <p style="font-size:.86rem"><b>UNESCO:</b> {s['inscribed']} • {s['criteria']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(f"{tr('open')} →", key=f"home_{site}", use_container_width=True):
                go(site)

    st.markdown(f'<div class="rg-section-title">{tr("why")}</div><div class="rg-section-sub">{tr("why_text")}</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    mini = [
        (c1, "📚", tr("learn"), tr("learn_d")),
        (c2, "🎮", tr("play"), tr("play_d")),
        (c3, "🏛️", tr("protect"), tr("protect_d")),
    ]
    for col, icon, title, desc in mini:
        with col:
            st.markdown(f'<div class="rg-card"><div class="rg-site-icon">{icon}</div><h4>{title}</h4><p>{desc}</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    a, b = st.columns(2)
    with a:
        if st.button(f"🏆 {tr('challenge_cta')}", key="home_challenge_cta", use_container_width=True, type="primary"):
            go("Heritage Challenge")
    with b:
        if st.button(f"💬 {tr('assistant_cta')}", key="home_assistant_cta", use_container_width=True):
            go("Heritage Assistant")

# -----------------------------
# Page: Site detail
# -----------------------------
def page_site(site_key):
    s = SITES[site_key][st.session_state.lang]
    st.markdown(
        f"""
        <div class="rg-hero" style="padding-bottom:28px">
            <div class="rg-kicker">ROBO GUIDE • Zimbabwe Heritage</div>
            <h1 style="font-size:3.2rem">{SITES[site_key]['emoji']} {s['name']}</h1>
            <p>{s['subtitle']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    q1, q2, q3 = st.columns(3)
    with q1:
        st.markdown(f'<div class="rg-stat"><div class="n">{s["inscribed"]}</div><div class="l">{tr("inscribed")}</div></div>', unsafe_allow_html=True)
    with q2:
        st.markdown(f'<div class="rg-stat"><div class="n">{s["criteria"]}</div><div class="l">{tr("criteria")}</div></div>', unsafe_allow_html=True)
    with q3:
        st.markdown(f'<div class="rg-stat"><div class="n" style="font-size:1rem">{s["location"]}</div><div class="l">{tr("location")}</div></div>', unsafe_allow_html=True)

    left, right = st.columns([1.25, 1])
    with left:
        st.markdown(f"### 📜 {tr('history')}")
        st.write(s["history"])
        st.markdown(f"### 👥 {tr('culture')}")
        st.write(s["culture"])
    with right:
        st.markdown(f"### ✨ {tr('features')}")
        render_list(s["features"], "◆")

    st.markdown(f'<div class="rg-strip"><b>🌐 {tr("unesco")}</b><br>{s["unesco"]}</div>', unsafe_allow_html=True)

    p1, p2 = st.columns(2)
    with p1:
        st.markdown(f"### 🛡️ {tr('protection')}")
        for x in s["protection"]:
            st.markdown(f'<div class="rg-protect">✓ {x}</div>', unsafe_allow_html=True)
    with p2:
        st.markdown(f"### 💡 {tr('facts')}")
        for x in s["facts"]:
            st.markdown(f'<div class="rg-callout">★ {x}</div>', unsafe_allow_html=True)

    st.markdown(f"### 🌟 {tr('significance')}")
    st.info(s["significance"], icon="🌍")

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button(tr("back"), key=f"site_back_{site_key}", use_container_width=True):
            go("Home")
    with c2:
        if st.button(f"🏆 {tr('challenge_cta')}", key=f"site_quiz_{site_key}", use_container_width=True):
            go("Heritage Challenge")
    with c3:
        if st.button(f"💬 {tr('assistant_cta')}", key=f"site_assistant_{site_key}", use_container_width=True):
            go("Heritage Assistant")

# -----------------------------
# Page: Quiz
# -----------------------------
def page_quiz():
    bank = QUIZ[st.session_state.lang]
    total = len(bank)
    st.markdown(
        f"""
        <div class="rg-hero" style="padding-bottom:28px">
            <div class="rg-kicker">ROBO GUIDE • Learn by playing</div>
            <h1 style="font-size:3.1rem">🏆 {tr('quiz_title')}</h1>
            <p>{tr('quiz_intro')}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state.quiz_finished:
        pct = round(100 * st.session_state.quiz_score / total)
        guardian = pct >= 80
        title = tr("guardian") if guardian else tr("guide")
        desc = tr("guardian_desc") if guardian else tr("guide_desc")
        trophy = "🛡️🏆" if guardian else "🧭🏅"
        st.markdown(
            f"""
            <div class="rg-achievement">
                <div class="trophy">{trophy}</div>
                <div style="letter-spacing:1.3px;text-transform:uppercase;font-size:.8rem">{tr('achievement')}</div>
                <h2>{title}</h2>
                <p>{desc}</p>
                <h3>{st.session_state.quiz_score}/{total} • {pct}% • {st.session_state.quiz_points} Heritage Points</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.balloons()
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            if st.button(f"🔁 {tr('reset')}", key="quiz_reset", use_container_width=True, type="primary"):
                reset_quiz()
                st.rerun()
        with c2:
            if st.button(f"📚 {tr('explore')}", key="quiz_explore", use_container_width=True):
                go("Home")
        return

    idx = st.session_state.quiz_index
    item = bank[idx]
    progress = idx / total
    st.progress(progress)

    m1, m2, m3 = st.columns(3)
    m1.metric(f"{tr('question')}", f"{idx + 1}/{total}")
    m2.metric(tr("score"), f"{st.session_state.quiz_score}/{total}")
    m3.metric(tr("points"), st.session_state.quiz_points)

    st.markdown('<div class="rg-quizbox">', unsafe_allow_html=True)
    st.markdown(f"### {idx + 1}. {item['q']}")
    choice = st.radio(
        "Choose one" if st.session_state.lang == "English" else ("Khetha impendulo" if st.session_state.lang == "isiNdebele" else "Sarudza mhinduro"),
        options=list(range(len(item["options"]))),
        format_func=lambda i: item["options"][i],
        index=None,
        key=f"quiz_radio_{st.session_state.lang}_{idx}",
        disabled=st.session_state.quiz_answered,
        label_visibility="collapsed",
    )

    if not st.session_state.quiz_answered:
        if st.button(f"✅ {tr('submit')}", key=f"quiz_submit_{idx}", type="primary", use_container_width=True, disabled=choice is None):
            st.session_state.quiz_selected = choice
            st.session_state.quiz_answered = True
            if choice == item["answer"]:
                st.session_state.quiz_score += 1
                st.session_state.quiz_points += 100
                st.session_state.quiz_feedback = "correct"
            else:
                st.session_state.quiz_points += 20
                st.session_state.quiz_feedback = "incorrect"
            st.rerun()
    else:
        if st.session_state.quiz_feedback == "correct":
            st.success(f"🎉 {tr('correct')} +100 Heritage Points\n\n{item['why']}")
        else:
            correct_text = item["options"][item["answer"]]
            st.error(f"💡 {tr('incorrect')} +20 Participation Points\n\n**✓ {correct_text}**\n\n{item['why']}")

        button_text = tr("finish") if idx == total - 1 else tr("next")
        if st.button(button_text, key=f"quiz_next_{idx}", type="primary", use_container_width=True):
            if idx == total - 1:
                st.session_state.quiz_finished = True
            else:
                st.session_state.quiz_index += 1
                st.session_state.quiz_answered = False
                st.session_state.quiz_selected = None
                st.session_state.quiz_feedback = None
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Page: Assistant
# -----------------------------
def page_assistant():
    st.markdown(
        f"""
        <div class="rg-hero" style="padding-bottom:28px">
            <div class="rg-kicker">ROBO GUIDE • Free rule-based heritage intelligence</div>
            <h1 style="font-size:3.1rem">💬 {tr('assistant_title')}</h1>
            <p>{tr('assistant_intro')}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    suggestions = {
        "English": [
            "Who built Great Zimbabwe?",
            "Why are Matobo caves important?",
            "What are the Zimbabwe Birds?",
            "Tell me about Torwa history at Khami.",
            "Compare Great Zimbabwe and Khami.",
            "How should visitors protect rock art?",
        ],
        "isiNdebele": [
            "Ngubani owakha iGreat Zimbabwe?",
            "Kungani imigede yeMatobo iqakathekile?",
            "Yini iZimbabwe Birds?",
            "Ngitshele ngombuso weTorwa eKhami.",
            "Qhathanisa iGreat Zimbabwe leKhami.",
            "Izivakashi zingayivikela njani imidwebo emadwaleni?",
        ],
        "Shona": [
            "Ndiani akavaka Great Zimbabwe?",
            "Sei mapako eMatobo akakosha?",
            "Zimbabwe Birds chii?",
            "Ndiudze nezveTorwa paKhami.",
            "Enzanisa Great Zimbabwe neKhami.",
            "Vashanyi vangachengetedza sei rock art?",
        ],
    }

    st.markdown(f"**{tr('suggested')}:**")
    cols = st.columns(3)
    for i, s in enumerate(suggestions[st.session_state.lang]):
        with cols[i % 3]:
            if st.button(s, key=f"suggest_{i}", use_container_width=True):
                answer = assistant_answer(s, st.session_state.lang)
                st.session_state.chat.append((s, answer))
                st.rerun()

    st.markdown("---")
    for q, a in st.session_state.chat[-8:]:
        st.markdown(f'<div class="rg-chat-user"><b>👤 Visitor</b><br>{escape(q)}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="rg-chat-bot"><b>🤖 ROBO GUIDE</b><br>{escape(a)}</div>', unsafe_allow_html=True)

    with st.form("assistant_form", clear_on_submit=True):
        question = st.text_input("Question", key="assistant_question_input", placeholder=tr("assistant_placeholder"), label_visibility="collapsed")
        submitted = st.form_submit_button(f"🤖 {tr('ask')}", key="assistant_submit", use_container_width=True, type="primary")
        if submitted and question.strip():
            answer = assistant_answer(question, st.session_state.lang)
            st.session_state.chat.append((question.strip(), answer))
            st.rerun()

    if st.session_state.chat:
        if st.button(f"🧹 {tr('clear_chat')}", key="assistant_clear_chat"):
            st.session_state.chat = []
            st.rerun()

    st.caption("No API key • No paid AI service • Local rule-based knowledge routing inside app.py")

# -----------------------------
# Route current page
# -----------------------------
page = st.session_state.page
if page == "Home":
    page_home()
elif page in ("Matobo Hills", "Great Zimbabwe", "Khami Ruins"):
    page_site(page)
elif page == "Heritage Challenge":
    page_quiz()
elif page == "Heritage Assistant":
    page_assistant()
else:
    st.session_state.page = "Home"
    st.rerun()

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    f"""
    <div class="rg-footer">
        <b>{tr('footer')}</b><br>
        Built as a single-file Streamlit experience for the WRO 2026 Zimbabwe National Finals.
    </div>
    """,
    unsafe_allow_html=True,
)
