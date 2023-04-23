# UFO Spotter

#### Description:
This is full-stack web application built with Python, Flask, and MongoDB Atlas along with HTML (with the help of Bootstrap) and CSS as markup languages. This app allows you to look up UFO sightings in your area in the U.S. based on a [publicly available dataset](https://www.kaggle.com/datasets/NUFORC/ufo-sightings) loaded to Atlas. You can also submit a UFO sighting of your own to the database so others can be aware of your sighting in their area. To use this application code you will need to upload the dataset to your own free Atlas database and input your Atlas connection string in the app.py and helpers.py files. 

#### Dependencies
* The web program is written in Python 3 with the Flask framework.
* Some code depends on the Flask library:
    * app.py
    * helpers.py
* Some code depends on the requests library:
    * app.py
    * helpers.py
* Some code depends on Python re library:
    * app.py
* Some code depends on the Python date library:
    * app.py
* Some code depends on the pymongo library:
    * app.py
    * helpers.py
* HTML and CSS are used as markup langauges.

Create a virtual environment for your code with: python -m venv .venv; ./.venv/bin/activate; pip install -r requirements.txt; python app.py

#### Files

#### HTML and CSS Files

| File | Description|
| --- | --- |
|main.css| This file includes the basic styling for classes used across different html files. 
|city.html| Displays a form for the user to submit a U.S. city and state and get statistics on UFO sightings in the area as well as the 10 most recent sightings in the database. |
|error.html| Displays a message to the user if they have input information in an incorrect format (with special characters in a city name, for example). |
|layout.html| An html template page that is used throughout the other html pages with Jinja. Provides the content for the navbar. |
|results.html| Based on the city and state submitted by the user in city.html, this page displays the total number of UFO sightings in that state and in that city as well as a list of the UFO sightings available. |
|submit.html| Displays a form that allows the users to submit a report of a UFO sighting to the MongoDB Atlas database at the backend of the application. |
|thank_you.html| Displays a cheeky thank-you message to the user after they submit a report of a UFO sighting. |

#### Python Files

| File | Description|
| --- | --- |
|app.py| This file connects to the MongoDB Atlas database and contains two functions. The city() function handles both GET and POST requests. A GET request to this function displays the city.html page and allows the user to enter their city and state via a form. A POST request takes that information submitted by the user and then calls other functions to get the number of UFO sightings in that state, the number of UFO sightings in that city in that state, and a list of the UFO sightings in that city and state available in the database. The second core function in this file, submit(), also handles GET and POST requests. A GET request to this page displays a form where a user can submit the details of a UFO sighting. A POST request then takes that information, combines the objects submitted into a Python dictionary, and submits that dictionary as a JSON document to be stored in the MongoDB Atlas database for future users to look up for that region. |
|helpers.py| This file connects to the MongoDB Atlas database and contains two helper functions. One counts the number of UFO sightings for the city and state submitted by the user using the MongoDB Query API. The other looks up documents for the UFO sightings for that city and state, also using MongoDB Query API syntax. |
