FROM golang:1.19.3
RUN go install github.com/heistp/irtt/cmd/irtt@latest

ENTRYPOINT ["irtt", "client -i 1s -d 1m -l 172 --fill=rand --sfill=rand -o irtt_data.json localhost"]
