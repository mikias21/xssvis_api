import uvicorn
from pathlib import Path 
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Local
from routers.xss import router
from constants.general import General

# Define generated images path
images_folder = "workspace/generated_images" if General.DIGITAL_OCEN.value else "generated_images" 
generated_images_path = Path(__file__).parent / images_folder

origins = [
    'http://127.0.0.1:3000', 'http://localhost:3000', 'https://xssvis.netlify.app'
]

app = FastAPI()

app.mount("/images", StaticFiles(directory=generated_images_path), name="images")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    max_age=3600,
)

app.include_router(router)


def run_server():
    if General.RELEASE.value:
        if General.DIGITAL_OCEN.value:
            uvicorn.run(app, host="0.0.0.0", port=8080)
        else:
            uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        app.debug = True
        uvicorn.run(app, host="127.0.0.1", port=5000)

if __name__ == "__main__":
    run_server()