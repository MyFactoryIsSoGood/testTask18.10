import json
import os

from fastapi import FastAPI
from fastapi import Response
from pydantic import typing
from meta.config import ROOT_PATH

app = FastAPI()


class IndentJsonResponse(Response):
    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")


@app.get("/api/meta", response_class=IndentJsonResponse)
async def get_meta():
    path = ROOT_PATH
    files = os.listdir(path)
    response = {
        "data": [
            {
                "name": os.path.basename(path + "/" + file),
                "type": "file" if os.path.isfile(path + "/" + file) else "folder",
                "time": int(os.path.getctime(path + "/" + file) * 1000),  # возвращаем миллисекунды, согласно примеру
            }
            for file in files
        ]
    }
    return response
