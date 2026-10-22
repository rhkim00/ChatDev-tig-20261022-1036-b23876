# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template
from folium import Map
from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urljoin
from urllib.request import urlopen
from fake_useragent import UserAgent

# Set up Flask application
app = Flask(__name__)

# Set up User-Agent for requests
ua = UserAgent()

# Function to get data from Trip Advisor
def get_trip_advisor_data(url):
    try:
        # Send GET request with User-Agent
        headers = {'User-Agent': ua.random}
        response = requests.get(url, headers=headers)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract relevant data
            destinations = []
            ratings = []
            for review in soup.find_all('div', {'class': 'review-container'}):
                destination = review.find('span', {'class': 'ui_bubble_rating'}).get('title')
                rating = review.find('span', {'class': 'rating'}).get('aria-label')
                destinations.append(destination)
                ratings.append(rating)
            
            # Create DataFrame
            data = pd.DataFrame({'destination': destinations, 'rating': ratings})
            
            return data
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to create interactive visualizations
def create_visualizations(data):
    try:
        # Create bar chart
        fig, ax = plt.subplots()
        ax.bar(data['destination'], data['rating'])
        plt.title('Destination Popularity')
        plt.xlabel('Destination')
        plt.ylabel('Rating')
        plt.show()
        
        # Create web application using Flask
        @app.route('/')
        def index():
            return render_template('index.html')
        
        @app.route('/destination/<destination>')
        def destination(destination):
            destination_data = data[data['destination'] == destination]
            return render_template('destination.html', destination_data=destination_data)
        
        # Run the web application
        if __name__ == '__main__':
            app.run(debug=True)
        
        # Create a map using Folium
        map = Map(location=[40.7128, -74.0060], zoom_start=10)
        map.save('map.html')
    except Exception as e:
        print(f"Error: {e}")

# Main function
def main():
    url = 'https://www.tripadvisor.com/'
    data = get_trip_advisor_data(url)
    if data is not None:
        create_visualizations(data)

if __name__ == '__main__':
    main()