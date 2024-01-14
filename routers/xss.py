from fastapi import APIRouter, status

# Local
from schemes.request import XssRequestModel
from schemes.response import XssResponseModel
from controllers.detection_controller import xss_detection_controller

router = APIRouter(prefix='/main')


@router.post('/', status_code=status.HTTP_200_OK, response_model=XssResponseModel)
def detect_xss(http: XssRequestModel):
    response = xss_detection_controller(http)
    return response