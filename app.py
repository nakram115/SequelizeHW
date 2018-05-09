from flask import Flask, jsonify
# SQL Alchemy

from sqlalchemy import create_engine, func

from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

import pandas as pd
import numpy as np

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
   
    results = session.query(measurement.prcp).all()

    # Convert list of tuples into normal list
    prep= list(np.ravel(results))

    return jsonify(prep)

@app.route("/api/v1.0/stations")
def stations():
    
    results = session.query(station.station).all()

    # Convert list of tuples into normal list
    stations = list(np.ravel(results))

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    
    results = session.query(measurement.tobs).all()

    # Convert list of tuples into normal list
    tobs = list(np.ravel(results))

    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def start():
    
    results = session.query().all()

    # Convert list of tuples into normal list
    start = list(np.ravel(results))

    return jsonify(start)

@app.route("/api/v1.0/<start>/<end>")
def end():
    
    results = session.query().all()

    # Convert list of tuples into normal list
    start_end = list(np.ravel(results))

    return jsonify(start_end)


@app.route("/jsonified")
def jsonified():
    return jsonify()


if __name__ == "__main__":
    app.run(debug=True)