import time
import paho.mqtt.client as mqtt


BROKER = "localhost"
PORT = 1883
TOPIC = "/factory/control"


def main():

    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2
    )

    print("=" * 60)
    print("          MQTT REPLAY ATTACK SIMULATOR")
    print("=" * 60)

    print()
    print("Connecting to MQTT broker...")

    client.connect(
        BROKER,
        PORT,
        60
    )

    print("Connected successfully.")
    print()

    # This represents a legitimate MQTT message
    original_message = "temperature=25"

    print("Captured MQTT message:")
    print(f"  {original_message}")

    print()
    print("Replaying captured message...")
    print()

    # Replay the same message multiple times
    for i in range(20):

        client.publish(
            TOPIC,
            original_message
        )

        print(
            f"Replay #{i + 1}: {original_message}"
        )

        # Very small delay creates unusually high frequency
        time.sleep(0.1)

    client.disconnect()

    print()
    print("=" * 60)
    print("Replay attack simulation completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()