# 🩺 Health Data Analyzer

The **Health Data Analyzer** is a Flask-based web application that allows users to upload health datasets (CSV format) and instantly generate **interactive visualizations and summaries**.  
It transforms raw health tracking data (steps, calories, sleep hours, heart rate) into **clear insights** with charts and trends.  

---

## ✨ Features
- 📂 Upload CSV health datasets through a web interface  
- 📊 Generate visual charts for:  
  - Steps (daily + rolling average)  
  - Calories burned  
  - Sleep hours  
  - Heart rate trends  
- 📈 Handles large datasets with **monthly aggregation** and **rolling averages**  
- 🎨 Clean and responsive UI built with HTML + CSS  

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS  
- **Backend:** Flask (Python)  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Matplotlib  

---

## 🚀 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/health-data-analyzer.git
   cd health-data-analyzer

   
2. Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows


3. Install dependencies:

pip install -r requirements.txt


4. Run the Flask app:

python app.py


5. Open the app in your browser:

http://127.0.0.1:5000/
