# 🚀 Day 17 – Loading and Transforming Customer Reviews for RAG

## 30 Days of AI

The **#30DaysOfAI** challenge is designed to help you build real-world AI applications using Streamlit and Snowflake.

---

## 📌 Day 17 Goal

On Day 17, we:

- Load customer reviews extracted in **Day 16**
- Process them into searchable text chunks
- Save structured chunks into Snowflake
- Prepare data for embedding generation (Day 18)

The source table is:

```
RAG_DB.RAG_SCHEMA.EXTRACTED_DOCUMENTS
```

Each review contains:
- Product feedback
- Date
- Sentiment score
- Order ID  
- ~50–150 words per review

---

# 🏗️ App Overview

This app performs 4 main steps:

1. Load reviews from Snowflake  
2. Choose chunking strategy  
3. Create chunks  
4. Save chunks into a new Snowflake table  

---

# 1️⃣ Load Reviews from Day 16

The app connects to Snowflake using Snowpark and queries:

- DOC_ID  
- FILE_NAME  
- EXTRACTED_TEXT  
- WORD_COUNT  
- CHAR_COUNT  

The data is converted to a Pandas DataFrame using:

```python
df = session.sql(query).to_pandas()
```

The DataFrame is stored in `st.session_state` so it persists across reruns.

---

# 2️⃣ Choose Processing Strategy

Two processing options are provided:

### ✅ Option 1 – Keep Each Review Intact (Recommended)
- One review = one chunk
- Best for short reviews (~150 words)

### 🔀 Option 2 – Split Long Reviews
- Used when reviews exceed a threshold
- Adjustable:
  - Chunk size (default: 200 words)
  - Overlap (default: 50 words)

Overlap ensures context continuity between chunks.

Example logic:

```python
for i in range(0, len(words), chunk_size - overlap):
```

If chunk_size = 200 and overlap = 50 → step size = 150 words.

---

# 3️⃣ Chunk Creation Logic

## Full Review Mode

Each review becomes:

- CHUNK_ID
- DOC_ID
- FILE_NAME
- CHUNK_TEXT
- CHUNK_SIZE
- CHUNK_TYPE = full_review

## Split Mode

Long reviews are split into overlapping segments:

- chunk_type = chunked_review
- Overlapping windows preserve semantic continuity

---

# 4️⃣ Save Chunks to Snowflake

Chunks are stored in:

```
RAG_DB.RAG_SCHEMA.REVIEW_CHUNKS
```

Table schema:

- CHUNK_ID
- DOC_ID
- FILE_NAME
- CHUNK_TEXT
- CHUNK_SIZE
- CHUNK_TYPE
- CREATED_TIMESTAMP

Chunks are written using bulk upload:

```python
session.write_pandas(chunks_df, table_name=..., overwrite=replace_mode)
```

Bulk writes are much faster than individual INSERT statements.

---

# 🔁 Replace Mode

If enabled:
- Existing chunks are cleared using TRUNCATE TABLE
- New chunks overwrite old data

If disabled:
- New chunks are appended

---

# 🔎 Query & Verify

You can:

- View total chunks
- See full vs split counts
- Preview first 100 characters
- Load full chunk text

This ensures chunking worked correctly before embedding generation.

---

# 🔗 Integration with Day 18

After saving, the app stores:

```
st.session_state.chunks_table
st.session_state.chunks_database
st.session_state.chunks_schema
```

Day 18 will:
- Load these chunks
- Generate embeddings
- Store vectors for RAG search

---

# 🧠 Why Chunking Matters

Good chunking:

- Improves embedding quality
- Reduces token waste
- Enhances retrieval accuracy
- Maintains semantic continuity

Since reviews are short, full-review mode is typically best.

---

# 📦 Result

After running this app:

✔ Reviews are transformed into properly sized chunks  
✔ Chunks are stored in Snowflake  
✔ Data is ready for embedding generation  
✔ RAG pipeline is progressing step-by-step  

---

**Day 17 Complete – Chunking Ready for Vectorization 🚀**
