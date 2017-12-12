FROM python:3.6.3
WORKDIR /app
ADD ./ /app
RUN pip install -r requirements.txt
CMD ["python","dbserver.py"]
EXPOSE 8001
