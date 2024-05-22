from datetime import datetime
from flask import Flask, request, jsonify, Response
from models import get_all_rooms, init_db, Room, Order, get_order, add_order, insert_room_to_bd

app = Flask(__name__)

@app.route("/rooms")
def retrieve_all_rooms():
    check_in = request.args.get('checkIn')
    check_out = request.args.get('checkOut')
    if check_in and check_out:
        rooms = get_all_rooms(check_in, check_out)
    else:
        rooms = get_all_rooms()
    room_list = {"rooms": []}
    for room in rooms:
        room_list["rooms"].append({
            "roomId": room.id,
            "floor": room.floor,
            "beds": room.beds,
            "guestNum": room.guestNum,
            "price": room.price,
            "bookingParams": {
                "checkIn": check_in,
                "checkOut": check_out,
                "roomId": room.id
            }
        })
    return jsonify(room_list), 200

@app.route('/book', methods=['POST'])
def make_booking():
    if request.method == "POST":
        data = request.get_json()
        check_in_date = datetime.strptime(str(data["bookingDates"]["checkIn"]), "%Y%m%d")
        check_out_date = datetime.strptime(str(data["bookingDates"]["checkOut"]), "%Y%m%d")
        new_order = Order(
            id=None,
            checkIn=check_in_date,
            checkOut=check_out_date,
            firstName=data["firstName"],
            lastName=data["lastName"],
            roomId=data["roomId"]
        )
        if get_order(new_order):
            return Response(status=409)
        order_id = add_order(new_order)
        return jsonify({"roomId": order_id}), 201

@app.route('/room-add', methods=['POST'])
def add_new_room():
    if request.method == "POST":
        data = request.get_json()
        new_room = Room(
            id=None,
            floor=data["floor"],
            beds=data["beds"],
            guestNum=data["guestNum"],
            price=data["price"]
        )
        insert_room_to_bd(new_room)
        return jsonify({"id": new_room.id}), 201

if __name__ == '__main__':
    init_db()
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True, host='localhost', port=5000)
