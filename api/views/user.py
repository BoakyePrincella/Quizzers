from flask import Flask,render_template, request, url_for, Blueprint

user_blueprint = Blueprint('user_bp', __name__, template_folder='templates')

@user_blueprint.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@user_blueprint.route('/signup', methods=["POST","GET"])
def signup():
    user_name = "Princy"
    user_password = "1234"

    if request.method == "POST":
        form_data = request.form
        username = form_data.get("user_name")
        password = form_data.get("password")

        if username == user_name and password == user_password:
            return "You're logged in"
        return "Please log in first"
    return render_template("signup.html")