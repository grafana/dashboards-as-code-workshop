# Hands-on lab — Grafana as code: Build and deploy your dashboards at scale

## Running the code

```shell
gradle run 
```

It will generate a single dashboard and print its representation to stdout.
This mode is meant for development, to be used alongside `grafanactl`:

```shell
grafanactl resources serve --script 'gradle run -q' --watch .
```

## Where should I start?

The [`Main.java`](./src/main/java/lab/Main.java) file is the entrypoint both for the development and
deployment *modes*.

The [`Overview.java`](./src/main/java/lab/Overview.java) file defines a `Overview.forService()`
method that will be called to generate the dashboard.

The [`Common.java`](./src/main/java/lab/Common.java) file is where "base functions" for each panel type should be defined.

> [!TIP]
> It is highly recommended that every panel created for your dashboard use one
> of these utility functions.

## Deploying the dashboards

```shell
gradle run --args="--manifests"
```

This will generate a YAML manifest for the test dashboard.
The manifest is written under `./resources/` by default and can be deployed
from the CLI:

```shell
grafanactl resources push
```
