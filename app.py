import streamlit as st
import re
import random


# ============================================================
# ROBO GUARD
# WRO 2026 - ROBOTS MEET CULTURE
# Visitor Heritage Education Portal
#
# No paid APIs required
# No external AI API keys required
# Designed for Streamlit Community Cloud
# ============================================================


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ROBO GUARD | Zimbabwe Heritage",
    page_icon="🇿🇼",
    layout="wide"
)


# ============================================================
# GREEN & GOLD DESIGN
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f7f8f3;
    }

    [data-testid="stSidebar"] {
        background-color: #075b36;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    h1, h2, h3 {
        color: #075b36;
    }

    .main-title {
        background: linear-gradient(90deg, #075b36, #0b7a48);
        color: white;
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        border-bottom: 6px solid #d4af37;
        margin-bottom: 20px;
    }

    .main-title h1 {
        color: white !important;
        margin: 0;
        font-size: 42px;
    }

    .main-title p {
        color: #f5d76e;
        font-size: 18px;
        margin-top: 8px;
    }

    .heritage-card {
        background-color: white;
        padding: 22px;
        border-radius: 15px;
        border-left: 7px solid #d4af37;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        margin-bottom: 18px;
    }

    .fact-box {
        background-color: #eef7f1;
        border: 1px solid #b7d7c3;
        border-radius: 12px;
        padding: 18px;
        margin-top: 12px;
    }

    .guardian-box {
        background-color: #075b36;
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 3px solid #d4af37;
    }

    .chat-answer {
        background-color: #ffffff;
        padding: 18px;
        border-radius: 15px;
        border-left: 6px solid #d4af37;
        margin: 10px 0 20px 0;
    }

    .source-note {
        font-size: 13px;
        color: #555555;
        border-top: 1px solid #dddddd;
        padding-top: 10px;
        margin-top: 25px;
    }

    .tag {
        display: inline-block;
        background-color: #075b36;
        color: white;
        padding: 4px 10px;
        margin: 3px;
        border-radius: 15px;
        font-size: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HERITAGE DATABASE
# ============================================================

HERITAGE = {

    "Matobo Hills": {

        "short_name": "Matobo",

        "location": (
            "Matobo Hills is located in south-western Zimbabwe, "
            "south of Bulawayo."
        ),

        "intro": (
            "Matobo Hills is a remarkable cultural landscape of granite "
            "formations, rock shelters, archaeological remains, sacred places "
            "and an exceptional concentration of rock paintings."
        ),

        "unesco": (
            "Matobo Hills was inscribed on the UNESCO World Heritage List "
            "in 2003 under cultural criteria (iii), (v) and (vi)."
        ),

        "dates": (
            "Human interaction with the Matobo landscape stretches back for "
            "many thousands of years. UNESCO reports archaeological evidence "
            "of occupation extending hundreds of thousands of years, while "
            "rock paintings in the area date back at least about 13,000 years."
        ),

        "builders": (
            "The rock paintings are principally associated with ancient "
            "hunter-gatherer communities of southern Africa, commonly "
            "associated with San cultural traditions. They were not produced "
            "by one single named builder or ruler."
        ),

        "rock_art": (
            "Matobo has one of the highest concentrations of rock art in "
            "southern Africa. The paintings include human figures, animals "
            "and scenes that provide evidence about the lives, beliefs and "
            "environment of earlier communities."
        ),

        "caves": (
            "Important researched rock-art shelters include Pomongwe Cave, "
            "Bambata Cave and Nswatugi Cave. Each contributes different "
            "archaeological and artistic evidence about early occupation."
        ),

        "pomongwe": (
            "Pomongwe Cave contains important Middle and Late Stone Age "
            "deposits and rock paintings. Some paintings were unfortunately "
            "darkened after linseed oil was applied during conservation "
            "experiments in the 1920s. This is an important lesson in why "
            "heritage conservation methods must be carefully researched."
        ),

        "bambata": (
            "Bambata Cave is one of the extensively researched prehistoric "
            "sites in Matobo. Archaeological excavations there revealed "
            "important evidence of early human occupation, including a "
            "decorated stone object dated to roughly 10,000 years ago."
        ),

        "nswatugi": (
            "Nswatugi Cave is an important archaeological and rock-art site. "
            "Research recorded evidence of Middle Stone Age occupation, and "
            "the cave is particularly well known for the variety and beauty "
            "of its paintings."
        ),

        "religion": (
            "Matobo remains a living cultural and spiritual landscape. "
            "Traditional beliefs associated with Mwari, ancestral spirits, "
            "sacred shrines and community practices remain an important part "
            "of the site's cultural significance."
        ),

        "threats": (
            "Threats include natural weathering, environmental pressures, "
            "vegetation, erosion and inappropriate visitor behaviour. "
            "Touching or interfering with paintings can contribute to "
            "their deterioration."
        ),

        "protection": (
            "Visitors should observe rock paintings from designated safe "
            "areas, avoid touching or applying substances to the rock, "
            "follow site rules and respect sacred places and local traditions."
        ),

        "why_important": (
            "Matobo is important because it combines archaeology, rock art, "
            "living spiritual traditions and a distinctive natural landscape. "
            "It helps tell the story of the long relationship between people "
            "and their environment."
        )
    },


    "Great Zimbabwe": {

        "short_name": "Great Zimbabwe",

        "location": (
            "Great Zimbabwe National Monument lies near Masvingo in "
            "south-eastern Zimbabwe."
        ),

        "intro": (
            "Great Zimbabwe is the monumental stone-built centre that gave "
            "modern Zimbabwe its name. It was one of the most important "
            "political and trading centres of pre-colonial southern Africa."
        ),

        "unesco": (
            "Great Zimbabwe National Monument was inscribed on the UNESCO "
            "World Heritage List in 1986."
        ),

        "dates": (
            "The major monumental settlement developed between approximately "
            "the 11th and 15th centuries. UNESCO identifies roughly "
            "1100 to 1450 AD as the principal building and occupation period."
        ),

        "builders": (
            "Archaeological research attributes Great Zimbabwe to indigenous "
            "African communities, particularly ancestors of Shona-speaking "
            "peoples. Its architecture was created locally rather than by "
            "foreign civilizations."
        ),

        "masonry": (
            "Great Zimbabwe is famous for dry-stone masonry. Carefully shaped "
            "and selected granite blocks were laid in courses without mortar. "
            "The quality of the walls demonstrates sophisticated architectural "
            "knowledge and craftsmanship."
        ),

        "structures": (
            "The monument is commonly divided into three principal areas: "
            "the Hill Complex or Hill Ruins, the Great Enclosure, and the "
            "Valley Ruins."
        ),

        "great_enclosure": (
            "The Great Enclosure is one of Great Zimbabwe's most famous "
            "architectural features. It contains massive dry-stone walls and "
            "the well-known Conical Tower."
        ),

        "conical_tower": (
            "The Conical Tower is a solid stone structure within the Great "
            "Enclosure. Its exact historical function remains debated, so it "
            "is better understood as an important architectural and symbolic "
            "feature rather than assigning it an unsupported single purpose."
        ),

        "hill_complex": (
            "The Hill Complex occupies a granite hill and contains some of "
            "the earliest and longest-used monumental areas of Great Zimbabwe. "
            "It overlooks the surrounding settlement."
        ),

        "birds": (
            "Carved soapstone birds are among the most famous artifacts "
            "associated with Great Zimbabwe. The Zimbabwe Bird later became "
            "an important national symbol and appears on Zimbabwe's flag "
            "and national emblems."
        ),

        "trade": (
            "Great Zimbabwe participated in extensive regional and "
            "long-distance trade networks. Archaeological finds demonstrate "
            "connections between inland southern Africa and wider Indian Ocean "
            "commercial systems."
        ),

        "population": (
            "At its height, Great Zimbabwe supported a substantial urban "
            "population. UNESCO notes that its population exceeded about "
            "10,000 inhabitants during its period of greatest importance."
        ),

        "decline": (
            "The centre declined around the 15th century. Environmental "
            "pressure, the difficulty of supporting a large population and "
            "changes in political and trading patterns are among factors "
            "associated with its decline."
        ),

        "protection": (
            "Visitors should never climb fragile walls, remove stones or "
            "artifacts, write on structures, or enter restricted areas. "
            "The ruins must be protected as archaeological evidence, not "
            "treated simply as ordinary stone structures."
        ),

        "why_important": (
            "Great Zimbabwe demonstrates the architectural, economic and "
            "political achievements of indigenous African civilization and "
            "is central to Zimbabwe's national identity."
        )
    },


    "Khami Ruins": {

        "short_name": "Khami",

        "location": (
            "Khami Ruins National Monument is about 22 kilometres west of "
            "Bulawayo, close to the Khami River."
        ),

        "intro": (
            "Khami was an important political and trading centre that "
            "developed after the decline of Great Zimbabwe. It is particularly "
            "famous for decorated stone retaining walls and terraced platforms."
        ),

        "unesco": (
            "Khami Ruins National Monument was inscribed on the UNESCO "
            "World Heritage List in 1986."
        ),

        "dates": (
            "Khami rose to prominence after the decline of Great Zimbabwe. "
            "It was particularly important from around the 15th century and "
            "was associated with the Torwa state before later political change."
        ),

        "builders": (
            "Khami was associated with the Torwa dynasty and communities "
            "continuing the wider Zimbabwe stone-building tradition."
        ),

        "torwa": (
            "Khami served as the capital of the Torwa dynasty. The Torwa state "
            "developed after the decline of the Great Zimbabwe political centre "
            "and became an important regional power."
        ),

        "architecture": (
            "Khami is characterized by dry-stone retaining walls, raised "
            "platforms, narrow passages and elaborate decorative stonework. "
            "Chevron and chequered patterns demonstrate highly skilled masonry."
        ),

        "platforms": (
            "A distinctive feature of Khami is the use of stone-faced terraces "
            "and platforms. Buildings could be constructed on raised areas "
            "supported by retaining walls."
        ),

        "hill_ruin": (
            "The Hill Ruin is one of Khami's important areas. UNESCO records "
            "that the ruler's residence was located towards the north on the "
            "Hill Ruin, with associated terraces."
        ),

        "trade": (
            "Khami participated in long-distance trade. Archaeological finds "
            "include imported objects associated with Europe and China, "
            "demonstrating that the settlement was connected to wider "
            "international trading networks."
        ),

        "artifacts": (
            "Archaeological evidence from Khami includes imported ceramics "
            "and other objects associated with long-distance trade. UNESCO "
            "mentions finds such as Ming porcelain, European ceramics and "
            "Rhineland stoneware."
        ),

        "decorations": (
            "Khami's stone architecture includes impressive chevron and "
            "chequered decorative patterns. Its decorated retaining walls "
            "are one of the monument's most distinctive characteristics."
        ),

        "decline": (
            "Khami was eventually abandoned following major political changes "
            "in the region, including conflicts and incursions during later "
            "centuries."
        ),

        "protection": (
            "Visitors should remain on permitted routes, avoid climbing or "
            "touching fragile stonework, never remove stones or artifacts, "
            "and follow the instructions of heritage authorities."
        ),

        "why_important": (
            "Khami is important because it helps explain the development of "
            "Zimbabwe's stone-building tradition after Great Zimbabwe. Its "
            "architecture and artifacts also provide evidence of political, "
            "economic and international trading connections."
        )
    }
}


# ============================================================
# INTENT / QUESTION DATABASE
# ============================================================

INTENTS = {

    "location": [
        "where",
        "location",
        "located",
        "how far",
        "which city",
        "near"
    ],

    "dates": [
        "when",
        "date",
        "dates",
        "how old",
        "built",
        "century",
        "period",
        "year",
        "age"
    ],

    "builders": [
        "who built",
        "who made",
        "builders",
        "builder",
        "built it",
        "created",
        "painted",
        "who painted"
    ],

    "unesco": [
        "unesco",
        "world heritage",
        "inscribed",
        "inscription",
        "heritage list"
    ],

    "protection": [
        "protect",
        "protection",
        "preserve",
        "preservation",
        "conservation",
        "rules",
        "touch",
        "damage",
        "visitor"
    ],

    "why_important": [
        "importance",
        "important",
        "significance",
        "special",
        "why should",
        "why is"
    ],

    "trade": [
        "trade",
        "trading",
        "commerce",
        "china",
        "europe",
        "indian ocean",
        "imports"
    ]
}


# ============================================================
# SPECIAL TOPIC MATCHES
# ============================================================

SPECIAL_TOPICS = {

    # Matobo
    "pomongwe": ("Matobo Hills", "pomongwe"),
    "pomongwe cave": ("Matobo Hills", "pomongwe"),

    "bambata": ("Matobo Hills", "bambata"),
    "bambata cave": ("Matobo Hills", "bambata"),

    "nswatugi": ("Matobo Hills", "nswatugi"),
    "nswatugi cave": ("Matobo Hills", "nswatugi"),

    "rock painting": ("Matobo Hills", "rock_art"),
    "rock paintings": ("Matobo Hills", "rock_art"),
    "rock art": ("Matobo Hills", "rock_art"),

    "mwari": ("Matobo Hills", "religion"),
    "spiritual": ("Matobo Hills", "religion"),
    "religion": ("Matobo Hills", "religion"),

    # Great Zimbabwe
    "great enclosure": ("Great Zimbabwe", "great_enclosure"),
    "conical tower": ("Great Zimbabwe", "conical_tower"),
    "tower": ("Great Zimbabwe", "conical_tower"),

    "hill complex": ("Great Zimbabwe", "hill_complex"),
    "hill ruins": ("Great Zimbabwe", "hill_complex"),

    "zimbabwe bird": ("Great Zimbabwe", "birds"),
    "zimbabwe birds": ("Great Zimbabwe", "birds"),
    "soapstone bird": ("Great Zimbabwe", "birds"),
    "soapstone birds": ("Great Zimbabwe", "birds"),

    "mortar": ("Great Zimbabwe", "masonry"),
    "mortarless": ("Great Zimbabwe", "masonry"),
    "dry stone": ("Great Zimbabwe", "masonry"),
    "stone walls": ("Great Zimbabwe", "masonry"),

    "population": ("Great Zimbabwe", "population"),

    # Khami
    "torwa": ("Khami Ruins", "torwa"),
    "torwa dynasty": ("Khami Ruins", "torwa"),

    "terrace": ("Khami Ruins", "platforms"),
    "terraces": ("Khami Ruins", "platforms"),
    "platform": ("Khami Ruins", "platforms"),
    "platforms": ("Khami Ruins", "platforms"),

    "hill ruin": ("Khami Ruins", "hill_ruin"),

    "chevron": ("Khami Ruins", "decorations"),
    "chequered": ("Khami Ruins", "decorations"),
    "decoration": ("Khami Ruins", "decorations"),

    "porcelain": ("Khami Ruins", "artifacts"),
    "ming": ("Khami Ruins", "artifacts"),
    "artifact": ("Khami Ruins", "artifacts"),
    "artifacts": ("Khami Ruins", "artifacts")
}


# ============================================================
# SITE DETECTION
# ============================================================

SITE_KEYWORDS = {

    "Matobo Hills": [
        "matobo",
        "matopos",
        "rock art",
        "rock painting",
        "san",
        "pomongwe",
        "bambata",
        "nswatugi",
        "mwari"
    ],

    "Great Zimbabwe": [
        "great zimbabwe",
        "great enclosure",
        "conical tower",
        "soapstone",
        "zimbabwe bird",
        "hill complex"
    ],

    "Khami Ruins": [
        "khami",
        "torwa",
        "terraced",
        "terrace",
        "platform",
        "khami river"
    ]
}


# ============================================================
# CHATBOT FUNCTIONS
# ============================================================

def normalize(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s'-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def detect_site(question):

    q = normalize(question)

    scores = {}

    for site, keywords in SITE_KEYWORDS.items():

        score = 0

        for keyword in keywords:
            if keyword in q:
                score += len(keyword.split()) + 1

        scores[site] = score

    best_site = max(scores, key=scores.get)

    if scores[best_site] == 0:
        return None

    return best_site


def detect_special_topic(question):

    q = normalize(question)

    # Longer phrases checked first
    ordered_topics = sorted(
        SPECIAL_TOPICS.keys(),
        key=len,
        reverse=True
    )

    for phrase in ordered_topics:

        if phrase in q:
            return SPECIAL_TOPICS[phrase]

    return None


def detect_intent(question):

    q = normalize(question)

    scores = {
        intent: 0
        for intent in INTENTS
    }

    for intent, patterns in INTENTS.items():

        for phrase in patterns:

            if phrase in q:
                scores[intent] += len(phrase.split())

    best = max(scores, key=scores.get)

    if scores[best] == 0:
        return None

    return best


def chatbot_answer(question, preferred_site=None):

    q = normalize(question)

    if not q:
        return "Please enter a question about Zimbabwe's cultural heritage."

    # --------------------------------------------------------
    # GREETINGS
    # --------------------------------------------------------

    greetings = [
        "hello",
        "hi",
        "good morning",
        "good afternoon",
        "hey"
    ]

    if q in greetings:

        return (
            "Hello! 👋 I am the ROBO GUARD Heritage Assistant. "
            "Ask me about Matobo Hills, Great Zimbabwe or Khami Ruins. "
            "You can ask about history, builders, caves, rock art, "
            "artifacts, architecture, trade, UNESCO status
