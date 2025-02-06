# AI-Based Stress Detection Module  

This repository contains the **Stress Detection Module**, a key component of the **AI-Based Stress Detection System for University Students**. This module is responsible for analyzing facial expressions and determining whether a student is stressed or not. It uses deep learning techniques to classify emotions and assess stress levels in real time.  

## 📌 Features  

- **Facial Expression Analysis** – Uses convolutional neural networks (CNNs) to classify emotions.  
- **Stress Classification** – Determines if a student is **stressed** or **not stressed** based on facial expressions. 
- **Real-time Prediction** – Receives images via API and returns stress predictions instantly.  
- **Integration Ready** – Designed to work seamlessly with the Face Detection and Frontend modules.  

## 🛠️ Technologies Used  

- **Python**  
- **TensorFlow / Keras**  
- **OpenCV**  
- **Flask**  
- **NumPy**  
- **Base64 Encoding**  

## 🚀 How It Works  

1. Receives an **image** (base64-encoded) from the frontend.  
2. Preprocesses the face and feeds it into the **trained CNN model**.  
3. Predicts the **emotion** (angry, happy, neutral, sad, etc.).  
4. Maps emotions to **stress states** (e.g., "angry," "sad," "fear" → **stressed**).  
5. Returns the **predicted label** and **stress state** via API response.  

## 📂 Project Structure  

```
/stress-detection
│── stressdetector.json  # Model architecture
│── stressdetectorV1.h5  # Pre-trained model weights
│── app.py  # Flask API for stress prediction
│── requirements.txt  # Dependencies
│── README.md  # Documentation
```

## 🔧 Installation  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/yourusername/stress-detection-module.git
cd stress-detection-module
```

### 2️⃣ Create a Virtual Environment  
```sh
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Stress Detection API  
```sh
python app.py
```

## 📡 API Endpoints  

### 🎭 **Predict Stress Level**  

- **URL:** `/predict`  
- **Method:** `POST`  
- **Request Body:**  
  ```json
  {
    "image": "base64_encoded_image_string"
  }
  ```
- **Response:**  
  ```json
  [
    {
      "label": "sad",
      "state": "stressed",
      "box": [x, y, width, height]
    }
  ]
  ```

## 🛠 Future Improvements  
- Improve model accuracy with **larger datasets**.  
- Enhance **multi-face detection** capabilities.  
- Integrate with student support services for **automated interventions**.  

---

**📌 Related Modules:**  
- **Frontend Module** → [GitHub Repo](https://github.com/gnjayasekara/AI-Based-Stress-Detection-System)  
- **Face Detection Module** → [GitHub Repo](https://github.com/gnjayasekara/face-recognition-backend)  

🔗 **Project Maintainer:** [Nimtharu Jayasekara](https://github.com/gnjayasekara)  

