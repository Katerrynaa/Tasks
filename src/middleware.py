from fastapi import FastAPI, Request

async def print_hello(request: Request, call_next):
    print("Hello")
    response = await call_next(request)
    print("Goodbye")
    return response
