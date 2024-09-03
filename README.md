# FastAPI Cron Job API

Hello! My name is Agustín, and I created this project to learn FastAPI and FastAPI 😄 .

## Setup

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```

## Endpoints

- `POST /cronjobs/`: Create a new cron job.
- `GET /cronjobs/`: Retrieve a list of cron jobs.
- `DELETE /cronjobs/{cronjob_id}`: Delete a cron job by ID.

## Running Tests

To run the tests, use:

```bash
pytest
```
