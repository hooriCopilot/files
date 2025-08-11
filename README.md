# Quiz-to-Career Backend

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API

- POST `/quiz/submit`  
  Body: `{0: "2", 1: "1", ...}`  
  Returns: Top 5 careers, each with title, description, match, skills, and resources.