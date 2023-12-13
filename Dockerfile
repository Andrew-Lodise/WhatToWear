FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN pip install requests_html
CMD ["python", "main.py"]