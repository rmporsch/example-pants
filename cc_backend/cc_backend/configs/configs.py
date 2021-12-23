from pydantic import BaseSettings


class Configs(BaseSettings):
    environment: str
