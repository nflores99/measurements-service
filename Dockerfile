FROM golang:1.19.3
RUN go install github.com/heistp/irtt/cmd/irtt@latest

ENTRYPOINT ["irtt", "server"]
