from app import create_app
from flask import render_template

app = create_app('config')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
