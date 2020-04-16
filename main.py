import json
import pymongo
import requests
from config import api_key

from flask import Flask, jsonify

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the 'classDB' database in Mongo
db = client.CarPopularity

dropdownSelection = web.input()
print (dropdownSelection.Year)

#API Endpoint for Car Data
newNationalApi = f"https://marketcheck-prod.apigee.net/v2/popular/cars?api_key={api_key}&car_type=new"
usedNationalApi = f"https://marketcheck-prod.apigee.net/v2/popular/cars?api_key={api_key}&car_type=used"
caStateApi = f"https://marketcheck-prod.apigee.net/v2/popular/cars?api_key={api_key}&car_type=new&state=CA"
nyStateApi = f"https://marketcheck-prod.apigee.net/v2/popular/cars?api_key={api_key}&car_type=new&state=NY"
kiaCarApi = f"https://marketcheck-prod.apigee.net/v2/search/car/active?api_key={api_key}&car_type=new&year=2019,2018,2017,2016,2015,2014&make=kia&model=rio"
chevyCarApi = f"https://marketcheck-prod.apigee.net/v2/search/car/active?api_key={api_key}&car_type=new&year=2019,2018,2017,2016,2015,2014&make=chevrolet&model=cruze"
hondaCarApi = f"https://marketcheck-prod.apigee.net/v2/search/car/active?api_key={api_key}&car_type=new&year=2019,2018,2017,2016,2015,2014&make=honda&make=accord"
toyotaCarApi = f"https://marketcheck-prod.apigee.net/v2/search/car/active?api_key={api_key}&car_type=new&year=2019,2018,2017,2016,2015,2014&make=toyota&model=camry"
lexusCarApi = f"https://marketcheck-prod.apigee.net/v2/search/car/active?api_key={api_key}&car_type=new&year=2019,2018,2017,2016,2015,2014&make=lexus&model=es"
mercedesCarApi = f"https://marketcheck-prod.apigee.net/v2/search/car/active?api_key={api_key}&car_type=new&year=2019,2018,2017,2016,2015,2014&make=mercedes-benz&make=c-class"

#Convert JSON
newResponse = requests.get(newNationalApi).json()
usedResponse = requests.get(usedNationalApi).json()
caResponse = requests.get(caStateApi).json()
nyResponse = requests.get(nyStateApi).json()
kiaResponse = requests.get(kiaCarApi).json()
chevyResponse = requests.get(chevyCarApi).json()
hondaResponse = requests.get(hondaCarApi).json()
toyotaResponse = requests.get(toyotaCarApi).json()
lexusResponse = requests.get(lexusCarApi).json()
mercadesResponse = requests.get(mercedesCarApi).json()

#Send to Mongo
newCollection = db.NationalNewCars
usedCollection = db.NationalUsedCars
caCollection = db.StateCaliforniaCars
nyCollection = db.StateNewYorkCars
kiaCollection = db.SalesKia
chevyCollection = db.SalesChevy
hondaCollection = db.SalesHonda
toyotaCollection = db.SalesToyota
lexusCollection = db.SalesLexus
mercedesCollection = db.SalesMercedes

newCollection.insert_many(newResponse)
usedCollection.insert_many(usedResponse)
caCollection.insert_many(caResponse)
nyCollection.insert_many(nyResponse)
kiaCollection.insert_many(kiaResponse)
chevyCollection.insert_many(chevyResponse)
hondaCollection.insert_many(hondaResponse)
toyotaCollection.insert_many(toyotaResponse)
lexusCollection.insert_many(lexusResponse)
mercedesCollection.insert_many(mercadesResponse)

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/2019<br/>"
        f"/api/v1.0/2018<br/>"
        f"/api/v1.0/2017<br/>"
        f"/api/v1.0/2016<br/>"
        f"/api/v1.0/2015<br/>"
        f"/api/v1.0/2014"
    )


@app.route("/")
def get():
   

@app.route("/api/v1.0/2019")
def 2019():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    
    results = session.query(kiaCollection.year).2019()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/2018")
def 2018():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(kiaCollection.year).2018()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

    @app.route("/api/v1.0/2017")
def 2017():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(kiaCollection.year).2017()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

    @app.route("/api/v1.0/2016")
def 2016():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(kiaCollection.year).2016()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

    @app.route("/api/v1.0/2015")
def 2015():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(kiaCollection.year).2015()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

    @app.route("/api/v1.0/2014")
def 2014():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(kiaCollection.year).2014()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)