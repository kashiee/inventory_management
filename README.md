# Inventory Management Tool (Backend)

A simple FastAPI backend for inventory management with user authentication and product management.

## Features
- User registration and JWT login
- Add, update, and list products
- SQLite database (easy to switch to PostgreSQL)
- OpenAPI/Swagger docs
- **Bonus:** Bash script and Python CLI for API interaction

## Setup

1. **Clone the repo and navigate to the backend folder**
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`

## API Documentation
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- OpenAPI JSON: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

## Database
- Uses SQLite by default (`inventory.db` in project root).
- To switch to PostgreSQL, update `SQLALCHEMY_DATABASE_URL` in `app/database.py`.

## Testing
- Use the provided `test_api.sh` bash script:
  ```bash
  bash test_api.sh
  ```
- Or use the Python CLI:
  ```bash
  python app/cli.py --help
  ```
- Or use Swagger UI/Postman for manual testing.

## CLI Usage Examples
- Register: `python app/cli.py register --username puja --password mypassword`
- Login: `python app/cli.py login --username puja --password mypassword`
- Add Product: `python app/cli.py add-product --token <TOKEN> --name Phone --type Electronics --sku PHN-001 --image_url https://example.com/phone.jpg --description "Latest Phone" --quantity 5 --price 999.99`
- Update Quantity: `python app/cli.py update-quantity --token <TOKEN> --product_id 1 --quantity 15`
- Get Products: `python app/cli.py get-products --token <TOKEN>`

## Assumptions
- Only basic user and product management is implemented (no roles/admins).
- JWT secret is hardcoded for demo; use env vars in production.
- No email verification or password reset for simplicity.

## Clean Code & Modularity
- Code is organized by responsibility (models, schemas, crud, auth, dependencies, main).
- All functions and endpoints are documented with docstrings and comments.
- Follows PEP8 and FastAPI best practices.

## Stretch Work / Bonus
- Bash script (`test_api.sh`) for quick API testing
- Python CLI (`app/cli.py`) for interactive API usage

--- 