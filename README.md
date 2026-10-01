# Flash-Card-Generator
🧠 AI Flashcard Generator — Hugging Face
A simple GenAI mini-project that converts study notes or a topic into structured flashcards using a Hugging Face-hosted LLM.

Features
Generate 3–15 flashcards
Easy / Medium / Hard difficulty
Uses Hugging Face Inference API
Structured JSON output
Streamlit user interface
Suitable as a GenAI mini-project
1. Install Python
Use Python 3.10+.

2. Install dependencies
pip install -r requirements.txt
3. Create a Hugging Face token
Create an access token from your Hugging Face account and give it the permissions required for inference.

Then set the environment variable.

Windows PowerShell
$env:HF_TOKEN="hf_your_token_here"
$env:HF_MODEL="meta-llama/Llama-3.1-8B-Instruct"
macOS / Linux
export HF_TOKEN="hf_your_token_here"
export HF_MODEL="meta-llama/Llama-3.1-8B-Instruct"
Do not put your real token inside GitHub or share it publicly.

4. Run
streamlit run app.py
Then open the local Streamlit address shown in the terminal.

Project structure
flashcard_generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
└── app/
    ├── __init__.py
    └── generator.py
How it works
User notes/topic
      ↓
Streamlit UI
      ↓
Prompt engineering
      ↓
Hugging Face Inference API
      ↓
LLM generates JSON
      ↓
JSON parser
      ↓
Interactive flashcards
Possible upgrades
PDF upload using PyMuPDF
MCQ mode
Spaced-repetition revision
Flashcard database with SQLite
User accounts
Export to CSV/PDF
Automatic topic detection
Difficulty adaptation based on answers
