FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN pip install requests
#CMD ["python", "TextingTutorial.py"]
CMD ["python", "main.py"]