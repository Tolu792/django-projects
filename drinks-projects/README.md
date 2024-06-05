# Drinks API

## Overview
The Drinks API is a simple API for managing a collection of drinks. It allows you to perform CRUD (Create, Read, Update, Delete) operations on drinks.

## Features
- **GET**: Retrieve a list of drinks or a specific drink by ID.
- **POST**: Add a new drink to the collection.
- **PUT**: Update an existing drink by ID.
- **DELETE**: Remove a drink from the collection by ID.


# **GET**: Get all drinks
http://127.0.0.1:8000/drinks/ - 
The route returns a JSON with the data from all the drinks in the database

# **POST**: Add a drink
http://127.0.0.1:8000/drinks/ - 
**Body**:
{
"name": "Apple Soda",
"description": "Very good"
}

# **PUT**: Update a drink
http://127.0.0.1:8000/drinks/1 -
**Body**:
{
    "id": 1,
    "name": "Grape Soda",
    "description": "Very Grapey"
}

# **DELETE**: Delete a drink
http://127.0.0.1:8000/drinks/2 -
Deletes a drink from the database
