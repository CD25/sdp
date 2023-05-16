# exam-practise
API and back end for serving exam practise questions.  
## Virtual environment
All commands are from the project root folder unless otherwise specified.  
To create the virtual environement from scratch.  
```
python3 -m venv venv
```
To activate the virtual environment
```
source venv/bin/activate
```
To update the virtual environement
```
pip install -r requirements.txt
```
## Configuration  
All the configurations are there in config.py file located in root folder.  
Add the specified configurations according to the project.  
## To run project  
1. create a .env file in the root directory.  
2. Ensure you have a .env folder in root that reflects example.env 
3. Then run this command in folder exampractise
```
flask run
```  
## Pre-commit
So we don't tear our hair out over formatting we use pre-commit to run black, isort and flake8 over the code base before every commit.
Usage:
1. Create the venv(see above)
2. Run
```
pre-commit install
```
## Running tests
1. Go to this path /exam-practise
2. Run python3 -m pytest or python -m pytest for running all the tests

