# Medical Document Analyzer 📄

## Description

The Medical Document Analyzer is a Streamlit-powered web application that uses Google's Gemini AI model to analyze medical documents. Users can upload an image of a medical document (e.g., prescriptions, test reports) and receive a structured summary of its key contents. The app also supports user input for custom queries about the uploaded document.

## Features 🚀

- Medical Document Analysis: Identifies document type and extracts relevant information.

- **Custom Queries:** Allows users to ask specific questions about the uploaded document.

- **Image Upload:** Supports JPG, JPEG, and PNG formats.

- **Real-time AI Response:** Uses Google Gemini 1.5 Pro for content generation.

- **User-friendly Interface:** Built with Streamlit for simplicity and ease of use.

- **Disclaimer:** Highlights that the tool is for informational purposes only, not medical advice.

## Tech Stack 💻

- Python 3.7+

- Streamlit

- Google Generative AI (Gemini)

- Pillow (PIL)

- Python-dotenv

## How It Works ⚙️

- **Upload:** Users upload a medical document image.

- **Input Prompt:** Optionally, users can enter a question or instruction.

- **Analysis:** On clicking "Analyze this Document", the app processes the image and prompt using Gemini AI.

- **Output:** Displays a structured analysis with sections like Document Type, Key Findings, Diagnosis, and Treatment Plan.

## Installation 🛠️

1. Clone the repository:
```
git clone https://github.com/yourusername/Medical-Document-Analyzer.git
```
2. Navigate to the project directory:
```
cd Medical-Document-Analyzer
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. **Set up environment variables:** Create a ```.env``` file and add your Google API key:
```
GOOGLE_API_KEY=your_google_api_key
```
5. Run the app:
```
streamlit run app.py
```
## Usage 🏥

- **Step 1:** Open the app in your browser.

- **Step 2:** Upload an image of a medical document.

- **Step 3:** Optionally, enter a custom prompt (e.g., "What is the diagnosis?").

- **Step 4:** Click "Analyze this Document" to view AI-generated insights.

## Disclaimer ⚠️

The Medical Document Analyzer is intended for informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.

## Contributing 🤝

Contributions are welcome! If you'd like to improve the project, feel free to open an issue or submit a pull request.

## Contact 📧

For questions or feedback, please reach out via GitHub or email.