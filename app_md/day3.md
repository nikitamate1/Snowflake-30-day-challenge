# 🌊 30 Days of AI — Day 3  
### Write Streams

The **#30DaysOfAI** challenge focuses on building real-world AI applications using **Streamlit** and **Snowflake**.

On **Day 3**, we move from simple LLM calls to a **real-time streaming experience** by calling **Snowflake Cortex through an OpenAI-compatible REST API**.

---

## 🎯 Objective

- Call Snowflake Cortex using the OpenAI-compatible API
- Let users select an LLM model
- Accept a prompt through Streamlit
- Stream the LLM response back in real time

---

## ✅ Prerequisites

Before starting Day 3, ensure you have:

### 1. Completed Day 1 & Day 2
- Working Streamlit ↔ Snowflake connection
- Familiarity with Cortex LLMs and prompts

### 2. Snowflake Account with Cortex Enabled
- Snowflake trial or paid account
- Access to **Cortex REST API**
- A **Programmatic Access Token (PAT)**

### 3. Required Python Libraries
- `streamlit`
- `openai` (used to call the OpenAI-compatible Cortex API)

---

## 🔐 Secrets Configuration

Authentication is done using a **Snowflake Programmatic Access Token (PAT)**.

Your `secrets.toml` should include:

```toml
[connections.snowflake]
account = "your_account"
password = "your_pat_token"
```

**Day 3 complete — you’re officially building real-world AI applications! 🎉**
