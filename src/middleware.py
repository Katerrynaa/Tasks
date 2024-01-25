from fastapi import Request
from src.models import SessionLocal, Department
import contextvars


async def start_session(data: dict):
    session_var = contextvars.ContextVar("session")
    async with SessionLocal() as session:
        with session.begin():
            session_var.set(session)
            obj = Department(**data)
            session.add(obj)
            session.flush()
            session.refresh(obj)
            session.expunge_all()
            return obj


async def reset_variable(request: Request, call_next, session_var):
    response = await call_next(request)
    session_var.reset()
    return response
