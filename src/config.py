from dataclasses import dataclass

from dotenv import dotenv_values


def read_config():
    return Config(**dotenv_values())


@dataclass
class Config:
    DATABASE_URL: str
