from flask import Flask, request, send_from_directory, redirect
from zipfile import ZipFile
import subprocess, os, uuid

from threading import Thread
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    # Your code here
    return 'Success!'

PIO_PATH = "/root/.platformio/penv/bin/platformio"
WOKWI_PATH = "/root/bin/wokwi-cli"
@app.route("/play", methods=["POST"])
def submit_code():
     
    print(os.listdir(), os.getcwd())
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return {"error": "Content type not supported!"}
    
    data = request.json
    code = data["code"]

    uu = uuid.uuid1()
    path = f"/tmp/gctf-hardware-{uu}"
    os.mkdir(path)
    with ZipFile("/app/server/project.zip", "r") as z:
        z.extractall(path = path)
    proj_path = os.path.join(path, "project")
    # path will contain project/
    code_path = os.path.join(proj_path, "src", "main.cpp")
    print("code\n", code)
    with open(code_path, "w") as f:
        f.write(code)
    
    subprocess.run([PIO_PATH, "run", "-d", proj_path]) # appropriate build files will be generated.
    wokwi_process = subprocess.run([WOKWI_PATH, proj_path, "--scenario", "fv2.yml", "--timeout", "120000"])

    if wokwi_process.returncode != 0:
        # failed
        print("failed")
        error = wokwi_process.stderr
        return {"error": "Validation failed", "msg": error}
    else:
        with open("/app/server/flag.txt") as f:
            flag = f.read()
        return {"success": True, "flag": flag}


@app.route('/playground/<path:path>')
def static_playground(path):
    return send_from_directory('/app/server/ui/dist', path) 

@app.route("/")
def redirect():
  return redirect("/playground/index.html")

if __name__ == '__main__':
    
    app.run(threaded=True)
    
app.run(threaded=True, port=9989)


