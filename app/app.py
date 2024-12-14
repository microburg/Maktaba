from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import json

app = Flask(__name__)

# To store in the JSON file
def load_data():
    with open('./data.json', 'r') as file:
        return json.load(file)

def save_data(data):
    with open('./data.json', 'w') as file:
        json.dump(data, file, indent=4)

# CRUD Endpoints
@app.route('/books', methods=['POST'])
def add_book():
    data = load_data()
    new_book = request.json

    # Ensure required fields are present
    if not all(key in new_book for key in ('title', 'author', 'published_year', 'isbn')):
        return jsonify({"error": "Missing required fields!"}), 400

    # Check for duplicate
    if any(book['isbn'] == new_book['isbn'] for book in data):
        return jsonify({"error": "ISBN already exists!"}), 400

    data.append(new_book)
    save_data(data)
    return jsonify({"message": "Book added successfully!"}), 201

@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(load_data())

@app.route('/books/search', methods=['GET'])
def search_books():
    data = load_data()
    filters = request.args
    filtered_books = [book for book in data if all(str(book.get(k, '')).lower() == v.lower() for k, v in filters.items())]
    return jsonify(filtered_books)

@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    data = load_data()
    book = next((b for b in data if b['isbn'] == isbn), None)
    if not book:
        return jsonify({"error": "Book not found!"}), 404

    updates = request.json
    book.update(updates)
    save_data(data)
    return jsonify({"message": "Book updated successfully!"})

@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    data = load_data()
    updated_data = [b for b in data if b['isbn'] != isbn]
    if len(data) == len(updated_data):
        return jsonify({"error": "Book not found!"}), 404

    save_data(updated_data)
    return jsonify({"message": "Book deleted successfully!"})

# Swagger Integration
SWAGGER_URL = '/api-docs'
API_DOCS_PATH = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI endpoint
    API_DOCS_PATH # Swagger JSON file
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger_json():
    swagger_data = {
        "openapi": "3.0.0",
        "info": {
            "title": "Library Management API",
            "description": "API for managing a collection of books in a library",
            "version": "1.0.0"
        },
        "paths": {
            "/books": {
                "get": {
                    "summary": "List all books",
                    "responses": {
                        "200": {
                            "description": "A list of all books",
                            "content": {
                                "application/json": {
                                    "example": [
                                        {
                                            "title": "Book Title",
                                            "author": "Author Name",
                                            "published_year": 2020,
                                            "isbn": "1234567890123",
                                            "genre": "Fiction"
                                        }
                                    ]
                                }
                            }
                        }
                    }
                },
                "post": {
                    "summary": "Add a new book",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "example": {
                                    "title": "New Book",
                                    "author": "Author Name",
                                    "published_year": 2022,
                                    "isbn": "9876543210987",
                                    "genre": "Non-Fiction"
                                }
                            }
                        }
                    },
                    "responses": {
                        "201": {"description": "Book added successfully"}
                    }
                }
            },
            "/books/search": {
                "get": {
                    "summary": "Search for books",
                    "parameters": [
                        {"name": "author", "in": "query", "required": False},
                        {"name": "published_year", "in": "query", "required": False},
                        {"name": "genre", "in": "query", "required": False}
                    ],
                    "responses": {
                        "200": {
                            "description": "Books matching the criteria",
                            "content": {"application/json": {}}
                        }
                    }
                }
            },
            "/books/{isbn}": {
                "put": {
                    "summary": "Update book details",
                    "parameters": [{"name": "isbn", "in": "path", "required": True}],
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "example": {"title": "Updated Title"}
                            }
                        }
                    },
                    "responses": {
                        "200": {"description": "Book updated successfully"},
                        "404": {"description": "Book not found"}
                    }
                },
                "delete": {
                    "summary": "Delete a book by ISBN",
                    "parameters": [{"name": "isbn", "in": "path", "required": True}],
                    "responses": {
                        "200": {"description": "Book deleted successfully"},
                        "404": {"description": "Book not found"}
                    }
                }
            }
        }
    }
    return jsonify(swagger_data)

if __name__ == "__main__":
    app.run(debug=True)
