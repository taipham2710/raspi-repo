FROM python:3.13-slim-bullseye

WORKDIR /opt/

COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/*.py .

EXPOSE 8050

CMD ["python", "app.py"]