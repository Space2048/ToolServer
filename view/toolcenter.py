from flask import Blueprint
from flask import Response, request, abort
from flask import jsonify
from loguru import logger
from utils import globalvb as gv

toolcenter = Blueprint("toolcenter", __name__)

@toolcenter.route(rule='/token', methods=["POST"])
def getToken():
    print("[REQUEST] " + request.path)
    passd = request.json.get("psd")
    
    return Response("Test", status=200)

#登录
@toolcenter.router(rule="/login", methods=["POST"])
def login():
    return

#获取ip
@toocenter.router(rule="/icanlink", methods=["POST"])
def getAreaIp():

    return
#def get
