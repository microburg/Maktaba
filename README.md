# Library Management API

## Description
This is a RESTful API for managing a library's collection of books. The API allows users to add, list, search, update, and delete books. It also provides a Swagger UI for API documentation.

## Features
- Add new books
- List all books
- Search books by author, published year, or genre
- Update book details by ISBN
- Delete a book by ISBN
- Swagger documentation available at `/api-docs`

---

## Setup Instructions

### Prerequisites
- Docker installed on your machine.
- Python (if running without Docker).

---

### **Running the API with Docker**

1. **Build the Docker Image**:
   ```bash
   docker build -t library-api .

---

### **Add requests for each endpoint:**
   - **POST `/books`**: Add a sample book.
   - **GET `/books`**: Retrieve all books.
   - **GET `/books/search`**: Search by filters.
   - **PUT `/books/<isbn>`**: Update a book by ISBN.
   - **DELETE `/books/<isbn>`**: Delete a book by ISBN.
