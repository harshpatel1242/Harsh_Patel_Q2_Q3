FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install tensorflow
COPY . .
EXPOSE 5000
ENV MODEL_PATH=models/transformers/
CMD ["python3", "app.py"]
