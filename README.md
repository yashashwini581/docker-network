When you run multiple containers (whether with Docker Compose or manually), they often need to communicate with each other — like:
a backend container talking to a database container
a frontend container calling an API container

This is where Docker networks come into play. Container networking refers to the ability for containers to connect to and communicate with each other, or to non-Docker workloads.
Containers have networking enabled by default, and they can make outgoing connections. A container has no information about what kind of network it's attached to, or whether their peers are also Docker workloads or not. A container only sees a network interface with an IP address, a gateway, a routing table, DNS services, and other networking details. That is, unless the container uses the none network driver.

Here in this project: I connected multiple containers using a custom bridge network, so they could communicate by container names instead of IPs. This is cleaner, avoids hardcoding IPs, and is exactly how you’d run multi-service apps locally.
