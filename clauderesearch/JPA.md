# What is JPA?

JPA stands for **Java Persistence API**.

It's a specification in Java that defines how to map Java objects to relational database tables — a concept called **ORM (Object-Relational Mapping)**. Rather than writing raw SQL, you work with plain Java objects (called **entities**), and JPA handles the database communication for you.

Key concepts in JPA:

- **Entity** — a Java class annotated with `@Entity` that maps to a database table
- **EntityManager** — the main interface for performing database operations (persist, find, remove, etc.)
- **JPQL** — Java Persistence Query Language, a SQL-like query language that works with entity objects instead of tables
- **Repository** — a higher-level abstraction (common in Spring Data JPA) that provides ready-made CRUD methods

A simple example of a JPA entity:

```java
@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private String email;

    // getters and setters
}
```

**Important distinction:** JPA is just a _specification_ (a set of rules/interfaces). The actual implementations are separate libraries, the most popular being:

- **Hibernate** (by far the most widely used)
- EclipseLink
- OpenJPA

In practice, most Java developers use JPA through **Spring Data JPA**, which sits on top of Hibernate and makes database access even simpler by auto-generating queries from method names like `findByEmail(String email)`.
