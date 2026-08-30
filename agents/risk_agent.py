from agent_state import AgentState


def risk_agent(state: AgentState):

    print()
    print("=" * 60)
    print("               RISK AGENT")
    print("=" * 60)

    attack = state.get(
        "ml_prediction",
        state.get("attack", "Unknown")
    )

    severity = state.get(
        "severity",
        "MEDIUM"
    )

    # Calculate risk based on attack type
    if attack == "MQTT Flood / DoS Attack":

        risk_score = 90.0
        risk_level = "CRITICAL"

    elif attack == "Replay Attack":

        risk_score = 78.0
        risk_level = "CRITICAL"

    elif attack == "Normal Traffic":

        risk_score = 5.0
        risk_level = "LOW"

    else:

        if severity == "CRITICAL":

            risk_score = 80.0
            risk_level = "CRITICAL"

        elif severity == "HIGH":

            risk_score = 65.0
            risk_level = "HIGH"

        else:

            risk_score = 40.0
            risk_level = "MEDIUM"

    print()

    print(
        f"Risk Score: {risk_score}"
    )

    print(
        f"Risk Level: {risk_level}"
    )

    print()

    return {

        "risk_score": risk_score,

        "risk_level": risk_level
    }