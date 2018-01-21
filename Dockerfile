FROM python:2.7-alpine
MAINTAINER Your Name

COPY proj/ /proj/proj/
COPY setup.py /proj/
WORKDIR /proj
RUN pip install .

# Create unprivileged user
RUN adduser -H -D -s /bin/false euser \
  && chown -R euser:euser /proj/*
USER euser
