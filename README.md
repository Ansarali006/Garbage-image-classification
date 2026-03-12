# ♻️ Garbage Classification using Deep Learning

## 📌 Project Overview

The project presents an end-to-end deep learning solution for **automatic garbage classification using computer vision**.  
The model is trained using **Transfer Learning with MobileNetV2 and EfficientNetB0** to classify waste images into multiple categories.

The final trained model is deployed using **Streamlit**, allowing users to upload an image and receive the predicted waste category.

---

## 🧠 Problem Statement

Build a deep learning model that classifies images of waste into categories like plastic, metal, glass, paper, and organic. This system will assist in automating recycling by sorting garbage based on image input, using a deep learning model deployed via a simple user interface.

---

## 🔄 Project Workflow

The project follows a structured machine learning pipeline from data preparation to deployment.

1. **Data Loading**
   - Images were loaded using TensorFlow's `image_dataset_from_directory`.
   - Training, validation, and testing datasets were created.

2. **Exploratory Data Analysis (EDA)**
   - Analyzed class distribution.
   - Visualized sample images from each class.
   - Examined pixel intensity distribution.

3. **Data Preprocessing**
   - Image resizing to **224 × 224**.
   - Pixel normalization.
   - Data augmentation techniques such as rotation, flipping, and zooming.

4. **Handling Class Imbalance**
   - Class weights were computed using **Scikit-learn**.
   - Minority classes were assigned higher weights to balance the training process.

5. **Model Development**
   - Transfer learning was applied using pretrained CNN architectures:
     - MobileNetV2
     - EfficientNetB0

6. **Model Training**
   - Stage 1: Feature extraction with frozen base layers.
   - Stage 2: Fine-tuning the last layers of the network.

7. **Model Evaluation**
   - Performance measured using:
     - Accuracy
     - Precision
     - Recall
     - F1 Score
     - Confusion Matrix

8. **Model Deployment**
   - The final model was integrated into a **Streamlit web application**.
   - Users can upload an image and receive the predicted waste category.

---
## 🛠 Technologies Used

1. Python  
2. TensorFlow / Keras  
3. NumPy  
4. Matplotlib  
5. Scikit-learn  
6. Streamlit

---

## 📂 Dataset

The dataset contains **15000+** images belonging to **12 garbage categories**.

1. **Classes included**
   - Battery
   - Biological
   - Brown Glass
   - Cardboard
   - Clothes
   - Green Glass
   - Metal
   - Paper
   - Plastic
   - Shoes
   - Trash
   - White Glass

2. **Dataset Characteristics**
   - Multi-class image dataset
   - Class imbalance present
   - Real-world waste images

---

## 📊 Exploratory Data Analysis

EDA was performed to understand the dataset.

1. **Class Distribution**
   - Analyzed the number of images in each category.
    <img width="1077" height="755" alt="image" src="https://github.com/user-attachments/assets/5ab912de-1c6b-407d-ba71-5ad0915efb5b" />


2. **Sample Image Visualization**
   - Displayed random images from each class.
    <img width="1020" height="695" alt="image" src="https://github.com/user-attachments/assets/61a18c02-6f19-4c30-99ba-9e5a3272c283" />


3. **Pixel Intensity Analysis**
   - Analyzed brightness distribution across images.
   <img width="1004" height="659" alt="image" src="https://github.com/user-attachments/assets/e6afbe2c-9678-44cd-b736-1761ed7e9ec6" />


---

## ⚙️ Data Preprocessing

Several preprocessing techniques were applied before model training.

1. **Image Resizing**
   - All images resized to **224 × 224**.

2. **Normalization**
   - Pixel values normalized to improve training stability.

3. **Data Augmentation**
   - Random Flip
   - Random Rotation
   - Random Zoom

4. **Class Weight Calculation**
   - Computed using `compute_class_weight` from Scikit-learn.

---


## 🤖 Model Development

Transfer learning was used to build the classification models.

1. **MobileNetV2**
   - Lightweight architecture suitable for efficient image classification.

2. **EfficientNetB0**
   - Advanced CNN architecture optimized for accuracy and efficiency.

3. **Custom Classification Head**
   - Global Average Pooling
   - Batch Normalization
   - Dense Layer
   - Dropout
   - Softmax Output Layer

---

## 🏋️ Model Training

Training was performed in two phases.

1. **Feature Extraction**
   - Base model layers were frozen.
   - Only custom classification layers were trained.

2. **Fine Tuning**
   - Last **30 layers of the base model were unfrozen**.
   - Model retrained using a lower learning rate.

---

## 📊 Model Evaluation

The model was evaluated using multiple performance metrics.

1. **Evaluation Metrics**
   - Accuracy
   - Precision
   - Recall
   - F1 Score

2. **Confusion Matrix**
   - Used to visualize prediction performance across classes.
   <img width="1120" height="781" alt="image" src="https://github.com/user-attachments/assets/c86ec05e-71de-4d82-976f-91eaa898e5af" />


---

## 📈 Model Performance

<img width="393" height="165" alt="image" src="https://github.com/user-attachments/assets/5f51e8fb-9ee3-4221-96b8-26f2ea5422f9" />

---

## 🚀 Streamlit Deployment

A Streamlit web application was developed to interact with the trained model.

1. **Application Features**
   - Upload waste image
   - Predict garbage category
   - Display prediction result
   <img width="1483" height="789" alt="image" src="https://github.com/user-attachments/assets/f4790273-5780-47f4-ba80-acbe59c4999d" />
2.**Result**
    <img width="1508" height="885" alt="image" src="https://github.com/user-attachments/assets/218e3f13-2a9e-49bf-8d72-1f21fbc76cd9" />



---
