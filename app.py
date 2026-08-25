import os
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

IMAGE_SIZE = (350, 350)
MODEL_PATH = os.path.join("model", "best_model.hdf5")
CLASS_LABELS = [
    "Normal",
    "Adenocarcinoma",
    "Large Cell Carcinoma",
    "Squamous Cell Carcinoma",
]

@st.cache_resource
def load_model_with_weights():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model weights not found at '{MODEL_PATH}'. "
            "Place best_model.hdf5 in the model/ folder."
        )

    base = tf.keras.applications.Xception(
        weights="imagenet",
        include_top=False,
        input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3),
    )
    base.trainable = False

    model = tf.keras.Sequential([
        base,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(4, activation="softmax"),
    ])
    model.load_weights(MODEL_PATH)
    return model

def preprocess(image: Image.Image):
    image = image.convert("RGB").resize(IMAGE_SIZE)
    arr = np.asarray(image, dtype=np.float32) / 255.0
    return np.expand_dims(arr, axis=0), image

st.set_page_config(
    page_title="Lung Cancer CT Classifier",
    page_icon="🫁",
    layout="centered",
)

st.title("🫁 Lung Cancer CT Image Classification")
st.write(
    "Research/educational application using Xception transfer learning "
    "to classify CT images into four classes."
)

st.info(
    "This application is not a medical diagnostic tool. "
    "Predictions should not be used for clinical decisions."
)

uploaded = st.file_uploader(
    "Upload a CT scan image",
    type=["png", "jpg", "jpeg"],
)

if uploaded is not None:
    image = Image.open(uploaded)
    st.image(image, caption="Uploaded image", use_container_width=True)

    if st.button("Predict"):
        with st.spinner("Loading model and predicting..."):
            try:
                model = load_model_with_weights()
                x, processed = preprocess(image)
                probabilities = model.predict(x, verbose=0)[0]
                idx = int(np.argmax(probabilities))
                label = CLASS_LABELS[idx]
                confidence = float(probabilities[idx]) * 100

                st.success(f"Prediction: {label}")
                st.metric("Confidence", f"{confidence:.2f}%")

                st.subheader("Class probabilities")
                for name, probability in zip(CLASS_LABELS, probabilities):
                    st.write(f"{name}: {probability * 100:.2f}%")

            except Exception as exc:
                st.error(str(exc))
                st.caption(
                    "Ensure model/best_model.hdf5 is present. "
                    "It is intentionally excluded from GitHub because it is a large file."
                )

st.divider()
st.caption("Lung Cancer Prediction • Xception Transfer Learning")
