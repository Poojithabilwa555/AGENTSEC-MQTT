from dataclasses import dataclass


@dataclass
class SecurityEvent:

    alert_id: str
    topic: str
    attack: str

    total_messages: int
    unique_payloads: int

    duplicate_ratio: float
    message_frequency: float

    severity: str