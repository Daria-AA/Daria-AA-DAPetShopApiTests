STORE_SCHEMA = {
    "oneOf": [
        # 1. Схема для инвентаря магазина (/store/inventory)
        {
            "type": "object",
            "properties": {
                "approved": {"type": "integer"},
                "placed": {"type": "integer"},
                "delivered": {"type": "integer"}
            },
            "additionalProperties": False
        },
        # 2. Схема для заказа (/store/order)
        {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "petId": {
                    "type": "integer"
                },
                "quantity": {
                    "type": "integer"
                },
                "shipDate": {
                    "type": "string",
                    "format": "date-time"
                },
                "status": {
                    "type": "string",
                    "enum": ["placed", "approved", "delivered"]
                },
                "complete": {
                    "type": "boolean"
                }
            },
            "required": ["id", "petId", "quantity", "status", "complete"],
            "additionalProperties": False
        }
    ]
}
