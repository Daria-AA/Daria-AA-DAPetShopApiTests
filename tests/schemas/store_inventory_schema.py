STORE_INVENTORY_SCHEMA = {
        # Схема для инвентаря магазина (/store/inventory)
            "type": "object",
            "properties": {
                "approved": {"type": "integer"},
                "placed": {"type": "integer"},
                "delivered": {"type": "integer"}
            },
            "additionalProperties": False
}
