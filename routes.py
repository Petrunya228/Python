from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from models import Books, ReceivingBooks, session, Base, engine

app = Flask(__name__)


@app.route('/get-all-books', methods=['GET'])
def get_all_books():
    query_result = session.query(Books).all()
    books = []
    for book in query_result:
        books.append(book.to_json())
    return jsonify(books=books)


@app.route('/get-students-debtors', methods=['GET'])
def get_students_debtors():
    query_result = (session.query(ReceivingBooks)
                    .filter(ReceivingBooks.date_of_issue < (datetime.now() - timedelta(days=14)),
                            ReceivingBooks.date_of_return is None).all())
    students_debtors = []
    for receiving_book in query_result:
        students_debtors.append(receiving_book.to_json())
    return jsonify(students_debtors=students_debtors)


@app.route('/give-book-to-student', methods=['POST'])
def give_book_to_student():
    try:
        book_id = request.form.get('book_id', type=int)
        student_id = request.form.get('student_id', type=int)
        new_receiving_book = ReceivingBooks(book_id=book_id, student_id=student_id, date_of_issue=datetime.now())
        session.add(new_receiving_book)
        return jsonify({"message": "Книга выдана студенту"})
    except:
        return jsonify({"message": "Что-то пошло не так"}), 400


@app.route('/return-book-to-lib', methods=['POST'])
def return_book_to_lib():
    try:
        book_id = request.form.get('book_id', type=int)
        student_id = request.form.get('student_id', type=int)

        receiving_book = session.query(ReceivingBooks).filter(ReceivingBooks.book_id == book_id,
                                                              ReceivingBooks.student_id == student_id).one()
        receiving_book.date_of_return = datetime.now()
        return jsonify({"message": "Книга успешно возвращена"})
    except:
        return jsonify({"message": "Что-то пошло не так"}), 400


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True)
