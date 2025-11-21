import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse

from cat import endpoint

@endpoint.get("/{path:path}", prefix="/ui", include_in_schema=False)
async def frontend(path: str, req: Request):

    ccat = req.app.state.ccat

    ui_static_path = os.path.abspath(
        os.path.join(ccat.plugin.path, "web")
    )

    file_path = os.path.abspath(os.path.join(ui_static_path, path))

    if not file_path.startswith(ui_static_path):
        raise HTTPException(status_code=403, detail="Access forbidden")

    if file_path.endswith("/web"):
        file_path += "/index.html"

    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(path=file_path)
