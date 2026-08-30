import time
import paho.mqtt.client as mqtt


BROKER = "localhost"
PORT = 1883
TOPIC = "/factory/control"


def main():

    client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

    print("Connecting to MQTT broker...")

    client.connect(
        BROKER,
        PORT,
        60
    )

    print("Connected successfully.")
    print()
    print("Sending MQTT traffic...")
    print()

    for i in range(10):

        temperature = 25 + i

        message = f"temperature={temperature}"

        result = client.publish(
            TOPIC,
            message
        )

        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Published: {message}")
        else:
            print("Failed to publish message")

        time.sleep(1)

    client.disconnect()

    print()
    print("MQTT simulation completed.")


if __name__ == "__main__":
    main()