# What does FetchType.LAZY imply in Hibernate?

`FetchType.LAZY` in Hibernate controls **when** related data gets loaded from the database.

---

**The two fetch types:**

|             | `FetchType.LAZY`   | `FetchType.EAGER`       |
| ----------- | ------------------ | ----------------------- |
| Loads data  | Only when accessed | Immediately with parent |
| DB queries  | On demand          | Always, even if unused  |
| Performance | Generally better   | Can be wasteful         |

---

**What LAZY means:**
When you load an entity, Hibernate **skips loading its relationships** right away. It only fetches them from the database the moment your code actually accesses them.

```java
@OneToMany(fetch = FetchType.LAZY)
private List<Order> orders;
```

```java
Customer customer = session.get(Customer.class, 1);
// At this point, "orders" is NOT loaded yet — just a proxy

customer.getOrders();
// NOW Hibernate fires a query to fetch the orders
```

---

**Why use LAZY?**

- **Performance** — avoids loading large or unnecessary data you might never use
- **Memory efficiency** — doesn't pull entire object graphs into memory
- **Common default** — `@OneToMany` and `@ManyToMany` are LAZY by default in Hibernate

---

**The classic pitfall — LazyInitializationException:**
If you try to access a LAZY field **after the Hibernate session is closed**, you'll get this error:

```java
session.close();
customer.getOrders(); // 💥 LazyInitializationException!
```

To avoid this, make sure you either:

- Access lazy fields **within an active session/transaction**
- Use `JOIN FETCH` in your query to load them eagerly when needed
- Or annotate the method with `@Transactional` in Spring

---

**The bottom line:** `FetchType.LAZY` is a performance optimization that says _"don't load this until I actually need it."_ It's the preferred default for collections, but you need to be mindful of session scope.
