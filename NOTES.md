MVT: MVT is an architectural pattern that seperates data structures, request handling, and presentation logic, making them easier to manage, maintain, and scale. 
MODEL: A model is basically a Python class that defines the attributes or fields of data we want to store
VIEW: The View acts like some form of middleman between the user, the model, and the template and it handles the user requests and passes the necessary data onto the template
TEMPLATE: The template is basically what the user sees, a presantation of the information as a webpage.

MIGRATION: A migration is a set of instructions that tell Django what changes to be made to the database. Migrations are part of the source code and can be committed to git so everyone working on the project can have a consistent database structure. If each developer were to edit the database by hand, there would be inconsistencies.

DIFFERENCE BETWEEN A VIEW AND A TEMPLATE: In simple words, a view handles the logic, and requests and decides what to show to the user while a template decides how to show it to the user and how it is displayed. A view handles the python logic and a template handles the html and design.

DEPLOYEMENT: Deploying means taking an application that was developed locally on a computer and making it available for everyone else to use on a server through a web URL. Git was used to clone the GitHub repository on PythonAnywhere to allow the server to get the same project files and version of code developed locally. Using Git makes deployment more organized because changes to the project can be tracked through commits and the server can pull the latest version of the code from the repository.