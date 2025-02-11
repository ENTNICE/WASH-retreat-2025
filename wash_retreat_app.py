import streamlit as st
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Page setup
st.set_page_config(page_title="WASH Retreat Game", layout="centered")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Live Polling & Word Cloud", "WASH Quiz Game"])

# Function for Polling & Word Cloud
def polling_wordcloud():
    st.title("Live Polling & Word Cloud")
    st.write("Enter words that describe the key challenges in WASH programming.")
    
    if 'words' not in st.session_state:
        st.session_state.words = []
    
    new_word = st.text_input("Enter a word:")
    if st.button("Submit"):
        if new_word:
            st.session_state.words.append(new_word)
    
    if st.session_state.words:
        st.write("### Word Cloud Preview")
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(st.session_state.words))
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)
    
# Function for WASH Quiz Game
def wash_quiz():
    st.title("WASH Quiz Game")
    st.write("Test your knowledge about WASH programming!")
    
    questions = [
        {"question": "What is the most effective method to ensure clean drinking water?", "options": ["Boiling", "Filtering", "Chlorination", "All of the above"], "answer": "All of the above"},
        {"question": "Which SDG focuses on Clean Water and Sanitation?", "options": ["SDG 4", "SDG 6", "SDG 8", "SDG 10"], "answer": "SDG 6"},
        {"question": "What is the main cause of waterborne diseases?", "options": ["Air pollution", "Contaminated water", "Lack of exercise", "Deforestation"], "answer": "Contaminated water"}
    ]
    
    score = 0
    for i, q in enumerate(questions):
        st.write(f"**{i+1}. {q['question']}**")
        choice = st.radio("Select your answer:", q["options"], key=i)
        if st.button(f"Submit Answer {i+1}", key=f"btn{i}"):
            if choice == q["answer"]:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Incorrect! The correct answer is: {q['answer']}")
    
    if st.button("Show Score"):
        st.write(f"Your final score: **{score}/{len(questions)}**")

# Page routing
if page == "Live Polling & Word Cloud":
    polling_wordcloud()
elif page == "WASH Quiz Game":
    wash_quiz()
