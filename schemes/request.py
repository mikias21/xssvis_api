from pydantic import BaseModel

class XssRequestModel(BaseModel):
    http_url: str
