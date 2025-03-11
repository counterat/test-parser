from parse.parser import parser
import asyncio
import uvicorn
from server.main import app


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    