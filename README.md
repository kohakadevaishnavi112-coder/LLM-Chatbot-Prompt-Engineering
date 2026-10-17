# LLM Chatbot with Prompt Engineering

A beginner-friendly mini project using Python, Streamlit, and the Gemini API.

## Features
- Q&A
- Text summarization
- Text sentiment classification (Positive / Negative / Neutral)
- Basic vs improved prompt comparison
- Manual evaluation scores saved to `evaluation_results.csv`
- Small custom FAQ dataset in `faq_dataset.csv`

> The FAQ CSV is sample project data; this version does not automatically retrieve answers from it or train the model.

## 1. Requirements
- Python 3.10 or newer recommended
- Internet connection
- Google AI Studio API key

Create an API key at https://aistudio.google.com/ . Never share the key or commit it to GitHub.

## 2. Open the project in VS Code
1. Extract the ZIP file.
2. Open VS Code.
3. Select **File → Open Folder**.
4. Choose the extracted `LLM_Chatbot_Project` folder.
5. Open **Terminal → New Terminal**.

## 3. Create and activate virtual environment (Windows)
Run these commands one at a time in the VS Code terminal:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, try this in the same terminal:
```powershell
venv\Scripts\activate.bat
```
If the terminal still has trouble, use Command Prompt as the VS Code terminal or run `venv\Scripts\python.exe -m pip install -r requirements.txt` and `venv\Scripts\python.exe -m streamlit run app.py`.

## 4. Install packages
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Add your API key
1. In VS Code Explorer, copy `.env.example` and rename the copy to `.env`.
2. Open `.env`.
3. Replace `PASTE_YOUR_API_KEY_HERE` with your actual API key.
4. Save the file.
5. Do not upload `.env` to GitHub.

The default model is `gemini-2.5-flash`. If AI Studio shows a different available model, set `GEMINI_MODEL` in `.env` to that exact model ID. Model availability can change by account/region.

## 6. Run the project
In the VS Code terminal:
```powershell
python -m streamlit run app.py
```
A browser tab should open. If not, open the Local URL printed in the terminal (usually http://localhost:8501).

## 7. Test the features
- Q&A: `Explain machine learning in simple English.`
- Summarization: paste a paragraph and choose Text Summarization.
- Classification: `I loved this product. It works perfectly!`
- Run the same input once with Basic prompt and once with Improved prompt, then enter your manual scores in the evaluation section.

## 8. Upload to GitHub safely
1. Create a new empty repository on GitHub.
2. In VS Code terminal, run:
```powershell
git init
git add .
git commit -m "Initial LLM chatbot project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
Replace `YOUR_GITHUB_REPOSITORY_URL` with the repository URL copied from GitHub. Ensure `.env` is not included.

## 9. Deploy online (optional)
- Push the code to GitHub.
- Open https://share.streamlit.io/ and deploy `app.py`.
- In Streamlit Cloud app settings, add secrets:
```toml
GEMINI_API_KEY = "YOUR_REAL_API_KEY"
GEMINI_MODEL = "gemini-2.5-flash"
```
For cloud deployment, the app reads environment variables. Streamlit Cloud exposes secrets as environment variables for this app. If your deployment setup doesn't, update `app.py` to read `st.secrets` as a fallback.
- Keep your API key secret. Never add it to the repository.

## Common errors
- `ModuleNotFoundError`: activate the environment and run `pip install -r requirements.txt`.
- API key error: check `.env` spelling and that the key is valid.
- Model not found / unavailable: update `GEMINI_MODEL` in `.env` to an exact model ID available in your AI Studio/API account.
- Quota error: check API usage and limits in Google AI Studio.
