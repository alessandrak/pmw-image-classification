import numpy as np
from keras.engine.functional import Functional
from tensorflow import keras
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image


def load_best_model() -> Functional:
    model_name = "best_model"
    model = keras.models.load_model(model_name)
    return model


def predict_image(img_path: str) -> str:
    # Load and process the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    # Load the best model
    model = load_best_model()
    prediction = model.predict(img_preprocessed)
    # Predict
    result = np.where(prediction.flatten().round(2) > 0.5, 1, 0)
    return "PMW" if result[0] == 0 else "not-PMW"
