import joblib
import pandas as pd
from pathlib import Path

from agent_state import AgentState


PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_FILE = PROJECT_ROOT / "ml" / "model.pkl"


def ml_agent(state: AgentState):

    print()
    print("=" * 60)
    print("                 ML AGENT")
    print("=" * 60)

    # ---------------------------------------------------------
    # Load trained model
    # ---------------------------------------------------------

    model = joblib.load(MODEL_FILE)

    # ---------------------------------------------------------
    # Create feature data
    # ---------------------------------------------------------

    features = pd.DataFrame(
        [[
            state["total_messages"],
            state["unique_payloads"],
            state["duplicate_ratio"],
            state["message_frequency"],
            state.get("topic_frequency", 10.0),
            state.get("payload_length", 25.0),
            state.get("time_interval", 0.1)
        ]],
        columns=[
            "total_messages",
            "unique_payloads",
            "duplicate_ratio",
            "message_frequency",
            "topic_frequency",
            "payload_length",
            "time_interval"
        ]
    )

    # ---------------------------------------------------------
    # Print features for debugging
    # ---------------------------------------------------------

    print()
    print("Features sent to ML model:")

    for column in features.columns:

        print(
            f"  → {column}: {features.iloc[0][column]}"
        )

    print()

    # ---------------------------------------------------------
    # Make prediction
    # ---------------------------------------------------------

    prediction = model.predict(features)[0]

    probabilities = model.predict_proba(features)[0]

    confidence = max(probabilities)

    # ---------------------------------------------------------
    # Convert prediction to attack name
    # ---------------------------------------------------------

    if prediction == 0:

        attack = "Normal Traffic"

    elif prediction == 1:

        attack = "Replay Attack"

    elif prediction == 2:

        attack = "MQTT Flood / DoS Attack"

    else:

        attack = "Unknown"

    # ---------------------------------------------------------
    # Create finding
    # ---------------------------------------------------------

    finding = (
        f"{attack} classification "
        f"confidence: {confidence:.2%}"
    )

    # ---------------------------------------------------------
    # Display result
    # ---------------------------------------------------------

    print(
        f"Prediction: {attack}"
    )

    print(
        f"Confidence: {confidence:.2%}"
    )

    print()

    return {

        "ml_findings": [
            finding
        ]
    }