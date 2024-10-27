import streamlit as st
from main import invoke_main_pipeline
from fuzzywuzzy import fuzz


if 'item' not in st.session_state:
    st.session_state.item = ""
    
if 'category' not in st.session_state:
    st.session_state.category = ""
    
if 'question' not in st.session_state:
    st.session_state.question = ""

if 'options' not in st.session_state:
    st.session_state.options = ""

if 'hint' not in st.session_state:
    st.session_state.hint = False


        

# Add some space at the top to prevent overlap
st.markdown("<br><br><br>", unsafe_allow_html=True)

# 1. Central button to fetch and display text from backend
st.markdown("<h2 style='text-align: center;'>LLM Quizzer!</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("Generate Question!"):
        st.session_state.category, st.session_state.item, st.session_state.question, st.session_state.options = invoke_main_pipeline()
        st.session_state.hint = False
        st.session_state.user_input = ""
        
    if st.session_state.question:
        st.success(st.session_state.question)
        st.success(st.session_state.category)

    
    
# Add more space between sections
st.markdown("<br><br>", unsafe_allow_html=True)

# 2. Input field and button to check user text with backend text
# st.markdown("<h2 style='text-align: center;'>Text Checker</h2>", unsafe_allow_html=True)

user_input = st.text_input("Enter your answer here:", value=st.session_state.get('user_input', ''),disabled=st.session_state.hint)
st.session_state.user_input = user_input

if st.button('Show hints!'):
    st.session_state.hint = True
    
if st.session_state.hint:
    if st.session_state.question:
            st.session_state.user_input = st.radio(
                "Choose your answer:",
                st.session_state.options
            )


if st.button("Check Answer"):
    fuzzy_score = fuzz.ratio(st.session_state.user_input, st.session_state.item)
    if fuzzy_score > 75:
        st.success("Correct Answer")
    else:
        st.error("Incorrect")
        st.success(f"Correct answer : {st.session_state.item}")
        
if st.button("See Answer"):
    st.success(st.session_state.item)
