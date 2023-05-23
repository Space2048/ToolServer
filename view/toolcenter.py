from flask import Blueprint
from flask import Response, request, abort
from loguru import logger

toolcenter = Blueprint("toolcenter", __name__)

@toolcenter.route(rule='/token', methods=["POST"])
def getToken():
    print("[REQUEST] " + request.path)
    passd = request.json.get("psd")
    
    return Response("Test", status=200)



#def get
