import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="SAI GOAT FARM",
    page_icon="🐐",
    layout="wide"
)

# =========================================================
# SIDEBAR
# =========================================================

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

st.sidebar.divider()

st.sidebar.write("🏷️ Goat Farming & Livestock Business")
st.sidebar.write("📍 Chitali, Rahata, Ahilyanagar")
st.sidebar.write("📱 9579187477")


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.title("🐐 SAI GOAT FARM")

    st.subheader(
        "Healthy Goats • Better Farming • Better Future"
    )

    st.success(
        "🏷️ Goat Farming & Livestock Business"
    )

    st.divider()

    st.header("Welcome to SAI GOAT FARM")

    st.write(
        """
        **SAI GOAT FARM** is a goat farming and livestock business
        located at Chitali, Rahata, Ahilyanagar, Maharashtra.

        Our focus is on healthy goat rearing, proper feeding,
        clean management and responsible livestock farming practices.
        """
    )

    st.divider()

    st.header("What We Focus On")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🐐 Healthy Goats")
        st.write(
            "Focus on proper care, feeding and healthy goat management."
        )

    with col2:
        st.subheader("🌱 Better Farming")
        st.write(
            "Responsible and sustainable goat farming practices."
        )

    with col3:
        st.subheader("🤝 Customer Trust")
        st.write(
            "Quality, transparency and long-term relationships."
        )

    st.divider()

    st.header("Our Business")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🐐 Business Name: SAI GOAT FARM")
        st.info("🏷️ Category: Goat Farming & Livestock Business")

    with col2:
        st.success(
            "💬 Healthy Goats • Better Farming • Better Future"
        )
        st.success(
            "📍 At Post Chitali, Ta. Rahata, Dist. Ahilyanagar"
        )


# =========================================================
# ABOUT US
# =========================================================

elif page == "📖 About Us":

    st.title("📖 About SAI GOAT FARM")

    st.write(
        """
        **SAI GOAT FARM** is a livestock farming business focused
        on goat rearing and goat farming.

        We aim to maintain healthy goats through proper feeding,
        clean surroundings and responsible livestock management.
        """
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 Our Mission")

        st.write(
            """
            To develop a sustainable goat farming business by
            maintaining healthy livestock and following better
            farming practices.
            """
        )

    with col2:
        st.subheader("🚀 Our Vision")

        st.write(
            """
            To become a trusted name in goat farming and
            livestock business.
            """
        )

    st.divider()

    st.info(
        "🐐 Our goal is to combine proper goat care with better farming practices."
    )


# =========================================================
# GOAT BREEDS
# =========================================================

elif page == "🐐 Goat Breeds":

    st.title("🐐 Our Goat Breeds")

    st.write(
        "SAI GOAT FARM focuses on different popular goat breeds."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🐐 Beetel")

        st.write(
            """
            A well-known Indian goat breed with good body size
            and productive characteristics.
            """
        )

        st.info("💰 Price: As per breed")

        st.divider()

        st.subheader("🐐 Osmanabadi")

        st.write(
            """
            A popular Maharashtra breed known for adaptability
            and suitability to local conditions.
            """
        )

        st.info("💰 Price: As per breed")

    with col2:

        st.subheader("🐐 Boer")

        st.write(
            """
            A popular meat goat breed known for its growth
            and strong body structure.
            """
        )

        st.info("💰 Price: As per breed")

        st.divider()

        st.subheader("🐐 Sannen")

        st.write(
            """
            A well-known dairy goat breed recognized for
            milk production.
            """
        )

        st.info("💰 Price: As per breed")


# =========================================================
# SERVICES
# =========================================================

elif page == "🌾 Services":

    st.title("🌾 Our Services")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🐐 Goat Rearing")
        st.write(
            "Proper care and management of goats."
        )

    with col2:
        st.subheader("🌱 Feed Management")
        st.write(
            "Proper feeding and nutrition management."
        )

    with col3:
        st.subheader("🏡 Livestock Management")
        st.write(
            "Clean and responsible goat management."
        )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🤝 Goat Sales")
        st.write(
            "Goats available according to breed and requirements."
        )

    with col2:
        st.subheader("📚 Farming Guidance")
        st.write(
            "Basic guidance for people interested in goat farming."
        )

    with col3:
        st.subheader("🚜 Sustainable Farming")
        st.write(
            "Responsible livestock farming practices."
        )


# =========================================================
# WHY CHOOSE US
# =========================================================

elif page == "⭐ Why Choose Us":

    st.title("⭐ Why Choose SAI GOAT FARM?")

    st.divider()

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

    st.title("📞 Contact SAI GOAT FARM")

    st.divider()

    st.header("🐐 SAI GOAT FARM")

    st.subheader(
        "Healthy Goats • Better Farming • Better Future"
    )

    st.info(
        "📱 Phone: 9579187477"
    )

    st.info(
        "📧 Email: ashutosh123@gmail.com"
    )

    st.info(
        "📍 At Post Chitali, Ta. Rahata, Dist. Ahilyanagar"
    )

    st.info(
        "🏷️ Goat Farming & Livestock Business"
    )

    st.divider()

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

st.divider()

st.caption(
    "🐐 SAI GOAT FARM | Healthy Goats • Better Farming • Better Future"
)

st.caption(
    "📱 9579187477 | 📧 ashutosh123@gmail.com"
)

st.caption(
    "© 2026 SAI GOAT FARM • All Rights Reserved"
)
