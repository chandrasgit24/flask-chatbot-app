from flask import Flask, render_template, request
import chatbot_logic

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    response = ""
    if request.method == "POST":
        message = request.form["message"]
        response = chatbot_logic.get_response(message)
    return render_template("index.html", message=message, response=response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
