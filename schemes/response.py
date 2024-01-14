from pydantic import BaseModel

class XssResponseModel(BaseModel):
    generated_image: str
    prediction: int
    