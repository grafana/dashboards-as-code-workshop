# Hands-on lab: Grafana as code

## Installing dependencies

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the code

```shell
python main.py
```

It will generate a single dashboard, with a hardcoded service configuration.
This mode is meant for development, to be used alongside `grafanactl`:

```shell
grafanactl resources serve --script 'python main.py' --watch .
```

## Where should I start?

The [`main.py`](./main.py) file is the entrypoint both for the development and
deployment *modes*.

The [`./src/dashboard.py`](./src/dashboard.py) file defines a `example_dashboard()`
function that will be called to generate the dashboard.

The [`./src/common.py`](./src/common.py) file is where "base functions" for each panel type should be defined.

> [!TIP]
> It is highly recommended that every panel created for your dashboard use one
> of these utility functions.

## Deploying the dashboards

```shell
python main.py --manifests
```

This will generate a YAML manifest for the test dashboard.
The manifest is written under `./resources/` by default and can be deployed
from the CLI:

```shell
grafanactl resources push
```
