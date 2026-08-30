import csv
import random


OUTPUT_FILE = "ml/dataset.csv"

SAMPLES_PER_CLASS = 500


def generate_normal():

    total_messages = random.randint(15, 40)

    unique_payloads = random.randint(
        int(total_messages * 0.60),
        total_messages
    )

    duplicate_ratio = (
        total_messages - unique_payloads
    ) / total_messages

    message_frequency = random.uniform(
        0.5,
        5.0
    )

    topic_frequency = random.uniform(
        0.5,
        5.0
    )

    payload_length = random.randint(
        10,
        30
    )

    time_interval = random.uniform(
        0.2,
        2.0
    )

    label = 0

    return [
        total_messages,
        unique_payloads,
        round(duplicate_ratio, 4),
        round(message_frequency, 4),
        round(topic_frequency, 4),
        payload_length,
        round(time_interval, 4),
        label
    ]


def generate_replay():

    total_messages = random.randint(
        15,
        30
    )

    unique_payloads = random.randint(
        1,
        5
    )

    duplicate_ratio = (
        total_messages - unique_payloads
    ) / total_messages

    message_frequency = random.uniform(
        5.0,
        15.0
    )

    topic_frequency = random.uniform(
        5.0,
        15.0
    )

    payload_length = random.randint(
        10,
        30
    )

    time_interval = random.uniform(
        0.05,
        0.2
    )

    label = 1

    return [
        total_messages,
        unique_payloads,
        round(duplicate_ratio, 4),
        round(message_frequency, 4),
        round(topic_frequency, 4),
        payload_length,
        round(time_interval, 4),
        label
    ]


def generate_flood():

    total_messages = random.randint(
        80,
        200
    )

    unique_payloads = random.randint(
        int(total_messages * 0.80),
        total_messages
    )

    duplicate_ratio = (
        total_messages - unique_payloads
    ) / total_messages

    message_frequency = random.uniform(
        30.0,
        100.0
    )

    topic_frequency = random.uniform(
        30.0,
        100.0
    )

    payload_length = random.randint(
        10,
        30
    )

    time_interval = random.uniform(
        0.005,
        0.03
    )

    label = 2

    return [
        total_messages,
        unique_payloads,
        round(duplicate_ratio, 4),
        round(message_frequency, 4),
        round(topic_frequency, 4),
        payload_length,
        round(time_interval, 4),
        label
    ]


def main():

    print("=" * 60)
    print("       AGENTSEC-MQTT DATASET GENERATOR")
    print("=" * 60)

    print()

    rows = []

    print("Generating Normal Traffic samples...")

    for _ in range(SAMPLES_PER_CLASS):

        rows.append(
            generate_normal()
        )

    print("Generating Replay Attack samples...")

    for _ in range(SAMPLES_PER_CLASS):

        rows.append(
            generate_replay()
        )

    print("Generating MQTT Flood / DoS samples...")

    for _ in range(SAMPLES_PER_CLASS):

        rows.append(
            generate_flood()
        )

    random.shuffle(rows)

    headers = [

        "total_messages",

        "unique_payloads",

        "duplicate_ratio",

        "message_frequency",

        "topic_frequency",

        "payload_length",

        "time_interval",

        "label"
    ]

    with open(
        OUTPUT_FILE,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            headers
        )

        writer.writerows(
            rows
        )

    print()

    print(
        f"Dataset created: {OUTPUT_FILE}"
    )

    print(
        f"Total samples: {len(rows)}"
    )

    print()

    print("Class distribution:")

    print(
        "  0 → Normal Traffic: 500"
    )

    print(
        "  1 → Replay Attack: 500"
    )

    print(
        "  2 → MQTT Flood / DoS Attack: 500"
    )

    print()

    print("=" * 60)


if __name__ == "__main__":

    main()