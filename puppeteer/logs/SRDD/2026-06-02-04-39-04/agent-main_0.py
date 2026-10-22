import json
import os

class NewsSummaryGenerator:
    def __init__(self, data_file):
        self.data_file = data_file

    def read_file(self):
        if not os.path.exists(self.data_file):
            print(f"File {self.data_file} not found.")
            return None
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Failed to parse JSON in file {self.data_file}.")
            return None

    def get_user_preferences(self):
        user_preferences_file = 'user_preferences.json'
        if not os.path.exists(user_preferences_file):
            print(f"File {user_preferences_file} not found.")
            return None
        try:
            with open(user_preferences_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Failed to parse JSON in file {user_preferences_file}.")
            return None

    def generate_summary(self, news_articles, user_preferences):
        # Filter news articles based on categories, keywords, and topics
        filtered_articles = []
        for article in news_articles:
            if (article['category'] in user_preferences['categories'] and
                any(keyword in article['summary'] for keyword in user_preferences['keywords']) and
                any(topic in article['summary'] for topic in user_preferences['topics'])):
                filtered_articles.append(article)
        # Perform sentiment analysis on the filtered articles
        sentiment_scores = {}
        for article in filtered_articles:
            sentiment_score = self.sentiment_analysis(article['summary'])
            sentiment_scores[article['title']] = sentiment_score
        # Rank the filtered articles based on sentiment scores
        ranked_articles = sorted(filtered_articles, key=lambda x: sentiment_scores[x['title']], reverse=True)
        # Generate the summary
        summary = {'summary': ' '.join([article['summary'] for article in ranked_articles])}
        return summary

    def sentiment_analysis(self, text):
        # For simplicity, let's assume we're using a basic sentiment analysis model
        # In a real-world application, you would use a more advanced model or library
        if 'positive' in text.lower():
            return 1
        elif 'negative' in text.lower():
            return -1
        else:
            return 0

def main():
    data_file = input("Please enter the filename you want to read: ")
    generator = NewsSummaryGenerator(data_file)
    news_articles = generator.read_file()
    if news_articles:
        user_preferences = generator.get_user_preferences()
        if user_preferences:
            summary = generator.generate_summary(news_articles, user_preferences)
            print(json.dumps(summary, indent=4))
        else:
            print("Failed to read user preferences.")
    else:
        print("Failed to read file.")

if __name__ == "__main__":
    main()