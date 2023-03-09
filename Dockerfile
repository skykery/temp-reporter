FROM python:3.8-alpine
ADD src/requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
ADD src/ /
CMD ["python", "main.py"]