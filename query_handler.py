#converting a question to SQL and running it on the SQLite database.

import google.generativeai as genai
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()


# Configure Gemini API
genai.configure(api_key="api_key")  
model = genai.GenerativeModel("gemini-pro")

# Connect to the SQLite database
engine = create_engine("sqlite:///data/ecommerce.db")

def get_sql_from_question(question):
    # Ask Gemini to convert question into SQL
    prompt = f"""
Convert this question to a SQL query using tables: ad_sales, total_sales, eligibility.
Don't explain, just return SQL.
Question: {question}
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"--ERROR FROM GEMINI--: {e}"


def execute_sql(sql_query):
    try:
        with engine.connect() as conn:
            df = pd.read_sql(text(sql_query), conn)
            return df
    except Exception as e:
        return str(e)

def handle_question(question):
    sql = get_sql_from_question(question)
    result = execute_sql(sql)
    if isinstance(result, str):
        return {"sql": sql, "error": result}
    else:
        return {"sql": sql, "result": result.to_dict(orient="records")}
