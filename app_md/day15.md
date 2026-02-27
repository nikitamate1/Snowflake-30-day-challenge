# Day 15 -- Model Comparison Arena 🏟️

**30 Days of AI -- Streamlit × Snowflake**

Day 15 wraps up Week 2 (Chatbots) by building a Model Comparison Tool.

After creating multiple chatbot apps, the big question becomes:

> Which model should I actually use?

This app helps answer that by running the same prompt through two
different LLMs and comparing:

-   ⏱️ Latency (response time)
-   🔢 Estimated token usage
-   💬 Response quality (side-by-side)

------------------------------------------------------------------------

## 🚀 What This App Does

The Model Comparison Arena:

-   Lets you select **Model A** and **Model B**
-   Sends the same prompt to both models
-   Runs them sequentially
-   Displays:
    -   Responses side-by-side
    -   Latency per model
    -   Estimated token count

This helps evaluate:

-   ⚡ Speed vs Quality\
-   💰 Cost vs Capability\
-   🧠 Model size vs Output quality

------------------------------------------------------------------------

## 🧠 Core Concepts Used

### 1️⃣ Snowflake Cortex AI (`ai_complete`)

The app uses Snowflake's Cortex AI function to call foundation models
directly from Snowpark.

Instead of calling an external API manually, we:

-   Create a Snowpark DataFrame
-   Call `ai_complete()` inside a `select`
-   Collect the result
-   Parse the JSON response

Everything runs inside Snowflake.

------------------------------------------------------------------------

### 2️⃣ Measuring Latency

We record the time before and after the model call.

Total Response Time = End Time -- Start Time

This metric is critical when comparing smaller vs larger models.

------------------------------------------------------------------------

### 3️⃣ Token Estimation

Since token usage impacts cost, we estimate tokens using:

1 token ≈ 0.75 words

This gives a rough cost indicator.

------------------------------------------------------------------------

### 4️⃣ Streamlit UI Structure

The UI is built using:

-   `st.columns(2)` → Side-by-side layout\
-   `st.container(height=400)` → Scrollable response area\
-   `st.metric()` → Performance metrics display\
-   `st.chat_message()` → Chat-style interface\
-   `st.session_state` → Store latest comparison results

A loop dynamically renders both panels to avoid code duplication.

------------------------------------------------------------------------

## 🛠️ Prerequisites

Before running this app, you need:

1.  Snowflake account with Cortex AI enabled\
2.  Snowpark Python support\
3.  Streamlit installed

Install locally:

pip install streamlit snowflake-snowpark-python

4.  Snowflake credentials stored in:

.streamlit/secrets.toml

------------------------------------------------------------------------

## 🏗️ Project Structure

day15-model-comparison/ │ ├── app.py ├── requirements.txt └── README.md

------------------------------------------------------------------------

## 🎯 Why This Project Matters

Before moving into RAG systems, choosing the right model is critical.

This project gives you:

-   Practical benchmarking experience
-   Performance awareness
-   Cost-awareness thinking
-   Production mindset

------------------------------------------------------------------------

## 🏁 Day 15 Complete

You now have a clean, practical LLM benchmarking interface built with:

-   Streamlit\
-   Snowflake Snowpark\
-   Cortex AI

Week 3: RAG Applications 🚀
