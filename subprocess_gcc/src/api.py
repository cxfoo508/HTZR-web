import json
import os

import flask
import yaml
from flask_cors import CORS

import cfg2C

# 导入Flask模块
# 创建Flask的实例对象
app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/api/hello', methods=["GET"])
def hello():
    return {"msg": 'Hello World!', "status": 200}


@app.route('/api/uploadcfg/<u_id>', methods=["POST"])
def upload(u_id):
    if len(u_id) <= 0:
        u_id = "default"
    data = json.loads(flask.request.get_data())
    yamlObj = cfg2C.json2Yaml(data)
    # store yaml object
    fileOut = open("rsc/configs_repo/{}.yml".format(u_id), "w", encoding="utf-8")
    fileOut.write(yaml.dump(yamlObj, default_flow_style=False, Dumper=yaml.Dumper))
    fileOut.close()
    # generate cFiles from yaml
    tCaseList = cfg2C.yaml2TCase(yamlObj)
    for tCase in tCaseList:
        cfg2C.toCCase(tCase, tCase.name)
    # gen maintest.c
    path0 = "../out/" + u_id
    if os.path.exists(path0):
        os.removedirs(path0)
    os.mkdir(path0)

    return {"msg": {"upload": "ok"}, "status": 200}


@app.route('/user/<u_id>')
def user_info(u_id):
    return {
        "msg": "success",
        "data": {
            "id": u_id,
            "username": 'ye13',
            "age": 18
        }
    }


@app.route("/downld/configs/<path:filename>")
def downloaderConfigs(filename):
    dir_path = "../rsc/configs_repo"
    try:
        return flask.send_from_directory(dir_path, filename, as_attachment=True)
    except Exception as e:
        print(e)
        return "文件路径出错或文件不存在"


@app.route("/downld/cfiles/<uid>")
def downloaderCfiles(uid):
    dir_path = "../out"
    filename = str(uid) + ".zip"
    print("try to download file: {}/{}".format(dir_path, filename))
    try:
        return flask.send_from_directory(dir_path, filename, as_attachment=True)
    except Exception as e:
        print(e)
        return "文件路径出错或文件不存在"


if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
