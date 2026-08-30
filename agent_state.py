from typing import TypedDict


class AgentState(TypedDict, total=False):

    alert_id: str

    topic: str

    attack: str

    total_messages: int

    unique_payloads: int

    duplicate_ratio: float

    message_frequency: float

    topic_frequency: float

    payload_length: float

    time_interval: float

    severity: str

    mqtt_findings: list[str]

    log_findings: list[str]

    ml_findings: list[str]
    
    auth_findings:list[str]

    investigation: str

    risk_score: float

    risk_level: str

    recommendations: list[str]

    final_report: str