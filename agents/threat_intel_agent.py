import json


def threat_intel_agent(state):

    source_ip = state.get(
        "source_ip",
        ""
    )

    attack_type = state.get(
        "attack_type",
        "Unknown"
    )

    findings = []

    # Load local threat intelligence database
    with open(
        "data/threat_intelligence/ip_reputation.json",
        "r"
    ) as file:

        threat_data = json.load(file)

    # Check IP reputation
    ip_data = threat_data.get(source_ip)

    if ip_data:

        reputation = ip_data.get(
            "reputation",
            "unknown"
        )

        reputation_score = ip_data.get(
            "risk_score",
            0
        )

        known_attacks = ip_data.get(
            "known_attacks",
            []
        )

        description = ip_data.get(
            "description",
            ""
        )

        findings.append(
            f"IP reputation: {reputation}"
        )

        findings.append(
            f"Threat intelligence risk score: "
            f"{reputation_score}/100"
        )

        if known_attacks:

            findings.append(
                f"Known associated attacks: "
                f"{', '.join(known_attacks)}"
            )

        if attack_type in known_attacks:

            findings.append(
                f"Current attack type '{attack_type}' "
                f"matches known activity for this IP."
            )

        findings.append(
            description
        )

    else:

        reputation = "unknown"

        reputation_score = 0

        findings.append(
            f"No threat intelligence record found "
            f"for IP {source_ip}."
        )

    state["threat_intel_findings"] = findings

    state["threat_intel_score"] = reputation_score

    state.setdefault(
        "agent_logs",
        []
    ).append({

        "agent": "Threat Intelligence Agent",

        "status": "completed",

        "ip": source_ip,

        "reputation": reputation,

        "risk_score": reputation_score,

        "findings": findings
    })

    return state