class DailyDigest:
    def __init__(self):
        self.preferences = {}

    def set_preferences(self, user, categories):
        self.preferences[user] = categories
        print(f"Preferences set for user {user}: {categories}")

    def get_digest(self, user):
        if user in self.preferences:
            categories = self.preferences[user]
            print(f"Generating digest for user {user} with categories: {categories}")
            # Code to fetch and format news articles based on user's preferences
            print("Digest generated successfully.")
        else:
            print(f"No preferences set for user {user}. Please set preferences first.")

# Example usage
digest = DailyDigest()
digest.set_preferences("Alice", ["Technology", "Science"])
digest.get_digest("Alice")
digest.get_digest("Bob")