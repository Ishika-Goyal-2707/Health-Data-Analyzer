from flask import Flask, render_template, redirect, request, url_for
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
app.config['PLOT_FOLDER'] = os.path.join('static', 'plots')

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PLOT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/analyze', methods=["POST"])
def analyze():
    if "file" not in request.files:
        return "No file uploaded!"
    
    file= request.files['file']

    if file.filename == '':
        return "No file selected!"
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)


    df = pd.read_csv(filepath, parse_dates = ['Date'])

    # Aggregate monthly and compute rolling averages
    df_monthly = df.resample('M', on='Date').mean()
    df['Steps_MA30'] = df['Steps'].rolling(window=30).mean()

    summary = df.describe().to_html(classes="data", index=True)


    # Line chart for Steps over time

    plt.figure(figsize=(10,4))
    plt.plot(df_monthly.index, df_monthly['Steps'], marker='o', color='blue')
    plt.title("Monthly Average Steps")
    plt.xlabel("Date")
    plt.ylabel("Steps")
    steps_chart = os.path.join(app.config['PLOT_FOLDER'], "steps.png")
    plt.savefig(steps_chart)
    plt.close()


    # Bar chart for Calories
    plt.figure(figsize=(11,5))
    plt.bar(df_monthly.index, df_monthly['Calories'], color='orange')
    plt.title("Monthly Average Calories Burned")
    plt.xlabel("Date")
    plt.ylabel("Calories")
    calories_chart = os.path.join(app.config['PLOT_FOLDER'], "calories.png")
    plt.savefig(calories_chart)
    plt.close()

    # Histogram for Heart Rate
    plt.figure(figsize=(10,4))
    plt.hist(df['HeartRate'], bins=10, color='green', edgecolor='black')
    plt.title("Heart Rate Distribution")
    plt.xlabel("Heart Rate")
    plt.ylabel("Frequency")
    hr_chart = os.path.join(app.config['PLOT_FOLDER'], "heart_rate.png")
    plt.savefig(hr_chart)
    plt.close()


    return render_template("result.html", 
                           summary=summary,
                           steps_chart="steps.png",
                           calories_chart="calories.png",
                           hr_chart="heart_rate.png")


if __name__ == "__main__":
    app.run(debug=True)