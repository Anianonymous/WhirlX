FROM python:3.8-slim

RUN apt-get update && apt-get install -y sudo dbus

WORKDIR /app
COPY typewind.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV STREAMLIT_SERVER_ENABLE_TELEMETRY false

CMD ["streamlit", "run", "typewind.py"]