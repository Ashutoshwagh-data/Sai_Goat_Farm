import streamlit as st

st.set_page_config(
    page_title="Sai Goat Farm",
    page_icon="🐐",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>

.stApp {
    background: #f7fbf7;
}

.hero {
    padding: 60px 25px;
    border-radius: 25px;
    text-align: center;
    background: linear-gradient(135deg, #14532d, #22c55e);
    color: white;
    margin-bottom: 35px;
}

.hero h1 {
    font-size: 58px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    font-size: 21px;
}

.logo {
    font-size: 70px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
    min-height: 180px;
    margin-bottom: 20px;
}

.goat-card {
    background: white;
    padding: 15px;
    border-radius: 20px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.10);
    text-align: center;
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

</style>
""", unsafe_allow_html=True)


# ---------- HERO ----------
st.markdown("""
<div class="hero">

<div class="logo">🐐</div>

<h1>SAI GOAT FARM</h1>

<p>Healthy Goats • Quality Farming • Trusted Service</p>

<p>🌱 Professional Goat Rearing & Livestock Management</p>

</div>
""", unsafe_allow_html=True)


# ---------- ABOUT ----------
st.header("🌱 Welcome to Sai Goat Farm")

st.markdown("""
<div class="card">

<h2>🐐 About Sai Goat Farm</h2>

<p>
Sai Goat Farm is focused on healthy goat rearing,
proper feeding, livestock care and quality goat management.
</p>

<p>
Our goal is to provide healthy and quality goats
while following proper farming and management practices.
</p>

</div>
""", unsafe_allow_html=True)


# ---------- SERVICES ----------
st.header("🌾 Our Services")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <h2>🐐 Goat Rearing</h2>
    <p>
    Proper care, feeding and management of goats
    for healthy growth.
    </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h2>🌾 Quality Feed</h2>
    <p>
    Focus on proper nutrition and feeding practices
    for healthy livestock.
    </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h2>🤝 Customer Support</h2>
    <p>
    Contact us for goat availability, pricing
    and farming information.
    </p>
    </div>
    """, unsafe_allow_html=True)


# ---------- GOAT COLLECTION ----------
st.header("🐐 Our Goat Collection")

g1, g2 = st.columns(2)

with g1:

    st.markdown('<div class="goat-card">', unsafe_allow_html=True)

    st.image(
        "images/10-months-old-healthy-male-live-beetal-goat-with-25-kilograms-weight-640.jpg",
        caption="🐐 Beetal Goat",
        use_container_width=True
    )

    st.markdown("""
    <h2>Beetal Goat</h2>
    <p>Healthy and quality Beetal breed.</p>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


with g2:

    st.markdown('<div class="goat-card">', unsafe_allow_html=True)

    st.image(
        "images/e5a3a59f732d25419dc2cd33d1845104",
        caption="🐐 Boer Goat",
        use_container_width=True
    )

    st.markdown("""
    <h2>Boer Goat</h2>
    <p>Quality Boer breed livestock.</p>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- WHY US ----------
st.header("⭐ Why Choose Sai Goat Farm")

col1, col2 = st.columns(2)

with col1:
    st.success("✓ Healthy goat rearing")
    st.success("✓ Proper feeding & care")
    st.success("✓ Quality livestock")

with col2:
    st.success("✓ Customer-focused service")
    st.success("✓ Transparent communication")
    st.success("✓ Professional farming")


# ---------- ENQUIRY ----------
st.header("📝 Send Your Enquiry")

with st.form("enquiry"):

    name = st.text_input("👤 Your Name")

    phone = st.text_input("📱 Mobile Number")

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

    message = st.text_area("💬 Your Message")

    submit = st.form_submit_button("Submit Enquiry")

    if submit:

        if name and phone and message:

            st.success(
                f"Thank you {name}! Your enquiry for "
                f"{goat_type} has been received."
            )

        else:

            st.warning(
                "Please fill all required details."
            )


# ---------- CONTACT ----------
st.header("📞 Contact Sai Goat Farm")

st.markdown("""
<div class="contact-card">

<h1>🐐 SAI GOAT FARM</h1>

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


# ---------- FOOTER ----------
st.markdown("""
<div class="footer">

<hr>

🐐 <b>SAI GOAT FARM</b>

<br>

Healthy Goats • Better Farming • Trusted Service

<br><br>

© 2026 Sai Goat Farm

</div>
""", unsafe_allow_html=True)
