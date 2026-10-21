FROM golang:1.25-alpine@sha256:1ae0735f00daffa3aaf1363a5184c0d2dc55c78e3db4ec70241cdac97bf84b59 AS build

WORKDIR /app

COPY . .
RUN go mod download

RUN go build -o app

FROM alpine:3.19 AS release

WORKDIR /

# Create log directory and set permissions before switching to nonroot user
RUN mkdir -p /tmp/app-logs && \
    chown -R nobody:nobody /tmp/app-logs && \
    chmod 777 /tmp/app-logs

COPY --from=build /app/app /app

EXPOSE 8080

USER nobody:nobody

ENTRYPOINT ["/app"]