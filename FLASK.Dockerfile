FROM python:alpine3.18

RUN adduser -D abhinav
USER abhinav

WORKDIR /home/abhinav

COPY requirements.txt ./requirements.txt
COPY src ./src

RUN python3 -m venv .venv

RUN source .venv/bin/activate && pip install -r ./requirements.txt

CMD [".venv/bin/flask", "--app", "src/app", "run", "--port", "5001", "--host=0.0.0.0", "--debug"]