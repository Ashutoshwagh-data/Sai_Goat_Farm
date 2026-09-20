import streamlit as st

st.set_page_config(
    page_title="Sai Goat Farm",
    page_icon="🐐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
    .stApp {
        background: #f7fbf7;
    }

    .hero {
        padding: 70px 30px;
        border-radius: 25px;
        text-align: center;
        background: linear-gradient(135deg, #14532d, #22c55e);
        color: white;
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 58px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 22px;
    }

    .card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
        min-height: 180px;
        margin-bottom: 20px;
    }

    .contact-card {
        background: #dcfce7;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
    }

    .whatsapp {
        display: inline-block;
        padding: 13px 25px;
        background: #25D366;
        color: white !important;
        text-decoration: none;
        border-radius: 30px;
        font-weight: bold;
        font-size: 18px;
    }

    .footer {
        text-align: center;
        padding: 25px;
        color: #555;
    }

    h2 {
        color: #14532d;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <h1>🐐 Sai Goat Farm</h1>
    <p>Healthy Goats • Quality Farming • Trusted Service</p>
    <p>🌱 Professional Goat Rearing & Livestock Management</p>
</div>
""", unsafe_allow_html=True)


# ---------------- INTRO ----------------
st.header("🌱 Welcome to Sai Goat Farm")

st.markdown("""
<div class="card">

### 🐐 About Us

Sai Goat Farm is a goat farming business focused on healthy goat
rearing, proper feeding, livestock care and customer satisfaction.

Our aim is to provide healthy and quality goats while following
proper farming and management practices.

</div>
""", unsafe_allow_html=True)


# ---------------- SERVICES ----------------
st.header("🐐 Our Services")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <h2>🐐 Goat Rearing</h2>
        <p>
        Proper care, feeding and management of goats for healthy growth.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h2>🌾 Quality Feed</h2>
        <p>
        Focus on proper nutrition and feeding practices for livestock.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h2>🤝 Customer Support</h2>
        <p>
        Contact us for goat availability, pricing and farming information.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- GOAT TYPES ----------------
st.header("🐐 Our Goat Collection")

g1, g2, g3 = st.columns(3)

with g1:
    st.image(
        "https://images.unsplash.com/photo-1524024973431-2ad916746881",
        caption="Healthy Goat"
    )

with g2:
    st.image(
        "https://images.unsplash.com/photo-1484557985045-edf25e08da73",
        caption="Goat Farming"
    )

with g3:
    st.image(
        "https://images.unsplash.com/photo-1516734212186-a967f81ad0d7",
        caption="Quality Livestock"
    )


# ---------------- WHY US ----------------
st.header("⭐ Why Choose Sai Goat Farm?")

col1, col2 = st.columns(2)

with col1:
    st.success("✓ Healthy goat rearing")
    st.success("✓ Proper feeding & care")
    st.success("✓ Quality livestock")

with col2:
    st.success("✓ Customer-focused service")
    st.success("✓ Transparent communication")
    st.success("✓ Farming management")


# ---------------- ENQUIRY ----------------
st.header("📝 Send Your Enquiry")

with st.form("enquiry"):

    name = st.text_input("👤 Your Name")

    phone = st.text_input("📱 Mobile Number")

    goat_type = st.selectbox(
        "🐐 What are you looking for?",
        [
            "Goat",
            "Goat Farming Information",
            "Goat Price",
            "Other"
        ]
    )

    message = st.text_area("💬 Your Message")

    submit = st.form_submit_button("Submit Enquiry")

    if submit:

        if name and phone and message:
            st.success(
                f"Thank you {name}! Your enquiry has been submitted."
            )
        else:
            st.warning("Please fill all required details.")


# ---------------- CONTACT ----------------
st.header("📞 Contact Sai Goat Farm")

st.markdown("""
<div class="contact-card">

<h2>🐐 Sai Goat Farm</h2>

<p>📱 <b>9579187477</b></p>

<p>📧 <b>ashutosh123@gmail.com</b></p>

<br>

<a class="whatsapp"
href="https://wa.me/919579187477"
target="_blank">
💬 Chat on WhatsApp
</a>

</div>
""", unsafe_allow_html=True)


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
<hr>
🐐 <b>Sai Goat Farm</b><br>
Healthy Goats • Better Farming • Trusted Service<br><br>
© 2026 Sai Goat Farm
</div>
""", unsafe_allow_html=True)
