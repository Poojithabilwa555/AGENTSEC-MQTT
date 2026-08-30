from agent_state import AgentState


def response_agent(state: AgentState):

    print()
    print("=" * 60)
    print("             RESPONSE AGENT")
    print("=" * 60)

    attack = state.get(
        "ml_prediction",
        state.get("attack", "Unknown")
    )

    print()

    print("Recommended actions:")

    if attack == "MQTT Flood / DoS Attack":

        recommendations = [

            "Rate-limit MQTT messages from the affected source.",

            "Monitor the broker for continued high-frequency traffic.",

            "Review the affected device and identify the source of the flood.",

            "Consider temporary containment if the attack continues.",

            "Human analyst approval is required before taking any containment action."
        ]

    elif attack == "Replay Attack":

        recommendations = [

            "Review repeated MQTT messages from the affected device.",

            "Verify the device authentication credentials.",

            "Monitor the device for additional anomalous traffic.",

            "Human analyst approval is required before taking any containment action."
        ]

    elif attack == "Normal Traffic":

        recommendations = [

            "No immediate containment action is required.",

            "Continue monitoring MQTT traffic."
        ]

    else:

        recommendations = [

            "Continue monitoring the affected MQTT device.",

            "Review broker and device security logs.",

            "Human analyst approval is required before taking any containment action."
        ]

    for recommendation in recommendations:

        print(
            f"  → {recommendation}"
        )

    print()

    return {

        "recommendations": recommendations
    }