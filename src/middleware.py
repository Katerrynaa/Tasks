from fastapi import Request
from src.models import SessionLocal, session_var


async def start_session(request: Request, call_next):
    with SessionLocal() as session:
        with session.begin():
            token = session_var.set(session)
            response = await call_next(request)
            session_var.reset(token)
            return response
