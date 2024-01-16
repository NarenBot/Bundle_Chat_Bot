echo [$(date)]: "START"
echo [$(date)]: "Creating Conda Env. With Python 3.10..." # Change the version based on the project.
conda create --prefix venv python==3.10 -y
echo [$(date)]: "Activating Virtual Environment..."
source activate venv/
echo [$(date)]: "Installing Requirements..."
pip install -r requirements.txt
echo [$(date)]: "END"
