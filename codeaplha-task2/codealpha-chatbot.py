import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Page Configuration ---
st.set_page_config(page_title="CodeAlpha FAQ Chatbot", page_icon="🤖")

# --- Load Data ---
@st.cache_data
def load_data():
    
    file_path = "faq.csv" 
    df = pd.read_csv(file_path)
    # Convert to strings to avoid errors during vectorization
    df['Question'] = df['Question'].astype(str)
    df['Answer'] = df['Answer'].astype(str)
    return df

try:
    df = load_data()
    questions = df['Question'].tolist()
    answers = df['Answer'].tolist()

    # --- NLP Setup (Task 2 Requirements) ---
    # Using TfidfVectorizer for text preprocessing and vectorization [cite: 29]
    vectorizer = TfidfVectorizer(stop_words='english')
    faq_vectors = vectorizer.fit_transform(questions)

    # --- UI Layout ---
    st.title("🤖 AI FAQ Chatbot")
    st.markdown("Welcome! Ask me anything about our services.")
    st.divider()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if user_input := st.chat_input("Type your question here..."):
        # Display user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Process matching using Cosine Similarity [cite: 30]
        query_vector = vectorizer.transform([user_input.lower()])
        similarities = cosine_similarity(query_vector, faq_vectors)
        
        best_match_idx = similarities.argmax()
        confidence = similarities[0][best_match_idx]

        # Determine response [cite: 31]
        if confidence > 0.2:  # Threshold for matching
            response = answers[best_match_idx]
        else:
            response = "I'm sorry, I couldn't find a specific answer to that. Please reach out to services@codealpha.tech for more help."

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

except FileNotFoundError:
    st.error("Error: 'faq.csv' not found. Please ensure the file is in the project folder.")
except Exception as e:
    st.error(f"An error occurred: {e}")