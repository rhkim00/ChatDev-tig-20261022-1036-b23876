import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import json
from flask import Flask, render_template, request

class TravelInsights:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config["SECRET_KEY"] = "secret_key"
        self.data = self.load_data()

    def load_data(self):
        # Sample data
        data = {
            "Destination": ["Paris", "Rome", "Tokyo", "New York", "London"],
            "Average Temperature": [12, 18, 22, 15, 10],
            "Population": [2140000, 2870000, 3820000, 8530000, 8820000]
        }
        return pd.DataFrame(data)

    def create_form(self):
        class AnalysisForm:
            def __init__(self, request):
                self.request = request
                self.destination = StringField("Destination", validators=[DataRequired()])
                self.temperature = IntegerField("Temperature", validators=[DataRequired()])
                self.population = IntegerField("Population", validators=[DataRequired()])
                self.submit = SubmitField("Submit")

            def validate(self):
                if self.request.method == "POST":
                    self.destination.data = self.request.form["destination"]
                    self.temperature.data = int(self.request.form["temperature"])
                    self.population.data = int(self.request.form["population"])
                    return True
                return False

        return AnalysisForm

    def analyze(self, form):
        if form.validate():
            destination = form.destination.data
            temperature = int(form.temperature.data)
            population = int(form.population.data)

            filtered_df = self.data[(self.data["Destination"] == destination) & (self.data["Average Temperature"] >= temperature) & (self.data["Population"] >= population)]

            # Perform data analysis and visualization
            avg_temp = filtered_df["Average Temperature"].mean()
            avg_population = filtered_df["Population"].mean()

            plt.figure(figsize=(10, 6))
            plt.bar(filtered_df["Destination"], filtered_df["Average Temperature"])
            plt.title("Average Temperature by Destination")
            plt.xlabel("Destination")
            plt.ylabel("Average Temperature")
            plt.xticks(rotation=45)

            img = BytesIO()
            plt.savefig(img)
            img.seek(0)
            img_url = base64.b64encode(img.getvalue()).decode("utf-8")

            return {
                "data": filtered_df.to_dict(orient="records"),
                "avg_temp": avg_temp,
                "avg_population": avg_population,
                "img_url": img_url
            }
        else:
            return None

    def run(self):
        self.app.add_url_rule("/", view_func=self.home)
        self.app.add_url_rule("/analyze", view_func=self.analyze_form, methods=["POST"])
        self.app.run(debug=True)

    def home(self):
        return "Welcome to our travel insights platform! Here, you can find valuable insights and trends about popular travel destinations. Thank you for using our platform. Have a great day!"

    def analyze_form(self):
        form = self.create_form()(request)
        result = self.analyze(form)
        if result:
            return render_template("analysis.html", **result)
        else:
            return "Invalid input", 400

if __name__ == "__main__":
    app = TravelInsights()
    app.run()