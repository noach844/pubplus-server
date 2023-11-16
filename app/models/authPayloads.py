from dataclasses import dataclass


@dataclass
class LoginPayload:
    username: str
    password: str


@dataclass
class RegisterPayload:
    username: str
    fullname: str
    password: str
