# Counter-Examples and Edge Cases

*This document provides concrete examples where the Code Periodic Table approach fails or doesn't apply.*

---

## 1. Patterns That Cannot Be Classified

### 1.1 Context-Dependent Patterns

**Example: Database Query Pattern**

```python
# In a financial system - MUST use transactions
def transfer_money(from_account, to_account, amount):
    with db.transaction():  # CRITICAL for consistency
        debit(from_account, amount)
        credit(to_account, amount)

# In a logging system - transactions would be WRONG
def log_event(event):
    db.insert(event)  # No transaction needed, would hurt performance
```

**Why Classification Fails**: The same pattern (database operation) requires opposite approaches depending on context. No universal classification can capture this.

### 1.2 Domain-Specific Patterns

**Example: Game Loop vs. Web Request Handler**

```javascript
// Game loop - runs continuously
function gameLoop() {
    while (true) {
        processInput();
        updateWorld();
        render();
        sleep(16); // 60 FPS
    }
}

// Web handler - runs once per request  
function handleRequest(req, res) {
    processInput(req);
    updateData();
    res.send(result);
    // Must NOT loop
}
```

**Why Classification Fails**: These patterns serve similar purposes (process-update-output) but have fundamentally incompatible structures.

---

## 2. Cross-Language Patterns That Don't Translate

### 2.1 Paradigm-Specific Patterns

**Haskell Monads - No True Equivalent in Java**

```haskell
-- Haskell: Elegant monad composition
computation :: IO String
computation = do
    x <- getLine
    y <- getLine  
    return (x ++ y)
```

```java
// Java: Clunky attempted translation
public CompletableFuture<String> computation() {
    return getUserInput()
        .thenCompose(x -> getUserInput()
            .thenApply(y -> x + y));
}
// Not really the same - missing laws, composition, abstraction
```

**Why It Fails**: Monads require language features Java doesn't have. The "equivalent" isn't equivalent.

### 2.2 Memory Model Differences

**C++ RAII vs. Java Try-With-Resources**

```cpp
// C++: Deterministic destruction
{
    std::lock_guard<std::mutex> lock(mutex);
    // Mutex GUARANTEED released at scope end
} // Destructor called here, exactly
```

```java
// Java: Non-deterministic with GC
try (var lock = mutex.lock()) {
    // Released at try block end
} // But object may live longer in memory
// GC timing undefined
```

**Why It Fails**: Fundamental runtime differences make these patterns behaviorally different despite syntactic similarity.

---

## 3. Security Patterns That Can't Be Automated

### 3.1 Business Logic Security

**Example: Authorization That Depends on Business Rules**

```python
def can_view_document(user, document):
    # These rules cannot be derived from code structure
    if document.is_public:
        return True
    if user.is_admin:
        return True
    if user.department == document.department:
        return True
    if user in document.shared_with:
        return True
    if document.created_by == user and not document.archived:
        return True
    # Company-specific rule that changes quarterly
    if user.security_clearance >= document.classification_level:
        return datetime.now() < document.declassification_date
    return False
```

**Why It Fails**: Security depends on business requirements that aren't encoded in patterns.

### 3.2 Timing Attack Mitigation

```python
# Looks secure but has timing attack
def verify_signature(provided, expected):
    return provided == expected  # Comparison time reveals info

# Fixed version - but tools can't detect the difference
def verify_signature_secure(provided, expected):
    return hmac.compare_digest(provided, expected)  # Constant time
```

**Why It Fails**: Both patterns look identical structurally but have critically different security properties.

---

## 4. Performance Patterns That Depend on Hardware

### 4.1 Cache-Optimized vs. Memory-Optimized

```c
// Array of Structs - good for cache if accessing all fields
struct Entity {
    float x, y, z;
    float vx, vy, vz;
    int health;
    int armor;
};
Entity entities[1000];

// Struct of Arrays - good if accessing only position
struct Entities {
    float x[1000], y[1000], z[1000];
    float vx[1000], vy[1000], vz[1000];
    int health[1000];
    int armor[1000];
};
```

**Why It Fails**: Optimal pattern depends on access patterns and CPU cache architecture, not determinable from code alone.

---

## 5. Patterns That Evolve Too Quickly

### 5.1 JavaScript Framework Patterns

```javascript
// 2013: Backbone.js pattern
var UserView = Backbone.View.extend({
    initialize: function() {
        this.model.on('change', this.render, this);
    }
});

// 2015: Angular 1 pattern
app.controller('UserController', function($scope) {
    $scope.$watch('user', function() { /* ... */ });
});

// 2017: React pattern
class UserComponent extends React.Component {
    componentDidUpdate() { /* ... */ }
}

// 2019: React Hooks pattern
function UserComponent() {
    useEffect(() => { /* ... */ }, [user]);
}

// 2023: React Server Components
async function UserComponent() {
    const user = await fetchUser();
    return <div>{user.name}</div>;
}
```

**Why It Fails**: By the time you classify the pattern, it's already obsolete.

---

## 6. Anti-Pattern or Best Practice? Depends!

### 6.1 Global State

```python
# In a web app - TERRIBLE (shared mutable state)
global_cache = {}

def handle_request(request):
    global global_cache
    global_cache[request.id] = process(request)  # Race condition!

# In a CLI tool - PERFECTLY FINE
global_config = None

def main():
    global global_config
    global_config = load_config()  # Set once, read-only after
```

**Why It Fails**: Same pattern, opposite quality assessment based on context.

### 6.2 Tight Coupling

```java
// In a framework - GOOD (intentional coupling)
class SpringController {
    @Autowired
    private ServiceA serviceA;  // Framework manages this
    @Autowired
    private ServiceB serviceB;  // Intentional design
}

// In business logic - BAD (unwanted coupling)
class OrderProcessor {
    private EmailSender emailer = new EmailSender();  // Hardcoded!
    private Database db = new MySQLDatabase();  // Can't test!
}
```

**Why It Fails**: Coupling is sometimes desirable, sometimes not. No universal rule.

---

## 7. Patterns That Shouldn't Be Abstracted

### 7.1 One-Off Business Logic

```python
def calculate_swedish_tax_2025(income):
    # Swedish tax law for 2025 - highly specific
    if income <= 509300:
        return income * 0.32
    else:
        base = 509300 * 0.32
        excess = income - 509300
        return base + (excess * 0.52)
    # This SHOULD NOT be generalized into a "tax pattern"
    # It's specific legislation that changes annually
```

**Why It Fails**: Some code is inherently specific and shouldn't be pattern-ized.

---

## 8. Cultural and Team Patterns

### 8.1 Naming Conventions

```python
# Team A: Descriptive names preferred
def get_user_by_email_address_with_profile_data(email_address_string):
    pass

# Team B: Concise names preferred
def get_user(email):
    pass

# Both are "correct" for their teams
```

**Why It Fails**: No objective "best" pattern - depends on team culture.

---

## 9. Patterns That Break Under Scale

### 9.1 Works for 10 Users, Fails for 10 Million

```python
# Pattern: Load all data, filter in memory
def find_active_users():
    all_users = db.query("SELECT * FROM users")  # Works fine for 10 users
    return [u for u in all_users if u.active]   # DISASTER for 10M users

# Different pattern needed at scale
def find_active_users_scalable():
    return db.query("SELECT * FROM users WHERE active = true LIMIT 1000")
    # Completely different approach required
```

**Why It Fails**: Pattern validity depends on scale, which isn't encoded in the pattern itself.

---

## 10. Machine Learning Patterns - Inherently Unpredictable

### 10.1 Neural Network Behavior

```python
def predict(input_data):
    # This pattern's behavior depends on training data
    model = load_model("model.h5")
    return model.predict(input_data)
    # Can't classify behavior without knowing training data
    # Same pattern could be face recognition or spam detection
```

**Why It Fails**: ML patterns' behavior determined by data, not code structure.

---

## Conclusion

These counter-examples demonstrate that:

1. **Context is everything** - Same pattern can be good or bad
2. **Domain specifics matter** - Universal classification often impossible
3. **Language differences are real** - Not everything translates
4. **Business logic resists patterns** - Some code is inherently unique
5. **Scale changes everything** - Patterns that work small fail big
6. **Culture affects code** - No objective "best" patterns
7. **Evolution is too fast** - Classifications become obsolete quickly

**The Code Periodic Table can AT BEST classify a subset of patterns in specific contexts. It cannot be a universal solution.**

---

*Last Updated: 2025*  
*Purpose: Honest acknowledgment of classification limitations*