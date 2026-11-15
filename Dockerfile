FROM python:3.13-slim
RUN apt-get update
RUN apt-get install -y zip
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "inventory.py", "show"]
