# 🤖 30 Days of AI — Day 2  
### Hello, Cortex!

The **#30DaysOfAI** challenge helps you learn how to build AI applications using **Streamlit** and **Snowflake**.

On **Day 2**, we take the next big step:  
**running a Large Language Model (LLM) directly inside Snowflake using Cortex** and interacting with it through a Streamlit UI.

---

## 🎯 Objective

- Run an LLM using **Snowflake Cortex**
- Accept a user prompt via Streamlit
- Send the prompt to a Cortex model
- Display the AI-generated response in the app

---

## ✅ Prerequisites

Before starting Day 2, ensure you have:

### 1. Completed Day 1
- A working **Streamlit ↔ Snowflake connection**
- Proper Snowflake credentials configured

### 2. Snowflake Account with Cortex Access
- Snowflake trial or paid account
- Role with access to **Cortex AI functions**
- Internet access enabled for Cortex models

### 3. Required Python Libraries

The following libraries are required to use Snowflake Cortex and Snowpark:

- `snowflake-ml-python==1.20.0`
- `snowflake-snowpark-python==1.44.0`

#### Installation Options
- **Local development**: add them to `requirements.txt` and install
- **Streamlit Community Cloud**: include `requirements.txt` in your repo
- **Streamlit in Snowflake**: add them from the *Packages* dropdown

---

## 🧠 Key Concepts Explained

### 1. Snowflake Cortex
**Snowflake Cortex** allows you to run large language models *inside Snowflake* without managing infrastructure.

Key benefits:
- No external API calls
- Secure, governed execution
- Works directly with Snowpark and SQL workflows

---

### 2. Environment-Aware Connection
The app automatically detects where it’s running:

- **Streamlit in Snowflake** → uses the active session
- **Local / Community Cloud** → uses credentials from `secrets.toml`

This ensures **one codebase works everywhere**, which is ideal for production apps.

---

### 3. Using `ai_complete()`
The `ai_complete()` function is a **Snowpark Cortex function** that:
- Sends a prompt to a selected LLM
- Executes inference inside Snowflake
- Returns the result as **JSON**

Why use it?
- Integrates naturally with Snowpark DataFrames
- Works well in SQL-style pipelines

⚠️ Note:  
`ai_complete()` does **not support streaming** and returns JSON that must be parsed.  
A simpler Python API with streaming support is introduced in later days.

---

### 4. Model Selection
A specific Cortex model is selected (e.g. `claude-3-5-sonnet`) and stored as a variable.

This makes it easy to:
- Switch models
- Experiment with different LLMs
- Compare outputs across models

---

### 5. Running Inference via Streamlit
The app uses:
- A text input for the user prompt
- A button to trigger inference

When the button is clicked:
- A single-row Snowpark DataFrame is created
- The Cortex LLM runs on that row
- The response is returned to the app

This pattern allows AI inference to behave like a database operation.

---

### 6. Parsing and Displaying the Response
Cortex returns output as a **JSON string**.

Steps involved:
1. Execute the Snowflake query
2. Collect the result into Python
3. Parse the JSON response
4. Display the AI output in Streamlit

This ensures the response is readable and user-friendly.

---

## 🟢 Expected Output

When the app runs successfully:
- The user enters a prompt
- Clicks **Generate Response**
- The AI-generated answer appears on screen

This confirms:
- Cortex is enabled
- The model is accessible
- LLM inference is working inside Snowflake

---

## 🛠 Troubleshooting

- Ensure your Snowflake role has access to Cortex
- Verify required packages are installed
- Check that a valid model name is used
- Confirm Day 1 connection works correctly

---

## 📚 Resources

- Snowflake Cortex LLM Functions  
- COMPLETE Function Reference  
- Available Cortex Models  
- Snowpark Python API  

---

## 🚀 What’s Next?

With LLMs now running inside Snowflake, upcoming days will explore:
- Streaming responses
- Prompt engineering
- Data-aware AI workflows
- Building production-grade AI apps

**Day 2 complete — you’re officially running LLMs in Snowflake! 🎉**
