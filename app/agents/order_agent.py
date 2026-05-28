def handle_order_message(message: str, customer_id: int | None = None):
    message_lower = message.lower()

    if "menu" in message_lower:
        return "You can view the menu using GET /menu."

    if "order" in message_lower or "want" in message_lower:
        return (
            "I can help create your order. "
            "Please provide item name, quantity, and customer ID."
        )

    if "status" in message_lower:
        return "Please provide your order ID to check order status."

    return (
        "I can help with menu, creating food orders, "
        "and checking order status."
    )