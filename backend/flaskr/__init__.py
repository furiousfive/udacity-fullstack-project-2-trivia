from flaskr.config import configure_app
from flask import Flask, jsonify
from flask_cors import CORS
from flaskr.trivia import trivia
from flaskr.models import setup_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    configure_app(app)
    setup_db(app)
    CORS(app)
    app.register_blueprint(trivia)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    return app
