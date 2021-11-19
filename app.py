# Import dependancies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# prepare the database for a future connection; this allows us to access and query our file
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model (set the foundation to build upon)
Base = automap_base()
# reflect the tables (reflect the schema of SQLite tables into code and create mappings)
Base.prepare(engine, reflect=True)

# Save the references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# Set up Flask
# Create Flask application 
app = Flask(__name__)

# Define the welcome route
@app.route("/")

# add routing info for each of the other routes
# create welcome function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br>
    Available Routes:<br>
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/temp/start/end<br>
    ''')

# add new route and route name for precipitation analysis
@app.route("/api/v1.0/precipitation")

# define route for precipitation      Note: '\ this allows the code to continue onto the next line
# def precipitation():
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#    precipitation = session.query(Measurement.date, Measurement.prcp).\
#    filter(Measurement.date >= prev_year).all() 
#    return

# use jasonify function to format our results in a JSON structured file
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

if __name__ == '__main__':
    app.run()
    
# in the anaconda prompt (from this file directory), type "flask run"   
# then go to the web and look at local webpage: 'localhost5000' or "http://127.0.0.1:5000/api/v1.0/precipitation"
# need to restart flask each time (control c)

# Define route and route name for Stations analysis
@app.route("/api/v1.0/stations")

# define new function for stations
def stations():
    results = session.query(Station.station).all() # create query that allos us to get stations in our database
    stations = list(np.ravel(results))   # unravel result into one-dimensional array and convert results to a list
    return jsonify(stations=stations)   # Jsonify the list and return it as a JSON

# run code here in VS Code
# in the anaconda prompt (from this file directory), restart flask each time (control c), then type "flask run"   
# then go to the web and look at local webpage: 'localhost5000' or "http://127.0.0.1:5000//api/v1.0/stations"

# Define and name route for temperature
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# save and run code here in VS Code
# in the anaconda prompt (from this file directory), restart flask each time (control c), then type "flask run"   
# then go to the web and look at local webpage: 'localhost5000' or "http://127.0.0.1:5000/api/v1.0/tobs"

# Define and name routes for Statistics - need start and end dates
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

# save and run code here in VS Code
# in the anaconda prompt (from this file directory), restart flask each time (control c), then type "flask run"   
# then go to the web and look at local webpage: 'localhost5000' or "http://127.0.0.1:5000/api/v1.0/temp/start/end route"
# the result will be [null,null,null] because i haven't specified dates yet
# I need to change the web address to include dates; example of ending portion of code:  /api/v1.0/temp/2017-06-01/2017-06-30
