#!/bin/bash

BASE_URL="http://127.0.0.1:8000"
USERNAME="puja"
PASSWORD="mypassword"

# Register user
echo "\n== Register User =="
curl -s -X POST "$BASE_URL/register" \
  -H 'Content-Type: application/json' \
  -d '{"username": "'$USERNAME'", "password": "'$PASSWORD'"}'
echo

# Login and get token
echo "\n== Login =="
LOGIN_RESPONSE=$(curl -s -X POST "$BASE_URL/login" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d "username=$USERNAME&password=$PASSWORD")
echo "$LOGIN_RESPONSE"
TOKEN=$(echo $LOGIN_RESPONSE | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")

# Add product
echo "\n== Add Product =="
ADD_PRODUCT_RESPONSE=$(curl -s -X POST "$BASE_URL/products" \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Phone", "type": "Electronics", "sku": "PHN-001", "image_url": "https://example.com/phone.jpg", "description": "Latest Phone", "quantity": 5, "price": 999.99}')
echo "$ADD_PRODUCT_RESPONSE"
PRODUCT_ID=$(echo $ADD_PRODUCT_RESPONSE | python3 -c "import sys, json; print(json.load(sys.stdin)['id'])")

# Update product quantity
echo "\n== Update Product Quantity =="
UPDATE_RESPONSE=$(curl -s -X PUT "$BASE_URL/products/$PRODUCT_ID/quantity" \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"quantity": 15}')
echo "$UPDATE_RESPONSE"

# Get products
echo "\n== Get Products =="
curl -s -X GET "$BASE_URL/products" \
  -H "Authorization: Bearer $TOKEN"
echo 