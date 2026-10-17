import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from google import genai
from prompts import get_prompt

load_dotenv()

st.set_page_config(page_title="LLM Chatbot with Prompt Engineering", page_icon="🤖", layout="centered")
st.title("🤖 LLM Chatbot with Prompt Engineering")
st.caption("Q&A • Text Summarization • Text Classification")

api_key = os.getenv("GEMINI_API_KEY", "").strip()

with st.sidebar:
    st.header("Project details")
    st.write("This mini project demonstrates prompt engineering with an LLM API.")
    st.write("Tasks: Q&A, summarization, classification")
    st.write("Evaluation: compare basic and improved prompts.")
    st.divider()
    st.caption("Keep your API key private. Never upload it to GitHub.")

if not api_key:
    st.warning("API key not found. Create a .env file and add GEMINI_API_KEY=your_key_here. See README.md.")
    st.stop()

# Use a model name supported by your Google AI Studio/API account.
# If this model is unavailable, change GEMINI_MODEL in .env to a model shown in AI Studio.
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()
client = genai.Client(api_key=api_key)

task = st.selectbox("Choose task", ["Q&A", "Text Summarization", "Text Classification"])
prompt_style = st.radio("Prompt type", ["Improved prompt", "Basic prompt"], horizontal=True)
user_text = st.text_area(
    "Enter your question or text",
    height=180,
    placeholder="Example: Explain machine learning in simple English."
)

def call_model(prompt: str) -> str:
    response = client.models.generate_content(model=model, contents=prompt)
    return response.text or "The model returned an empty response."

if st.button("Generate response", type="primary"):
    if not user_text.strip():
        st.error("Please enter a question or some text first.")
    else:
        prompt = get_prompt(task, user_text.strip(), improved=(prompt_style == "Improved prompt"))
        with st.spinner("Generating response..."):
            try:
                answer = call_model(prompt)
                st.subheader("Response")
                st.write(answer)
                st.session_state["last_result"] = {
                    "task": task,
                    "prompt_type": prompt_style,
                    "input": user_text.strip(),
                    "response": answer
                }
            except Exception as exc:
                st.error("Could not generate a response.")
                st.write("Check your internet connection, API key, model name, and API quota.")
                st.code(str(exc))

st.divider()
st.subheader("Prompt comparison / simple evaluation")
st.write("Enter the same text and run once with Basic prompt and once with Improved prompt. Compare relevance, clarity, correctness, and completeness from 1 (low) to 5 (high).")

with st.form("evaluation_form"):
    eval_task = st.selectbox("Task for evaluation", ["Q&A", "Text Summarization", "Text Classification"], key="eval_task")
    eval_input = st.text_input("Test input", value="Explain machine learning in simple English.")
    basic_score = st.slider("Basic prompt score (1–5)", 1, 5, 3)
    improved_score = st.slider("Improved prompt score (1–5)", 1, 5, 4)
    notes = st.text_input("Notes (optional)", placeholder="e.g. Improved answer was clearer and better structured.")
    submitted = st.form_submit_button("Save evaluation row")
    if submitted:
        row = {
            "task": eval_task,
            "test_input": eval_input,
            "basic_prompt_score": basic_score,
            "improved_prompt_score": improved_score,
            "notes": notes
        }
        path = "evaluation_results.csv"
        df = pd.DataFrame([row])
        if os.path.exists(path):
            df.to_csv(path, mode="a", header=False, index=False)
        else:
            df.to_csv(path, index=False)
        st.success(f"Evaluation saved to {path}")

if os.path.exists("evaluation_results.csv"):
    st.subheader("Saved evaluation results")
    st.dataframe(pd.read_csv("evaluation_results.csv"), use_container_width=True)
