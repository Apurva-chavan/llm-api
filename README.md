# Free LLM API Setup — Groq
AutoJob Project 

## What is this?
Free LLM API using Groq for AutoJob project.
Used for resume tailoring, form filling questions
and HR outreach emails.

## Models Tested
| Model | Best For |
|---|---|
| llama-3.3-70b-versatile | Resume tailoring, HR emails |
| llama-3.1-8b-instant | Fast form filling questions |

## How to Check it is Working

### Step 1 — Clone the repo
git clone https://github.com/Apurva-chavan/llm-api.git
cd llm-api

### Step 2 — Install libraries
pip install -r requirements.txt

### Step 3 — Get your own free Groq API key
1. Go to console.groq.com
2. Sign up with Google
3. Click API Keys → Create Key
4. Copy the key starting with gsk_...

### Step 4 — Create .env file
copy .env.example .env
Then open .env and replace your_groq_api_key_here with your real key

### Step 5 — Run test file
python test_llm.py

### Expected Output
Conducted A/B hypothesis testing to identify
key drivers of business outcomes, quantifying
a monthly savings of INR 2.07L...

If you see output like this — API is working!

## How to Use in Your Module
from llm_config import ask_llm
result = ask_llm("Your prompt here")
print(result)

## Free Tier Limits
- 14,400 requests/day
- 30 requests/minute
- Completely free

## Troubleshooting
If you get error check:
- Is .env file created?
- Is real Groq key added in .env?
- Is pip install -r requirements.txt done?


