import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
  
Station= Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

session=Session(engine)
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stac tions<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>`<br/>"

    )


@app.route("/api/v1.0/precipitation")
def precipitation():

    Last_day= session.query("SELECT MAX(date) FROM measurement") 

    date_prcp = session.query("SELECT date, prcp FROM measurement")

    session.close()

    Last_list = list(np.ravel(Last_day))

    return jsonify(Last_day)

    

@app.route("/api/v1.0/station`")
def station():
    results = session.query(measurement.station).all()

    session.close()

    prcp_list = list(np.ravel(active_stations))

    return jsonify(prcp_list)

@app.route("/api/v1.0/tobs")
def tobs():
    active_stations = session.query("SELECT DISTINCT station FROM station").first() 

    session.close()

    # Convert list of tuples into normal list
    tobs = list(np.ravel(active_stations))

    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def start():
    active_stations = session.query(Measure.date, Measure.prcp).filter(
        Measure.date > "2016-08-23").all()

    session.close()

    # Convert list of tuples into normal list
    start = list(np.ravel(active_stations))

    return jsonify(start)

@app.route("/api/v1.0/<end>")
def end():
    end_stations = session.query(Measure.date, Measure.prcp).filter(
        Measure.date == "2017-08-23").all()

    session.close()

    # Convert list of tuples into normal list
    tobs = list(np.ravel(end_stations))

    return jsonify(end)



if __name__ == '__main__':
    app.run(debug=True)
