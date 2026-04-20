from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "hello, world"
@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"hola,{nombre}"

@app.route("/app/data")
def api_data():
    data=(
        "name : jonh doe"
        "age:"30
        "city: new york"
    )
    return data


if __name__== "__main__":
    app.run(debug=True)
