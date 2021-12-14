import json
from Station.app_conf import db
from flask import Blueprint, request, Response
from Station.entity import Wagon

wagon = Blueprint('wagon', __name__)


@wagon.route('/wagon/createWagon', methods=['POST'])
def wagon_create():
    number = request.values.get('number', 0, int)
    capacity = request.values.get('capacity', 0, int)
    type = request.values.get('type', '', str)
    wagon = Wagon(number=number, capacity=capacity, type=type)
    db.session.add(wagon)
    db.session.commit()
    return getAnswer({'Wagon': wagon.as_dict()})


@wagon.route('/wagon/edit')
def wagon_edit():
    number = request.values.get('number', 0, int)
    capacity = request.values.get('capacity', 0, int)
    type = request.values.get('type', '', str)
    wagon = Wagon.query.filter_by(number=number).first()
    wagon.number = number
    wagon.capacity = capacity
    wagon.type = type
    db.session.commit()
    wagon = Wagon.query.filter_by(number=number).first()
    return getAnswer({'wagon': wagon})

def getAnswer(text, info=None):
    if info is None:
        info = {}
    res = {
        'status': 'ok',
        'message': text
    }
    answer = {**res, **info}
    return Response(
        response=json.dumps(answer, ensure_ascii=False),
        mimetype='application/json',
        status=200
    )