from flask import Flask, render_template

from .models import db
from .views import api_bp


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    @app.route('/')
    def _render_template():
        return render_template('feature_request.html')

    db.init_app(app)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
