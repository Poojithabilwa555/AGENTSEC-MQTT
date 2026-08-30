from typing import TypedDict, List, Dict, Any


class SecurityState(TypedDict, total=False):

    # Alert information
    alert_id: str
    timestamp: str
    device_id: str
    client_id: str
    source_ip: str
    topic: str
    attack_type: str
    ml_confidence: float

    # MQTT information
    packet_frequency: float
    duplicate_payload_ratio: float
    qos: int

    # Supervisor
    selected_agents: List[str]

    # Agent findings
    mqtt_findings: List[str]
    log_findings: List[str]
    
    threat_intel_findings: List[str]
    threat_intel_score: float
    
    investigation_summary: str

    # Risk
    risk_score: float
    severity: str

    # Response
    recommendations: List[str]

    # Agent execution tracking
    agent_logs: List[Dict[str, Any]]