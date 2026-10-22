import json
import os

class NewsSummaryGenerator:
    def __init__(self, data_file):
        self.data_file = data_file

    def read_file(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.data_file} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Failed to parse JSON in file {self.data_file}.")
            return None
        except Exception as e:
            print(f"Error processing file: {str(e)}")
            return None

    def get_user_preferences(self):
        # For simplicity, let's assume user preferences are stored in a file named 'user_preferences.json'
        user_preferences_file = 'user_preferences.json'
        try:
            with open(user_preferences_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {user_preferences_file} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Failed to parse JSON in file {user_preferences_file}.")
            return None
        except Exception as e:
            print(f"Error processing file: {str(e)}")
            return None

    def generate_summary(self, news_articles, user_preferences):
        # For simplicity, let's assume we're filtering news articles based on categories
        filtered_articles = [article for article in news_articles if article['category'] in user_preferences['categories']]
        return {'summary': ' '.join([article['summary'] for article in filtered_articles])}

def main():
    data_file = input("Please enter the filename you want to read: ")
    generator = NewsSummaryGenerator(data_file)
    news_articles = generator.read_file()
    if news_articles:
        print(json.dumps(news_articles, indent=4))
    else:
        print("Failed to read file.")

if __name__ == "__main__":
    main()