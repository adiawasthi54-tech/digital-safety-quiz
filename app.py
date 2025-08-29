import streamlit as st
import json

# Load questions
with open("questions.json", "r") as f:
    quiz_data = json.load(f)

st.set_page_config(page_title="Digital Safety Quiz", page_icon="🛡️")
st.title("🛡️ Digital Safety Quiz for Seniors")
st.write("Welcome! Test your knowledge and learn how to stay safe online.")

score = 0
responses = []

# Quiz loop
for i, item in enumerate(quiz_data):
    st.subheader(f"Q{i+1}: {item['question']}")
    user_answer = st.radio("Choose your answer:", item["options"], key=i)
    responses.append((item["question"], user_answer, item["answer"]))
    if user_answer == item["answer"]:
        score += 1

# Show results
if st.button("Submit Quiz"):
    st.success(f"✅ You scored {score} out of {len(quiz_data)}!")
    st.write("Here’s how you did:")
    for q, ua, ca in responses:
        st.write(f"**Q:** {q}")
        st.write(f"Your answer: {ua}")
        st.write(f"Correct answer: {ca}")
        st.markdown("---")

    if score == len(quiz_data):
        st.balloons()
        st.write("🎉 Excellent! You're a digital safety champion.")
    elif score >= len(quiz_data) // 2:
        st.write("👍 Good job! Keep learning and stay alert.")
    else:
        st.write("📘 No worries—every mistake is a chance to learn.")
