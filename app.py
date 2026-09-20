
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SAI GOAT FARM",
    page_icon="🐐",
    layout="wide"
)

# Custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5faf5;
    }

    .hero {
        background: linear-gradient(135deg, #064e3b, #16a34a);
        padding: 45px;
        border-radius: 25px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
    }

    .hero-logo {
        font-size: 70px;
    }

    .hero-title {
        font-size: 48px;
        font-weight: bold;
    }

    .hero-tagline {
        font-size: 21px;
    }

    .category {
        background-color: #facc15;
        color: black;
        padding: 8px 18px;
        border-radius: 25px;
        display: inline-block;
        font-weight: bold;
    }

    .section-title {
        text-align: center;
        color: #065f46;
        font-size: 32px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .card-icon {
        font-size: 45px;
    }

    .breed-card {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .contact {
        background: #064e3b;
        color: white;
        padding: 35px;
        border-radius: 20px;
        text-align: center;
    }

    .footer {
        background: #022c22;
        color: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("🐐 SAI GOAT FARM")

page = st.sidebar.radio(
    "Navigation",
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
st.sidebar.write("🏷️ Goat Farming & Livestock")
st.sidebar.write("📍 Chitali, Rahata, Ahilyanagar")


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-logo">🐐</div>
            <div class="hero-title">SAI GOAT FARM</div>
            <div class="hero-tagline">
                Healthy Goats • Better Farming • Better Future
            </div>
            <br>
            <div class="category">
                🏷️ Goat Farming & Livestock Business
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Welcome to SAI GOAT FARM</div>',
        unsafe_allow_html=True
    )

    st.write(
        """
        **SAI GOAT FARM** is a goat farming and livestock business
        located at Chitali, Rahata, Ahilyanagar, Maharashtra.

        Our focus is on healthy goat rearing, proper feeding,
        clean management and responsible livestock farming practices.
        """
    )

    st.markdown(
        '<div class="section-title">What We Focus On</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="card">
                <div class="card-icon">🐐</div>
                <h3>Healthy Goats</h3>
                <p>
                Focus on proper care, feeding and healthy
                goat management.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <div class="card-icon">🌱</div>
                <h3>Better Farming</h3>
                <p>
                Responsible and sustainable goat farming
                practices.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card">
                <div class="card-icon">🤝</div>
                <h3>Customer Trust</h3>
                <p>
                We believe in quality, transparency and
                long-term relationships.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">Our Business</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("🐐 Business Name: SAI GOAT FARM")
        st.info("🏷️ Category: Goat Farming & Livestock")

    with col2:
        st.success(
            "💬 Tagline: Healthy Goats • Better Farming • Better Future"
        )
        st.success(
            "📍 Location: At Post Chitali, Ta. Rahata, Dist. Ahilyanagar"
        )


# =========================================================
# ABOUT
# =========================================================

elif page == "📖 About Us":

    st.markdown(
        '<div class="section-title">📖 About SAI GOAT FARM</div>',
        unsafe_allow_html=True
    )

    st.write(
        """
        **SAI GOAT FARM** is a livestock farming business focused
        on goat rearing and goat farming.

        We aim to maintain healthy goats through proper feeding,
        clean surroundings and responsible livestock management.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <div class="card-icon">🎯</div>
                <h3>Our Mission</h3>
                <p>
                To develop a sustainable goat farming business
                by maintaining healthy livestock and following
                better farming practices.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <div class="card-icon">🚀</div>
                <h3>Our Vision</h3>
                <p>
                To become a trusted name in goat farming and
                livestock business.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# BREEDS
# =========================================================

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
            "A well-known Indian goat breed with good body size "
            "and productive characteristics."
        ),
        (
            "Osmanabadi",
            "A popular Maharashtra breed known for adaptability "
            "and suitability to local conditions."
        ),
        (
            "Boer",
            "A popular meat goat breed known for its growth "
            "and strong body structure."
        ),
        (
            "Sannen",
            "A well-known dairy goat breed recognized for "
            "milk production."
        )
    ]

    col1, col2 = st.columns(2)

    for i, (breed_name, description) in enumerate(breeds):

        with col1 if i % 2 == 0 else col2:

            st.markdown(
                f"""
                <div class="breed-card">
                    <div class="card-icon">🐐</div>
                    <h2>{breed_name}</h2>
                    <p>{description}</p>
                    <strong>Price: As per breed</strong>
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# SERVICES
# =========================================================

elif page == "🌾 Services":

    st.markdown(
        '<div class="section-title">🌾 Our Services</div>',
        unsafe_allow_html=True
    )

    services = [
        ("🐐", "Goat Rearing", "Proper care and management of goats."),
        ("🌱", "Feed Management", "Proper feeding and nutrition management."),
        ("🏡", "Livestock Management", "Clean and responsible goat management."),
        ("🤝", "Goat Sales", "Goats available according to breed and requirements."),
        ("📚", "Farming Guidance", "Basic guidance for people interested in goat farming."),
        ("🚜", "Sustainable Farming", "Responsible livestock farming practices.")
    ]

    columns = st.columns(3)

    for i, (icon, title, description) in enumerate(services):

        with columns[i % 3]:

            st.markdown(
                f"""
                <div class="card">
                    <div class="card-icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# WHY CHOOSE US
# =========================================================

elif page == "⭐ Why Choose Us":

    st.markdown(
        '<div class="section-title">⭐ Why Choose SAI GOAT FARM?</div>',
        unsafe_allow_html=True
    )

    st.success("🐐 Focus on healthy livestock")
    st.success("🌱 Better farming practices")
    st.success("🥬 Proper feeding and care")
    st.success("🧹 Clean and responsible management")
    st.success("🤝 Customer-focused approach")
    st.success("📈 Focus on sustainable growth")


# =========================================================
# CONTACT
# =========================================================

elif page == "📞 Contact":

    st.markdown(
        '<div class="section-title">📞 Contact Us</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="contact">

            <h2>🐐 SAI GOAT FARM</h2>

            <p>
            Healthy Goats • Better Farming • Better Future
            </p>

            <p>📱 9579187477</p>

            <p>📧 ashutosh123@gmail.com</p>

            <p>
            📍 At Post Chitali, Ta. Rahata,
            Dist. Ahilyanagar
            </p>

            <p>
            🏷️ Goat Farming & Livestock Business
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

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


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        <h3>🐐 SAI GOAT FARM</h3>

        <p>
        Healthy Goats • Better Farming • Better Future
        </p>

        <p>
        📱 9579187477 &nbsp; | &nbsp;
        📧 ashutosh123@gmail.com
        </p>

        <p>
        © 2026 SAI GOAT FARM • All Rights Reserved
        </p>

    </div>
    """,
    unsafe_allow_html=True
)

