import streamlit as st
import google.generativeai as genai

def generate_story_ai(noun, adjective, verb):
    prompt = f"""
    Create a short and concise one-sentence story using the following words:
    - Noun: {noun}
    - Adjective: {adjective}
    - Verb: {verb}
    Ensure the sentence is meaningful and directly incorporates the provided words without unnecessary details.
    """
    
    genai.configure(api_key="AIzaSyBa5WZHnfs5OZ4_roPGR6jcMM5N9waVqH8")
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    
    return response.text if response else "Sorry, I couldn't generate a story."

def generate_story_logic(noun, adjective, verb):
    return f"One fine morning, a {adjective} {noun} decided to {verb} through the bustling city, marveling at the sights and sounds of the world coming to life."  

# Streamlit UI
st.set_page_config(page_title="Mad Libs Story Generator", page_icon="📝", layout="centered")
st.markdown("""
    <style>
        .main {background-color: #f5f5f5;}
        h1 {color: #4CAF50; text-align: center;}
        .stButton>button {background-color: #4CAF50; color: white; font-size: 18px; padding: 10px; border-radius: 8px;}
        .stButton>button:hover {background-color: #45a049;}
        .stRadio div {display: flex; justify-content: center;}
        .stTextInput>div>div>input {border-radius: 5px; border: 1px solid #4CAF50;}
    </style>
""", unsafe_allow_html=True)

st.title("📝 Mad Libs Story Generator with AI & Logic")
st.write("### Choose AI-generated or predefined logic-based story generation!")

# Input Fields with Columns
col1, col2, col3 = st.columns(3)
noun = col1.text_input("Enter a noun", placeholder="e.g., cat")
adjective = col2.text_input("Enter an adjective", placeholder="e.g., fluffy")
verb = col3.text_input("Enter a verb", placeholder="e.g., jumps")

# Story Type Selection
story_type = st.radio("Select story type:", ["AI-generated", "Logic-based"], horizontal=True)

# Button and Output
if st.button("✨ Generate Story"):
    if noun and adjective and verb:
        noun, adjective, verb = noun.strip(), adjective.strip(), verb.strip()
        
        if any(" " in word or "," in word for word in [noun, adjective, verb]):
            st.error("🚨 Please enter only one word per field without spaces or commas!")
        else:
            if story_type == "AI-generated":
                story = generate_story_ai(noun, adjective, verb)
            else:
                story = generate_story_logic(noun, adjective, verb)
            
            st.success("🎉 Your Generated Story:")
            st.markdown(f"<div style='padding: 15px; background-color: #e8f5e9; border-radius: 8px; font-size: 18px;'> {story} </div>", unsafe_allow_html=True)
    else:
        st.error("🚨 Please enter all required words!")
