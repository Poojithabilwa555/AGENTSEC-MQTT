from agent_state import AgentState


def auth_agent(state: AgentState):

    print()
    print("=" * 60)
    print("              AUTHENTICATION AGENT")
    print("=" * 60)

    attack = state.get("attack", "")

    findings = []

    if attack == "Unauthorized Publish":

        findings.append(
            "✓ Unauthorized MQTT publish attempt detected."
        )

        findings.append(
            "✓ Authentication failure observed for MQTT client."
        )

        findings.append(
            "✓ Publish request was rejected by the MQTT broker."
        )

    else:

        findings.append(
            "✓ No unauthorized publish activity detected."
        )

    for finding in findings:
        print(finding)

    return {
        "auth_findings": findings
    }