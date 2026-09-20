import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Sai Goat Farm",
    page_icon="🐐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# IMAGE URLS
# =========================================================

BEETAL_IMAGE = (
    "https://commons.wikimedia.org/wiki/"
    "Special:FilePath/Beetal%20goat.jpg"
)

BOER_IMAGE = (
    "https://commons.wikimedia.org/wiki/"
    "Special:FilePath/Boer%20Goat%20%2849944899088%29.jpg"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: #f7fbf7;
    }

    /* Remove top padding */
    .block-container {
        padding-top: 2rem;
    }

    /* Hero section */
    .hero {
        padding: 65px 25px;
        border-radius: 28px;
        text-align: center;
        background:
            linear-gradient(
                135deg,
                #064e3b,
                #15803d,
                #22c55e
            );
        color: white;
        margin-bottom: 35px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
    }

    .hero-logo {
        font-size: 75px;
        margin-bottom: 5px;
    }

    .hero h1 {
        font-size: 58px;
        font-weight: 900;
        letter-spacing: 2px;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 21px;
        margin: 7px;
    }

    .tagline {
        font-size: 17px !important;
        opacity: 0.9;
    }

    /* Section headings */
    .section-title {
        color: #14532d;
        font-size: 34px;
        font-weight: 800;
        margin-top: 25px;
        margin-bottom: 20px;
    }

    /* General card */
    .card {
        background: white;
        padding: 28px;
        border-radius: 20px;
        box-shadow: 0px 5px 22px rgba(0,0,0,0.08);
        min-height: 190px;
        margin-bottom: 20px;
        border: 1px solid #e5e7eb;
    }

    .card h2 {
        color: #166534;
        margin-bottom: 12px;
    }

    .card p {
        color: #4b5563;
        font-size: 16px;
        line-height: 1.6;
    }

    /* Goat cards */
    .goat-title {
        text-align: center;
        color: #14532d;
        font-size: 25px;
        font-weight: 800;
        margin-top: 10px;
    }

    .goat-description {
        text-align: center;
        color: #555;
        font-size: 16px;
    }

    /* Contact card */
    .contact-card {
        background:
            linear-gradient(
                135deg,
                #dcfce7,
                #bbf7d0
            );
        padding: 35px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
    }

    .contact-card h1 {
        color: #14532d;
        font-size: 38px;
    }

    .contact-card p {
        font-size: 19px;
        color: #166534;
    }

    /* WhatsApp button */
    .whatsapp {
        display: inline-block;
        padding: 14px 28px;
        background: #25D366;
        color: white !important;
        text-decoration: none;
        border-radius: 30px;
        font-weight: bold;
        font-size: 18px;
        transition: 0.3s;
    }

    .whatsapp:hover {
        background: #128C7E;
        transform: scale(1.03);
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 30px;
        color: #555;
    }

    .footer-title {
        color: #14532d;
        font-size: 22px;
        font-weight: bold;
    }

    /* Stats */
    .stat-card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 5px 18px rgba(0,0,0,0.07);
    }

    .stat-number {
        color: #15803d;
        font-size: 35px;
        font-weight: 900;
    }

    .stat-text {
        color: #555;
        font-size: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-logo">🐐</div>

        <h1>SAI GOAT FARM</h1>

        <p>
            Healthy Goats • Quality Farming • Trusted Service
        </p>

        <p class="tagline">
            🌱 Professional Goat Rearing & Livestock Management
        </p>

    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# QUICK STATS
# =========================================================

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">🐐</div>
            <div class="stat-text">Quality Goats</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with s2:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">🌾</div>
            <div class="stat-text">Quality Feed</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with s3:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">❤️</div>
            <div class="stat-text">Proper Care</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with s4:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">🤝</div>
            <div class="stat-text">Trusted Service</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# =========================================================
# ABOUT US
# =========================================================

st.markdown(
    '<div class="section-title">🌱 About Sai Goat Farm</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="card">

        <h2>🐐 Our Farm</h2>

        <p>
        Sai Goat Farm is focused on healthy goat rearing,
        proper feeding, livestock care and quality goat
        management.
        </p>

        <p>
        Our goal is to provide healthy and quality goats
        while following proper farming and management
        practices.
        </p>

        <p>
        We believe that proper nutrition, cleanliness,
        regular care and good management are important
        for successful goat farming.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SERVICES
# =========================================================

st.markdown(
    '<div class="section-title">🌾 Our Services</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="card">

            <h2>🐐 Goat Rearing</h2>

            <p>
            Proper care, feeding and management of goats
            for healthy growth and development.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="card">

            <h2>🌾 Quality Feed</h2>

            <p>
            Focus on proper nutrition and feeding practices
            for healthy livestock.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="card">

            <h2>🤝 Customer Support</h2>

            <p>
            Contact us for goat availability, pricing,
            farming information and enquiries.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# GOAT COLLECTION
# =========================================================

st.markdown(
    '<div class="section-title">🐐 Our Goat Collection</div>',
    unsafe_allow_html=True
)

g1, g2 = st.columns(2)

# ---------------- BEETAL ----------------

with g1:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    try:
        st.image(
            BEETAL_IMAGE,
            caption="🐐 Beetal Goat",
            use_container_width=True
        )
    except Exception:
        st.warning(
            "Beetal goat image could not be loaded."
        )

    st.markdown(
        """
        <div class="goat-title">
            Beetal Goat
        </div>

        <div class="goat-description">
            Healthy and quality Beetal breed.
            <br>
            Suitable for professional goat farming.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ---------------- BOER ----------------

with g2:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    try:
        st.image(
            BOER_IMAGE,
            caption="🐐 Boer Goat",
            use_container_width=True
        )
    except Exception:
        st.warning(
            "Boer goat image could not be loaded."
        )

    st.markdown(
        """
        <div class="goat-title">
            Boer Goat
        </div>

        <div class="goat-description">
            Quality Boer breed livestock.
            <br>
            Known for good growth and meat production.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# =========================================================
# WHY CHOOSE US
# =========================================================

st.markdown(
    '<div class="section-title">⭐ Why Choose Sai Goat Farm?</div>',
    unsafe_allow_html=True
)

w1, w2 = st.columns(2)

with w1:

    st.success("✓ Healthy goat rearing")
    st.success("✓ Proper feeding & care")
    st.success("✓ Quality livestock")

with w2:

    st.success("✓ Customer-focused service")
    st.success("✓ Transparent communication")
    st.success("✓ Professional farming")

# =========================================================
# ENQUIRY FORM
# =========================================================

st.markdown(
    '<div class="section-title">📝 Send Your Enquiry</div>',
    unsafe_allow_html=True
)

with st.form("enquiry_form"):

    name = st.text_input(
        "👤 Your Name"
    )

    phone = st.text_input(
        "📱 Mobile Number"
    )

    goat_type = st.selectbox(
        "🐐 What are you looking for?",
        [
            "Beetal Goat",
            "Boer Goat",
            "Other Goat",
            "Goat Farming Information",
            "Goat Price"
        ]
    )

    message = st.text_area(
        "💬 Your Message"
    )

    submit = st.form_submit_button(
        "Submit Enquiry"
    )

    if submit:

        if name and phone and message:

            st.success(
                f"Thank you {name}! "
                f"Your enquiry for {goat_type} "
                f"has been received."
            )

        else:

            st.warning(
                "Please fill all required details."
            )

# =========================================================
# CONTACT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">📞 Contact Us</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="contact-card">

        <h1>🐐 SAI GOAT FARM</h1>

        <p>
            📱 <b>9579187477</b>
        </p>

        <p>
            📧 <b>ashutosh123@gmail.com</b>
        </p>

        <br>

        <a
            class="whatsapp"
            href="https://wa.me/919579187477"
            target="_blank"
        >
            💬 Chat on WhatsApp
        </a>

    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        <hr>

        <div class="footer-title">
            🐐 SAI GOAT FARM
        </div>

        <p>
            Healthy Goats • Better Farming • Trusted Service
        </p>

        <p>
            © 2026 Sai Goat Farm | All Rights Reserved
        </p>

    </div>
    """,
    unsafe_allow_html=True
)
