from agent_state import AgentState


def mqtt_agent(state: AgentState):

    duplicate_ratio = state["duplicate_ratio"]

    frequency = state["message_frequency"]

    total_messages = state["total_messages"]

    topic = state["topic"]

    findings = []

    # ------------------------------------------------
    # Replay Attack indicators
    # ------------------------------------------------

    if duplicate_ratio >= 0.80:

        findings.append(
            "High duplicate MQTT payload ratio detected."
        )

    # ------------------------------------------------
    # Flood / DoS indicators
    # ------------------------------------------------

    if frequency >= 30:

        findings.append(
            "Extremely high MQTT packet frequency detected."
        )

        findings.append(
            "Large number of MQTT messages received in a short time."
        )

    elif frequency >= 5:

        findings.append(
            "Abnormally high MQTT packet frequency detected."
        )

    # ------------------------------------------------
    # Traffic volume
    # ------------------------------------------------

    if total_messages >= 80:

        findings.append(
            "Large MQTT traffic volume detected."
        )

    # ------------------------------------------------
    # Topic information
    # ------------------------------------------------

    findings.append(
        f"Traffic was observed on MQTT topic: {topic}"
    )

    return {

        "mqtt_findings": findings
    }