# FastAPI SQL Query Generator

This FastAPI project provides an API for generating and validating SQL queries based on user-provided topics. It includes endpoints for generating pseudo-SQL, explaining queries, and validating them.

## Features
- **Generate SQL queries** from natural language input.
- **Explain SQL queries** with detailed descriptions.
- **Validate SQL queries** for correctness.

## Installation

### Prerequisites
- Python 3.8+
- FastAPI
- Uvicorn
- Required dependencies from `helper.py`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/fastapi-sql-query-generator.git
   cd fastapi-sql-query-generator
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
   ```
3. Ensure `helper.py` contains the required functions:
   - `pseudo_SQL()`
   - `explain()`
   - `validator()`

## Running the API
Start the FastAPI server with Uvicorn:
```bash
uvicorn main:app --reload
```

## API Endpoints

### `GET /`
**Description:** Root endpoint for testing the API.
**Response:**
```json
{
  "Hello": "World"
}
```

### `POST /query`
**Description:** Generates an SQL query from a given topic.
**Request Body:**
```json
{
  "topic": "Find all users"
}
```
**Response:**
```json
{
  "query": "SELECT * FROM users;"
}
```

### `GET /explain`
**Description:** Provides an explanation for the generated SQL query.
**Request Body:**
```json
{
  "topic": "Find all users"
}
```
**Response:**
```json
{
  "explanation": "This query retrieves all records from the users table."
}
```

### `POST /validate`
**Description:** Validates the generated SQL query.
**Request Body:**
```json
{
  "topic": "Find all users"
}
```
**Response:**
```json
{
  "validation": "Query is valid."
}
```



## License
This project is open-source and available under the MIT License.

