# 🤖 Routing Agent Customer Support (v2)

This repository contains **Version 2 (v2)** of the customer support routing agent https://github.com/meetarahulshukla/routing-agent-customer-support. It upgrades the project from a simple text classifier into a true tool-use ReAct workflow using the Google ADK framework.

---

## 🚀 Active Agent Tools (v2)

The agent dynamically selects from three core tools to handle live support queries:
*   **`generate_password_reset_link()`**: Triggers secure, temporary token generation for login issues.
*   **`get_return_policy()`**: Retrieves static store terms (simplest validation pipeline).
*   **`lookup_order_tracking()`**: Fetches structured tracking payload dictionaries from the database.

---

## 📂 Project Architecture

```text
app/
├── app/                      # Core agent runtime
│   ├── agent.py              # Tool bindings, prompt instructions, and Agent setup
│   └── app_utils/            # Agent framework utilities and helpers
├── tests/                    # Target suite for unit and integration testing
├── GEMINI.md                 # AI-assisted development context configuration
└── pyproject.toml            # Package locks and project environment dependencies
```

---

## 💡 Core Engine Overview (`agent.py`)

The agent engine routes conversations explicitly using the following logic layer:

*   **Model Core**: `gemini-3.6-flash`
*   **Routing Rules**:
    *   *Login/Password issues* ➡️ `generate_password_reset_link`
    *   *Returns/Exchanges* ➡️ `get_return_policy`
    *   *Order/Delivery tracking* ➡️ `lookup_order_tracking`
    *   *General inquiries* ➡️ Natural fallback answering

---

## 📈 Architecture Metrics (Interview Prep)

| Feature | V1 (`routing-agent-customer-support`) | V2 (`routing-agent-customer-support_v2`) |
| :--- | :--- | :--- |
| **Core Objective** | Classifies message into department | Resolves customer concerns end-to-end |
| **Output Type** | Categorical label text (e.g., `BILLING`) | Natural conversational response with live data |
| **Tool Availability** | None (Static routing classifier) | 3 integrated tool functions |
| **Workflow Class** | Deterministic Classifier | True Autonomous ReAct Agent |
