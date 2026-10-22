import json
import requests

class LanguageTutor:
    def __init__(self):
        self.base_url = "https://arxiv.org"
        self.resources = {
            "grammar_lessons": "https://example.com/grammar-lessons",
            "vocabulary_exercises": "https://example.com/vocabulary-exercises",
            "pronunciation_practice": "https://example.com/pronunciation-practice"
        }

    def search_arxiv(self, query):
        params = {
            "query": query,
            "sort": "relevance",
            "source": "all",
            "size": 10
        }
        response = requests.get(f"{self.base_url}/search/query", params=params)
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Error parsing JSON response")
            return None

    def get_paper_info(self, paper_id):
        paper_url = f"{self.base_url}/pdf/{paper_id}"
        response = requests.get(paper_url)
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Error parsing JSON response")
            return None

    def get_resource(self, resource_name):
        return self.resources.get(resource_name)

    def provide_feedback(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            return "Correct!"
        else:
            return "Incorrect. Try again."

def main():
    language_tutor = LanguageTutor()
    query = "language learning software"
    results = language_tutor.search_arxiv(query)
    if results is not None:
        for result in results['hits']['hits']:
            print(json.dumps(result, indent=4))
            paper_id = result['_id']
            paper_info = language_tutor.get_paper_info(paper_id)
            if paper_info is not None:
                print(json.dumps(paper_info, indent=4))
                resource_name = input("Choose a resource: ")
                resource_url = language_tutor.get_resource(resource_name)
                if resource_url is not None:
                    print(f"Resource: {resource_url}")
                    user_answer = input("Enter your answer: ")
                    correct_answer = input("Enter the correct answer: ")
                    feedback = language_tutor.provide_feedback(user_answer, correct_answer)
                    print(feedback)

if __name__ == "__main__":
    main()