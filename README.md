# Neuropathy Prediction System

An AI-powered web application for predicting neuropathy risk in prediabetic patients using biomedical markers. Built with Flask and Random Forest machine learning model.

## Features

- 🧠 **AI-Powered Prediction**: Uses Random Forest model with 91.67% accuracy
- 🎨 **Beautiful UI**: Modern, responsive design with gradient backgrounds
- ⚡ **Real-time Analysis**: Instant predictions based on 13 biomedical markers
- 📊 **Confidence Scores**: Shows prediction reliability
- 🎯 **Input Validation**: Ensures data quality with appropriate ranges
- 📱 **Mobile Friendly**: Fully responsive design

## Biomedical Markers Analyzed

1. Age
2. HbA1c (Glycated Hemoglobin)
3. FBG (Fasting Blood Glucose)
4. 2h-PPBG (2-hour Post-Prandial Blood Glucose)
5. Total Cholesterol
6. LDL (Low-Density Lipoprotein)
7. HDL (High-Density Lipoprotein)
8. TG (Triglycerides)
9. 25(OH) Vitamin D
10. Ionized Calcium
11. Phosphorus
12. PTH (Parathyroid Hormone)
13. BMI (Body Mass Index)

## Local Development

### Prerequisites

- Python 3.11 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd predictive_model
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Train and save the model:
```bash
python train_model.py
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and visit:
```
http://localhost:5000
```

## Deployment to Render (Free Hosting)

### Step 1: Prepare Your Code

Make sure you have the following files in your repository:
- `app.py` - Flask application
- `requirements.txt` - Python dependencies
- `render.yaml` - Render configuration
- `templates/index.html` - Frontend template
- `random_forest_model.pkl` - Trained model
- `scaler.pkl` - Feature scaler
- `feature_names.pkl` - Feature names

### Step 2: Push to GitHub

1. Initialize git repository:
```bash
git init
git add .
git commit -m "Initial commit"
```

2. Create a new repository on GitHub

3. Push your code:
```bash
git remote add origin https://github.com/your-username/your-repo-name.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Render

1. Go to [render.com](https://render.com)
2. Sign up for a free account
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Render will automatically detect your `render.yaml` configuration
6. Click "Create Web Service"

### Step 4: Access Your App

After deployment (takes 2-3 minutes), Render will provide you with a URL like:
```
https://neuropathy-predictor.onrender.com
```

Share this URL with your friends!

## Alternative Deployment Options

### PythonAnywhere

1. Create account at [pythonanywhere.com](https://pythonanywhere.com)
2. Create a new Web app
3. Upload your files
4. Configure the WSGI file
5. Install requirements from the dashboard

### Railway

1. Install Railway CLI: `npm install -g @railway/cli`
2. Login: `railway login`
3. Initialize: `railway init`
4. Deploy: `railway up`

## Model Performance

- **Accuracy**: 91.67%
- **AUC Score**: 0.9552
- **Cross-validation**: 88.00% ± 5.72%

**Top Predictive Features:**
1. Age (14.38% importance)
2. 2h-PPBG (14.32% importance)
3. LDL (11.46% importance)
4. HDL (10.76% importance)
5. FBG (8.90% importance)

## Important Disclaimer

⚠️ **Medical Disclaimer**: This tool is for educational purposes only and should not replace professional medical advice. Always consult with a healthcare provider for proper diagnosis and treatment.

## Technology Stack

- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn (Random Forest)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Deployment**: Render.com (free tier)

## Support

For issues or questions, please open an issue on GitHub.

## License

This project is for educational purposes.

---

**Built with ❤️ for better health awareness**
