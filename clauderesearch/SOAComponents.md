# What are SOA Components?

SOA (Service-Oriented Architecture) is an architectural style where software is structured as a collection of interoperable services. Here are its core components:

## Services

The fundamental building blocks. Each service is a self-contained unit of functionality (e.g., "PaymentService", "AuthService") that exposes a well-defined interface and can be called over a network.

## Service Provider

The entity that creates, maintains, and hosts a service. It defines the service contract (what the service does and how to call it) and publishes it for consumers to discover.

## Service Consumer (Client)

The application or service that invokes another service. It binds to the service using the published contract and sends requests to it.

## Service Registry / Repository

A directory where service providers publish their service descriptions and where consumers can discover available services. The classic example is UDDI (Universal Description, Discovery, and Integration).

## Service Contract

Defines the interface of a service — what operations it exposes, what inputs/outputs it expects, and any usage policies. Commonly expressed as a WSDL (Web Services Description Language) document or an OpenAPI spec in REST-based SOA.

## Enterprise Service Bus (ESB)

The communication backbone that routes messages between services. It handles:

- Message transformation (converting formats between services)
- Protocol mediation
- Routing and orchestration
- Load balancing and error handling

## Service Orchestration & Choreography

- **Orchestration** — a central coordinator (often a BPEL engine) directs services in a workflow, telling each one what to do and when.
- **Choreography** — services coordinate themselves by reacting to events, with no central controller.

## Message / Data Layer

Defines how data is exchanged between services — typically XML or JSON payloads over protocols like SOAP (over HTTP) or REST.

---

### Quick Summary Table

| Component     | Role                                |
| ------------- | ----------------------------------- |
| Service       | Unit of business functionality      |
| Provider      | Hosts and exposes the service       |
| Consumer      | Calls the service                   |
| Registry      | Discover/publish services           |
| Contract      | Defines interface/protocol          |
| ESB           | Routes and mediates messages        |
| Orchestration | Coordinates multi-service workflows |

SOA principles emphasize **loose coupling**, **reusability**, **abstraction**, and **interoperability** — making it the conceptual predecessor to modern microservices architecture.
