
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SAI GOAT FARM",
    page_icon="🐐",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

html {
    scroll-behavior: smooth;
}

.main {
    background-color: #f7fff7;
}

.hero {
    padding: 55px 30px;
    border-radius: 25px;
    text-align: center;
    background: linear-gradient(135deg, #14532d, #22c55e);
    color: white;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 55px;
    margin-bottom: 10px;
    font-weight: 800;
}

.hero h3 {
    font-size: 24px;
    font-weight: 400;
}

.badge {
    display: inline-block;
    background: #facc15;
    color: #222;
    padding: 8px 20px;
    border-radius: 30px;
    font-weight: bold;
    margin-top: 15px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
    min-height: 180px;
    margin-bottom: 20px;
}

.card h3 {
    color: #166534;
}

.section-title {
    text-align: center;
    color: #166534;
    font-size: 35px;
    font-weight: 800;
    margin-top: 35px;
    margin-bottom: 25px;
}

.contact {
    background: #14532d;
    color: white;
    padding: 35px;
    border-radius: 20px;
    text-align: center;
}

.contact h2 {
    color: white;
}

.footer {
    text-align: center;
    padding: 25px;
    background: #052e16;
    color: white;
    border-radius: 15px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
st.sidebar.title("🐐 SAI GOAT FARM")

st.sidebar.markdown("""
### Navigation
""")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "About Us",
        "Our Breeds",
        "Our Services",
        "Why Choose Us",
        "Gallery",
        "Contact"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "🐐 Quality Goat Farming\n\n"
    "🌱 Healthy & Natural Farming\n\n"
    "📍 Maharashtra, India"
)


# =========================================================
# HOME
# =========================================================

if page == "Home":

    st.markdown("""
    <div class="hero">

        <div style="font-size:80px;">🐐</div>

        <h1>SAI GOAT FARM</h1>

        <h3>
        Healthy Goats • Better Farming • Better Future
        </h3>

        <div class="badge">
        🏷️ Goat Farming & Livestock Business
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Welcome to SAI GOAT FARM</div>',
        unsafe_allow_html=True
    )

    st.write(
        """
        **SAI GOAT FARM** is a goat farming and livestock business focused
        on healthy goat rearing, quality livestock management and sustainable
        farming practices.

        Our goal is to provide healthy goats and promote modern,
        responsible and profitable goat farming.
        """
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🐐 Quality Goats</h3>
        <p>
        We focus on healthy and well-maintained goats with proper care.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🌱 Natural Farming</h3>
        <p>
        Focus on proper feeding, hygiene and healthy farming practices.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>🤝 Customer Trust</h3>
        <p>
        We believe in transparent service and long-term customer relationships.
        </p>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# ABOUT
# =========================================================

elif page == "About Us":

    st.markdown(
        '<div class="section-title">🐐 About SAI GOAT FARM</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1524024973431-2ad916746881?auto=format&fit=crop&w=900&q=80",
            use_container_width=True
        )

    with col2:

        st.subheader("Our Story")

        st.write("""
        SAI GOAT FARM is a growing livestock farming business dedicated
        to goat rearing and quality livestock management.

        We believe that successful goat farming requires proper feeding,
        clean surroundings, regular care and responsible management.
        """)

        st.subheader("Our Mission")

        st.write("""
        To build a sustainable goat farming business by maintaining
        healthy livestock, adopting better farming practices and
        delivering value to customers.
        """)

        st.subheader("Our Vision")

        st.write("""
        To become a trusted name in goat farming and livestock business.
        """)


# =========================================================
# BREEDS
# =========================================================

elif page == "Our Breeds":

    st.markdown(
        '<div class="section-title">🐐 Our Goat Breeds</div>',
        unsafe_allow_html=True
    )

    breeds = [
        ("🐐 Osmanabadi",
         "A popular goat breed from Maharashtra, known for adaptability and farming suitability."),

        ("🐐 Sirohi",
         "A well-known Indian goat breed suitable for meat production and different climatic conditions."),

        ("🐐 Beetal",
         "A large Indian goat breed known for good body size and productive characteristics."),

        ("🐐 Jamunapari",
         "One of India's well-known breeds, recognized for its large size and distinctive appearance.")
    ]

    cols = st.columns(2)

    for i, (name, description) in enumerate(breeds):

        with cols[i % 2]:

            st.markdown(f"""
            <div class="card">

            <h3>{name}</h3>

            <p>{description}</p>

            </div>
            """, unsafe_allow_html=True)


# =========================================================
# SERVICES
# =========================================================

elif page == "Our Services":

    st.markdown(
        '<div class="section-title">🌾 Our Services</div>',
        unsafe_allow_html=True
    )

    services = [
        ("🐐 Goat Rearing",
         "Proper care, feeding and management of goats."),

        ("🏡 Livestock Management",
         "Focus on clean housing and healthy livestock management."),

        ("🌱 Feed Management",
         "Proper feeding practices for healthy goat growth."),

        ("🤝 Goat Sales",
         "Quality livestock available for interested customers."),

        ("📚 Farming Guidance",
         "Basic guidance for people interested in goat farming."),

        ("🚜 Sustainable Farming",
         "Encouraging responsible and sustainable livestock farming.")
    ]

    cols = st.columns(3)

    for i, (title, description) in enumerate(services):

        with cols[i % 3]:

            st.markdown(f"""
            <div class="card">

            <h3>{title}</h3>

            <p>{description}</p>

            </div>
            """, unsafe_allow_html=True)


# =========================================================
# WHY CHOOSE US
# =========================================================

elif page == "Why Choose Us":

    st.markdown(
        '<div class="section-title">⭐ Why Choose SAI GOAT FARM?</div>',
        unsafe_allow_html=True
    )

    points = [
        "🐐 Focus on healthy livestock",
        "🌱 Responsible farming practices",
        "🥬 Proper feeding and care",
        "🧹 Clean farming environment",
        "🤝 Customer-focused approach",
        "📈 Focus on sustainable growth"
    ]

    for point in points:
        st.success(point)


# =========================================================
# GALLERY
# =========================================================

elif page == "Gallery":

    st.markdown(
        '<div class="section-title">📸 Our Gallery</div>',
        unsafe_allow_html=True
    )

    images = [
        "https://images.unsplash.com/photo-1524024973431-2ad916746881?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1484557985045-edf25e08da73?auto=format&fit=crop&w=900&q=80",
        "https://images.unsplash.com/photo-1598974357801-cbca100e65d3?auto=format&fit=crop&w=900&q=80"
    ]

    cols = st.columns(3)

    for i, image in enumerate(images):

        with cols[i]:

            st.image(
                image,
                use_container_width=True
            )


# =========================================================
# CONTACT
# =========================================================

elif page == "Contact":

    st.markdown(
        '<div class="section-title">📞 Contact Us</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="contact">

        <h2>🐐 SAI GOAT FARM</h2>

        <p>Healthy Goats • Better Farming • Better Future</p>

        <br>

        <p>📱 <b>9579187477</b></p>

        <p>📧 <b>ashutosh123@gmail.com</b></p>

        <p>🏷️ <b>Goat Farming & Livestock Business</b></p>

        <p>📍 Maharashtra, India</p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("###")

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "📱 Contact on WhatsApp",
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

st.markdown("""
<div class="footer">

    <h3>🐐 SAI GOAT FARM</h3>

    <p>Healthy Goats • Better Farming • Better Future</p>

    <p>
    © 2026 SAI GOAT FARM. All Rights Reserved.
    </p>

</div>
""", unsafe_allow_html=True)
