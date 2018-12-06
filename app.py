from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
	return jsonify({"1":"https://ibb.co/QkHBt2F","2":"https://ibb.co/JCWGMK6","3":"https://ibb.co/JCWGMK6","4":"https://ibb.co/SBnCLS0","5":"https://ibb.co/2WdZ9tG","6":"https://ibb.co/BTrRb19"})

if __name__ == '__main__':
	app.run(debug=True)
