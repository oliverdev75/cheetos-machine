from app import api
from app.database.models import User
from flask import request

@api.route("/user", methods=['POST'])
def create_user():
    data = request.get_json(force=True)
    print(User.__dict__)