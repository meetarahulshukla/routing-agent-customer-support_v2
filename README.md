# 🤖 Routing Agent Customer Support (v2)

![Google ADK](https://img.shields.io/badge/Google%20ADK-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini%203.6%20Flash-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ReAct](https://img.shields.io/badge/Pattern-ReAct-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Working-brightgreen?style=for-the-badge)

This repository contains **Version 2 (v2)** of the customer support routing agent https://github.com/meetarahulshukla/routing-agent-customer-support. It upgrades the project from a simple text classifier into a true tool-use ReAct workflow using the Google ADK framework.

---

<p align="center">
  <img src="./Routing%20Agent%20Image.png" alt="Routing Agent" width="600"/>
</p>

## 🚀 Active Agent Tools (v2)

The agent dynamically selects from three core tools to handle live support queries:
*   **`generate_password_reset_link()`**: Triggers secure, temporary token generation for login issues.
*   **`get_return_policy()`**: Retrieves static store terms (simplest validation pipeline).
*   **`lookup_order_tracking()`**: Fetches structured tracking payload dictionaries from the database.

---

## 📂 Project Architecture

```text
app/
├── .github/
│   └── ISSUE_TEMPLATE/       # GitHub issue template directory
├── app/                      # Core agent runtime
│   ├── agent.py              # Tool bindings, prompt instructions, and Agent setup
│   └── app_utils/            # Agent framework utilities and helpers
├── tests/                    # Target suite for unit and integration testing
├── .env                      # Environment configuration variables
├── CODE_OF_CONDUCT.md        # Contributor Covenant Code of Conduct
├── CONTRIBUTING.md           # Contribution guidelines
├── GEMINI.md                 # AI-assisted development context configuration
├── LICENSE                   # MIT License
├── README.md                 # Project documentation (v2 overview & image)
├── SECURITY.md               # Security policy
├── Routing Agent Image.png   # Routing architecture diagram/screenshot
├── cant_login.png            # Customer support flow asset (Login issue)
├── pyproject.toml            # Package locks and project environment dependencies
├── pull_request_template.md  # PR submission template
├── return_policy.png         # Customer support flow asset (Returns)
└── where_is_my_order.png     # Customer support flow asset (Order status)
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

