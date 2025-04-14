# Prerequisites

For the purposes of this workshop, an entire stack is provided with:

 * [Grafana](https://grafana.com/grafana/)
 * [Alloy](https://grafana.com/docs/alloy/latest/)
 * [Loki](https://grafana.com/products/cloud/logs/)
 * [Prometheus](https://prometheus.io/)

To run it, you will need [Docker](https://docs.docker.com/engine/) and [Docker Compose](https://docs.docker.com/compose/).

> [!TIP]
> Verify that Docker is ready:
> ```shell
> docker ps
> docker compose ps
> ```

## 🚨 Important: Authenticating to Docker Hub

Before going forward with the prerequisites, and to ensure everyone can go through them,
check that you are authenticated to Docker.

<details>
    <summary><b>For Docker Desktop</b></summary>

> If you are using Docker Desktop, you can sign in to Docker Hub from the Docker Desktop menu.
> Select Sign in / Create Docker ID from the Docker Desktop menu and follow the on-screen instructions to complete the sign-in process.
</details>

<details>
    <summary><b>For Docker Engine</b></summary>

> If you're using a standalone version of Docker Engine, run the `docker login` command from a terminal to authenticate with Docker Hub.
> For information on how to use the command, see [docker login](https://docs.docker.com/reference/cli/docker/login/).
</details>

> [!WARNING]
> Make sure you are logged in to Docker Hub, otherwise we'll trip we'll trip Docker's [pull usage and limits](https://docs.docker.com/docker-hub/usage/pulls/).

## Forking the Lab Repository

In order to ensure you can work with the lab and experiment freely, it is recommended that you [fork this repository](https://github.com/grafana/dashboards-as-code-workshop/fork).

## Working with the Lab Repository (Local)

In order to run the lab locally on your development machine you will need to clone your forked repository:

```shell
git clone https://github.com/<your_username>/dashboards-as-code-workshop
```

Once done, move into the repository directory:

```shell
cd dashboards-as-code-workshop
```

Then start the stack using Docker:

```shell
docker compose -f docker-compose.yaml up --build
```

> [!TIP]
> Verify that the Grafana instance is accessible at [`http://localhost:3003`](http://localhost:3003)
>
> Credentials: `admin` / `admin`

## Working with the Lab Repository (CodeSandbox.io)

If you are unable to run the workshop locally on your machine, you can use [CodeSandbox.io](https://codesandbox.io), a browser-based virtual development environment.

- First, sign up for a free CodeSandbox account and login.

- Once done, click on **Import** at the top right to begin importing the GitHub repository.

- Click on **Find by URL** and enter the URL of your *forked repository*.

- Click on the title of your repository to open it in a new code sandbox environment.

Once you've opened the repository in CodeSandbox, you can start the stack by:

- Clicking on **Create Terminal** undernearth the **Shared Terminals** section in the left side panel.

- In the Terminal that opens, run the following:

```shell
docker compose -f docker-compose.yaml up --build
```

You can verify that Grafana is up and running by clicking **Open Externally** on the popup that appears which says "Port 3003 has been opened".

The rest of the instructions in these docs should work the same within the CodeSandbox.io environment.

## Install Grizzly

[Grizzly](https://grafana.github.io/grizzly/) is a CLI tool used to manage Grafana resources.

Make sure it is installed:

<details>
    <summary><b>For macOS (with Homebrew)</b></summary>

```shell
brew install grizzly
```
</details>

<details>
    <summary><b>For macOS (Apple silicon)</b></summary>

```shell
sudo curl -fSL -o "/usr/local/bin/grr" "https://github.com/grafana/grizzly/releases/download/v0.7.1/grr-darwin-arm64"
sudo chmod +x /usr/local/bin/grr
```
</details>

<details>
    <summary><b>For macOS (Intel chips)</b></summary>

```shell
sudo curl -fSL -o "/usr/local/bin/grr" "https://github.com/grafana/grizzly/releases/download/v0.7.1/grr-darwin-amd64"
sudo chmod +x /usr/local/bin/grr
```
</details>

<details>
    <summary><b>For Linux</b></summary>

```shell
sudo curl -fSL -o "/usr/local/bin/grr" "https://github.com/grafana/grizzly/releases/download/v0.7.1/grr-linux-amd64"
sudo chmod +x /usr/local/bin/grr
```
</details>

> [!TIP]
> Verify that Grizzly is installed and accessible:
> ```shell
> grr --version
> ```

## Configure Grizzly

With Grizzly installed, configure it to connect to the lab's Grafana instance:

```shell
grr config set grafana.url http://localhost:3003
grr config set grafana.user admin
grr config set grafana.token admin
```

> [!TIP]
> Check that Grizzly can indeed connect to the stack:
> ```shell
> grr config check
> ```

## Next steps

[Start the lab!](./part-one.md)
