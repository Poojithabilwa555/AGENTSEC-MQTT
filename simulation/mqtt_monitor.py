import time
import paho.mqtt.client as mqtt

from pathlib import Path
import sys


# =========================================================
# IMPORT SECURITY EVENT
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from security_event import SecurityEvent


# =========================================================
# MQTT CONFIGURATION
# =========================================================

BROKER = "localhost"
PORT = 1883
TOPIC = "/factory/control"

USERNAME = "agentsec"
PASSWORD = "1234"


# =========================================================
# TRAFFIC STORAGE
# =========================================================

messages = []

first_message_time = None
last_message_time = None


# =========================================================
# MQTT CONNECT
# =========================================================

def on_connect(client, userdata, flags, reason_code, properties):

    print()

    if reason_code == 0:

        print("Connected to MQTT broker.")
        print(f"Monitoring topic: {TOPIC}")
        print()

        client.subscribe(TOPIC)

    else:

        print(
            f"MQTT connection failed. "
            f"Reason code: {reason_code}"
        )


# =========================================================
# MQTT DISCONNECT
# =========================================================

def on_disconnect(
    client,
    userdata,
    disconnect_flags,
    reason_code,
    properties
):

    print()

    if reason_code == 0:

        print(
            "MQTT disconnected. "
            "Reason code: Normal disconnection"
        )

    else:

        print(
            f"MQTT disconnected. "
            f"Reason code: {reason_code}"
        )


# =========================================================
# MQTT MESSAGE
# =========================================================

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

    print(
        f"Received: {payload}"
    )


# =========================================================
# TRAFFIC ANALYSIS
# =========================================================

def analyze_traffic():

    print()
    print("=" * 60)
    print("             TRAFFIC ANALYSIS")
    print("=" * 60)

    total_messages = len(messages)

    print()
    print(
        f"Total messages: {total_messages}"
    )

    if total_messages == 0:

        print()
        print("No MQTT traffic detected.")

        print()
        print("=" * 60)

        return None

    # -----------------------------------------------------
    # UNIQUE PAYLOADS
    # -----------------------------------------------------

    unique_messages = len(
        set(messages)
    )

    print(
        f"Unique payloads: {unique_messages}"
    )

    # -----------------------------------------------------
    # DUPLICATE RATIO
    # -----------------------------------------------------

    duplicate_ratio = (
        total_messages - unique_messages
    ) / total_messages

    print(
        f"Duplicate payload ratio: "
        f"{duplicate_ratio:.2%}"
    )

    # -----------------------------------------------------
    # MESSAGE FREQUENCY
    # -----------------------------------------------------

    if (
        first_message_time is not None
        and last_message_time is not None
    ):

        elapsed_time = (
            last_message_time
            - first_message_time
        )

        if elapsed_time <= 0:

            frequency = float(
                total_messages
            )

        else:

            frequency = (
                total_messages
                / elapsed_time
            )

    else:

        frequency = 0.0

    print(
        f"Message frequency: "
        f"{frequency:.2f} messages/sec"
    )

    print()

    # =====================================================
    # ATTACK DETECTION
    # =====================================================

    attack = "Normal Traffic"

    severity = "LOW"

    findings = []

    # =====================================================
    # REPLAY ATTACK
    # =====================================================

    if (
        duplicate_ratio >= 0.80
        and frequency >= 5
    ):

        attack = "Replay Attack"

        severity = "CRITICAL"

        findings.append(
            "Very high duplicate MQTT payload ratio detected."
        )

        findings.append(
            "Abnormally high MQTT packet frequency detected."
        )

        findings.append(
            "Repeated MQTT payload detected."
        )

        print(
            "🚨 POSSIBLE REPLAY ATTACK DETECTED"
        )

    # =====================================================
    # MQTT FLOOD / DOS
    # =====================================================

    elif frequency >= 30:

        attack = "MQTT Flood / DoS Attack"

        severity = "CRITICAL"

        findings.append(
            "Extremely high MQTT message frequency detected."
        )

        findings.append(
            "Large number of MQTT messages received "
            "in a short time."
        )

        findings.append(
            "Traffic pattern is consistent with "
            "an MQTT flood attack."
        )

        print(
            "🚨 POSSIBLE MQTT FLOOD / DOS ATTACK DETECTED"
        )

    # =====================================================
    # HIGH RATE TRAFFIC
    # =====================================================

    elif frequency >= 10:

        attack = "Suspicious High-Rate MQTT Traffic"

        severity = "HIGH"

        findings.append(
            "Abnormally high MQTT message frequency detected."
        )

        findings.append(
            "Traffic rate exceeds the normal "
            "monitoring threshold."
        )

        print(
            "⚠️ SUSPICIOUS HIGH-RATE MQTT TRAFFIC"
        )

    # =====================================================
    # NORMAL
    # =====================================================

    else:

        print(
            "✓ Traffic appears normal."
        )

    # =====================================================
    # EVIDENCE
    # =====================================================

    if findings:

        print()
        print("Detection Evidence:")

        for finding in findings:

            print(
                f"  → {finding}"
            )

    # =====================================================
    # SECURITY EVENT
    # =====================================================

    if attack != "Normal Traffic":

        security_event = SecurityEvent(

            alert_id="ALERT-001",

            topic=TOPIC,

            attack=attack,

            total_messages=total_messages,

            unique_payloads=unique_messages,

            duplicate_ratio=duplicate_ratio,

            message_frequency=frequency,

            severity=severity
        )

        print()
        print("=" * 60)
        print("             SECURITY EVENT")
        print("=" * 60)

        print()

        print(
            security_event
        )

        print()
        print("=" * 60)

        return security_event

    print()
    print("=" * 60)

    return None


# =========================================================
# MAIN
# =========================================================

def main():

    global messages
    global first_message_time
    global last_message_time

    messages = []

    first_message_time = None
    last_message_time = None

    print("=" * 60)
    print("           AGENTSEC-MQTT MONITOR")
    print("=" * 60)

    print()
    print("Connecting to MQTT broker...")
    print()
    print("Waiting for MQTT traffic...")
    print()

    client = mqtt.Client(
        callback_api_version=
        mqtt.CallbackAPIVersion.VERSION2
    )

    # -----------------------------------------------------
    # MQTT AUTHENTICATION
    # -----------------------------------------------------

    client.username_pw_set(
        USERNAME,
        PASSWORD
    )

    # -----------------------------------------------------
    # CALLBACKS
    # -----------------------------------------------------

    client.on_connect = on_connect

    client.on_disconnect = on_disconnect

    client.on_message = on_message

    try:

        client.connect(
            BROKER,
            PORT,
            60
        )

        # -------------------------------------------------
        # Run MQTT network loop
        # -------------------------------------------------

        client.loop_forever()

    except KeyboardInterrupt:

        print()
        print("Stopping monitor...")

        try:

            client.disconnect()

        except Exception:

            pass

    except Exception as e:

        print()
        print(
            "MQTT error:",
            e
        )

        try:

            client.disconnect()

        except Exception:

            pass

    # =====================================================
    # ANALYZE AFTER MQTT LOOP STOPS
    # =====================================================

    print()
    print("Analyzing captured traffic...")

    try:

        analyze_traffic()

    except KeyboardInterrupt:

        print()
        print(
            "Analysis interrupted."
        )


# =========================================================
# START PROGRAM
# =========================================================

if __name__ == "__main__":

    main()

