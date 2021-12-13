from flask import Flask
from flask import request
from flask import jsonify
import numpy as np
import pickle

##/.local/bin/jupyter-notebook
##pipenv install scikit-learn==1.0 numpy flask gunicorn
##pipenv run gunicorn --bind 0.0.0.0:9696 predict:app
##sudo docker build -t predict .
##sudo docker run -it --rm --entrypoint=bash predict
##sudo docker run -it --rm -p 9696:9696 predict

def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv = load('dv2.bin')
model = load('model2.bin')

app = Flask('booking')

@app.route('/predict', methods=['POST'])
def predict():
    rest = request.get_json()

    X = dv.transform([rest])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        'book_decision': y_pred,
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

