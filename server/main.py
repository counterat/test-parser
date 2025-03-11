from fastapi import  FastAPI, Request, Header, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from parse.parser import parser

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_start():
    await parser.main()


