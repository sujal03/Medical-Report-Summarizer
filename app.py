import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Function to get response from the model
def get_gemini_response(user_input, image):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    if not user_input:
        # Default prompt for medical document analysis
        user_input = (
            "Identify the type of medical document shown in the image and provide a summary of its key contents. "
            "Please format your response with the following sections:\n"
            "- Document Type\n"
            "- Key Findings\n"
            "- Diagnosis (if applicable)\n"
            "- Treatment Plan (if applicable)\n"
            "- Other Relevant Information"
        )
    response = model.generate_content([user_input, image])
    return response.text

# Streamlit app configuration
st.set_page_config(page_title="Medical Document Analyzer")
st.header("💡 Medical Document Analyzer 📄")

# Sidebar with instructions and disclaimer
st.sidebar.title("About")
st.sidebar.info(
    "### How to Use\n"
    "1. Upload an image of a medical document (jpg, jpeg, png).\n"
    "2. Optionally, enter a specific question or instruction in the text box.\n"
    "3. Click 'Analyze this Document' to get the analysis."
)
st.sidebar.warning(
    "⚠️ **Disclaimer**: This tool is for informational purposes only and should not be used as a substitute for professional medical advice."
)

# Main application
user_input = st.text_input(
    "Input Prompt:",
    placeholder="Enter your question or instruction (e.g., 'Summarize the key findings')",
    key="user_input"
)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
else:
    image = None

# Analyze button
submit = st.button("Analyze this Document")

# Process submission
if submit:
    if image is None:
        st.warning("Please upload an image first.")
    else:
        with st.spinner("Analyzing the document..."):
            try:
                response = get_gemini_response(user_input, image)
                st.subheader("Analysis Result")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
