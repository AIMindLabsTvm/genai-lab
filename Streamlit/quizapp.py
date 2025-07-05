import streamlit as st

st.set_page_config(page_title="Quiz App", layout="centered")
st.title("🧠 Simple Quiz App")

# Define quiz questions
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "answer": "Paris"
    },
    {
        "question": "Which language is primarily used for Data Science?",
        "options": ["Java", "Python", "C++", "Ruby"],
        "answer": "Python"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Trainer Marking Language",
            "HyperText Markup Language",
            "HyperText Markdown Language",
            "None of the above"
        ],
        "answer": "HyperText Markup Language"
    },
]

# Use session state to store user answers and score
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Display questions
for i, q in enumerate(quiz):
    st.subheader(f"Q{i+1}: {q['question']}")
    st.session_state.answers[i] = st.radio(
        f"Choose an option:",
        q["options"],
        key=f"q{i}",
        label_visibility="collapsed"
    )

# Submit button
if st.button("Submit Quiz"):
    st.session_state.submitted = True

# Score and feedback
if st.session_state.submitted:
    score = 0
    for i, q in enumerate(quiz):
        user_ans = st.session_state.answers[i]
        correct = q["answer"]
        if user_ans == correct:
            score += 1
            st.success(f"✅ Q{i+1} Correct! ({user_ans})")
        else:
            st.error(f"❌ Q{i+1} Incorrect. You chose {user_ans}, correct answer is {correct}")
    
    st.markdown("---")
    st.subheader(f"🎯 Your Score: {score} / {len(quiz)}")

    # Option to retry
    if st.button("Try Again"):
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.experimental_rerun()
