from flask import Flask
import pickle
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/predict/<jml_pekerja>/<jml_sku>/<shelf_total>")
def predict(jml_pekerja,jml_sku,shelf_total):
    data = {"Jml_pekerja" : jml_pekerja,
            "jumlah SKU OTC" : jml_sku,
            "Luas Shelf Total" : shelf_total}
    X = pd.DataFrame(data, index=[0])
    model = pickle.load(open('DT Store Value Grup (16).pkl', 'rb'))
    result = model.predict(X)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)