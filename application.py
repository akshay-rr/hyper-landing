from flask import *

application = app = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
	application.run(debug=True, host='0.0.0.0', port=8000)