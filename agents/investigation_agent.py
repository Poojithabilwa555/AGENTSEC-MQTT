from agent_state import AgentState


def investigation_agent(state: AgentState):

    print()
    print("=" * 60)
    print("            INVESTIGATION AGENT")
    print("=" * 60)

    mqtt_findings = state.get(
        "mqtt_findings",
        []
    )

    log_findings = state.get(
        "log_findings",
        []
    )

    ml_findings = state.get(
        "ml_findings",
        []
    )

    ml_prediction = state.get(
        "ml_prediction",
        state.get("attack", "Unknown")
    )

    print()

    print(
        f"Evidence reviewed:"
    )

    print(
        f"  → MQTT findings: {len(mqtt_findings)}"
    )

    print(
        f"  → Log findings: {len(log_findings)}"
    )

    print(
        f"  → ML findings: {len(ml_findings)}"
    )

    # Investigation conclusion
    if ml_prediction == "MQTT Flood / DoS Attack":

        conclusion = (
            "Strong evidence supports the ML classification "
            "of MQTT Flood / DoS Attack."
        )

    elif ml_prediction == "Replay Attack":

        conclusion = (
            "Strong evidence supports the ML classification "
            "of Replay Attack."
        )

    elif ml_prediction == "Normal Traffic":

        conclusion = (
            "Available evidence is consistent with normal "
            "MQTT traffic."
        )

    else:

        conclusion = (
            f"Evidence supports the ML classification "
            f"of {ml_prediction}."
        )

    print()

    print(
        "Investigation conclusion:"
    )

    print(
        f"  → {conclusion}"
    )

    print()

    return {

        "investigation": conclusion
    }