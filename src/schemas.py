from datetime import date, time
from pydantic import BaseModel, Field
from datetime import datetime
from pydantic import BaseModel

class Item(BaseModel):
    """
        shortDescription:
            description: The Short Product Description for the item.
            type: string
            pattern: "^[\\w\\s\\-]+$"
            example: "Mountain Dew 12PK"
        price:
            description: The total price paid for this item.
            type: string
            pattern: "^\\d+\\.\\d{2}$"
            example: "6.49"
    """
    desc: str = Field(..., alias="shortDescription")
    price: float

class Receipt(BaseModel):
    """
        retailer:
            description: The name of the retailer or store the receipt is from.
            type: string
            pattern: "^[\\w\\s\\-&]+$"
            example: "M&M Corner Market"
        purchaseDate:
            description: The date of the purchase printed on the receipt.
            type: string
            format: date
            example: "2022-01-01"
        purchaseTime:
            description: The time of the purchase printed on the receipt. 24-hour time expected.
            type: string
            format: time
            example: "13:01"
        items:
            type: array
            minItems: 1
            items:
                $ref: "#/components/schemas/Item"
        total:
            description: The total amount paid on the receipt.
            type: string
            pattern: "^\\d+\\.\\d{2}$"
            example: "6.49"
    """
    retailer: str
    purchaseDate: date
    purchaseTime: time
    items: list[Item]
    total: float
