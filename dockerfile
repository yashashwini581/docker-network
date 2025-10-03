FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN pip install mysql-connector-python
CMD ["python","app.py"]
