from fastapi import Request
from src.models import SessionLocal, session_var


async def start_session(request: Request, call_next):
    async with SessionLocal() as session:
        with session.begin():
            session_var.set(session)
            response = await call_next(request)
            session_var.reset()
            return response
