from dataclasses import dataclass


@dataclass
class Delivery:
    id: str
    start_time: int
    finish_time: int
    