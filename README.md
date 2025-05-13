# simple-python-server
Simple python server


local setup


# Step 1: Create a virtual environment
python3 -m venv simple-python-server

# Step 2: Activate the virtual environment
source simple-python-server/bin/activate  # On Linux/macOS
# my_project_env\Scripts\activate  # On Windows

# Step 3: Install packages
pip install -r requirements.txt

# Step 4: Save installed packages to requirements.txt
pip freeze > requirements.txt


<!-- wath mode, usig nodemon for python -->
node_modules/.bin/nodemon --exec python3 main.py  --ignore fake_fruit.json  