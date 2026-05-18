# What are Test Containers in Java?

A **test container** in Java refers to two related concepts:

## 1. Testcontainers (the library)

**Testcontainers** is a popular Java library that provides lightweight, throwaway instances of real services (databases, message brokers, etc.) running in **Docker containers** during tests.

```java
@Testcontainers
class MyDatabaseTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
            .withDatabaseName("testdb")
            .withUsername("user")
            .withPassword("password");

    @Test
    void testDatabaseQuery() {
        String jdbcUrl = postgres.getJdbcUrl();
        // Connect and run your test against a real Postgres instance
    }
}
```

**Common use cases:**

- PostgreSQL, MySQL, MongoDB for integration tests
- Kafka or RabbitMQ for messaging tests
- Redis for caching tests
- Any service with a Docker image

---

## 2. A Generic "Test Container" Pattern

More broadly, a _test container_ can mean any **wrapper class or setup** that bootstraps an application context for testing — for example, a Spring Boot test slice:

```java
@SpringBootTest
@ActiveProfiles("test")
class MyServiceIntegrationTest {

    @Autowired
    private MyService myService;

    @Test
    void shouldReturnExpectedResult() {
        var result = myService.doSomething();
        assertThat(result).isNotNull();
    }
}
```

---

## Key Differences

| | Testcontainers | Spring Test Context |

|---|---|---|
| **Runs Docker?** | Yes | No |
| **Tests against** | Real external services | Application beans |
| **Speed** | Slower (container startup) | Faster |
| **Best for** | DB/infra integration tests | Service/component tests |

---

## Getting Started with Testcontainers

Add to your `pom.xml`:

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.19.0</version>
    <scope>test</scope>
</dependency>
```

The Testcontainers library is the most common meaning of "test container" in modern Java development, especially for **integration testing** where you need real infrastructure without mocking.
