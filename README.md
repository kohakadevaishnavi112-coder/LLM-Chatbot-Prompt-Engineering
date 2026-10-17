# 🤖 LLM Chatbot with Prompt Engineering

A beginner-friendly Large Language Model (LLM) chatbot built using **Python, Streamlit, and the Google Gemini API**. This project demonstrates how prompt engineering can improve the quality and consistency of AI-generated responses across different text-based tasks.

## 📌 Project Overview

This project provides an interactive interface for experimenting with different prompting techniques. Users can ask questions, summarize text, classify sentiment, and compare basic prompts with improved prompts.

The project is designed as a mini project to explore LLM integration, prompt design, and response evaluation.

## ✨ Features

- **Question Answering:** Generate AI-powered answers to user questions.
- **Text Summarization:** Convert longer text into concise summaries.
- **Sentiment Classification:** Classify text as Positive, Negative, or Neutral.
- **Prompt Comparison:** Compare responses generated using basic and improved prompts.
- **Manual Evaluation:** Record evaluation scores for comparing response quality.
- **Sample FAQ Dataset:** Includes a small custom FAQ dataset in CSV format.
- **Interactive Interface:** Simple and user-friendly interface built with Streamlit.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive user interface |
| Google Gemini API | Large language model integration |
| Pandas | CSV and tabular data handling |
| CSV | Sample FAQ and evaluation data |
| python-dotenv | Environment variable configuration |

## 📂 Project Structure

```text
LLM-Chatbot-Prompt-Engineering/
│
├── app.py              # Main Streamlit application
├── prompts.py          # Prompt templates and prompt logic
├── faq_dataset.csv     # Sample FAQ dataset
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment configuration
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/kohakadevaishnavi112-coder/LLM-Chatbot-Prompt-Engineering.git
```

### 2. Open the Project Folder

```bash
cd LLM-Chatbot-Prompt-Engineering
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API Key

1. Obtain an API key through [Google AI Studio](https://aistudio.google.com/).
2. Create a file named `.env` in the project root directory.
3. Add your own API key and model configuration:

```env
GEMINI_API_KEY=your_actual_api_key_here
GEMINI_MODEL=gemini-3.5-flash-lite
```

Replace `your_actual_api_key_here` with your own key. Never publish your actual API key in GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 🧪 How to Use

1. Start the Streamlit application.
2. Select a task from the available options.
3. Enter a question or text, depending on the selected task.
4. Generate a response using the Gemini API.
5. Experiment with basic and improved prompts.
6. Review the outputs and available evaluation scores.

## 🧠 What I Learned

- Integrating an LLM API into a Python application.
- Designing prompts for different natural language processing tasks.
- Building interactive applications using Streamlit.
- Managing API keys with environment variables.
- Organizing a Python project into multiple files.
- Exploring response comparison and manual evaluation.

## 🔐 Security

- Keep `.env` out of version control.
- Never commit API keys or other secrets.
- Use `.env.example` as a template without real credentials.
- Keep your `.gitignore` configured to exclude `.env` and virtual environment folders.

## 🚀 Future Improvements

- Add automated evaluation metrics for response quality.
- Expand the FAQ dataset and implement retrieval-based answers.
- Improve error handling and API usage feedback.
- Add conversation history and additional NLP tasks.
- Compare different prompt strategies using a consistent evaluation dataset.


---

*This project was developed for learning and demonstrating LLM integration and prompt engineering concepts.*
