# CMSC 447 Homework 1 Submission
# Youssef Othman, yothman1@umbc.edu
# Professor Nick Allgood
# MW 2:30-3:45 Section
###

##Objective
Use CRUD (Create, Read, Update, Delete) approach to implement a basic database and website.
Implementation consisted of HTML front-end tied to an SQL database with Python function calls being made
to the back end. All these separate components were tied together using Flask. 
Following the CRUD approach user will have the ability to create new entries, view all
existing entries, update entries, or delete entries.

###Files
`/my_flask`: Contains all the other files.
<br>`app.py`: Contains all the python code with is connected to the database and makes all the function calls.
<br>`imports.db`: SQL database that contains all the current users and is edited by myapp.py.
<br>`requirments.txt`: contains pip freeze output, all dependencies needed to run the app.

<br><br>`/templates`: A folder that contains all the HTML files used.
<br>`base.html`: Interface code for any components on multiple pages, ie nav and search bar.
<br>`index.html`: Interface code for the home page, including title and table.
<br>`add.html`: Interface code for add page, asks user for all necessary information to make a new entry.
<br>`update.html`: Interface code for update page, asks user for new value to be updated.
<br>`delete.html`: Interface code for delete page, makes sure user wants to delete entry to avoid accidental deletion.
<br>`search.html`: Interface code for search results, displays all information about the searched entry after a search query is made.

### Requirments
A `requirements.txt` is provided for all the dependencies and app is run by the `app.py` executable. 
A virtual environment is not needed, but recommended.
Once in the `/my_flask` folder, all you need is to run the command: `flask run`.
The address should be: `http://127.0.0.1:5000/`; however it may be different.

###Using the application
Preliminary database is loaded in and displayed on the home page.<br>
Search bar is present on top-right corner, search must be provided with an ID and the ID must be in the database else it will fail.<br>
Update and delete buttons for each entry that redirect you to a page with information about how to proceed, specific to the selected entry.<br>
Home button in the top left redirects you to home page.<br>
Add is listed under actions and prompts you for 3 things: name, ID, and points. Once provided creates a new entry in the database and displays it on the home page.<br>
For adding a new entry: ID *must* be unique, otherwise it will error out.