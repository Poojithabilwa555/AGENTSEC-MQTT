import streamlit as st

from workflow import build_workflow


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AgentSec-MQTT",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🛡️ AgentSec-MQTT")

st.subheader(
    "Multi-Agent MQTT Intrusion Detection & Response System"
)

st.write(
    "Real-time MQTT security analysis using LangGraph, "
    "Machine Learning and multi-agent investigation."
)

st.divider()


# ============================================================
# ATTACK SCENARIOS
# ============================================================

scenarios = {

    "MQTT Flood / DoS Attack": {

        "alert_id": "ALERT-001",
        "topic": "/factory/control",
        "attack": "MQTT Flood / DoS Attack",

        "total_messages": 100,
        "unique_payloads": 100,
        "duplicate_ratio": 0.0,

        "message_frequency": 64.27,
        "topic_frequency": 64.27,

        "payload_length": 15,
        "time_interval": 0.015,

        "severity": "CRITICAL"
    },

    "Replay Attack": {

        "alert_id": "ALERT-002",
        "topic": "/factory/control",
        "attack": "Replay Attack",

        "total_messages": 20,
        "unique_payloads": 1,
        "duplicate_ratio": 0.95,

        "message_frequency": 9.65,
        "topic_frequency": 9.65,

        "payload_length": 13,
        "time_interval": 0.10,

        "severity": "CRITICAL"
    },

    "Normal Traffic": {

        "alert_id": "ALERT-003",
        "topic": "/factory/sensor",
        "attack": "Normal Traffic",

        "total_messages": 20,
        "unique_payloads": 18,
        "duplicate_ratio": 0.10,

        "message_frequency": 2.0,
        "topic_frequency": 2.0,

        "payload_length": 15,
        "time_interval": 0.5,

        "severity": "LOW"
    },

    "Unauthorized Publish": {

        "alert_id": "ALERT-004",
        "topic": "/factory/control",
        "attack": "Unauthorized Publish",

        "total_messages": 5,
        "unique_payloads": 5,
        "duplicate_ratio": 0.0,

        "message_frequency": 1.5,
        "topic_frequency": 1.5,

        "payload_length": 18,
        "time_interval": 0.7,

        "severity": "HIGH"
    }
}


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("🔍 Security Analysis")

selected_attack = st.sidebar.selectbox(
    "Select Security Scenario",
    list(scenarios.keys())
)

st.sidebar.write("")

run_analysis = st.sidebar.button(
    "🚀 Run Security Analysis",
    use_container_width=True
)


# ============================================================
# SELECTED SCENARIO
# ============================================================

security_event = scenarios[selected_attack]


st.header("📡 Security Event")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Attack Type",
        security_event["attack"]
    )

with col2:

    st.metric(
        "Severity",
        security_event["severity"]
    )

with col3:

    st.metric(
        "MQTT Messages",
        security_event["total_messages"]
    )

with col4:

    st.metric(
        "Message Frequency",
        f'{security_event["message_frequency"]:.2f}/sec'
    )


st.divider()


# ============================================================
# TRAFFIC FEATURES
# ============================================================

st.header("📊 MQTT Traffic Features")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Messages",
        security_event["total_messages"]
    )

with col2:

    st.metric(
        "Unique Payloads",
        security_event["unique_payloads"]
    )

with col3:

    st.metric(
        "Duplicate Ratio",
        f'{security_event["duplicate_ratio"]:.2%}'
    )

with col4:

    st.metric(
        "Topic Frequency",
        f'{security_event["topic_frequency"]:.2f}/sec'
    )


col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Payload Length",
        security_event["payload_length"]
    )

with col2:

    st.metric(
        "Time Interval",
        f'{security_event["time_interval"]:.3f}s'
    )

with col3:

    st.metric(
        "MQTT Topic",
        security_event["topic"]
    )


st.divider()


# ============================================================
# RUN LANGGRAPH WORKFLOW
# ============================================================

if run_analysis:

    with st.spinner(
        "Running multi-agent security analysis..."
    ):

        workflow = build_workflow()

        result = workflow.invoke(
            security_event
        )

    st.success(
        "Security analysis completed successfully."
    )


    # ========================================================
    # ML RESULTS
    # ========================================================

    st.header("🤖 Machine Learning Analysis")

    ml_findings = result.get(
        "ml_findings",
        []
    )

    if ml_findings:

        ml_text = ml_findings[0]

        st.info(
            ml_text
        )

    else:

        st.warning(
            "No ML findings were returned."
        )


    # ========================================================
    # INVESTIGATION
    # ========================================================

    st.header("🔎 Investigation")

    investigation = result.get(
        "investigation",
        result.get(
            "investigation_conclusion",
            ""
        )
    )

    if investigation:

        st.info(
            investigation
        )

    else:

        st.write(
            "Investigation completed."
        )


    # ========================================================
    # RISK ANALYSIS
    # ========================================================

    st.header("⚠️ Risk Assessment")

    risk_score = result.get(
        "risk_score",
        0
    )

    risk_level = result.get(
        "risk_level",
        security_event["severity"]
    )


    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Risk Score",
            f"{risk_score}/100"
        )

    with col2:

        st.metric(
            "Risk Level",
            risk_level
        )


    # ========================================================
    # AGENT RESULTS
    # ========================================================

    st.header("🧠 Multi-Agent Investigation")

    col1, col2 = st.columns(2)


    with col1:

        st.subheader("MQTT Agent")

        mqtt_findings = result.get(
            "mqtt_findings",
            []
        )

        for finding in mqtt_findings:

            st.write(
                "✓ " + finding
            )


        st.subheader(
            "Authentication Agent"
        )

        auth_findings = result.get(
            "authentication_findings",
            result.get(
                "auth_findings",
                []
            )
        )

        if auth_findings:

            for finding in auth_findings:

                st.write(
                    "✓ " + finding
                )

        else:

            st.write(
                "✓ No unauthorized activity detected."
            )


    with col2:

        st.subheader(
            "Investigation Agent"
        )

        if investigation:

            st.write(
                "✓ Evidence correlation completed."
            )

        else:

            st.write(
                "✓ Investigation completed."
            )


        st.subheader(
            "Risk Agent"
        )

        st.write(
            f"✓ Risk Score: {risk_score}"
        )

        st.write(
            f"✓ Risk Level: {risk_level}"
        )


    st.divider()


    # ========================================================
    # RESPONSE RECOMMENDATIONS
    # ========================================================

    st.header("🛡️ Recommended Security Actions")

    recommendations = result.get(
        "recommendations",
        result.get(
            "response_actions",
            []
        )
    )


    if recommendations:

        for action in recommendations:

            st.warning(
                "→ " + action
            )

    else:

        st.info(
            "Review the security event and "
            "continue monitoring the MQTT broker."
        )


else:

    st.info(
        "Select a security scenario from the sidebar "
        "and click **Run Security Analysis**."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AgentSec-MQTT | MQTT Intrusion Detection | "
    "LangGraph + Random Forest + Multi-Agent Security Analysis"
)

