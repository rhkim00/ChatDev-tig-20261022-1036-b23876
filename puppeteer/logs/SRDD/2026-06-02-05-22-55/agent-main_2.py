import requests
from bs4 import BeautifulSoup
import json
import os
import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt

class TravelMemoriesPlanner:
    def __init__(self):
        self.base_url = 'https://www.pinterest.com'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        self.headers = {'User-Agent': self.user_agent}

    def enable_javascript(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            script_tag = soup.find('script', {'type': 'text/javascript'})
            if script_tag:
                return script_tag.text
            else:
                return None
        except Exception as e:
            print(f"Error enabling JavaScript: {e}")
            return None

    def get_travel_memories(self):
        try:
            response = requests.get(self.base_url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            travel_memories = []
            for item in soup.find_all('div', {'class': '_1YhQa'}):
                memory = {}
                memory['title'] = item.find('h2').text
                memory['description'] = item.find('p').text
                memory['image'] = item.find('img')['src']
                travel_memories.append(memory)
            return travel_memories
        except Exception as e:
            print(f"Error getting travel memories: {e}")
            return []

    def save_travel_memories(self, travel_memories):
        try:
            with open('travel_memories.json', 'w') as f:
                json.dump(travel_memories, f)
            print("Travel memories saved to travel_memories.json")
        except Exception as e:
            print(f"Error saving travel memories: {e}")

    def read_file(self, filename):
        try:
            if not os.path.exists(filename):
                print(f"File {filename} does not exist.")
                return None
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
            return None

    def plan_travel(self, destination, dates, activities):
        try:
            # Calculate distance between destination and current location
            current_location = (37.7749, -122.4194)  # San Francisco
            destination_location = (destination['latitude'], destination['longitude'])
            distance_to_destination = distance.euclidean(current_location, destination_location)

            # Plan activities based on distance and dates
            planned_activities = []
            for activity in activities:
                if distance_to_destination < 100:  # within 100 miles
                    planned_activities.append(activity)
                elif dates['start_date'] <= dates['end_date']:
                    planned_activities.append(activity)

            return planned_activities
        except Exception as e:
            print(f"Error planning travel: {e}")
            return []

    def visualize_travel(self, travel_memories):
        try:
            # Extract image URLs from travel memories
            image_urls = [memory['image'] for memory in travel_memories]

            # Download images and display them
            images = []
            for url in image_urls:
                response = requests.get(url)
                image = np.array(Image.open(BytesIO(response.content)))
                images.append(image)

            # Display images in a grid
            fig, ax = plt.subplots(len(images), len(images[0]))
            for i in range(len(images)):
                for j in range(len(images[0])):
                    ax[i, j].imshow(images[i][j])
                    ax[i, j].axis('off')
            plt.show()
        except Exception as e:
            print(f"Error visualizing travel memories: {e}")

def main():
    planner = TravelMemoriesPlanner()
    url = 'https://www.pinterest.com/'
    javascript = planner.enable_javascript(url)
    if javascript:
        print("JavaScript enabled")
    else:
        print("Failed to enable JavaScript")
    travel_memories = planner.get_travel_memories()
    planner.save_travel_memories(travel_memories)
    filename = 'data.txt'
    result = planner.read_file(filename)
    if result:
        print(json.dumps(result, indent=4))
    destination = {'latitude': 37.7749, 'longitude': -122.4194}
    dates = {'start_date': '2022-01-01', 'end_date': '2022-01-31'}
    activities = ['Visit Golden Gate Bridge', 'Explore Fisherman\'s Wharf']
    planned_activities = planner.plan_travel(destination, dates, activities)
    print(planned_activities)
    planner.visualize_travel(travel_memories)

if __name__ == "__main__":
    main()