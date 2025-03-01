import streamlit as st
import google.generativeai as genai

# Function to generate AI-based story
def generate_story_ai(noun, adjective, verb):
    prompt = f"""
    Create a short and concise one-sentence story using the following words:
    - Noun: {noun}
    - Adjective: {adjective}
    - Verb: {verb}
    Ensure the sentence is meaningful and directly incorporates the provided words.
    """
    
    genai.configure(api_key="AIzaSyBa5WZHnfs5OZ4_roPGR6jcMM5N9waVqH8")
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    
    return response.text if response else "Sorry, I couldn't generate a story."

# Logic-based story generation
def generate_story_logic(noun, adjective, verb):
    return f"One fine morning, a {adjective} {noun} decided to {verb} through the bustling city, marveling at the sights and sounds."

# Streamlit UI Design
st.set_page_config(page_title="Mad Libs Story Generator", page_icon="📝", layout="centered")

st.markdown("""
    <style>
        .main {background-color: #ECEFF1;}
        h1 {color: #37474F; text-align: center; font-weight: bold;}
        .stTextInput>div>div>input {border: 2px solid #546E7A; border-radius: 8px; padding: 8px; font-size: 16px;}
        .stButton>button {background-color: #546E7A; color: white; font-size: 18px; padding: 10px 20px; border-radius: 8px;}
        .stButton>button:hover {background-color: #455A64;}
        .story-box {padding: 15px; background-color: #B0BEC5; color: black; border-radius: 10px; font-size: 18px;}
    </style>
""", unsafe_allow_html=True)

st.title("📝 Mad Libs Story Generator")
st.write("### Choose AI-generated or logic-based story generation!")

# Input Fields
col1, col2, col3 = st.columns(3)
noun = col1.text_input("Enter a noun", placeholder="e.g., cat")
adjective = col2.text_input("Enter an adjective", placeholder="e.g., fluffy")
verb = col3.text_input("Enter a verb", placeholder="e.g., jumps")

# Story Type Selection
story_type = st.radio("Select story type:", ["AI-generated", "Logic-based"], horizontal=True)

# Button & Story Output
if st.button("✨ Generate Story"):
    if noun and adjective and verb:
        noun, adjective, verb = noun.strip(), adjective.strip(), verb.strip()
        
        if any(" " in word or "," in word for word in [noun, adjective, verb]):
            st.error("🚨 Please enter only one word per field without spaces or commas!")
        else:
            story = generate_story_ai(noun, adjective, verb) if story_type == "AI-generated" else generate_story_logic(noun, adjective, verb)
            
            st.success("🎉 Your Generated Story:")
            st.markdown(f"<div class='story-box'>{story}</div>", unsafe_allow_html=True)
    else:
        st.error("🚨 Please enter all required words!")
