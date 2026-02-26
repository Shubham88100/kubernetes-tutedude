# FROM python:3.12-slim
# WORKDIR /app
# COPY backend/requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY backend/ .
# EXPOSE 5000
# CMD ["python","app.py"]

FROM python:3.12-alpine 
ADD requirements.txt . 
RUN pip install -r requirements.txt 
ADD . /app
WORKDIR /app 
ENTRYPOINT ["python"] 
CMD ["app.py"]