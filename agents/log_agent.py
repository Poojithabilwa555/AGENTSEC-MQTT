from agent_state import AgentState


def log_agent(state: AgentState):

    findings = [
        "Repeated activity detected for device_27.",
        "Multiple similar MQTT events were observed "
        "within the investigation window."
    ]

    return {
        "log_findings": findings
    }