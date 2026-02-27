# Day 16 -- Batch Document Text Extractor for RAG 📄

**30 Days of AI -- Streamlit × Snowflake**

Day 16 begins Week 3 by building the first step of a RAG
(Retrieval-Augmented Generation) pipeline:

Extract text from documents and store it in Snowflake.

This app allows you to upload multiple TXT, Markdown (MD), and PDF files
at once, extract raw text content, and save it into a structured
database table for downstream RAG processing.

------------------------------------------------------------------------

## 🚀 What This App Does

-   Upload multiple documents in one batch
-   Extract raw text from TXT, MD, and PDF files
-   Track word and character counts
-   Store extracted content in Snowflake
-   Support Replace or Append modes
-   Preview and query saved documents
-   Prepare clean data for chunking and embeddings (Day 17)

------------------------------------------------------------------------

## 🧠 Why This Matters for RAG

Before chunking and embeddings, you need:

1.  Clean extracted text\
2.  Structured storage\
3.  Metadata tracking

This tool creates a proper document ingestion pipeline so your RAG
system has reliable input data.

------------------------------------------------------------------------

## 📂 Supported File Types

-   `.txt`
-   `.md`
-   `.pdf`

PDF files are processed page by page using `pypdf`.

------------------------------------------------------------------------

## 🛠️ Core Features Explained

### 1️⃣ Batch Upload

Uses `st.file_uploader()` with:

accept_multiple_files=True

This allows uploading 10, 50, or even 100 files at once.

------------------------------------------------------------------------

### 2️⃣ Text Extraction Logic

-   TXT / MD → Read and decode as UTF-8
-   PDF → Loop through pages and extract text
-   Word count and character count calculated per file

All extracted content is stored in memory before saving.

------------------------------------------------------------------------

### 3️⃣ Replace vs Append Mode

If the target table already exists:

-   Replace Mode (checked) → Clears old data
-   Append Mode (unchecked) → Adds new documents

This gives flexibility when testing batches.

------------------------------------------------------------------------

### 4️⃣ Automatic Database Setup

The app automatically:

-   Creates Database if not exists
-   Creates Schema if not exists
-   Creates Table if not exists

Table structure:

-   DOC_ID (Auto Increment)
-   FILE_NAME
-   FILE_TYPE
-   FILE_SIZE
-   EXTRACTED_TEXT
-   WORD_COUNT
-   CHAR_COUNT
-   UPLOAD_TIMESTAMP

------------------------------------------------------------------------

### 5️⃣ Save to Snowflake

Each document is inserted into the table with:

-   Full extracted text
-   Metadata
-   Automatic timestamp

The EXTRACTED_TEXT column stores complete document content for RAG
processing.

------------------------------------------------------------------------

### 6️⃣ Query & Document Viewer

You can:

-   Query all saved documents
-   View metadata summary
-   Select a document by ID
-   Load and view full extracted text

This confirms that the entire document content is stored properly.

------------------------------------------------------------------------

## 📦 Prerequisites

Before running this app, you need:

1.  Snowflake account with Snowpark enabled
2.  Cortex access (for future RAG steps)
3.  Streamlit installed locally

Install dependencies:

pip install streamlit snowflake-snowpark-python pypdf pandas

4.  Snowflake credentials configured in:

.streamlit/secrets.toml

Or run inside Streamlit in Snowflake.

------------------------------------------------------------------------

## 🏗️ Project Structure

day16-batch-document-extractor/ │ ├── app.py ├── requirements.txt └──
README.md

------------------------------------------------------------------------

## 🔄 Integration with Day 17

The app stores:

-   Database name
-   Schema name
-   Table name

Inside session state so Day 17 can automatically:

-   Load documents
-   Chunk text
-   Generate embeddings
-   Build the RAG pipeline

------------------------------------------------------------------------

## 🎯 What You Built

A production-style document ingestion system that:

-   Handles batch uploads
-   Extracts multi-format content
-   Stores structured metadata
-   Prepares data for AI pipelines

This is the foundation of every real-world RAG system.

------------------------------------------------------------------------

## 🏁 Day 16 Complete

You now have a scalable document extraction pipeline ready for:

-   Chunking
-   Embeddings
-   Retrieval
-   Generation

Next: Day 17 -- Chunking & Embedding 🚀
