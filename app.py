from flask import Flask, jsonify,request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["ALLOWED_EXTENSIONS"] = set(['png', 'jpg', 'jpeg'])

@app.route("/")
def index():
    return jsonify({
        "status": {
            "code": 200,
            "message": "Sucess fetching the API",
        },
        "data": None
    }), 200

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        image = request.files["image"]
        if image:
            pass
        else:
            return jsonify({
                "status" : {
                    "code": 400,
                    "message": "Client side error"
                },
                "data": None
            }), 400
    else:
        return jsonify({
            "status": {
                "code": 405,
                "message": "Method not allowed",
            },
            "data": None,
        }), 405

if __name__ == "__main__":
    app.run()
