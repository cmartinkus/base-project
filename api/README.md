logic is as follows:
HTTP
↓
Endpoint "I received a request."
- HTTP requests/responses
- Authentication/authorization checks
- Input validation
- HTTP status codes
↓
Service "What should happen?"
- Business rules
- Workflow/orchestration
- Calls repositories
- Calls external services
- Starts transactions if needed
↓
Repository "How do I read/write the database?"
- SQLAlchemy
- SQL queries
- CRUD operations
- Nothing else
↓
Database

The endpoint should just call services; it should have no business logic.
The service has all the business logic.
The repository should be where all the sql lives.

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
