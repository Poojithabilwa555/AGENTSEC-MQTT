import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report
)

import joblib


DATASET = "ml/dataset.csv"

MODEL_FILE = "ml/model.pkl"


def main():

    print("=" * 60)
    print("          AGENTSEC-MQTT ML TRAINING")
    print("=" * 60)

    print()

    # Load dataset
    data = pd.read_csv(DATASET)

    print(
        f"Dataset size: {len(data)}"
    )

    print()

    # Features used by the ML model
    features = [

        "total_messages",

        "unique_payloads",

        "duplicate_ratio",

        "message_frequency",

        "topic_frequency",

        "payload_length",

        "time_interval"
    ]

    X = data[features]

    y = data["label"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42,

        stratify=y
    )

    print(
        f"Training samples: {len(X_train)}"
    )

    print(
        f"Testing samples: {len(X_test)}"
    )

    print()

    # Create Random Forest model
    print("Training Random Forest model...")

    model = RandomForestClassifier(

        n_estimators=100,

        random_state=42
    )

    model.fit(

        X_train,

        y_train
    )

    # Test model
    predictions = model.predict(X_test)

    accuracy = accuracy_score(

        y_test,

        predictions
    )

    print()

    print(
        f"Model Accuracy: {accuracy:.2%}"
    )

    print()

    print("Classification Report:")

    print(

        classification_report(

            y_test,

            predictions,

            target_names=[

                "Normal Traffic",

                "Replay Attack",

                "MQTT Flood / DoS Attack"
            ]
        )
    )

    # Save model
    joblib.dump(

        model,

        MODEL_FILE
    )

    print(

        f"Model saved to: {MODEL_FILE}"
    )

    print()

    print("=" * 60)


if __name__ == "__main__":

    main()