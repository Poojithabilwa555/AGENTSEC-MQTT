# AGENTSEC-MQTT

## Multi-Agent AI Framework for MQTT Intrusion Detection and Security Analysis

AGENTSEC-MQTT is an AI-powered cybersecurity system designed to detect, investigate, assess, and respond to security threats in MQTT-based IoT environments.

The system combines **MQTT traffic analysis, machine learning, security-log analysis, threat intelligence, and LangGraph-based multi-agent orchestration** to provide an end-to-end intrusion detection and security analysis workflow.

---

## 🚨 Problem

MQTT is widely used in IoT environments because of its lightweight communication model. However, its deployments can be exposed to several security threats, including:

* MQTT Flood / Denial-of-Service attacks
* Unauthorized Publish activity
* Topic Spoofing
* Replay Attacks
* Brute-Force Login Attempts

Traditional monitoring approaches may detect individual suspicious events, but they often lack coordinated investigation, evidence correlation, risk assessment, and contextual response recommendations.

**AGENTSEC-MQTT addresses this gap by coordinating multiple specialized security agents to analyze an MQTT security event from different perspectives.**

---

## 💡 Solution

AGENTSEC-MQTT follows a multi-stage security analysis pipeline:

```text
MQTT Traffic
     ↓
MQTT Monitoring
     ↓
Supervisor Agent
     ↓
Multi-Agent Security Analysis
     ↓
Machine Learning Classification
     ↓
Evidence Investigation
     ↓
Risk Assessment
     ↓
Response Recommendation
     ↓
Human Approval
```

The architecture allows different agents to independently analyze security evidence before the final risk and response decision is produced.

---

## 🧠 Multi-Agent Architecture

The system contains specialized agents responsible for different aspects of security analysis.

### Supervisor Agent

Coordinates the investigation workflow and determines which security analysis components should be executed for an incoming alert.

### MQTT Agent

Analyzes MQTT traffic and identifies suspicious characteristics such as unusually high message frequency, high traffic volume, and abnormal MQTT activity.

### Authentication Agent

Analyzes authentication and publishing activity to identify potential unauthorized MQTT operations.

### Log Agent

Analyzes security logs to identify repeated or suspicious activity associated with devices or events.

### ML Agent

Uses a machine-learning model to classify MQTT traffic based on extracted traffic features.

### Investigation Agent

Correlates evidence from MQTT analysis, security logs, and ML classification to determine whether the available evidence supports the detected threat.

### Risk Agent

Converts the investigation results into a risk score and severity level.

### Response Agent

Generates recommended security actions based on the detected threat and calculated risk.

### Threat Intelligence Agent

Provides additional context using available threat-intelligence information.

---

## 🤖 Machine Learning

The ML pipeline extracts traffic-level features from MQTT activity, including:

* Total messages
* Unique payloads
* Duplicate ratio
* Message frequency
* Topic frequency
* Payload length
* Time interval

The trained model is currently used to classify traffic into categories such as:

* Normal Traffic
* MQTT Flood / DoS Attack

### Example ML Input

```text
total_messages: 100
unique_payloads: 100
duplicate_ratio: 0.0
message_frequency: 64.27
topic_frequency: 64.27
payload_length: 15
time_interval: 0.015
```

### Example Prediction

```text
Prediction: MQTT Flood / DoS Attack
Confidence: 100.00%
```

> Note: The displayed confidence represents the model's prediction confidence for the demonstrated event. It should not be interpreted as overall model accuracy.

---

## 🔍 Detection Example

### 🔴 Scenario 1 — MQTT Flood / DoS

The system detected extremely high-frequency MQTT traffic associated with:

```text
Topic: /factory/control
Device: device_27
```

The multi-agent workflow produced:

```text
Prediction: MQTT Flood / DoS Attack
Confidence: 100.00%

Risk Score: 90
Risk Level: CRITICAL
```

The response agent recommended:

* Rate-limiting MQTT messages from the affected source
* Monitoring the MQTT broker for continued high-frequency traffic
* Identifying the source device
* Considering temporary containment if the attack continues
* Requiring human analyst approval before containment

---

### 🟢 Scenario 2 — Normal MQTT Traffic

The system was also tested with benign MQTT traffic.

Example features:

```text
total_messages: 20
unique_payloads: 18
duplicate_ratio: 0.1
message_frequency: 2.0
topic_frequency: 2.0
payload_length: 15
time_interval: 0.5
```

Prediction:

```text
Prediction: Normal Traffic
Confidence: 100.00%

Risk Score: 5
Risk Level: LOW
```

The response agent recommended continued monitoring without immediate containment.

---

## 🏗️ System Architecture

```text
                         MQTT / IoT TRAFFIC
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  MQTT MONITOR   │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │    SUPERVISOR   │
                         │      AGENT      │
                         └────────┬────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
        MQTT AGENT           LOG AGENT        AUTHENTICATION
              │                   │              AGENT
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  │
                                  ▼
                            ┌───────────┐
                            │ ML AGENT  │
                            └─────┬─────┘
                                  │
                                  ▼
                       ┌────────────────────┐
                       │ INVESTIGATION AGENT│
                       └──────────┬─────────┘
                                  │
                                  ▼
                            ┌───────────┐
                            │ RISK AGENT│
                            └─────┬─────┘
                                  │
                                  ▼
                          ┌────────────────┐
                          │ RESPONSE AGENT │
                          └───────┬────────┘
                                  │
                                  ▼
                         HUMAN APPROVAL
```

---

## 🖥️ Dashboard

The project includes a **Streamlit-based security dashboard** for presenting the results of the multi-agent investigation.

The dashboard is designed to visualize:

* Security alerts
* Attack classification
* ML confidence
* Risk score
* Severity level
* Agent findings
* Recommended response actions

Run the dashboard using:

```bash
streamlit run dashboard.py
```

Then open:

```text
http://localhost:8501
```

---

## 🧪 Demonstrated Scenarios

### Scenario 1 — MQTT Flood / DoS

```text
MQTT Traffic
     ↓
MQTT Agent
     ↓
ML Agent
     ↓
Investigation Agent
     ↓
Risk Score: 90
     ↓
CRITICAL
     ↓
Response Recommendation
```

### Scenario 2 — Normal MQTT Traffic

```text
MQTT Traffic
     ↓
MQTT Agent
     ↓
ML Agent
     ↓
Investigation Agent
     ↓
Risk Score: 5
     ↓
LOW
     ↓
Continue Monitoring
```

---

## 🔐 Security Approach

AGENTSEC-MQTT follows a **human-in-the-loop security model**.

The system generates recommended containment and mitigation actions rather than automatically performing potentially disruptive security operations.

This approach is intended to reduce the impact of false positives and keep final containment decisions under human analyst control.

---

## 🛠️ Technology Stack

| Technology   | Purpose                                        |
| ------------ | ---------------------------------------------- |
| Python       | Core implementation                            |
| MQTT         | IoT messaging protocol                         |
| Mosquitto    | MQTT broker and security configuration         |
| LangGraph    | Multi-agent workflow orchestration             |
| Scikit-learn | Machine learning                               |
| Streamlit    | Security dashboard                             |
| JSON         | Alerts and threat-intelligence data            |
| Wireshark    | MQTT traffic analysis / investigation workflow |

---

## 📂 Project Structure

```text
AGENTSEC-MQTT/
│
├── agents/
│   ├── __init__.py
│   ├── auth_agent.py
│   ├── investigation_agent.py
│   ├── log_agent.py
│   ├── ml_agent.py
│   ├── mqtt_agent.py
│   ├── response_agent.py
│   ├── risk_agent.py
│   ├── supervisor.py
│   └── threat_intel_agent.py
│
├── data/
│   ├── sample_alerts.json
│   └── threat_intelligence/
│       └── ip_reputation.json
│
├── graph/
│   ├── __init__.py
│   ├── state.py
│   └── workflow.py
│
├── ml/
│   ├── dataset.csv
│   ├── dataset_generator.py
│   ├── train_model.py
│   └── model.pkl
│
├── mqtt_security/
│   ├── acl.conf
│   ├── mosquitto.conf
│   └── passwd
│
├── simulation/
│   ├── __init__.py
│   ├── flood_attack.py
│   ├── mqtt_monitor.py
│   ├── mqtt_simulator.py
│   ├── replay_attack.py
│   └── unauthorized_publish.py
│
├── tools/
│   ├── __init__.py
│   └── llm.py
│
├── dashboard.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Future Improvements

The current prototype can be extended with:

* Real-time MQTT packet ingestion
* Additional attack-classification models
* SHAP-based ML explainability
* Real-time broker monitoring
* Persistent security-event storage
* Advanced threat-intelligence integration
* Containerized deployment
* Cloud deployment
* SOC/SIEM alert integration
* Additional MQTT attack scenarios

---

## 🎯 Project Highlights

* **Multi-agent cybersecurity architecture**
* **LangGraph-based workflow orchestration**
* **Machine-learning-based MQTT traffic classification**
* **MQTT-specific security analysis**
* **Evidence correlation across multiple agents**
* **Risk scoring and severity assessment**
* **Human-in-the-loop response recommendations**
* **Streamlit security dashboard**
* **Attack and benign traffic simulation**

---

## 👩‍💻 Author

**Poojitha Vadlamudi**

B.Tech Computer Science & Engineering
