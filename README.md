# AI Agent for E-commerce Data

## Overview

This project was done as part of my GenAI Internship. It uses a Gemini LLM (Google) to understand questions in English and convert them into SQL. The SQL is then run on a local database created from our e-commerce product data.

## Features

- Receives questions through a FastAPI endpoint
- Uses Gemini 2.5 API to generate SQL queries
- Returns accurate answers from a SQLite database
- Bonus: includes chart generation and stream-style responses

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Add your Gemini API key inside `query_handler.py`:
   ```python
   genai.configure(api_key="your_key_here")
   ```

3. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

4. Open your browser:
   - Ask questions like:
     - What is my total sales?
     - Calculate RoAS.
     - Which product has highest CPC?

## Notes

- SQLite DB is preloaded from provided CSVs.
- Gemini API is free with Google account at https://aistudio.google.com/apikey

-- End of README --
