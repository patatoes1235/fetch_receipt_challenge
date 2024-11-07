from fastapi import APIRouter

router = APIRouter(prefix="/receipts")

@router.post("/process")
def process_receipt():
    return {"message": "Receipt processed successfully"}

@router.get("/{reciept_id}/points")
def get_points(reciept_id: str):
    return {"points": 100}