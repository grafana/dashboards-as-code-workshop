FROM golang:1.27-alpine@sha256:eb61c3873c97416fff0116553fff65d67a3549f72e11d9758849a689cdd8b523 AS build

WORKDIR /app

COPY . .
RUN go mod download

RUN go build -o app

FROM alpine:3.19 AS release

WORKDIR /

COPY --from=build /app/app /app

EXPOSE 8080

USER nonroot:nonroot

ENTRYPOINT ["/app"]
