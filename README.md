# Snowflake Connection App

This is a simple Streamlit application that demonstrates how to connect to Snowflake and retrieve the current version.

## Prerequisites

- Python 3.8 or higher
- A Snowflake account with appropriate permissions
- Access to Snowflake database and warehouse

## Installation

1. Clone or download this repository.

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

For local development, you need to set up your Snowflake connection credentials in `Snowflake-30-day-challenge-main/.streamlit/secrets.toml`. Create this file if it doesn't exist and add your connection details: Find in Snowsight → Account → View account details.

```toml
[connections.snowflake]
account = "your_account"
user = "your_user"
password = "your_password"
role = "your_role"
warehouse = "your_warehouse"
database = "your_database"
schema = "your_schema"
```

**Security Note:** Never commit your `secrets.toml` file to version control. It is already included in `.gitignore`.

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app\dayx.py 
   ```
- where x is 1 to 30

2. Open your browser to the URL provided by Streamlit (usually `http://localhost:8501`).

The app will attempt to connect to Snowflake and display the current version.

## Notes

- This app is designed to work both in Snowflake's Streamlit environment and locally/on Streamlit Community Cloud.
- If running in Snowflake, it uses the active session; otherwise, it uses the configured secrets.
