from flask import Flask, render_template, request, url_for

app = Flask(__name__)

from api.views.user import user_blueprint

app.register_blueprint(user_blueprint)


if __name__ == '__main__':
    app.run(debug=True)