# Digital Ops home Assingment
A warehouse management system that handles package storage and shipping using trucks with limited cargo space. The system ensures efficient loading by requiring packages to fill at least 80% of a truck's volume before shipment, with optional bin packing algorithms for optimal arrangement.


## Table of Contents
- [Project Description](#project-description)
- [Documentation](#documentation)
- [Installation](#installation)

## Project Description
Implemented a simple flask api server for managing a wharehouse.    

## Documentation
Detailed documentation for **Work Item 1** can be found in the `Docs Work Item 1` directory at the root of this repository.

### implemntation details
1. Decided to use in memory store, instead of connecting to a real DB.    
This would help me to saev time and make sure the code is in a high standrat.   
I used a repostory pattern, so it would be easy to replace from in memory to a real DB connection in the future  

2. its better to use a vlidation Schema in the routes blueprint, using the marshmallow package its suitable over here.  


## Installation

### Local Setup

1. Create a virtual environment:
```bash
python3 -m venv simple-python-server
```

2. Activate the virtual environment:
```bash
# On Linux/macOS
source simple-python-server/bin/activate

# On Windows
my_project_env\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Save installed packages to requirements.txt:
```bash
pip freeze > requirements.txt
```

5. 
To run the server with hot-reloading enabled:
```bash
nvm use
npm i
node_modules/.bin/nodemon --exec python3 main.py 