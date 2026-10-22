import json
import random
import requests

class SportsTriviaGame:
    def __init__(self):
        self.sports = {
            "Soccer": {
                "questions": [
                    {"question": "Who is the all-time leading scorer in the FIFA World Cup?", "options": ["Pelé", "Cristiano Ronaldo", "Lionel Messi", "Diego Maradona"], "answer": 0},
                    {"question": "Which team has won the most FIFA World Cup titles?", "options": ["Brazil", "Germany", "Italy", "Argentina"], "answer": 0},
                    {"question": "Who is the current top scorer in the English Premier League?", "options": ["Harry Kane", "Mohamed Salah", "Sergio Agüero", "Jamie Vardy"], "answer": 0}
                ],
                "answers": ["Pelé", "Brazil", "Harry Kane"]
            },
            "Basketball": {
                "questions": [
                    {"question": "Who is the all-time leading scorer in the NBA?", "options": ["Kareem Abdul-Jabbar", "LeBron James", "Michael Jordan", "Kobe Bryant"], "answer": 0},
                    {"question": "Which team has won the most NBA championships?", "options": ["Boston Celtics", "Los Angeles Lakers", "Chicago Bulls", "Golden State Warriors"], "answer": 0},
                    {"question": "Who is the current top scorer in the NBA?", "options": ["Giannis Antetokounmpo", "Luka Doncic", "Stephen Curry", "James Harden"], "answer": 0}
                ],
                "answers": ["Kareem Abdul-Jabbar", "Boston Celtics", "Giannis Antetokounmpo"]
            },
            "Tennis": {
                "questions": [
                    {"question": "Who is the all-time leading winner of Grand Slam titles?", "options": ["Roger Federer", "Rafael Nadal", "Novak Djokovic", "Pete Sampras"], "answer": 0},
                    {"question": "Which player has won the most French Open titles?", "options": ["Rafael Nadal", "Roger Federer", "Novak Djokovic", "Bjorn Borg"], "answer": 0},
                    {"question": "Who is the current top-ranked player in the world?", "options": ["Novak Djokovic", "Rafael Nadal", "Roger Federer", "Stefanos Tsitsipas"], "answer": 0}
                ],
                "answers": ["Roger Federer", "Rafael Nadal", "Novak Djokovic"]
            }
        }

    def start_game(self):
        print("Welcome to the Sports Trivia Game!")
        print("Please select a sport category:")
        for i, sport in enumerate(self.sports.keys()):
            print(f"{i+1}. {sport}")

        while True:
            try:
                choice = int(input("Enter the number of your chosen sport: ")) - 1
                if choice < 0 or choice >= len(self.sports):
                    print("Invalid choice. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        sport = list(self.sports.keys())[choice]
        print(f"\nYou have chosen {sport}.")

        score = 0
        for question in self.sports[sport]["questions"]:
            print(f"\nQuestion: {question['question']}")
            for i, option in enumerate(question["options"]):
                print(f"{i+1}. {option}")

            while True:
                try:
                    answer = int(input("Enter the number of your answer: ")) - 1
                    if answer < 0 or answer >= len(question["options"]):
                        print("Invalid answer. Please try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if question["options"][answer] == self.sports[sport]["answers"][self.sports[sport]["questions"].index(question)]:
                print("Correct answer!")
                score += 1
            else:
                print(f"Incorrect answer. The correct answer was {self.sports[sport]['answers'][self.sports[sport]['questions'].index(question)]}.")

        print(f"\nYour final score is {score} out of {len(self.sports[sport]['questions'])}.")

    def run(self):
        self.start_game()

    def access_website(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

if __name__ == "__main__":
    game = SportsTriviaGame()
    print(json.dumps(game.access_website("https://www.example.com")))

response = requests.get(url, verify=False)