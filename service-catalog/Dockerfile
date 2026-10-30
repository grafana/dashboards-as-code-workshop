FROM golang:1.27-alpine@sha256:d200d2dd76b03a99b52651fd1325aff7dcd35422c35c01bac56571b0507f3deb AS build

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
