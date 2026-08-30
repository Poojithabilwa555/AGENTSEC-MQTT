import time

from security_event import SecurityEvent


TOPIC = "/factory/control"


def detect_attack(
    messages,
    first_message_time,
    last_message_time
):

    total_messages = len(messages)

    if total_messages == 0:
        return None

    unique_messages = len(set(messages))

    duplicate_ratio = (
        total_messages - unique_messages
    ) / total_messages

    if (
        first_message_time is not None
        and last_message_time is not None
    ):

        elapsed_time = (
            last_message_time
            - first_message_time
        )

        if elapsed_time <= 0:
            frequency = total_messages

        else:
            frequency = (
                total_messages
                / elapsed_time
            )

    else:
        frequency = 0

    topic_frequency = frequency

    if messages:

        payload_length = len(
            messages[-1]
        )

    else:

        payload_length = 0

    time_interval = (
        1 / frequency
        if frequency > 0
        else 0
    )

    # -----------------------------------------
    # Replay Attack Detection
    # -----------------------------------------

    if (
        duplicate_ratio >= 0.80
        and frequency >= 5
    ):

        attack = "Replay Attack"
        severity = "CRITICAL"

    # -----------------------------------------
    # Flood / DoS Detection
    # -----------------------------------------

    elif frequency >= 50:

        attack = "MQTT Flood Attack"
        severity = "CRITICAL"

    # -----------------------------------------
    # Normal Traffic
    # -----------------------------------------

    else:

        attack = "Normal Traffic"
        severity = "LOW"

    event = SecurityEvent(

        alert_id="ALERT-001",

        topic=TOPIC,

        attack=attack,

        total_messages=total_messages,

        unique_payloads=unique_messages,

        duplicate_ratio=duplicate_ratio,

        message_frequency=frequency,

        severity=severity
    )

    return event