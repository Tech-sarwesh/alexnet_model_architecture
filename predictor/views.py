from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image
import os

# Load TFLite model once
MODEL_PATH = os.path.join(settings.BASE_DIR, "predictor", "alexnet_model.tflite")
interpreter = tflite.Interpreter(model_path=MODEL_PATH)   # ✅ fixed
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def preprocess_image(image_path):
    img = Image.open(image_path).resize((224, 224))  
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0).astype(np.float32)
    return img

def index(request):
    return render(request, "index.html")

def predict_image(request):
    # Add signature by default
    context = {"signature": "Code by Tech_Sarwesh"}

    if request.method == "POST" and request.FILES.get("image"):
        upload = request.FILES["image"]
        fs = FileSystemStorage()
        file_path = fs.save(upload.name, upload)
        full_path = fs.path(file_path)

        # Preprocess
        img = preprocess_image(full_path)

        # Run inference
        interpreter.set_tensor(input_details[0]["index"], img)
        interpreter.invoke()
        prediction = interpreter.get_tensor(output_details[0]["index"])[0][0]

        result = "Dog" if prediction > 0.5 else "Cat"

        # Update context with result and uploaded image
        context.update({
            "result": result,
            "uploaded_image": fs.url(file_path),
        })

    return render(request, "index.html", context)
