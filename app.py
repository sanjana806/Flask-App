from flask import Flask, render_template, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Base directory for file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def home():
    return render_template('Index.html')


@app.route('/sanjana')
def about():
    return render_template('About.html')

@app.route('/next')
def next():
    return render_template('next.html')



@app.route('/game')
def game():
    return render_template('Game.html')


@app.route('/File')
def file():
    file_path = os.path.join(BASE_DIR, 'airlines_flights_data.csv')
    data_df = pd.read_csv(file_path).head()
    df = data_df[["airline", "source_city", "arrival_time"]]
    return render_template(
        'File.html',
        title="flights",
        table=df.to_html(index=False, classes="table")
    )


@app.route('/file2')
def file2():
    file_path = os.path.join(BASE_DIR, '9. Sales-Data-Analysis.csv')
    df = pd.read_csv(file_path)
    return render_template(
        'file2.html',
        title="Sales Data",
        table=df.head().to_html(index=False, classes="table")
    )


@app.route('/file3')
def file3():
    file_path = os.path.join(BASE_DIR, 'multilingual_mobile_app_reviews_2025.csv')
    df = pd.read_csv(file_path)
    return render_template(
        'file3.html',
        title="Mobile",
        table=df.head().to_html(index=False, classes="table")
    )


@app.route('/file4')
def file4():
    # Path to CSV
    file_path = os.path.join(BASE_DIR, 'BMW_Car_Sales_Classification.csv')

    # Read CSV
    df = pd.read_csv(file_path)

    # Select only first 9 columns
    df = df.iloc[:, :9]

    # Render HTML table
    return render_template(
        'file4.html',
        title="BMW",
        table=df.head().to_html(index=False, classes="table table-striped table-bordered")
    )





@app.route('/bar')
def bar():
    file_path = os.path.join(BASE_DIR, 'airlines_flights_data.csv')
    data_df = pd.read_csv(file_path).head()

    plt.figure(figsize=(10, 6))
    plt.bar(data_df["airline"], data_df["arrival_time"])
    plt.xlabel("Airlines")
    plt.ylabel("Time")
    plt.grid(False)

    chart_path = os.path.join(BASE_DIR, 'static', 'chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('bar.html', chart_url=url_for('static', filename='chart.png'))


@app.route('/bar1')
def bar1():
    file_path = os.path.join(BASE_DIR, '9. Sales-Data-Analysis.csv')
    data_df = pd.read_csv(file_path).head()

    plt.figure(figsize=(10, 6))
    plt.bar(data_df["Price"], data_df["Quantity"])
    plt.xlabel("Price")
    plt.ylabel("Quantity")
    plt.grid(False)

    chart_path = os.path.join(BASE_DIR, 'static', 'chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('bar1.html', chart_url=url_for('static', filename='chart.png'))


@app.route('/bar2')
def bar2():
    file_path = os.path.join(BASE_DIR, 'multilingual_mobile_app_reviews_2025.csv')
    data_df = pd.read_csv(file_path).head()

    plt.figure(figsize=(10, 6))
    plt.bar(data_df["review_id"], data_df["user_id"])
    plt.xlabel("Review ID")
    plt.ylabel("User ID")
    plt.grid(False)

    chart_path = os.path.join(BASE_DIR, 'static', 'chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('bar2.html', chart_url=url_for('static', filename='chart.png'))


@app.route('/bar3')
def bar3():
    file_path = os.path.join(BASE_DIR, 'BMW_Car_Sales_Classification.csv')
    data_df = pd.read_csv(file_path).head()

    plt.figure(figsize=(10, 6))
    plt.bar(data_df["Year"], data_df["Price_USD"])
    plt.xlabel("Year")
    plt.ylabel("Price (USD)")
    plt.grid(False)

    chart_path = os.path.join(BASE_DIR, 'static', 'chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('bar3.html', chart_url=url_for('static', filename='chart.png'))

@app.route('/hist')
def hist():
    file_path = os.path.join(BASE_DIR, 'airlines_flights_data.csv')
    data_df = pd.read_csv(file_path).head()

    plt.figure(figsize=(10, 6))
    plt.hist(data_df["price"], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel("Arrival Time")
    plt.ylabel("Frequency")
    plt.title("Distribution of Arrival Times")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    chart_path = os.path.join(BASE_DIR, 'static', 'hist_chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('hist.html', chart_url=url_for('static', filename='hist_chart.png'))

@app.route('/hist1')
def hist1():
    file_path = os.path.join(BASE_DIR, '9. Sales-Data-Analysis.csv')
    data_df = pd.read_csv(file_path).head()

    plt.figure(figsize=(10, 6))
    plt.hist(data_df["Price"], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.title("Distribution of Prices")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    chart_path = os.path.join(BASE_DIR, 'static', 'hist_chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('hist1.html', chart_url=url_for('static', filename='hist_chart.png'))


@app.route('/hist2')
def hist2():
    file_path = os.path.join(BASE_DIR, 'multilingual_mobile_app_reviews_2025.csv')
    data_df = pd.read_csv(file_path).head()

    plt.figure(figsize=(10, 6))
    plt.hist(data_df["review_id"],bins=10, color='skyblue', edgecolor='black')
    plt.xlabel("Review ID")
    plt.ylabel("Frequency")
    plt.title("Distribution of Arrival Times")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    chart_path = os.path.join(BASE_DIR, 'static', 'hist_chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('hist2.html', chart_url=url_for('static', filename='hist_chart.png'))


@app.route('/hist3')
def hist3():
    file_path = os.path.join(BASE_DIR, 'BMW_Car_Sales_Classification.csv')
    data_df = pd.read_csv(file_path).head()

    plt.figure(figsize=(10, 6))
    plt.hist(data_df["Price_USD"] ,  bins=10, color='skyblue', edgecolor='black')
    plt.xlabel("Price_USD")
    plt.ylabel("Mileage_KM")
    plt.title("Distribution of Prices and Mileage")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    chart_path = os.path.join(BASE_DIR, 'static', 'hist_chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('hist3.html', chart_url=url_for('static', filename='hist_chart.png'))


@app.route('/pie')
def pie():
    data_df = pd.read_csv('airlines_flights_data.csv').head()

    plt.figure(figsize=(8, 8))
    data=data_df["price"].value_counts()
    plt.pie(data.index,autopct='%1.1f%%', startangle=90)
    plt.title("Airline Distribution")
    chart_url = os.path.join('static', 'pie_chart.png')
    plt.savefig(chart_url)
    plt.close()
    return render_template('pie.html', chart_url=url_for('static', filename='pie_chart.png'))

@app.route('/pie1')
def pie1():
    data_df = pd.read_csv('9. Sales-Data-Analysis.csv').head()

    plt.figure(figsize=(8, 8))
    data=data_df["Price"].value_counts()
    plt.pie(data.index,autopct='%1.1f%%', startangle=90)
    plt.title("Sales Distribution")
    chart_url = os.path.join('static', 'pie_chart.png')
    plt.savefig(chart_url)
    plt.close()
    return render_template('pie1.html', chart_url=url_for('static', filename='pie_chart.png'))


@app.route('/pie2')
def pie2():
    data_df = pd.read_csv('multilingual_mobile_app_reviews_2025.csv').head()

    plt.figure(figsize=(8, 8))
    data=data_df["review_id"].value_counts()
    plt.pie(data.index,autopct='%1.1f%%', startangle=90)
    plt.title("Mobile App Reviews Distribution")
    chart_url = os.path.join('static', 'pie_chart.png')
    plt.savefig(chart_url)
    plt.close()
    return render_template('pie2.html', chart_url=url_for('static', filename='pie_chart.png'))


@app.route('/pie3')
def pie3():
    data_df = pd.read_csv('BMW_Car_Sales_Classification.csv').head()

    plt.figure(figsize=(8, 8))
    data=data_df["Price_USD"].value_counts()
    plt.pie(data.index,autopct='%1.1f%%', startangle=90)
    plt.title("BMW Car Sales Distribution")
    chart_url = os.path.join('static', 'pie_chart.png')
    plt.savefig(chart_url)
    plt.close()
    return render_template('pie3.html', chart_url=url_for('static', filename='pie_chart.png'))


if __name__ == '__main__':
    app.run(port=4000,host = "0.0.0.0", debug=True)


