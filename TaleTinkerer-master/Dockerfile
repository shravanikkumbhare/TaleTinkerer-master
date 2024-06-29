
FROM python:3.9.13

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001

ENV NAME TaleTinkerer

CMD ["python3", "run.py"]