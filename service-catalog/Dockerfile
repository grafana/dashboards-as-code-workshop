FROM golang:1.23-alpine AS build

WORKDIR /app

COPY . .
RUN go mod download

RUN go build -o app

FROM alpine:3.24@sha256:be2656061b536c1883c4034790e21d0a09c5aaaf51968b89368a3c0371ea2c9a AS release

WORKDIR /

COPY --from=build /app/app /app

EXPOSE 8080

USER nonroot:nonroot

ENTRYPOINT ["/app"]
