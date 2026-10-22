FROM golang:1.23-alpine AS build

WORKDIR /app

COPY . .
RUN go mod download

RUN go build -o app

FROM alpine:3.20@sha256:d9e853e87e55526f6b2917df91a2115c36dd7c696a35be12163d44e6e2a4b6bc AS release

WORKDIR /

COPY --from=build /app/app /app

EXPOSE 8080

USER nonroot:nonroot

ENTRYPOINT ["/app"]
