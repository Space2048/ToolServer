from flask import Blueprint
from flask import Response, request, abort

toolcenter = Blueprint("toolcenter", __name__)

@toolcenter.route(rule='/token', methods=["POST"])
def getToken():
    print("[REQUEST] " + request.path)
    return Response("Test", status=200)
