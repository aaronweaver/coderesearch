echo "Creating the virtual environment"
#create the virtual environment
virtualenv venv

echo "Activating the virtual environment"
#activate virtual environment
. venv/bin/activate

echo
echo "Installing required packages...."

#install the requirements
pip install -r requirements.txt
