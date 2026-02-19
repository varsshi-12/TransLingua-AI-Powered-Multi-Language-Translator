from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI-Powered Language Translator",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 AI-Powered Language Translator")
st.markdown("Translate text instantly using Google Gemini AI")

# ----------------------------
# Professional Styling (Only Once)
# ----------------------------
st.markdown(
    """
    <style>

    /* Background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #e4ecf7);
    }

    /* Header */
    h1 {
        text-align: center;
        font-weight: 700;
        color: #1f3b73;
    }

    /* Subtitle */
    .stMarkdown p {
        text-align: center;
        font-size: 17px;
        color: #555;
    }

    /* Text Area */
    .stTextArea textarea {
        font-size: 16px;
        border-radius: 12px;
        border: 1px solid #cfd9df;
        padding: 12px;
        background-color: #ffffff;
    }

    /* Dropdown */
    .stSelectbox > div > div {
        border-radius: 10px;
        border: 1px solid #cfd9df;
    }

    /* Button */
    .stButton>button {
        width: 100%;
        height: 3em;
        font-size: 16px;
        font-weight: bold;
        border-radius: 12px;
        background: linear-gradient(90deg, #4facfe, #00f2fe);
        color: white;
        border: none;
        transition: 0.3s ease-in-out;
    }

    .stButton>button:hover {
        transform: scale(1.03);
        background: linear-gradient(90deg, #43e97b, #38f9d7);
    }

    /* Result Card */
    .result-box {
        padding: 20px;
        border-radius: 12px;
        background-color: white;
        border: 1px solid #dce3ea;
        font-size: 18px;
        line-height: 1.6;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    /* Alerts */
    .stAlert {
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# ----------------------------
# Initialize Model (Unchanged)
# ----------------------------
model = genai.GenerativeModel("models/gemini-flash-latest")

# ----------------------------
# Translation Function
# ----------------------------
def translate_text(text, source_language, target_language):
    prompt = f"Translate the following text from {source_language} to {target_language}: {text}"
    response = model.generate_content(prompt)
    return response.text


# ----------------------------
# Main App (Improved Layout)
# ----------------------------
def main():

    with st.container():

        st.markdown("### 🌍 Language Selection")

        col1, col2 = st.columns(2)

        with col1:
            source_language = st.selectbox(
                "Source Language",
                ["English", "Spanish", "French", "German", "Chinese",
                 "Hindi", "Japanese", "Korean", "Italian",
                 "Tamil", "Telugu", "Portuguese", "Arabic",
                 "Russian", "Bengali", "Malayalam", "Urdu"]
            )

        with col2:
            target_language = st.selectbox(
                "Target Language",
                ["English", "Spanish", "French", "German", "Chinese",
                 "Hindi", "Japanese", "Korean", "Italian",
                 "Tamil", "Telugu", "Portuguese", "Arabic",
                 "Russian", "Bengali", "Malayalam", "Urdu"]
            )

        st.markdown("### 📝 Enter Text")
        text = st.text_area("Type your text below:", height=150)

        st.markdown("")

        if st.button("🚀 Translate Now"):

            if text and source_language and target_language:
                try:
                    with st.spinner("Translating..."):
                        translated_text = translate_text(
                            text, source_language, target_language
                        )

                    st.divider()

                    st.markdown("### 🗣️ Translated Output")

                    st.markdown(
                        f'<div class="result-box">{translated_text}</div>',
                        unsafe_allow_html=True
                    )

                except Exception as e:
                    st.error(f"⚠️ Error: {str(e)}")
            else:
                st.warning("⚠️ Please fill in all fields.")


# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    main()
