import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Startup Builder",
    page_icon="🚀",
    layout="wide"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

/* Main page */
.stApp {
    background-color: #f4f6fb;
}

/* Headings */
h1, h2, h3, h4 {
    color: #111827 !important;
}

/* Subtitle */
.subtitle {
    color: #374151 !important;
    font-size: 17px;
}

/* Main title */
.main-title {
    color: #111827 !important;
    font-size: 38px;
    font-weight: 800;
}

/* ==========================================================
   BLUE INFORMATION BOX
   ========================================================== */

.blue-box {
    background-color: #2563eb !important;
    color: white !important;

    border: 2px solid #1d4ed8;
    border-radius: 10px;

    padding: 16px 20px;
    margin: 12px 0;

    font-size: 16px;
    font-weight: 500;

    line-height: 1.6;

    box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25);
}

/* Force ALL text inside blue box to white */
.blue-box,
.blue-box p,
.blue-box div,
.blue-box span,
.blue-box strong,
.blue-box b {
    color: white !important;
}

/* Box title */
.blue-title {
    color: white !important;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 5px;
}

/* ==========================================================
   IDEA BOX
   ========================================================== */

.idea-box {
    background-color: #2563eb !important;
    color: white !important;

    border: 2px solid #1d4ed8;
    border-radius: 12px;

    padding: 20px;
    margin: 14px 0;

    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
}

.idea-box h3,
.idea-box p,
.idea-box strong,
.idea-box b {
    color: white !important;
}

/* ==========================================================
   SUCCESS BOX
   ========================================================== */

.success-box {
    background-color: #2563eb !important;
    color: white !important;

    border: 2px solid #1d4ed8;
    border-radius: 10px;

    padding: 18px;
    margin: 12px 0;

    font-size: 16px;
    line-height: 1.6;
}

.success-box,
.success-box p,
.success-box strong,
.success-box b {
    color: white !important;
}

/* ==========================================================
   RISK BOX
   ========================================================== */

.risk-box {
    background-color: #2563eb !important;
    color: white !important;

    border: 2px solid #1d4ed8;
    border-radius: 10px;

    padding: 16px 20px;
    margin: 12px 0;

    font-size: 16px;
    font-weight: 500;

    line-height: 1.6;

    box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25);
}

.risk-box,
.risk-box p,
.risk-box div,
.risk-box span,
.risk-box strong,
.risk-box b {
    color: white !important;
}

/* ==========================================================
   ROADMAP BOX
   ========================================================== */

.roadmap-box {
    background-color: #2563eb !important;
    color: white !important;

    border: 2px solid #1d4ed8;
    border-radius: 10px;

    padding: 16px 20px;
    margin: 12px 0;

    font-size: 16px;
    line-height: 1.6;

    box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25);
}

.roadmap-box,
.roadmap-box p,
.roadmap-box div,
.roadmap-box span,
.roadmap-box strong,
.roadmap-box b {
    color: white !important;
}

/* ==========================================================
   MARKETING BOX
   ========================================================== */

.marketing-box {
    background-color: #2563eb !important;
    color: white !important;

    border: 2px solid #1d4ed8;
    border-radius: 10px;

    padding: 16px 20px;
    margin: 12px 0;

    font-size: 16px;
    line-height: 1.6;

    box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25);
}

.marketing-box,
.marketing-box p,
.marketing-box div,
.marketing-box span,
.marketing-box strong,
.marketing-box b {
    color: white !important;
}

/* ==========================================================
   CUSTOMER / REVENUE BOX
   ========================================================== */

.customer-box {
    background-color: #2563eb !important;
    color: white !important;

    border: 2px solid #1d4ed8;
    border-radius: 10px;

    padding: 16px 20px;
    margin: 12px 0;

    font-size: 16px;
    line-height: 1.6;
}

.customer-box,
.customer-box p,
.customer-box div,
.customer-box span,
.customer-box strong,
.customer-box b {
    color: white !important;
}

/* ==========================================================
   USER IDEA BOX
   ========================================================== */

.user-idea {
    background-color: #2563eb !important;
    color: white !important;

    border: 2px solid #1d4ed8;
    border-radius: 10px;

    padding: 18px;
    margin: 12px 0;

    font-size: 17px;
    line-height: 1.6;
}

.user-idea,
.user-idea p,
.user-idea div,
.user-idea span,
.user-idea strong,
.user-idea b {
    color: white !important;
}

/* ==========================================================
   METRICS
   ========================================================== */

[data-testid="stMetricValue"] {
    color: #111827 !important;
}

[data-testid="stMetricLabel"] {
    color: #374151 !important;
}

/* ==========================================================
   BUTTONS
   ========================================================== */

.stButton > button {
    width: 100%;
    min-height: 45px;
    border-radius: 8px;
    font-weight: 600;
}

/* ==========================================================
   INPUT LABELS
   ========================================================== */

label {
    color: #111827 !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# INDUSTRY DATA
# ============================================================

INDUSTRY_DATA = {

    "Food": {
        "ideas": [
            "AI Smart Canteen Ordering System",
            "Food Waste Prediction System",
            "Healthy Meal Recommendation App",
            "Campus Food Delivery Platform"
        ],
        "customers": [
            "College Students",
            "College Staff",
            "Hostels",
            "Small Canteens"
        ],
        "revenue": [
            "Small transaction fee",
            "Monthly subscription",
            "Canteen partnership",
            "Premium analytics"
        ]
    },

    "Education": {
        "ideas": [
            "AI Personalized Study Planner",
            "AI Career Guidance Platform",
            "Student Performance Prediction System",
            "AI Notes and Question Generator"
        ],
        "customers": [
            "Students",
            "Colleges",
            "Teachers",
            "Coaching Institutes"
        ],
        "revenue": [
            "Freemium subscription",
            "College subscription",
            "Premium AI features",
            "Advertisements"
        ]
    },

    "Healthcare": {
        "ideas": [
            "AI Healthcare Assistant",
            "Smart Appointment Management",
            "Medicine Reminder Platform",
            "Hospital Queue Prediction System"
        ],
        "customers": [
            "Patients",
            "Clinics",
            "Hospitals",
            "Caregivers"
        ],
        "revenue": [
            "Clinic subscription",
            "Premium features",
            "Hospital partnerships",
            "Service commission"
        ]
    },

    "Technology": {
        "ideas": [
            "AI Coding Mentor",
            "AI Business Automation Platform",
            "No-Code Startup Builder",
            "AI Resume and Job Matching Platform"
        ],
        "customers": [
            "Students",
            "Startups",
            "Small Businesses",
            "Developers"
        ],
        "revenue": [
            "Subscription",
            "Premium tools",
            "Business licensing",
            "API usage"
        ]
    },

    "Agriculture": {
        "ideas": [
            "AI Crop Disease Detection",
            "Smart Irrigation System",
            "Crop Price Prediction Platform",
            "AI Farming Assistant"
        ],
        "customers": [
            "Farmers",
            "Agricultural Organizations",
            "Agri Businesses",
            "Government Programs"
        ],
        "revenue": [
            "Subscription",
            "Agri-business partnerships",
            "Commission",
            "Premium analytics"
        ]
    },

    "Finance": {
        "ideas": [
            "AI Student Budget Planner",
            "Smart Expense Tracker",
            "AI Financial Planning Assistant",
            "Small Business Finance Manager"
        ],
        "customers": [
            "Students",
            "Families",
            "Small Businesses",
            "Freelancers"
        ],
        "revenue": [
            "Premium subscription",
            "Business subscription",
            "Financial partnerships",
            "Premium reports"
        ]
    }
}


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🚀 AI Startup Builder</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Turn your idea into a practical startup plan with smart recommendations.</div>',
    unsafe_allow_html=True
)


# ============================================================
# HOME PAGE
# ============================================================

if st.session_state.page == "home":

    st.markdown("## 🎯 What do you want to do?")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("💡 I Have an Idea"):
            st.session_state.page = "myidea"
            st.rerun()

        if st.button("✨ Generate New Idea"):
            st.session_state.page = "newidea"
            st.rerun()

    with col2:

        if st.button("🔍 Validate My Idea"):
            st.session_state.page = "validate"
            st.rerun()

        if st.button("📊 Build My Startup"):
            st.session_state.page = "build"
            st.rerun()


# ============================================================
# INNER PAGES
# ============================================================

else:

    page_names = {
        "myidea": "💡 I Have an Idea",
        "newidea": "✨ Generate New Startup Idea",
        "validate": "🔍 Validate My Idea",
        "build": "📊 Build My Startup"
    }

    st.markdown(
        f"## {page_names[st.session_state.page]}"
    )

    # ========================================================
    # INPUTS
    # ========================================================

    col1, col2 = st.columns(2)

    with col1:

        industry = st.selectbox(
            "🏢 Select Industry",
            list(INDUSTRY_DATA.keys())
        )

        target = st.text_input(
            "🎯 Target Users",
            placeholder="Example: College Students"
        )

        budget = st.number_input(
            "💰 Available Budget (₹)",
            min_value=0,
            value=20000,
            step=5000
        )

    with col2:

        problem = st.text_area(
            "📝 Describe the Problem / Idea",
            placeholder="Example: Farmers have difficulty managing goat farm expenses.",
            height=130
        )

        skills = st.multiselect(
            "🧑‍💻 Your Skills",
            [
                "Python",
                "Java",
                "Web Development",
                "AI / ML",
                "Data Science",
                "Marketing",
                "Design",
                "Business"
            ]
        )

    st.markdown("## 🎯 Select Your Startup Goal")

    goal = st.selectbox(
        "What do you want to achieve?",
        [
            "Find a startup idea",
            "Solve a real-life problem",
            "Build a college project",
            "Start a business",
            "Create an AI product",
            "Find a profitable opportunity"
        ]
    )

    # ========================================================
    # GENERATE BUTTON
    # ========================================================

    if st.button("🚀 Generate Suggestions & Recommendations"):

        data = INDUSTRY_DATA[industry]

        st.markdown("---")

        # ====================================================
        # NEW IDEA
        # ====================================================

        if st.session_state.page == "newidea":

            st.markdown("## ✨ Recommended Startup Ideas")

            for i, idea in enumerate(data["ideas"], 1):

                st.markdown(
                    f"""
                    <div class="idea-box">
                        <div class="blue-title">
                            💡 Startup Idea {i}
                        </div>
                        <div style="color:white !important; font-size:22px; font-weight:700;">
                            {idea}
                        </div>
                        <br>
                        <div style="color:white !important;">
                            Suitable for the <b>{industry}</b> industry
                            and target users:
                            <b>{target if target else "Potential Customers"}</b>.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # ====================================================
        # MY IDEA
        # ====================================================

        elif st.session_state.page == "myidea":

            st.markdown("## 💡 Your Startup Analysis")

            idea_text = (
                problem
                if problem
                else "No problem description entered."
            )

            st.markdown(
                f"""
                <div class="user-idea">
                    <strong>💡 Your Idea / Problem</strong><br><br>
                    {idea_text}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("## 💡 Suggestions to Improve Your Idea")

            suggestions = [
                f"Clearly define the main problem faced by {target if target else 'your target customers'}.",
                f"Start with a simple MVP for the {industry} industry.",
                "Talk to at least 10 potential users before developing the complete product.",
                "Add one unique feature that makes your solution different from competitors.",
                "Test your idea with a small group before spending the complete budget.",
                "Collect user feedback and continuously improve the product."
            ]

            for i, suggestion in enumerate(suggestions, 1):

                st.markdown(
                    f"""
                    <div class="blue-box">
                        <div class="blue-title">
                            💡 Suggestion {i}
                        </div>
                        {suggestion}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # ====================================================
        # VALIDATE IDEA
        # ====================================================

        elif st.session_state.page == "validate":

            st.markdown("## 🔍 Startup Validation")

            # Problem clarity
            st.markdown(
                """
                <div class="success-box">
                    <strong>✅ Problem Clarity</strong><br><br>
                    Your idea is a good starting point.
                    Make sure the problem is specific, common and
                    important for your target users.
                </div>
                """,
                unsafe_allow_html=True
            )

            # =================================================
            # RECOMMENDATIONS
            # =================================================

            st.markdown("## 📊 Validation Recommendations")

            validation_points = [
                "Interview potential customers and understand their actual problems.",
                "Research existing competitors and compare their features.",
                "Create a small MVP instead of developing the complete product initially.",
                "Test whether users are willing to use your solution.",
                "Ask users for feedback after using the MVP.",
                "Check whether the idea can generate sustainable revenue."
            ]

            for i, item in enumerate(validation_points, 1):

                st.markdown(
                    f"""
                    <div class="blue-box">
                        <div class="blue-title">
                            🔎 Recommendation {i}
                        </div>
                        <div style="color:white !important;">
                            {item}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # =================================================
            # RISKS
            # =================================================

            st.markdown("## ⚠️ Possible Risks")

            risks = [
                "Strong competition from existing products.",
                "Customers may not adopt the product quickly.",
                "Development cost may become higher than expected.",
                "Difficulty reaching the right customers.",
                "The original problem may not be serious enough for customers.",
                "The business may require continuous marketing and support."
            ]

            for i, risk in enumerate(risks, 1):

                st.markdown(
                    f"""
                    <div class="blue-box">
                        <div class="blue-title">
                            ⚠️ Risk {i}
                        </div>
                        <div style="color:white !important;">
                            {risk}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # ====================================================
        # BUILD STARTUP
        # ====================================================

        elif st.session_state.page == "build":

            st.markdown("## 📊 Startup Blueprint")

            # =================================================
            # BASIC DETAILS
            # =================================================

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "🏢 Industry",
                    industry
                )

            with c2:
                st.metric(
                    "💰 Budget",
                    f"₹{budget:,}"
                )

            with c3:
                st.metric(
                    "🎯 Target Users",
                    target if target else "Customers"
                )

            # =================================================
            # TARGET CUSTOMERS
            # =================================================

            st.markdown("## 🎯 Recommended Target Customers")

            for i, customer in enumerate(data["customers"], 1):

                st.markdown(
                    f"""
                    <div class="customer-box">
                        <div class="blue-title">
                            👥 Customer Group {i}
                        </div>
                        {customer}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # =================================================
            # REVENUE
            # =================================================

            st.markdown("## 💰 Recommended Revenue Models")

            for i, revenue in enumerate(data["revenue"], 1):

                st.markdown(
                    f"""
                    <div class="blue-box">
                        <div class="blue-title">
                            💰 Revenue Model {i}
                        </div>
                        {revenue}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # =================================================
            # ROADMAP
            # =================================================

            st.markdown("## 🚀 Development Roadmap")

            roadmap = [
                ("Step 1", "Research the problem and understand the target users."),
                ("Step 2", "Talk to potential customers and collect requirements."),
                ("Step 3", "Create a simple MVP with the most important features."),
                ("Step 4", "Test the MVP with real users."),
                ("Step 5", "Improve the product using user feedback."),
                ("Step 6", "Launch the product and start marketing.")
            ]

            for step, description in roadmap:

                st.markdown(
                    f"""
                    <div class="roadmap-box">
                        <div class="blue-title">
                            🚀 {step}
                        </div>
                        {description}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # =================================================
            # MARKETING
            # =================================================

            st.markdown("## 📢 Marketing Recommendations")

            marketing = [
                "Create an Instagram and social media page for the startup.",
                "Create a simple website or landing page.",
                "Offer a free trial or demo to early users.",
                "Partner with colleges, local businesses or organizations.",
                "Collect customer reviews and testimonials.",
                "Use social media content to explain the problem and solution."
            ]

            for i, item in enumerate(marketing, 1):

                st.markdown(
                    f"""
                    <div class="marketing-box">
                        <div class="blue-title">
                            📢 Marketing Strategy {i}
                        </div>
                        {item}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # =================================================
            # SKILLS
            # =================================================

            st.markdown("## 🧑‍💻 Recommended Skills")

            if skills:

                for i, skill in enumerate(skills, 1):

                    st.markdown(
                        f"""
                        <div class="blue-box">
                            <div class="blue-title">
                                🧑‍💻 Skill {i}
                            </div>
                            {skill}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            else:

                st.markdown(
                    """
                    <div class="blue-box">
                        <div class="blue-title">
                            🧑‍💻 Suggested Skills
                        </div>
                        Python, Web Development, AI/ML,
                        Data Science, Marketing and UI/UX Design.
                    </div>
                    """,
                    unsafe_allow_html=True
                )


    # ========================================================
    # BACK TO DASHBOARD
    # ========================================================

    st.markdown("---")

    if st.button("⬅️ Back to Dashboard"):

        st.session_state.page = "home"

        st.rerun()