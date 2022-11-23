FROM golang:1.19.3
RUN go install github.com/heistp/irtt/cmd/irtt@latest
RUN mkdir -p /tmp/results
COPY client-entrypoint.sh /tmp/client-entrypoint.sh
RUN chmod +x /tmp/client-entrypoint.sh

ENTRYPOINT ["/tmp/client-entrypoint.sh"]
