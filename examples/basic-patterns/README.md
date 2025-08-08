# Basic Pattern Examples

**Status: Educational Examples - Pattern Classification Demonstrations**

## Overview

This directory contains simple, clear examples of how basic patterns would be classified and recognized by the Code Periodic Table system.

## Available Examples

### [Singleton Classification](./singleton-classification.md)
Detailed walkthrough of how the Singleton pattern would be classified, including its properties, relationships, and variations.

## Pattern Categories Demonstrated

### Creational Patterns
Examples showing object creation patterns:
- Singleton - Single instance control
- Factory - Object creation abstraction
- Builder - Step-by-step construction
- Prototype - Object cloning

### Structural Patterns
Examples showing composition patterns:
- Adapter - Interface translation
- Composite - Tree structures
- Decorator - Dynamic extension
- Facade - Simplified interface

### Behavioral Patterns
Examples showing interaction patterns:
- Observer - Event notification
- Strategy - Algorithm selection
- Command - Request encapsulation
- Iterator - Sequential traversal

## Example: Observer Pattern Classification

### Pattern Recognition
```python
# Python Implementation
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass
```

### Classification Result
```yaml
pattern:
  name: Observer
  category: Behavioral
  
  properties:
    coupling: loose
    cardinality: one-to-many
    communication: push/pull
    
  metrics:
    complexity: medium
    testability: high
    maintainability: high
    
  relationships:
    similar_to: [PublishSubscribe, EventEmitter]
    often_used_with: [MVC, MVP]
    alternative_to: [Polling, Callbacks]
```

## Example: Factory Pattern Variations

### Simple Factory
```java
public class AnimalFactory {
    public Animal createAnimal(String type) {
        switch(type) {
            case "dog": return new Dog();
            case "cat": return new Cat();
            default: return null;
        }
    }
}
```

### Factory Method
```java
public abstract class AnimalFactory {
    public abstract Animal createAnimal();
}

public class DogFactory extends AnimalFactory {
    public Animal createAnimal() {
        return new Dog();
    }
}
```

### Abstract Factory
```java
public interface AnimalFactory {
    Animal createAnimal();
    Food createFood();
}

public class DogFactory implements AnimalFactory {
    public Animal createAnimal() { return new Dog(); }
    public Food createFood() { return new DogFood(); }
}
```

### Classification Comparison
```yaml
simple_factory:
  complexity: low
  flexibility: low
  use_case: "Few, stable types"

factory_method:
  complexity: medium
  flexibility: medium
  use_case: "Subclass customization"

abstract_factory:
  complexity: high
  flexibility: high
  use_case: "Product families"
```

## Cross-Language Pattern Recognition

### Singleton in Multiple Languages

#### Python
```python
class Singleton:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
```

#### JavaScript
```javascript
class Singleton {
    constructor() {
        if (Singleton.instance) {
            return Singleton.instance;
        }
        Singleton.instance = this;
    }
}
```

#### Java
```java
public class Singleton {
    private static Singleton instance;
    private Singleton() {}
    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

### Unified Classification
Despite syntax differences, all recognized as:
```yaml
pattern: Singleton
fingerprint: SINGLE-INSTANCE-LAZY-INIT
properties:
  thread_safe: false
  lazy_loading: true
  testability: low
confidence: 95%
```

## Anti-Pattern Detection

### Example: God Object
```python
class SystemManager:
    def __init__(self):
        self.database = Database()
        self.ui = UserInterface()
        self.network = Network()
        self.cache = Cache()
        # ... 20 more dependencies
    
    def do_everything(self):
        # 1000+ lines of code
        pass
```

### Detection Result
```yaml
anti_pattern_detected: God Object
issues:
  - excessive_responsibilities: 23
  - high_coupling: 15 dependencies
  - low_cohesion: 0.2
  - difficult_testing: "extremely high"
  
recommendations:
  - apply: Single Responsibility Principle
  - refactor_to: [Service Layer, Repository, Controller]
  - split_into: 5-7 focused classes
```

## Pattern Evolution Examples

### Evolution: Callback → Promise → Async/Await

#### Stage 1: Callbacks
```javascript
getData(function(data) {
    processData(data, function(result) {
        saveResult(result, function() {
            console.log('Done');
        });
    });
});
```

#### Stage 2: Promises
```javascript
getData()
    .then(data => processData(data))
    .then(result => saveResult(result))
    .then(() => console.log('Done'));
```

#### Stage 3: Async/Await
```javascript
async function workflow() {
    const data = await getData();
    const result = await processData(data);
    await saveResult(result);
    console.log('Done');
}
```

### Classification Evolution
```yaml
evolution_chain:
  - pattern: Callback Hell
    year: 2000-2010
    issues: [readability, error_handling]
    
  - pattern: Promise Chain
    year: 2010-2015
    improvements: [chaining, error_propagation]
    
  - pattern: Async/Await
    year: 2015-present
    benefits: [readability, debugging, error_handling]
```

## Interactive Classification Demo

### Input Your Code (Conceptual)
```bash
$ cpt classify --code "
class Logger:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
"

Output:
Pattern: Singleton
Confidence: 98%
Category: Creational
Thread-Safe: No
Suggestion: Consider thread-safe implementation
```

## Learning Exercises

### Exercise 1: Identify the Pattern
```python
class Pizza:
    def __init__(self):
        self.toppings = []
    
    def add_cheese(self):
        self.toppings.append("cheese")
        return self
    
    def add_pepperoni(self):
        self.toppings.append("pepperoni")
        return self
    
    def build(self):
        return f"Pizza with: {', '.join(self.toppings)}"

# Usage
pizza = Pizza().add_cheese().add_pepperoni().build()
```

**Answer:** Builder pattern with fluent interface

### Exercise 2: Fix the Anti-Pattern
```python
# Anti-pattern code
def process_user_data(user_data):
    # Validate
    if not user_data: return None
    if not user_data.get('email'): return None
    if '@' not in user_data['email']: return None
    
    # Process
    user_data['email'] = user_data['email'].lower()
    user_data['name'] = user_data['name'].title()
    
    # Save
    database.save(user_data)
    
    # Send email
    email_service.send_welcome(user_data['email'])
    
    # Log
    logger.info(f"Processed {user_data['email']}")
    
    return user_data
```

**Issues:** Multiple responsibilities, hard to test, tightly coupled

## Summary

These basic examples demonstrate:
1. How patterns are recognized across languages
2. Classification properties and metrics
3. Pattern relationships and evolution
4. Anti-pattern detection
5. Practical applications

---

**Note:** These examples show conceptual classification. The actual system is not yet implemented.