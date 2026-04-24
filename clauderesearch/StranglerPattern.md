# What is the Strangler Pattern?

The **Strangler Fig Pattern** is a migration strategy used to incrementally replace a legacy system with a new one, without doing a risky "big bang" rewrite.

## The Analogy

The name comes from the strangler fig tree, which grows around a host tree, gradually replacing it until the original tree is gone — and the new tree stands on its own.

## Core Purpose

To **safely migrate a monolithic or legacy system to a modern architecture** (like microservices) piece by piece, while keeping the system live and functional throughout the transition.

## How It Works

1. **Intercept** — Place a proxy/facade (often an API Gateway) in front of the legacy system that routes all traffic
2. **Migrate** — Gradually extract individual features or domains into new services
3. **Redirect** — Route traffic for the migrated functionality to the new service instead of the legacy system
4. **Retire** — Once all functionality is migrated, decommission the legacy system entirely

## Why It's Used

- **Zero downtime migration** — the old system keeps running while the new one is built alongside it
- **Reduced risk** — you migrate incrementally, so failures are isolated and reversible
- **Continuous delivery** — new features can be added to the new system while migration is ongoing
- **Avoids big rewrites** — full rewrites are notoriously risky and expensive

## Real-World Relevance

This pattern is extremely common when companies move from a **monolith to microservices** — which aligns directly with SOA and microservice modernization work, like the kind of legacy system migration you worked on at Macy's.
