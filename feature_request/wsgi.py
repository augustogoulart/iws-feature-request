from flask_migrate import Migrate

from feature_request.app import create_app
from feature_request.models import db

app = create_app('feature_request.config')

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
