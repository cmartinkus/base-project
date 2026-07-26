#run locally
create .env file and fill with appropriate variables
create virtual environment venv
pip install -r requirements.txt
python -m app.main

#run tests
pytest

#run in docker
go to root project (outside of python service)
docker compose up --build -d python-service
