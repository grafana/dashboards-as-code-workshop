FROM golang:1.23-alpine AS build

WORKDIR /app

COPY . .
RUN go mod download

RUN go build -o app

FROM alpine:3.23@sha256:865b95f46d98cf867a156fe4a135ad3fe50d2056aa3f25ed31662dff6da4eb62 AS release

WORKDIR /

# Create log directory and set permissions before switching to nonroot user
RUN mkdir -p /tmp/app-logs && \
    chown -R nobody:nobody /tmp/app-logs && \
    chmod 777 /tmp/app-logs

COPY --from=build /app/app /app

EXPOSE 8080

USER nobody:nobody

ENTRYPOINT ["/app"]