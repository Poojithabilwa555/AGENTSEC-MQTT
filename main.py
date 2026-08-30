import json

from graph.workflow import build_workflow


def main():

    # -----------------------------
    # Load security alert
    # -----------------------------

    with open(
        "data/sample_alerts.json",
        "r"
    ) as file:

        alert = json.load(file)

    # -----------------------------
    # Build workflow
    # -----------------------------

    workflow = build_workflow()

    # -----------------------------
    # Execute workflow
    # -----------------------------

    result = workflow.invoke(alert)

    # -----------------------------
    # Security Report
    # -----------------------------

    print()
    print("=" * 60)
    print("       AGENTSEC-MQTT SECURITY REPORT")
    print("=" * 60)

    print()

    print(
        f"Alert ID: {result.get('alert_id', 'N/A')}"
    )

    print(
        f"Attack: {result.get('attack_type', 'Unknown')}"
    )

    confidence = result.get(
        "ml_confidence",
        0
    )

    print(
        f"ML Confidence: {confidence * 100:.2f}%"
    )

    # -----------------------------
    # MQTT Findings
    # -----------------------------

    print()
    print("MQTT Findings:")

    for finding in result.get(
        "mqtt_findings",
        []
    ):

        print(f"  ✓ {finding}")

    # -----------------------------
    # Log Findings
    # -----------------------------

    print()
    print("Log Findings:")

    for finding in result.get(
        "log_findings",
        []
    ):

        print(f"  ✓ {finding}")

    # -----------------------------
    # Threat Intelligence
    # -----------------------------

    print()
    print("Threat Intelligence Findings:")

    for finding in result.get(
        "threat_intel_findings",
        []
    ):

        print(f"  ✓ {finding}")

    threat_score = result.get(
        "threat_intel_score",
        0
    )

    print()
    print(
        f"Threat Intelligence Score: "
        f"{threat_score}/100"
    )

    # -----------------------------
    # Investigation
    # -----------------------------

    print()
    print("Investigation:")

    print(
        f"  {result.get('investigation_summary', 'No investigation summary available.')}"
    )

    # -----------------------------
    # Risk Assessment
    # -----------------------------

    print()
    print("Risk Assessment:")

    print(
        f"  Risk Score: "
        f"{result.get('risk_score', 0)}"
    )

    print(
        f"  Severity: "
        f"{result.get('severity', 'UNKNOWN')}"
    )

    # -----------------------------
    # Recommendations
    # -----------------------------

    print()
    print("Recommendations:")

    for recommendation in result.get(
        "recommendations",
        []
    ):

        print(
            f"  → {recommendation}"
        )

    # -----------------------------
    # Agent Execution
    # -----------------------------

    print()
    print("Agent Execution:")

    for log in result.get(
        "agent_logs",
        []
    ):

        agent_name = log.get(
            "agent",
            "Unknown Agent"
        )

        print(
            f"  ✓ {agent_name}"
        )

    # -----------------------------
    # End
    # -----------------------------

    print()
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()