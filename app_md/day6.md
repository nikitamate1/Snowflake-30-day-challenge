# ⏳ 30 Days of AI — Day 6  
### Status UI for Long-Running Tasks

The **#30DaysOfAI** challenge is designed to help you build real-world AI applications using **:contentReference[oaicite:0]{index=0}** and **:contentReference[oaicite:1]{index=1}**.

On **Day 6**, we enhance the LinkedIn Post Generator by adding a **status-based UI** that gives users real-time feedback while a long-running AI task is executing.

---

## 🎯 Objective

- Build **v2** of the LinkedIn Post Generator
- Call a Snowflake Cortex LLM to generate content
- Provide clear visual feedback during long-running operations
- Improve user experience using Streamlit’s status components

---

## ✅ Prerequisites

Before starting Day 6, make sure you have:

### 1. Completed Day 1–5
- Working Streamlit ↔ Snowflake connection
- Experience calling Snowflake Cortex LLMs
- Familiarity with prompt construction and caching

### 2. Snowflake Account with Cortex Enabled
- Snowflake trial or paid account
- Role with access to **Cortex AI functions**
- Claude 3.5 Sonnet (or equivalent) available

### 3. Required Python Libraries
- `streamlit`
- `snowflake-snowpark-python`
- `snowflake-ml-python`

---

## 🧠 Key Concepts Explained

### 1. Why Status UI Matters
LLM calls can take several seconds.  
Without feedback, users may think the app is broken.

A **status UI**:
- Shows progress clearly
- Prevents repeated clicks
- Makes long-running tasks feel responsive
- Improves perceived performance

This is essential for **production-grade AI apps**.

---

### 2. Environment-Aware Snowflake Connection
The app automatically detects where it’s running:

- **Streamlit in Snowflake** → uses the active session
- **Local / Community Cloud** → uses credentials from `secrets.toml`

This ensures one codebase works across all environments.

---

### 3. Cached Cortex LLM Calls
The LLM call is wrapped in a function decorated with `@st.cache_data`.

Benefits:
- Avoids repeated LLM calls for the same prompt
- Reduces latency and compute usage
- Makes the app faster on repeated inputs

Caching is especially important for text-generation workflows.

---

### 4. Snowpark Scalar Function Pattern
The LLM call is executed using a Snowpark pattern that:
- Creates a single-row DataFrame
- Executes the Cortex AI function inside Snowflake
- Returns the result as JSON

This approach keeps all AI computation **inside Snowflake**, maintaining security and governance.

---

### 5. Status-Driven Execution Flow
The app wraps the AI execution inside a **status container**, which visually communicates:

1. **Thinking** – analyzing tone and constraints  
2. **Generating** – calling Snowflake Cortex  
3. **Completed** – response successfully generated  

Once finished, the status collapses and shows a success indicator.

This prevents the UI from appearing frozen during blocking operations.

---

### 6. Prompt Engineering with User Inputs
The prompt is dynamically constructed using:
- Selected tone
- Desired word count
- Source content URL

The AI is instructed to act as an **expert social media manager**, which helps ensure:
- Professional tone
- Platform-appropriate formatting
- High-quality output

---

## 🟢 Expected Output

When the app runs:
- The user enters post parameters
- Clicks **Generate Post**
- A live status panel shows progress
- A formatted LinkedIn post appears below

This confirms:
- Cortex LLM integration works
- Status UI improves UX
- Long-running tasks are handled gracefully

---

## 🛠 Troubleshooting

- Ensure Cortex access is enabled for your Snowflake role
- Verify required packages are installed
- Remember cached results may return instantly for repeated prompts
- If the status does not update, ensure the task is inside the status context

---

## 📚 Resources

- Streamlit `st.status` Documentation  
- Snowflake Cortex LLM Functions  
- Best Practices for Long-Running Tasks in Streamlit  

---

## 🚀 What’s Next?

With status-aware execution in place, upcoming days will explore:
- Stateful and multi-step workflows
- Conversational memory
- Tool-using AI agents
- Production-ready AI UX patterns

**Day 6 complete — your AI app now communicates while it thinks! 🎉**

