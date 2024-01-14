from fastapi import APIRouter, status

# Local
from schemes.request import XssRequestModel
from controllers.detection_controller import xss_detection_controller

router = APIRouter(prefix='/main')


@router.get('/', status_code=status.HTTP_200_OK)
def detect_xss(http: XssRequestModel):
    image_name = xss_detection_controller(http)
    return image_name