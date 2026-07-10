# AI Orchestration Layer

## Overview

This project implements a simplified AI Orchestration Layer that routes requests to multiple AI providers through a common interface.

The application does not communicate directly with individual AI providers. Instead, every request is sent to an **AI Orchestrator**, which selects the appropriate provider, executes the requested operation, logs the execution, handles errors, and returns the provider's response.

The project uses **mock implementations** of OpenAI, Claude, and Gemini instead of real APIs to demonstrate software architecture, abstraction, inheritance, and extensibility.

---

# Objectives

- Build a common interface for AI providers.
- Route requests through a single orchestrator.
- Hide provider implementation details from the application.
- Demonstrate Object-Oriented Programming concepts.
- Implement logging and error handling.
- Design an architecture that can easily support additional AI providers.

---

# Project Structure

```
Day-3 Orchestration/
│
├── Providers/
│   ├── __init__.py
│   ├── base_provider.py
│   ├── openai_provider.py
│   ├── claude_provider.py
│   └── gemini_provider.py
│
├── logger.py
├── models.py
├── Orchestrator.py
├── main.py
├── ScreenShots/
└── Day3-Readme.md
```

---

# Architecture

The application interacts only with the **AI Orchestrator**.

The orchestrator is responsible for:

- Receiving requests
- Selecting the requested provider
- Executing the requested task
- Logging execution details
- Handling errors
- Returning the provider response

Each provider implements the same interface (`BaseAIProvider`), allowing the orchestrator to interact with every provider uniformly.

---

# Components

## 1. BaseAIProvider

Defines the common interface that every AI provider must implement.

Methods:

- generate_text()
- summarize()
- classify()
- health_check()

This ensures that every provider exposes the same functionality.

---

## 2. Mock Providers

The project contains three mock providers:

- OpenAIProvider
- ClaudeProvider
- GeminiProvider

Each provider implements the methods defined in `BaseAIProvider`.

Instead of calling real APIs, they return dummy responses.

Example:

```
Generated using OpenAI
Generated using Claude
Generated using Gemini
```

---

## 3. AI Orchestrator

The orchestrator acts as the central routing layer.

Responsibilities:

- Receives application requests.
- Identifies the requested provider.
- Executes the requested method.
- Returns the provider response.
- Handles invalid requests.
- Logs execution.

The application never communicates directly with providers.

---

## 4. Logger

Logging is implemented using Python's built-in `logging` module.

The following events are logged:

- Request received
- Selected provider
- Execution completed
- Errors

---

# Error Handling

The orchestrator handles the following cases:

### Invalid Provider

```
Provider not found
```

### Invalid Task

```
Invalid task
```

### Provider Failure

Unexpected provider exceptions are caught using `try-except`, preventing the application from crashing.

---

# Current Response Format

Each provider currently returns a response in the following format:

```python
{
    "success": True,
    "provider": "OpenAI",
    "output": "...",
    "execution_time": ...
}
```

Although every provider follows the same response structure, the response construction is currently implemented individually inside each provider.

---

# OOP Concepts Demonstrated

## Abstraction

Implemented using `BaseAIProvider`.

Every provider follows the same interface.

---

## Inheritance

OpenAIProvider, ClaudeProvider, and GeminiProvider inherit from `BaseAIProvider`.

---

## Polymorphism

The orchestrator calls identical methods on different providers without knowing their implementation.

Example:

```python
provider.generate_text(prompt)
```

The same line works for every provider.

---

## Encapsulation

Each provider manages its own implementation internally.

---


# Running the Project

Run:

```bash
python main.py
```

---

# Expected Outputs

## Generate Text

```
Generated using OpenAI
```

## Summarize

```
Summary generated using Claude
```

## Classify

```
Classification using Gemini
```