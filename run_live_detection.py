import time
import sys
from pathlib import Path

import paho.mqtt.client as mqtt


# ---------------------------------------------------------
# Project Root
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ---------------------------------------------------------
# Project Imports
# ---------------------------------------------------------

from mqtt_detection import detect_attack
from workflow import build_workflow


# ---------------------------------------------------------
# MQTT Configuration
# ---------------------------------------------------------

BROKER = "localhost"
PORT = 1883
TOPIC = "/factory/control"


# ---------------------------------------------------------
# Traffic Storage
# ---------------------------------------------------------

messages = []

first_message_time = None
last_message_time = None


# ---------------------------------------------------------
# MQTT Connection
# ---------------------------------------------------------

def on_connect(client, userdata, flags, reason_code, properties):

    print()
    print("Connected to MQTT broker.")

    client.subscribe(TOPIC)

    print(f"Monitoring topic: {TOPIC}")
    print()


# ---------------------------------------------------------
# MQTT Message
# ---------------------------------------------------------

def on_message(client, userdata, message):

    global first_message_time
    global last_message_time

    current_time = time.time()

    if first_message_time is None:
        first_message_time = current_time

    last_message_time = current_time

    payload = message.payload.decode(
        "utf-8",
        errors="ignore"
    )

    messages.append(payload)

    print(f"Received: {payload}")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    print("=" * 60)
    print("       AGENTSEC-MQTT LIVE SECURITY PIPELINE")
    print("=" * 60)

    print()
    print("Connecting to MQTT broker...")

    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2
    )

    client.on_connect = on_connect
    client.on_message = on_message

    try:

        client.connect(
            BROKER,
            PORT,
            60
        )

    except Exception as e:

        print()
        print("ERROR: Could not connect to MQTT broker.")
        print(f"Details: {e}")

        return

    client.loop_start()

    print()
    print("Waiting for MQTT traffic...")
    print("Generate an attack from another PowerShell window.")
    print("Press CTRL+C after the attack finishes.")
    print()

    try:

        while True:

            time.sleep(1)

    except KeyboardInterrupt:

        print()
        print("Stopping live monitor...")

    finally:

        try:
            client.disconnect()
        except Exception:
            pass

        try:
            client.loop_stop()
        except Exception:
            pass
    # -----------------------------------------------------
    # Check Traffic
    # -----------------------------------------------------

    if len(messages) == 0:

        print()
        print("No MQTT traffic detected.")

        return

    # -----------------------------------------------------
    # Detect Attack
    # -----------------------------------------------------

    security_event = detect_attack(
        messages,
        first_message_time,
        last_message_time
    )

    if security_event is None:

        print()
        print("Could not create security event.")

        return

    # -----------------------------------------------------
    # Display Event
    # -----------------------------------------------------

    print()
    print("=" * 60)
    print("             DETECTED SECURITY EVENT")
    print("=" * 60)

    print()
    print(security_event)

    # -----------------------------------------------------
    # Convert SecurityEvent to Dictionary
    # -----------------------------------------------------

    event_data = {

        "alert_id": security_event.alert_id,

        "topic": security_event.topic,

        "attack": security_event.attack,

        "total_messages": security_event.total_messages,

        "unique_payloads": security_event.unique_payloads,

        "duplicate_ratio": security_event.duplicate_ratio,

        "message_frequency": security_event.message_frequency,

        "severity": security_event.severity,

        "topic_frequency": security_event.message_frequency,

        "payload_length": (
            len(messages[-1])
            if messages
            else 0
        ),

        "time_interval": (
            1 / security_event.message_frequency
            if security_event.message_frequency > 0
            else 0
        )
    }

    # -----------------------------------------------------
    # Build LangGraph Workflow
    # -----------------------------------------------------

    print()
    print("=" * 60)
    print("        STARTING LANGGRAPH WORKFLOW")
    print("=" * 60)

    print()

    workflow = build_workflow()

    # -----------------------------------------------------
    # Invoke Multi-Agent System
    # -----------------------------------------------------

    result = workflow.invoke(
        event_data
    )

    # -----------------------------------------------------
    # Final Output
    # -----------------------------------------------------

    print()
    print("=" * 60)
    print("       LIVE SECURITY ANALYSIS COMPLETE")
    print("=" * 60)

    print()

    print("Attack:", result.get("attack"))

    print(
        "Severity:",
        result.get("severity")
    )

    print()

    print("MQTT Findings:")

    for finding in result.get(
        "mqtt_findings",
        []
    ):

        print(
            f"  ✓ {finding}"
        )

    print()

    print("Log Findings:")

    for finding in result.get(
        "log_findings",
        []
    ):

        print(
            f"  ✓ {finding}"
        )

    print()

    print("ML Findings:")

    for finding in result.get(
        "ml_findings",
        []
    ):

        print(
            f"  ✓ {finding}"
        )

    print()

    if result.get("investigation"):

        print("Investigation:")

        print(
            f"  → {result['investigation']}"
        )

        print()

    if result.get("risk_score") is not None:

        print("Risk Score:")

        print(
            f"  → {result['risk_score']}"
        )

        print()

    if result.get("risk_level"):

        print("Risk Level:")

        print(
            f"  → {result['risk_level']}"
        )

        print()

    if result.get("recommendations"):

        print("Recommendations:")

        for recommendation in result[
            "recommendations"
        ]:

            print(
                f"  → {recommendation}"
            )

    print()
    print("=" * 60)
    print("             END OF ANALYSIS")
    print("=" * 60)


# ---------------------------------------------------------
# Program Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":

    main()