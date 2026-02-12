# 🚀 30 Days of AI — Day 1  
### Connect Streamlit to Snowflake

The **#30DaysOfAI** challenge is a hands-on learning journey designed to help you build AI-powered applications using **Streamlit**.  
On **Day 1**, the goal is simple but important: **connect a Streamlit app to Snowflake** and verify the connection.

This step lays the foundation for all future days in the challenge.

---

## 🎯 Objective

- Establish a connection between **Streamlit** and **Snowflake**
- Run a basic query to confirm the connection
- Display the Snowflake version inside the Streamlit app

---

## ✅ Prerequisites

Before starting, make sure you have:

### 1. Snowflake Account
- Sign up for a **free Snowflake trial** (120 days)
- Ensure you have:
  - Account name
  - Username & password
  - Role
  - Warehouse
  - Database & schema

### 2. Python Environment
- Python **3.9+** recommended
- Install required libraries:
  - `streamlit`
  - `snowflake-snowpark-python`

### 3. Streamlit Setup
You can run this app in **any of the following environments**:
- Streamlit in Snowflake (recommended)
- Local machine
- Streamlit Community Cloud

---

## 🔐 Secrets Configuration (Local / Community Cloud)

For local development or Streamlit Community Cloud, create:

.streamlit/secrets.toml

Add your Snowflake credentials:

```toml
[connections.snowflake]
account = "your_account"
user = "your_username"
password = "your_password"
role = "your_role"
warehouse = "your_warehouse"
database = "your_database"
schema = "your_schema"
```

## ⚠️ Important

- Add .streamlit/secrets.toml to .gitignore
- Never commit secrets to GitHub
- If you’re using Streamlit in Snowflake, no secrets file is required.

**Day 1 complete — you’re officially running LLMs in Snowflake! 🎉**

