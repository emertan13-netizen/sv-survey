import streamlit as st
import csv
import os
from datetime import datetime

st.set_page_config(
    page_title="SupervisAI — User Research Survey",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .question-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 2rem 2.5rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        margin: 1.5rem 0;
    }
    .question-text {
        font-size: 1.25rem;
        font-weight: 600;
        color: #0A1628;
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }
    .question-note {
        font-size: 0.85rem;
        color: #888;
        font-style: italic;
        margin-bottom: 1rem;
        margin-top: -0.75rem;
    }
    .title-block {
        background: transparent;
        border-bottom: 3px solid #028090;
        padding: 1.5rem 0 1rem 0;
        margin-bottom: 1.5rem;
    }
    .title-block h1 { color: #028090; font-size: 2.2rem; font-weight: 700; margin: 0 0 0.25rem 0; }
    .title-block p { color: #555555; font-size: 0.95rem; margin: 0; }
    .title-block .meta { color: #888888; font-size: 0.82rem; margin-top: 0.5rem; }
    .hypothesis-box {
        background: #E8F4F7;
        border-left: 5px solid #028090;
        border-radius: 6px;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
    }
    .hypothesis-box h4 { color: #028090; margin: 0 0 0.5rem 0; font-size: 0.9rem; }
    .hypothesis-box p { color: #333; margin: 0.2rem 0; font-size: 0.875rem; }
    .success-box {
        background: linear-gradient(135deg, #E8F4F7, #EDFAF3);
        border: 2px solid #2DBFB8;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
    }
    .success-box h2 { color: #028090; }
    .success-box p { color: #555; }
    .footer-note {
        border-top: 2px solid #028090;
        padding: 0.75rem 1rem;
        font-size: 0.78rem;
        color: #777;
        margin-top: 2rem;
        font-style: italic;
    }
    .stButton > button {
        background: linear-gradient(135deg, #028090, #2DBFB8);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        width: 100%;
        margin-top: 0.5rem;
    }
    .stButton > button:hover { background: linear-gradient(135deg, #025F6B, #028090); }
</style>
""", unsafe_allow_html=True)

RESPONSES_FILE = "responses.csv"

def save_response(data):
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile(RESPONSES_FILE)
    with open(RESPONSES_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step = max(0, st.session_state.step - 1)

st.markdown("""
<div class="title-block">
    <h1>SupervisAI</h1>
    <p>User Research Survey — AI-Powered Clinical Supervision Support for DClinPsy Trainees</p>
    <p class="meta">Anonymous · 5–7 minutes</p>
</div>
""", unsafe_allow_html=True)

if st.session_state.submitted:
    st.markdown("""
    <div class="success-box">
        <h2>Thank you for your response!</h2>
        <p>Your input will directly shape the development of SupervisAI.<br>
        We really appreciate you taking the time.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

if st.session_state.step == 0:
    st.markdown("Thank you for taking part. Your responses are **anonymous** and will be used solely to inform an independent research project on AI-supported clinical supervision. There are no right or wrong answers — please respond based on your genuine experience.")
    st.markdown("""
    <div class="hypothesis-box">
        <h4>This survey is designed to test three hypotheses:</h4>
        <p>1. Supervisor time on direct clinical session support is a primary barrier to services taking on more DClinPsy trainees</p>
        <p>2. Trainees currently lack adequate structured reflection between supervision sessions</p>
        <p>3. Clinicians would be open to adopting an AI tool that addressed these gaps, provided their key concerns were met</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Start Survey", on_click=next_step)
    st.stop()

role = st.session_state.answers.get("role", None)

def get_questions(role):
    qs = ["q1_role", "q2_digital"]
    if role == "DClinPsy supervisor":
        qs += ["q3_hours", "q4_capacity", "q5_sup_reflection", "q6_sup_intersession"]
    elif role == "DClinPsy trainee":
        qs += ["q5_tra_reflection", "q6_tra_intersession", "q7_workarounds"]
    qs += ["q8_existing", "q9_attitude", "q10_usefulness", "q11_workflow",
           "q12_adoption", "q13_success", "q14_channels", "q15_concerns", "q15b_open"]
    return qs

questions = get_questions(role)
current_q_index = st.session_state.step - 1
total_qs = len(get_questions("DClinPsy supervisor"))
progress = min(current_q_index / total_qs, 1.0) if total_qs > 0 else 0
st.progress(progress)
st.caption(f"{int(progress * 100)}% complete")

if current_q_index < len(questions):
    q = questions[current_q_index]

    if q == "q1_role":
        st.markdown('<div class="question-card"><div class="question-text">What is your current role?</div>', unsafe_allow_html=True)
        ans = st.radio("", ["— Please select —", "DClinPsy supervisor", "DClinPsy trainee", "Other"], key="q1", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col2:
            if st.button("Next", key="n1"):
                if ans != "— Please select —":
                    st.session_state.answers["role"] = ans
                    next_step(); st.rerun()
                else:
                    st.warning("Please select an option.")

    elif q == "q2_digital":
        st.markdown('<div class="question-card"><div class="question-text">Have you ever used a digital tool to support clinical training or supervision?</div>', unsafe_allow_html=True)
        ans = st.radio("", ["Yes, regularly", "Yes, occasionally", "No, but open to it", "No, not interested"], key="q2", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b2")
        with col2:
            if st.button("Next", key="n2"):
                st.session_state.answers["digital_experience"] = ans; next_step(); st.rerun()

    elif q == "q3_hours":
        st.markdown('<div class="question-card"><div class="question-text">Approximately how many hours per week do you spend on direct supervision of trainee clinical sessions?</div><div class="question-note">e.g. sitting in, co-facilitating, observing, post-session debrief</div>', unsafe_allow_html=True)
        ans = st.radio("", ["Less than 1 hour", "1–2 hours", "3–5 hours", "More than 5 hours", "Not applicable"], key="q3", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b3")
        with col2:
            if st.button("Next", key="n3"):
                st.session_state.answers["sup_hours"] = ans; next_step(); st.rerun()

    elif q == "q4_capacity":
        st.markdown('<div class="question-card"><div class="question-text">Has supervision capacity ever been a factor in limiting the number of trainees your service could accommodate?</div>', unsafe_allow_html=True)
        ans = st.radio("", ["Yes, definitely", "Yes, to some extent", "Not sure", "No", "Not applicable"], key="q4", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b4")
        with col2:
            if st.button("Next", key="n4"):
                st.session_state.answers["sup_capacity"] = ans; next_step(); st.rerun()

    elif q == "q5_sup_reflection":
        st.markdown('<div class="question-card"><div class="question-text">How would you describe the quality of post-session reflection currently available to trainees in your service?</div>', unsafe_allow_html=True)
        ans = st.radio("", ["Very good", "Good", "Adequate", "Poor", "Very poor", "Not sure"], key="q5s", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b5s")
        with col2:
            if st.button("Next", key="n5s"):
                st.session_state.answers["sup_reflection"] = ans; next_step(); st.rerun()

    elif q == "q6_sup_intersession":
        st.markdown('<div class="question-card"><div class="question-text">How often do trainees in your service seek guidance or support between formal supervision sessions?</div>', unsafe_allow_html=True)
        ans = st.radio("", ["Very often", "Often", "Sometimes", "Rarely", "Never", "Not sure"], key="q6s", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b6s")
        with col2:
            if st.button("Next", key="n6s"):
                st.session_state.answers["sup_intersession"] = ans; next_step(); st.rerun()

    elif q == "q5_tra_reflection":
        st.markdown('<div class="question-card"><div class="question-text">How would you describe the quality of post-session reflection currently available to you in your placement?</div>', unsafe_allow_html=True)
        ans = st.radio("", ["Very good", "Good", "Adequate", "Poor", "Very poor", "Not sure"], key="q5t", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b5t")
        with col2:
            if st.button("Next", key="n5t"):
                st.session_state.answers["tra_reflection"] = ans; next_step(); st.rerun()

    elif q == "q6_tra_intersession":
        st.markdown('<div class="question-card"><div class="question-text">How often do you seek clinical guidance or support between your formal supervision sessions?</div>', unsafe_allow_html=True)
        ans = st.radio("", ["Very often", "Often", "Sometimes", "Rarely", "Never"], key="q6t", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b6t")
        with col2:
            if st.button("Next", key="n6t"):
                st.session_state.answers["tra_intersession"] = ans; next_step(); st.rerun()

    elif q == "q7_workarounds":
        st.markdown('<div class="question-card"><div class="question-text">How do you currently reflect on sessions between supervision meetings?</div><div class="question-note">Select all that apply</div>', unsafe_allow_html=True)
        opts = ["Written notes or reflective journal", "Informal discussion with colleagues", "Self-directed reading", "No structured process", "Other"]
        selected = [o for o in opts if st.checkbox(o, key=f"q7_{o}")]
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b7")
        with col2:
            if st.button("Next", key="n7"):
                st.session_state.answers["tra_workarounds"] = "|".join(selected); next_step(); st.rerun()

    elif q == "q8_existing":
        st.markdown('<div class="question-card"><div class="question-text">Are there any existing tools or processes in your service that help address supervision workload or trainee reflection?</div>', unsafe_allow_html=True)
        ans = st.radio("", ["Yes, and they work well", "Yes, but inadequate", "No", "Not sure"], key="q8", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b8")
        with col2:
            if st.button("Next", key="n8"):
                st.session_state.answers["existing_tools"] = ans; next_step(); st.rerun()

    elif q == "q9_attitude":
        st.markdown('<div class="question-card"><div class="question-text">How do you currently feel about the use of digital tools in clinical training and supervision?</div>', unsafe_allow_html=True)
        ans = st.radio("", ["Very positive", "Positive", "Neutral", "Negative", "Very negative"], key="q9", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b9")
        with col2:
            if st.button("Next", key="n9"):
                st.session_state.answers["digital_attitude"] = ans; next_step(); st.rerun()

    elif q == "q10_usefulness":
        st.markdown('<div class="question-card"><div class="question-text">How useful would an AI tool be that guided trainees through structured reflection after sessions and tracked their competency progress between supervision meetings?</div><div class="question-note">1 = not at all useful, 5 = extremely useful</div>', unsafe_allow_html=True)
        ans = st.select_slider("", options=["1 — Not at all useful", "2", "3 — Neutral", "4", "5 — Extremely useful"], key="q10", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b10")
        with col2:
            if st.button("Next", key="n10"):
                st.session_state.answers["usefulness"] = ans; next_step(); st.rerun()

    elif q == "q11_workflow":
        st.markdown('<div class="question-card"><div class="question-text">How easily could a digital reflection tool fit into your current working routine?</div>', unsafe_allow_html=True)
        ans = st.radio("", ["Very easily", "Fairly easily", "Neutral", "With some difficulty", "Very difficult"], key="q11", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b11")
        with col2:
            if st.button("Next", key="n11"):
                st.session_state.answers["workflow_fit"] = ans; next_step(); st.rerun()

    elif q == "q12_adoption":
        st.markdown('<div class="question-card"><div class="question-text">If a tool like this existed, would you use or recommend it?</div>', unsafe_allow_html=True)
        ans = st.radio("", ["Definitely yes", "Probably yes", "Not sure", "Probably not", "Definitely not"], key="q12", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b12")
        with col2:
            if st.button("Next", key="n12"):
                st.session_state.answers["adoption"] = ans; next_step(); st.rerun()

    elif q == "q13_success":
        st.markdown('<div class="question-card"><div class="question-text">What would make you consider a digital supervision support tool successful in your service?</div><div class="question-note">Select all that apply</div>', unsafe_allow_html=True)
        opts = [
            "Reduction in hours supervisors spend on direct session support",
            "More time for supervisors to focus on other clinical responsibilities",
            "Improved supervisor wellbeing and reduced burnout",
            "Increased trainee confidence and independence between sessions",
            "More structured and consistent reflection process for trainees",
            "Ability to accommodate more trainees in the service",
            "Better competency tracking and progression visibility",
            "Reduced waiting times for clients accessing the service",
            "Other"
        ]
        selected = [o for o in opts if st.checkbox(o, key=f"q13_{o}")]
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b13")
        with col2:
            if st.button("Next", key="n13"):
                st.session_state.answers["success_metrics"] = "|".join(selected); next_step(); st.rerun()

    elif q == "q14_channels":
        st.markdown('<div class="question-card"><div class="question-text">How would you most likely hear about and adopt a new digital tool for clinical supervision?</div><div class="question-note">Select all that apply</div>', unsafe_allow_html=True)
        opts = [
            "Recommendation from a colleague",
            "NHS England or trust-level rollout",
            "BPS or HCPC endorsement",
            "DClinPsy programme director recommendation",
            "Social media or professional networks",
            "Other"
        ]
        selected = [o for o in opts if st.checkbox(o, key=f"q14_{o}")]
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b14")
        with col2:
            if st.button("Next", key="n14"):
                st.session_state.answers["channels"] = "|".join(selected); next_step(); st.rerun()

    elif q == "q15_concerns":
        st.markdown('<div class="question-card"><div class="question-text">What would be your biggest concern about using an AI tool to support clinical supervision?</div><div class="question-note">Select all that apply</div>', unsafe_allow_html=True)
        opts = [
            "Data privacy and confidentiality",
            "Accuracy and reliability of the tool",
            "Risk of replacing human clinical judgement",
            "Impact on the trainee-supervisor relationship",
            "Increased workload for supervisors or trainees",
            "Lack of NHS data security compliance",
            "No concerns",
            "Other"
        ]
        selected = [o for o in opts if st.checkbox(o, key=f"q15_{o}")]
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b15")
        with col2:
            if st.button("Next", key="n15"):
                st.session_state.answers["concerns"] = "|".join(selected); next_step(); st.rerun()

    elif q == "q15b_open":
        st.markdown('<div class="question-card"><div class="question-text">Is there anything else you would like to share about your experience of clinical supervision or training?</div><div class="question-note">Optional</div>', unsafe_allow_html=True)
        ans = st.text_area("", placeholder="Your response here...", height=150, key="q15b", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: st.button("Back", on_click=prev_step, key="b15b")
        with col2:
            if st.button("Submit Survey", key="submit"):
                st.session_state.answers["open_feedback"] = ans
                save_response(st.session_state.answers)
                st.session_state.submitted = True
                st.rerun()

st.markdown("""
<div class="footer-note">
This survey is anonymous. Data will be used solely for an independent research project
and will not be shared with third parties. Your participation is voluntary and you may
withdraw at any time.
</div>
""", unsafe_allow_html=True)