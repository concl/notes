Tool for containerizing anything that is run from the command line.

## What does Docker do/ensure?

When programs are run from different machines, sometimes they work and sometimes they don't due to differences in the environment.

Docker solves this by **containerization**, where the program is isolated and provided with its own dependencies, runtime, and filesystem. The environment that Docker builds with the mentioned components is called a **container**.

### Containers

Containers include the following things that ensure that running a program is consistent across machines:

- OS Filesystem: A container comes with a filesystem that can be structured like Ubuntu and Debian
- Language Runtime: The exact version of python or node is included
- App dependencies and libraries: Python libraries (including those installed from pip and node_modules) are included
- System level tools and packages: Packages normally installed by terminal
	- Ex: One system level package is `gcc`
	- Others include but aren't limited to `curl`, `wget`, `ping`, `netcat`, `ffmpeg`, `git`, `postgresql-client`
- Environment Variables and Configs: Default settings, file paths, and internal port configs

Containers do **not** handle the following:
- OS kernel (On windows, the linux kernel is included with WSL)
- Physical Hardware (obviously): Docker containers only request a fraction of resources

## Creating a Docker Container

First we talk about Dockerfiles. Dockerfiles are the blueprint for a Docker image. Then, Docker images can be run, and the runtime is a Docker Container.


## Useful Commands

Cleaning up unused networks:
```
docker network prune -f
```
