# ruff: noqa
import os

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"
os.environ["GOOGLE_GENAI_USE_ENTERPRISE"] = "FALSE"

from google.adk.agents import Agent


# --- Tool 1: TECHNICAL ---
def generate_password_reset_link(email: str) -> str:
    """Generates a password reset link for the given email."""
    return f"https://support.mystore.com/reset-password?email={email}&token=abc123"


# --- Tool 2: RETURNS ---
def get_return_policy() -> str:
    """Returns the store return policy."""
    return "You can return any item within 30 days of delivery. Items must be unused and in original packaging. Refunds are processed within 5-7 business days."


# --- Tool 3: SHIPPING ---
def lookup_order_tracking(order_id: str) -> dict:
    """Looks up tracking status for a given order ID."""
    return {
        "order_id": order_id,
        "status": "In Transit",
        "location": "Mumbai Sorting Facility",
        "estimated_delivery": "2026-08-24",
    }


root_agent = Agent(
    name="customer_support_router",
    model="gemini-3.6-flash",
    instruction="""You are a helpful customer support agent.

When a customer asks about login or password issues, use the generate_password_reset_link tool and share the link.
When a customer asks about returns or exchanges, use the get_return_policy tool and share the policy.
When a customer asks about their order or delivery, use the lookup_order_tracking tool and share the status.

For anything else, answer helpfully on your own.""",
    tools=[
        generate_password_reset_link,
        get_return_policy,
        lookup_order_tracking,
    ],
)

# Required by __init__.py
app = root_agent
