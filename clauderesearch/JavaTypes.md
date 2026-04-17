# Why Should We Use Typed Generics in Java

Using typed generics like `List<Inventory>` instead of a raw `List` is strongly recommended for several reasons:

**1. Type Safety**
With `List<Inventory>`, the compiler ensures you can only add `Inventory` objects to the list. With a raw `List`, you could accidentally add a `String` or `Integer` — and the compiler won't warn you.

```java
List<Inventory> items = new ArrayList<>();
items.add(new Inventory()); // ✅ fine
items.add("oops");          // ❌ compile-time error — caught early!

List rawList = new ArrayList();
rawList.add(new Inventory()); // ✅
rawList.add("oops");          // ✅ no error — dangerous!
```

**2. No Manual Casting**
When retrieving items from a raw `List`, you have to cast manually, which is ugly and error-prone:

```java
// Raw list — requires casting
Inventory item = (Inventory) rawList.get(0); // could throw ClassCastException at runtime!

// Typed list — no cast needed
Inventory item = items.get(0); // clean and safe ✅
```

**3. Bugs Are Caught at Compile Time, Not Runtime**
A `ClassCastException` from a raw list crashes your program _while it's running_. A typed list catches the same mistake _before_ you even run it.

**4. Better Readability**
`List<Inventory>` immediately tells anyone reading your code exactly what's in the list — no guessing needed.

**5. IDE Support**
With generics, your IDE can offer accurate autocomplete and flag errors. With raw types, it loses that context.

---

**The bottom line:** Raw types like `List` exist in Java mainly for backwards compatibility with very old code (pre-Java 5). In modern Java, you should always use typed generics — the compiler becomes your safety net.
