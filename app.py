from flask import Flask, request, jsonify
import logging

# LOGGING SETTINGS

logging.basicConfig(
	level = logging.INFO,
	format = "%(asctime)s : %(levelname)s -- %(message)s",
	datefmt = "%Y-%m-%d %H:%M:%S",
	filename="requests.log"
)

# FLASK APP

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def base():
	if request.method == 'GET':
		logging.info("LOGGING$$ Received GET Request")
		return "<h1> Hit </h1>"
	elif request.method == 'POST':
		body = request.get_json()
		logging.info(f"LOGGING$$ Received POST Request {body}")
		return jsonify({"code": "1", "message": "Successfully received POST request", "body": body})
	elif request.method == 'DELETE':
		logging.info(f"LOGGING$$ Received DELETE Request")
		return jsonify({"code": "1", "message": "Successfully received DELETE request"})
	elif request.method == 'PUT':
		body = request.get_json()
		logging.info(f"LOGGING$$ Received PUT Request {body}")
		return jsonify({"code": "1", "message": "Successfully received PUT request", "body": body})
	else:
		logging.warning(f"LOGGING$$ Invalid method request {request.method}")
		return "<h1> error </h1>"

if __name__ == "__main__":
    app.run(debug=True)