FROM python:3.9-slim
RUN apt-get update && apt-get install -y nginx
COPY nginx.conf /etc/nginx/sites-available/default
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install tensorflow
COPY . .
EXPOSE 80
CMD service nginx start && python app.py
