# Flask-CRUD-Application
# Flask-Application-for-CRUD-operations-on-MongoDB
develop a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. The REST API endpoints should be accessible via HTTP requests and tested using Postman.

## Requirements
The application should be developed using Flask and the PyMongo library for MongoDB.The application should provide REST API endpoints for CRUD operations on a User resource.
The User resource should have the following fields:

id (a unique identifier for the user)

name (the name of the user)

email (the email address of the user)

password (the password of the user)

The application should connect to a MongoDB database.

The application should provide the following REST API endpoints:

GET /users - Returns a list of all users.


GET /users/<id> - Returns the user with the specified ID.

POST /users - Creates a new user with the specified data.

PUT /users/<id> - Updates the user with the specified ID with the new data.


DELETE /users/<id> - Deletes the user with the specified ID.

## Setup
Create a new Python virtual environment and activate it.

Install Flask and PyMongo libraries using pip.

Install Postman for testing the REST API endpoints.

Create a new MongoDB database and collection for the application.
## Implementation
Open the app.py file in your code editor.

Import the necessary libraries: Flask, PyMongo, and jsonify.

Create a new Flask application instance.

Set the MongoDB URI and database name in the Flask application configuration.

Create a new PyMongo client and database instance.

Create the necessary routes and functions for the REST API endpoints.

Run the Flask application using the flask run command.



Using Docker is mandatory
## Testing
Open Postman and create a new HTTP request for each of the REST API endpoints.

Send requests to the endpoints to test the CRUD operations on the User resource.

Verify that the responses are correct and the database is being updated correctly.

