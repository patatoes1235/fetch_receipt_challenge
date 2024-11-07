from fastapi import APIRouter, HTTPException
from uuid import uuid4

from .schemas import Receipt
from .services import calculate_points, points_dict, validate_receipt

THROW_ON_VALIDATION_ERROR = False

router = APIRouter(prefix="/receipts")

@router.post("/process")
def process_receipt(receipt: Receipt):
    """Process a receipt and return a receipt ID."""

    receipt_id = str(uuid4())
    points_earned = calculate_points(receipt)

    if receipt_id in points_dict:
        raise HTTPException(status_code=500, detail="Duplicate receipt ID generated, please try again.")

    points_dict[receipt_id] = points_earned

    try:
        validate_receipt(receipt)
    except ValueError as e:
        if THROW_ON_VALIDATION_ERROR:
            raise HTTPException(status_code=400, detail=str(e))
        else:
            print(f"WARNING:\t Failed to validate receipt: {e}")

    return {"id": receipt_id}

@router.get("/{id}/points")
def get_points_by_id(id: str):
    """Returns the points awarded for the receipt"""
    try: 
        return {"points": points_dict[id]}
    except KeyError:
        raise HTTPException(status_code=404, detail="Receipt ID not found.")