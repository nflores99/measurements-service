FROM python:3.9
RUN mkdir -p /tmp/results
COPY ntw-meas-entrypoint.sh /tmp/ntw-meas-entrypoint.sh
COPY ntw-meas.py /tmp/ntw-meas.py
RUN chmod +x /tmp/ntw-meas-entrypoint.sh

ENTRYPOINT ["/tmp/ntw-meas-entrypoint.sh"]