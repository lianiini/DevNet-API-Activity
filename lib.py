from flask import Flask, jsonify, request

lib = Flask(__name__)
books = [
    {
        "id": 1,
        "title": "The Love Hypothesis",
        "author": "Ali Hazelwood",
        "available": True
    },
    {
        "id": 2,
        "title": "Behind Five Willows",
        "author": "June Hur",
        "available": False
    },
    {
        "id": 3,
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "available": True
    }
]

def get_next_id():
    if not books:
        return 1
    return max(book["id"] for book in books) + 1

@lib.route("/books", methods=["GET"])
def get_books():

    if books is not None:
        return jsonify({
            "books": books
        }), 200

    else:
        return jsonify({
            "error": "Internal server error",
            "message": "Unable to retrieve books"
        }), 500

@lib.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next(
        (book for book in books if book["id"] == book_id),
        None
    )

    if book is None:
        return jsonify({
            "error": "Book not found"
        }), 404

    return jsonify(book), 200

@lib.route("/books", methods=["POST"])
def add_book():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "A JSON request body is required"
        }), 400

    title = data.get("title")
    author = data.get("author")

    if (not isinstance(title, str) or not title.strip()) and \
    (not isinstance(author, str) or not author.strip()):
        return jsonify({
            "error": "Title and author are required"
        }), 400

    if not isinstance(title, str) or not title.strip():
        return jsonify({
            "error": "Title is required"
        }), 400

    if not isinstance(author, str) or not author.strip():
        return jsonify({
            "error": "Author is required"
        }), 400

    new_book = {
        "id": get_next_id(),
        "title": title.strip(),
        "author": author.strip(),
        "available": True
    }

    books.append(new_book)

    return jsonify({
        "message": "Book added successfully",
        "book": new_book
    }), 201

if __name__ == "__main__":
        lib.run(debug=True)
