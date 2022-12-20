import re
from datetime import date

from flask import Flask, render_template, request
from pymongo import MongoClient
from helpers import get_count, get_ufos

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

client = MongoClient('mongodb+srv://test:test@cluster0.e6xf1kc.mongodb.net/test')
db = client['ufos']
ufos = db.ufos

# Declare array of U.S. states to use in later functions
states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

@app.route("/", methods=["GET", "POST"])
def city():

    # Let user submit city and state to look up UFO sightings
    if request.method == "GET":

        return render_template("city.html", states=states)

    # Return and display results
    if request.method == "POST":

        # Get city and state from user
        city = request.form.get("city")
        state = request.form.get("state")

        # Define error message
        message = "the name of a valid U.S. city"
        
        # Return error message if user enters number in city name
        if request.form.get("city").isnumeric() is True:
            return render_template("error.html", message=message)

        # Return error message if user enters special character in city name
        # Attribution: Found way to check for special characters with regex here: https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if regex.search(city) is not None:
            message = "the name of a valid U.S. city"
            return render_template("error.html", message=message)
        
        # Convert city and state to lower case
        state = state.lower()

        # Count number of UFO sightings in state
        state_count = ufos.count_documents({"state": state})

        # Get number of UFO sightings in city and state as a list
        city_count = list(get_count(city, state))

        # Get list of recent UFO sightings
        recent_ufos = get_ufos(city, state)

        return render_template("results.html", state_count=state_count, city_count=city_count, recent_ufos=recent_ufos)

@app.route("/submit.html", methods=["GET", "POST"])
def submit():

    # Display form for user to submit report of UFO sighting
    if request.method == "GET":

        return render_template("submit.html", states=states)
   
    # Get data on UFO sighting from form and add to MongoDB
    if request.method == "POST":

        # Create empty Python dictionary to hold UFO report submitted by form
        ufo_report = {}

        # Get UFO report information from user form submission
        # TODO get correct date input from user
        city = request.form.get("city")
        state = request.form.get("state").lower()
        shape = request.form.get("shape")
        duration_seconds = request.form.get("duration_seconds")
        duration_minutes = request.form.get("duration_minutes")
        comments = request.form.get("comments")
        sighting_date = request.form.get("datetime")
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        print(sighting_date)

        # TODO get today's date correctly
        # Get date that user submitted the form
        # Attribution: Found this way to convert time of form submission here: https://www.programiz.com/python-programming/datetime/current-datetime
        today = date.today()
        today = today.strftime("%m/%d/%y")
        print(today)

        # Return error message if user enters number in city name
        if request.form.get("city").isnumeric() is True:
            return render_template("error.html", message=message)

        # Return error message if user enters special character in city name
        # Attribution: Found way to check for special characters with regex here: https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if regex.search(city) is not None:
            message = "the name of a valid U.S. city"
            return render_template("error.html", message=message)

        # Compile report details into Python dictionary
        ufo_report["datetime"] = sighting_date
        ufo_report["city"] = city
        ufo_report["state"] = state
        ufo_report["shape"] = shape
        ufo_report["duration (seconds)"] = duration_seconds
        ufo_report["duration (hours/min)"] = duration_minutes
        ufo_report["comments"] = comments
        ufo_report["country"] = "us"
        ufo_report["date posted"] = today
        ufo_report["latitude"] = latitude
        ufo_report["longitude"] = longitude
        
        # Add UFO sighting report to MongoDB Atlas database
        ufos.insert_one(ufo_report)

        print(ufo_report)

        # Return thank-you message after report submission 
        return render_template("thank_you.html")

