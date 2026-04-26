# What might the Docker client-server architecture provide?

The Docker client-server architecture provides several key benefits:

1. **Separation of concerns** — the client handles user interaction while the daemon handles all the complex work of managing containers, images, and resources. Each component does what it's best at.

2. **Remote management** — because the client and daemon communicate via a REST API, they don't have to be on the same machine. You can point your Docker client at a remote daemon to manage containers on another host.

3. **Flexibility** — multiple clients can talk to the same daemon, and the same client can switch between different daemons. Tools like Docker Compose and Docker Desktop are all just clients under the hood.

4. **Scalability** — the daemon can manage many containers simultaneously without the client needing to be involved. You fire off a command and the daemon handles the rest.

5. **Security control** — access to the daemon can be controlled and restricted, so not every user or process on a machine can interact with Docker freely.

6. **Extensibility** — because the interface is API-based, third-party tools and platforms (like CI/CD pipelines or orchestration tools) can integrate with Docker without needing to replicate its internals.

In short, the client-server model gives Docker a clean, flexible, and powerful way to separate the _instruction_ side from the _execution_ side.

## Three Parts of the Docker Technology

Docker's underlying architecture is built on three core Linux kernel concepts:

1. **Namespaces** — provide isolation by giving each container its own view of the system. This includes its own process tree, network stack, user IDs, filesystem mount points, and more. Containers can't see or interfere with each other's namespaces.

2. **Control Groups (cgroups)** — control and limit the resources a container can use, such as CPU, memory, disk I/O, and network bandwidth. This prevents any single container from monopolizing the host's resources.

3. **Union File Systems (UnionFS)** — allow Docker images to be built in **layers**. Each instruction in a Dockerfile adds a new layer on top of the previous one, and these layers are shared and reused across images. This makes images lightweight and efficient to store and transfer. Common implementations include OverlayFS and AUFS.

Together, these three primitives are what make containers possible — **namespaces** give isolation, **cgroups** give resource control, and **UnionFS** gives efficient layered storage. Docker essentially packages these Linux kernel features into a developer-friendly interface.
