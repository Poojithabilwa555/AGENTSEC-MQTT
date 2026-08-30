from agent_state import AgentState


def supervisor_agent(state: AgentState):

    print()
    print("=" * 60)
    print("              SUPERVISOR AGENT")
    print("=" * 60)

    print()
    print(f"Alert received: {state['alert_id']}")
    print(f"Attack type: {state['attack']}")
    print(f"Severity: {state['severity']}")

    print()
    print("Supervisor decision:")
    print("  → Analyze MQTT traffic")
    print("  → Analyze security logs")
    print("  → Analyze ML classification")

    return {}