import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Water Supply Digital Support Portal",
    page_icon="💧",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #0066cc; }
    .sub-title { font-size: 18px; color: #555555; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("💧 AquaSupport Nav")
menu = st.sidebar.radio(
    "Select Portal Section:",
    ["🏠 Home / Overview", "👥 Citizen Digital Guide", "📚 Staff Training & SOPs", "❓ Digital Helpdesk & FAQ", "📝 Report an Issue"]
)

# --- HOME SECTION ---
if menu == "🏠 Home / Overview":
    st.markdown('<p class="main-title">Local Government Water Supply Department</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Digital Skill Support & Service Management Portal</p>', unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### 👥 For Citizens\nLearn how to pay bills online, track water schedules, and submit digital grievances easily.")
    with col2:
        st.success("### 🛠️ For Staff\nAccess Standard Operating Procedures (SOPs), digital meter reading guides, and ticketing tools.")
    with col3:
        st.warning("### 📊 Live Status\n- **Pumping Stations:** Operational\n- **Digital Portal:** Online\n- **Support Line:** Active")

# --- CITIZEN DIGITAL GUIDE ---
elif menu == "👥 Citizen Digital Guide":
    st.markdown('<p class="main-title">Citizen Digital Assistance Guide</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["💳 Online Bill Payment", "🚰 Report a Leak / Burst", "⏰ Check Supply Schedule"])

    with tab1:
        st.markdown("### How to Pay Your Water Bill Online")
        st.markdown("""
        1. **Visit the Portal:** Go to the official municipal water portal website.
        2. **Enter Consumer Number:** Find your 10-digit consumer number printed on your bill.
        3. **Make Payment:** Choose UPI, Credit/Debit Card, or Net Banking to complete the transaction.
        """)

    with tab2:
        st.markdown("### How to Report a Pipe Leakage")
        st.markdown("""
        1. Take a clear photo of the leak.
        2. Open the **Report an Issue** tab on this portal.
        3. Submit details to get an instant tracking ID.
        """)

    with tab3:
        st.markdown("### Checking Local Water Supply Timings")
        st.markdown("Select your zone from our app menu to view daily supply hours and emergency shutdown notices.")

# --- STAFF TRAINING & SOPS ---
elif menu == "📚 Staff Training & SOPs":
    st.markdown('<p class="main-title">Internal Staff Training & Digital SOPs</p>', unsafe_allow_html=True)

    with st.expander("📖 Module 1: Using the Digital Ticketing System"):
        st.write("Review incoming citizen grievances, categorize them by urgency, and assign them to zonal field teams within 30 minutes.")

    with st.expander("📖 Module 2: Managing Smart Meters & Data Logs"):
        st.write("Connect handheld Bluetooth reader devices to the central municipal database and sync daily reading logs before 5:00 PM.")

# --- DIGITAL HELPDESK & FAQ ---
elif menu == "❓ Digital Helpdesk & FAQ":
    st.markdown('<p class="main-title">Frequently Asked Questions (FAQ)</p>', unsafe_allow_html=True)
    
    with st.expander("What should I do if my online payment failed?"):
        st.write("Amounts deducted due to gateway failures are automatically refunded within 3-5 business days.")

    with st.expander("How do I change my registered mobile number?"):
        st.write("Visit the local municipal office water desk with valid identity proof.")

# --- REPORT AN ISSUE ---
elif menu == "📝 Report an Issue":
    st.markdown('<p class="main-title">Digital Issue Submission Form</p>', unsafe_allow_html=True)

    with st.form("issue_form"):
        name = st.text_input("Full Name")
        contact = st.text_input("Mobile Number / Email")
        issue_type = st.selectbox("Issue Category", ["No Water Supply", "Pipe Leakage / Burst", "Contaminated Water", "Billing Dispute", "Other"])
        description = st.text_area("Detailed Description of the Issue")
        
        submitted = st.form_submit_button("Submit Complaint")
        if submitted:
            if name and contact and description:
                st.success(f"Thank you, {name}! Your complaint has been registered. Tracking ID: **#WTR-2026-8942**.")
            else:
                st.error("Please fill in all mandatory fields.")
