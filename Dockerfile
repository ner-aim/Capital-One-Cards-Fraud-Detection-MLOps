FROM frolvlad/alpine-python-machinelearning:latest

COPY . /app
WORKDIR /app
EXPOSE 3840

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","app.py"]