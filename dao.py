import flask
from flask.json import jsonify
from pip.utils import outdated
from flask.globals import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


tpe = {
        "id":"0",
        "city_name":"Taipei",
        "country_name":"Taiwan",
        "is_capital":True,
        "location":{
            "longitude":121.569649,            
            "latitude":25.036786
        }
}

nyc = {
        "id":"1",
        "city_name":"New York",
        "country_name":"United States",
        "is_capital":False,
        "location":{
            "longitude":-74.004364,            
            "latitude":40.710045
        }
}

ldn = {
    "id": 2,
    "city_name": "London",
    "country_name": "United Kingdom",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}

cities = [tpe , nyc , ldn]


@app.route('/' , methods=['GET'])
def home():
    return "<h1>Hello Flask</h1>"

@app.route('/cities_all' , methods=['GET'])
def cities_all():
    return jsonify(cities) 

@app.route('/cities' , methods=['GET'])
def city_name():
    if 'city_name' in request.args:
        city_name = request.args['city_name']
    else:
        return "Error : no city_name provided. please specify a city_name."
    
    res = []
    
    for city in cities:
        if city['city_name'] == city_name:
            res.append(city)
    return jsonify(res)            


app.run()
