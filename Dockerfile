FROM golang:1.20-alpine

WORKDIR /app

COPY go.mod .
RUN go mod download

COPY . .

RUN go build -o ./bin/breezedb .

EXPOSE $PORT

CMD "bin/breezedb" $PORT

