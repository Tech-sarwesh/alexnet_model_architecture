# alexnet_model_architecture
🐶🐱 A simple yet powerful CNN built using the classic AlexNet architecture to classify images of cats and dogs. Trained on the popular Kaggle dataset, this project helped me understand deep learning fundamentals, experiment with data augmentation, and fine-tune hyperparameters for binary image classification

# 🐶🐱 Cats vs Dogs Classification with Alexnet(with UI using Django)  

**CODE_BY:** [tech_sarwesh](https://github.com/tech-sarwesh)  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red?style=for-the-badge&logo=keras&logoColor=white)

<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100"><img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="100">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="100">


---

## 📖 Project Description  
This project is a Django-based web application that allows users to upload an image and predict whether it contains a Cat or Dog using the AlexNet deep learning architecture converted to TFLite for lightweight inference.  

Features

Upload an image and get instant predictions: Cat 🐱 or Dog 🐶.
Uses TFLite for fast inference, suitable for web deployment.
Lightweight and easy-to-use Django web interface.
Shows uploaded image along with prediction.

---

## 📦 Requirements  

```bash
Django==5.2.6
numpy==1.24.4
Pillow==10.0.0
tflite-runtime==2.12.0
```

## ⚙️ Installation

Follow these steps to set up the project:
```bash
git clone https://github.com/Tech-sarwesh/alexnet_model_architecture.git
cd alexnet_model_architecture
```
```bash
python3 -m venv alexnetenv
source alexnetenv/bin/activate       # Linux / macOS
alexnetenv\Scripts\activate          # Windows
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```
---
## Update(SOON.....)

In Update - 
- Add API feature
- Ui Enhance
- Model prediction enhance

---

## IMAGES

![SCR-1](https://github.com/Tech-sarwesh/alexnet_model_architecture/blob/main/scr1.png)
--
![SCR-2](https://github.com/Tech-sarwesh/alexnet_model_architecture/blob/main/scr2.png)
--
