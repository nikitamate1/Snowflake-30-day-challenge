# 🧠 30 Days of AI — Day 4  
### Caching Your App

The **#30DaysOfAI** challenge is all about building efficient, production-ready AI applications using **Streamlit** and **Snowflake**.

On **Day 4**, the focus shifts from *making LLM calls work* to *making them fast and cost-efficient* by introducing **caching**.

---

## 🎯 Objective

- Call a Snowflake Cortex LLM from a Streamlit app
- Cache LLM responses to avoid repeated computation
- Measure and display the time taken for each request
- Improve performance and user experience

---

## ✅ Prerequisites

Before starting Day 4, make sure you have:

### 1. Completed Day 1–3
- Working Streamlit ↔ Snowflake connection
- Familiarity with Cortex LLM calls
- Understanding of streaming vs non-streaming responses

### 2. Snowflake Account with Cortex Access
- Snowflake trial or paid account
- Role with access to **Cortex AI functions**

### 3. Required Python Libraries
- `streamlit`
- `snowflake-snowpark-python`
- `snowflake-ml-python`

---

## 🧠 Key Concepts Explained

### 1. Why Caching Matters
Calling an LLM is:
- Computationally expensive
- Slower than normal functions
- Potentially costly

Caching allows your app to:
- Reuse previous results
- Avoid repeated LLM calls for the same prompt
- Respond instantly on repeated inputs

This is critical for **production-grade AI apps**.

---

### 2. Streamlit `@st.cache_data`
The `@st.cache_data` decorator tells Streamlit to:
- Store the output of a function
- Use the function inputs as a cache key
- Return cached results when inputs repeat

In this app:
- The **prompt text** is the cache key
- Same prompt → instant response
- Changed prompt → new LLM call

---

### 3. Encapsulating the LLM Call
The LLM logic is wrapped inside a dedicated function that:
- Calls the Cortex model
- Collects the result from Snowflake
- Parses the JSON response
- Returns a structured Python object

This design:
- Keeps the UI code clean
- Makes caching easy
- Encourages reusable, testable code

---

### 4. Measuring Performance
The app records:
- Time just before calling the LLM
- Time immediately after receiving the response

The elapsed time is displayed to the user, making the impact of caching **visible and measurable**.

You’ll typically see:
- First call: several seconds
- Cached call: near-instant response

---

### 5. Simple and Effective UI
The interface includes:
- A text input for the prompt
- A submit button to trigger the LLM call
- A success message showing execution time
- The full AI response rendered below

This keeps the focus on **functionality and performance**, not UI complexity.

---

## 🟢 Expected Output

When the app runs:
- Enter a prompt and click **Submit**
- The AI response appears below
- The time taken is displayed

Submitting the **same prompt again** will return the result almost instantly, proving the cache is working.

---

## 🛠 Troubleshooting

- Ensure Cortex access is enabled for your Snowflake role
- Verify required packages are installed
- Remember: changing the prompt even slightly triggers a cache miss
- Be aware of caching limitations in Streamlit in Snowflake

---

## 📚 Resources

- Streamlit `st.cache_data` Documentation  
- Caching in Streamlit  
- Streamlit in Snowflake Caching Limitations  

---

## 🚀 What’s Next?

With caching in place, future days will focus on:
- State management
- Conversational memory
- Tool-augmented LLMs
- Building scalable AI applications

**Day 4 complete — your AI app is now faster and smarter! ⚡**
