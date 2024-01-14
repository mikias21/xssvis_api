from fastapi import FastAPI

from routers.xss import router
from constants.general import General

app = FastAPI()
app.include_router(router)


# if __name__ == "__main__":
#     if General.RELEASE.value:
