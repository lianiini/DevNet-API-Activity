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

if *name* == "__main__":
        lib.run(debug=True)
