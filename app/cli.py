import argparse
import requests
import sys

BASE_URL = "http://127.0.0.1:8000"
TOKEN = None


def register(args):
    """Register a new user."""
    payload = {"username": args.username, "password": args.password}
    r = requests.post(f"{BASE_URL}/register", json=payload)
    print(r.status_code, r.text)

def login(args):
    """Login and store JWT token."""
    global TOKEN
    data = {"username": args.username, "password": args.password}
    r = requests.post(f"{BASE_URL}/login", data=data)
    if r.status_code == 200:
        TOKEN = r.json()["access_token"]
        print("Login successful. Token:", TOKEN)
    else:
        print(r.status_code, r.text)

def add_product(args):
    """Add a new product."""
    headers = {"Authorization": f"Bearer {args.token}"}
    payload = {
        "name": args.name,
        "type": args.type,
        "sku": args.sku,
        "image_url": args.image_url,
        "description": args.description,
        "quantity": args.quantity,
        "price": args.price
    }
    r = requests.post(f"{BASE_URL}/products", json=payload, headers=headers)
    print(r.status_code, r.text)

def update_quantity(args):
    """Update product quantity."""
    headers = {"Authorization": f"Bearer {args.token}"}
    payload = {"quantity": args.quantity}
    r = requests.put(f"{BASE_URL}/products/{args.product_id}/quantity", json=payload, headers=headers)
    print(r.status_code, r.text)

def get_products(args):
    """Get all products."""
    headers = {"Authorization": f"Bearer {args.token}"}
    r = requests.get(f"{BASE_URL}/products", headers=headers)
    print(r.status_code, r.text)

def main():
    parser = argparse.ArgumentParser(description="CLI for Inventory Management Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Register
    parser_register = subparsers.add_parser("register")
    parser_register.add_argument("--username", required=True)
    parser_register.add_argument("--password", required=True)
    parser_register.set_defaults(func=register)

    # Login
    parser_login = subparsers.add_parser("login")
    parser_login.add_argument("--username", required=True)
    parser_login.add_argument("--password", required=True)
    parser_login.set_defaults(func=login)

    # Add Product
    parser_add = subparsers.add_parser("add-product")
    parser_add.add_argument("--token", required=True)
    parser_add.add_argument("--name", required=True)
    parser_add.add_argument("--type", required=True)
    parser_add.add_argument("--sku", required=True)
    parser_add.add_argument("--image_url", required=True)
    parser_add.add_argument("--description", required=True)
    parser_add.add_argument("--quantity", type=int, required=True)
    parser_add.add_argument("--price", type=float, required=True)
    parser_add.set_defaults(func=add_product)

    # Update Quantity
    parser_update = subparsers.add_parser("update-quantity")
    parser_update.add_argument("--token", required=True)
    parser_update.add_argument("--product_id", type=int, required=True)
    parser_update.add_argument("--quantity", type=int, required=True)
    parser_update.set_defaults(func=update_quantity)

    # Get Products
    parser_get = subparsers.add_parser("get-products")
    parser_get.add_argument("--token", required=True)
    parser_get.set_defaults(func=get_products)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 