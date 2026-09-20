import streamlit as st

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="SAI GOAT FARM",
    page_icon="🐐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.stApp {
    background: #f5f9f3;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #0b4d2c, #2e8b57);
    padding: 55px 25px;
    border-radius: 25px;
    text-align: center;
    color: white;
    margin-bottom: 35px;
}

.logo {
    width: 105px;
    height: 105px;
    margin: auto;
    background: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 62px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

.hero h1 {
    font-size: 52px;
    margin: 18px 0 8px 0;
    font-weight: 800;
}

.hero h3 {
    font-size: 22px;
    font-weight: 400;
}

.category {
    display: inline-block;
    margin-top: 18px;
    padding: 9px 20px;
    border-radius: 30px;
    background: #ffd54f;
    color: #222;
    font-weight: bold;
}

/* Section */
.section-title {
    text-align: center;
    color: #0b4d2c;
    font-size: 34px;
    font-weight: 800;
    margin: 35px 0 25px 0;
}

/* Cards */
.card {
    background: white;
    padding: 28px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 5px 18px rgba(0,0,0,0.08);
    min-height: 190px;
    margin-bottom: 20px;
}

.card-icon {
    font-size: 48px;
}

.card h3 {
    color: #176b3a;
    margin: 12px 0;
}

/* Breed cards */
.breed {
    background: white;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid #dcebdc;
    box-shadow: 0 5px 18px rgba(0,0,0,0.07);
}

.breed-icon {
    font-size: 65px;
}

/* Contact */
.contact-box {
    background: linear-gradient(135deg, #0b4d2c, #287a4b);
    padding: 40px;
    border-radius: 22px;
    color: white;
    text-align: center;
}

.contact-box h2 {
    color: white;
}

/* Footer */
.footer {
    margin-top: 40px;
    padding: 25px;
    background: #07351f;
    color: white;
    text-align: center;
    border-radius: 18px;
}

.small-text {
    color: #666;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
st.sidebar.markdown(
    "<h1 style='text-align:center;'>🐐</h1>",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "<h2 style='text-align:center;color:#176b3a;'>SAI GOAT FARM</h2>",
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "MENU",
    [
        "🏠 Home",
        "📖 About Us",
        "🐐 Goat Breeds",
        "🌾 Services",
        "⭐ Why Choose Us",
        "📞 Contact"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    **Business Category**

    🐐 Goat Farming & Livestock

    **Location**

    📍 Chitali, Rahata, Ahilyanagar
    """
)


# ==========================================================
# HOME
# ==========================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">

        <div class="logo">🐐</div>

        <h1>SAI GOAT FARM</h1>

        <h3>Healthy Goats • Better Farming • Better Future</h3>

        <div class="category">
            🏷️ Goat Farming & Livestock Business
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Welcome to SAI GOAT FARM</div>',
        unsafe_allow_html=True
    )

    st.write("""
    **SAI GOAT FARM** is a goat farming and livestock business located at
    Chitali, Rahata, Ahilyanagar, Maharashtra.

    Our focus is on healthy goat rearing, proper feeding, clean management
    and responsible livestock farming practices.
    """)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🐐</div>
            <h3>Healthy Goats</h3>
            <p>Focus on proper care, feeding and healthy goat management.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🌱</div>
            <h3>Better Farming</h3>
            <p>Responsible and sustainable goat farming practices.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🤝</div>
            <h3>Customer Trust</h3>
            <p>We believe in quality, transparency and long-term relationships.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Our Business</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("🐐 **Business Name:** SAI GOAT FARM")

        st.info("🏷️ **Category:** Goat Farming & Livestock")

    with col2:
        st.success("💬 **Tagline:** Healthy Goats • Better Farming • Better Future")

        st.success("📍 **Location:** Chitali, Rahata, Ahilyanagar")


# ==========================================================
# ABOUT
# ==========================================================

elif page == "📖 About Us":

    st.markdown(
        '<div class="section-title">📖 About SAI GOAT FARM</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

        <div class="card-icon">🐐</div>

        <h3>Who We Are</h3>

        <p>
        SAI GOAT FARM is a livestock farming business focused on goat
        rearing and goat farming. We aim to maintain healthy goats through
        proper feeding, clean surroundings and responsible management.
        </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

        <div class="card-icon">🎯</div>

        <h3>Our Mission</h3>

        <p>
        To develop a sustainable goat farming business by maintaining
        healthy livestock and following better farming practices.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">

        <div class="card-icon">🚀</div>

        <h3>Our Vision</h3>

        <p>
        To become a trusted name in goat farming and livestock business
        while creating value for customers and farmers.
        </p>

        </div>
        """, unsafe_allow_html=True)


# ==========================================================
# BREEDS
# ==========================================================

elif page == "🐐 Goat Breeds":

    st.markdown(
        '<div class="section-title">🐐 Our Goat Breeds</div>',
        unsafe_allow_html=True
    )

    st.write(
        "SAI GOAT FARM focuses on different popular goat breeds."
    )

    breeds = [
        (
            "Beetel",
            "🐐",
            "A well-known Indian goat breed with good body size and productive characteristics."
        ),
        (
            "Boer",
            "🐐",
            "A popular meat goat breed known for its growth and strong body structure."
        ),
        (
            "Osmanabadi",
            "🐐",
            "A popular Maharashtra breed known for adaptability and suitability to local conditions."
        ),
        (
            "Sannen",
            "🐐",
            "A well-known dairy goat breed recognized for milk production."
        )
    ]

    col1, col2 = st.columns(2)

    for i, (name, icon, description) in enumerate(breeds):

        with (col1 if i % 2 == 0 else col2):

            st.markdown(f"""
            <div class="breed">

                <div class="breed-icon">{icon}</div>

                <h2>{name}</h2>

                <p>{description}</p>

                <b>Price: As per breed</b>

            </div>
            """, unsafe_allow_html=True)


# ==========================================================
# SERVICES
# ==========================================================

elif page == "🌾 Services":

    st.markdown(
        '<div class="section-title">🌾 Our Services</div>',
        unsafe_allow_html=True
    )

    services = [
        ("🐐", "Goat Rearing",
         "Proper care, feeding and management of goats."),

        ("🌱", "Feed Management",
         "Focus on proper feeding and nutritional management."),

        ("🏡", "Livestock Management",
         "Clean housing and responsible livestock management."),

        ("🤝", "Goat Sales",
         "Goats available according to breed and requirements."),

        ("📚", "Farming Guidance",
         "Basic guidance for people interested in goat farming."),

        ("🚜", "Sustainable Farming",
         "Promoting responsible and sustainable livestock farming.")
    ]

    cols = st.columns(3)

    for i, (icon, title, description) in enumerate(services):

        with cols[i % 3]:

            st.markdown(f"""
            <div class="card">

                <div class="card-icon">{icon}</div>

                <h3>{title}</h3>

                <p>{description}</p>

            </div>
            """, unsafe_allow_html=True)


# ==========================================================
# WHY CHOOSE US
# ==========================================================

elif page == "⭐ Why Choose Us":

    st.markdown(
        '<div class="section-title">⭐ Why Choose SAI GOAT FARM?</div>',
        unsafe_allow_html=True
    )

    points = [
        "🐐 Focus on healthy livestock",
        "🌱 Better farming practices",
        "🥬 Proper feeding and care",
        "🧹 Clean and responsible management",
        "🤝 Customer-focused approach",
        "📈 Focus on sustainable growth"
    ]

    for point in points:
        st.success(point)

    st.markdown("---")

    st.markdown("""
    <div class="card">

        <div class="card-icon">🌟</div>

        <h3>Our Promise</h3>

        <p>
        We aim to maintain quality livestock and provide transparent
        information to our customers.
        </p>

    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# CONTACT
# ==========================================================

elif page == "📞 Contact":

    st.markdown(
        '<div class="section-title">📞 Contact SAI GOAT FARM</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="contact-box">

        <h2>🐐 SAI GOAT FARM</h2>

        <p>Healthy Goats • Better Farming • Better Future</p>

        <br>

        <p>📱 <b>9579187477</b></p>

        <p>📧 <b>ashutosh123@gmail.com</b></p>

        <p>📍 <b>At Post Chitali, Ta. Rahata, Dist. Ahilyanagar</b></p>

        <p>🏷️ <b>Goat Farming & Livestock Business</b></p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("###")

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "📱 WhatsApp Us",
            "https://wa.me/919579187477",
            use_container_width=True
        )

    with col2:

        st.link_button(
            "📧 Send Email",
            "mailto:ashutosh123@gmail.com",
            use_container_width=True
        )

    st.markdown("###")

    st.info(
        "For goat availability and breed-wise pricing, please contact us directly."
    )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("""
<div class="footer">

    <h3>🐐 SAI GOAT FARM</h3>

    <p>Healthy Goats • Better Farming • Better Future</p>

    <p>
    📱 9579187477 &nbsp; | &nbsp;
    📧 ashutosh123@gmail.com
    </p>

    <p>
    © 2026 SAI GOAT FARM • All Rights Reserved
    </p>

</div>
""", unsafe_allow_html=True)
