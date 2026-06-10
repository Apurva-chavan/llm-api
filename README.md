# Free LLM API Setup — Groq

## What is this?
Free LLM API using Groq for AutoJob project.
Used for resume tailoring, form filling questions
and HR outreach emails.

## Models Tested
| Model | Best For |
|---|---|
| llama-3.3-70b-versatile | Resume tailoring, HR emails |
| llama-3.1-8b-instant | Fast form filling questions |

## Setup Steps

### Step 1 — Install dependencies
pip install -r requirements.txt

### Step 2 — Get free Groq API key
1. Go to console.groq.com
2. Sign up with Google
3. Click API Keys → Create Key
4. Copy the key (starts with gsk_...)

### Step 3 — Create .env file
Copy .env.example to .env
Add your Groq API key:
GROQ_API_KEY=your_gsk_key_here

### Step 4 — Test it
python test_llm.py

Expected output:
"Conducted A/B hypothesis testing to identify 
key drivers of business outcomes..."

## How teammates can use it
from llm_config import ask_llm
result = ask_llm("Your prompt here")
print(result)

## Free Tier Limits
- 14,400 requests/day
- 30 requests/minute
- Completely free

