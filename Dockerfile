FROM python:3
LABEL version=20200622
WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get install -y git gcc python3-dev
RUN pip install --no-cache-dir gunicorn git+https://github.com/hcvst/ttsapi#egg=ttsapi
EXPOSE 8000
CMD ["gunicorn", "-w 3", "-b 0.0.0.0", "ttsapi:app"]
