import streamlit as st
from deep_translator import GoogleTranslator

# --- Page Config ---

st.set_page_config(page_title="CodeAlpha Translator", page_icon="🌐")

st.title("🌐 AI Language Translator (Task 1)")
st.markdown("Enter text and select languages to translate using Google Translate API.")

# --- 1. Language Mapping ---
# Aap is list mein aur bhi languages add kar sakte hain
languages_dict = {
    'English': 'en',
    'Hindi': 'hi',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Arabic': 'ar',
    'Urdu': 'ur',
    'Chinese': 'zh-CN',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Russian': 'ru',
    'Portuguese': 'pt',
    'Italian': 'it',
    'Turkish': 'tr',
    'Bengali': 'bn',
    'Punjabi': 'pa',
    'Indonesian': 'id',
    'Tamil': 'ta'
}

# --- 2. User Interface (Requirement) ---
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Select Source Language", list(languages_dict.keys()), index=0)

with col2:
    target_lang = st.selectbox("Select Target Language", list(languages_dict.keys()), index=1)

# Input Box
input_text = st.text_area("Enter text to translate:", placeholder="Type here...", height=150)

# --- 3. API Processing & Output (Requirement) ---
if st.button("Translate Now"):
    if input_text.strip():
        try:
            # API Call logic
            translated_text = GoogleTranslator(
                source=languages_dict[source_lang], 
                target=languages_dict[target_lang]
            ).translate(input_text)

            # Display Result
            st.success("Translated Text:")
            st.subheader(translated_text)
            
            # Optional: Copy button feature (Streamlit builtin for code blocks)
            st.code(translated_text)

        except Exception as e:
            st.error(f"Translation Error: {e}")
    else:
        st.warning("Please enter some text to translate.")

st.divider()
st.caption("CodeAlpha Internship - AI Task 1")