FROM golang:1.23-alpine@sha256:383395b794dffa5b53012a212365d40c8e37109a626ca30d6151c8348d380b5f AS build

WORKDIR /app

COPY . .
RUN go mod download

RUN go build -o app

FROM alpine:3.19@sha256:6baf43584bcb78f2e5847d1de515f23499913ac9f12bdf834811a3145eb11ca1 AS release

WORKDIR /

COPY --from=build /app/app /app

EXPOSE 8080

USER nonroot:nonroot

ENTRYPOINT ["/app"]
