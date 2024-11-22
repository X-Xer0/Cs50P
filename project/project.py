import requests
import random
import json
import os

API_URL = "https://api.jikan.moe/v4/anime"

def main():
    while True:
        print("\nWelcome to MyAnimeWorld!")
        print("1. Search for Anime")
        print("2. Manage Watchlist")
        print("3. Get Recommendations")
        print("4. Play Anime Trivia")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            search_anime()
        elif choice == "2":
            manage_watchlist()
        elif choice == "3":
            get_recommendations()
        elif choice == "4":
            play_trivia()
        elif choice == "5":
            print("Goodbye! Enjoy your anime journey!")
            break
        else:
            print("Invalid choice. Please try again.")

def search_anime():
    query = input("Enter the name of an anime: ").strip()
    response = requests.get(f"{API_URL}?q={query}&limit=5")
    if response.status_code == 200:
        results = response.json()["data"]
        if results:
            print("\nSearch Results:")
            for i, anime in enumerate(results):
                print(f"{i + 1}. {anime['title']} ({anime['type']}, {anime['episodes']} episodes)")
                print(f"   Score: {anime['score']}, Aired: {anime['aired']['string']}")
                print(f"   Synopsis: {anime['synopsis'][:100]}...\n")
        else:
            print("No results found.")
    else:
        print("Error fetching data. Please try again.")

def manage_watchlist():
    watchlist_file = "watchlist.json"
    if not os.path.exists(watchlist_file):
        with open(watchlist_file, "w") as f:
            json.dump([], f)

    with open(watchlist_file, "r") as f:
        watchlist = json.load(f)

    print("\nYour Watchlist:")
    if watchlist:
        for i, anime in enumerate(watchlist):
            print(f"{i + 1}. {anime}")
    else:
        print("No anime in your watchlist.")

    print("\nOptions:")
    print("1. Add to Watchlist")
    print("2. Remove from Watchlist")
    print("3. Go Back")
    choice = input("Choose an option: ")

    if choice == "1":
        anime = input("Enter the name of the anime to add: ").strip()
        if anime not in watchlist:
            watchlist.append(anime)
            with open(watchlist_file, "w") as f:
                json.dump(watchlist, f)
            print(f"{anime} added to watchlist.")
        else:
            print(f"{anime} is already in your watchlist.")
    elif choice == "2":
        anime = input("Enter the name of the anime to remove: ").strip()
        if anime in watchlist:
            watchlist.remove(anime)
            with open(watchlist_file, "w") as f:
                json.dump(watchlist, f)
            print(f"{anime} removed from watchlist.")
        else:
            print(f"{anime} is not in your watchlist.")
    elif choice == "3":
        return
    else:
        print("Invalid choice.")

def get_recommendations():
    genre = input("Enter a genre (e.g., Action, Comedy, Romance): ").strip().lower()
    response = requests.get(f"{API_URL}?genres={genre}&limit=5")
    if response.status_code == 200:
        results = response.json()["data"]
        if results:
            print("\nRecommendations:")
            for i, anime in enumerate(results):
                print(f"{i + 1}. {anime['title']} ({anime['type']}, {anime['episodes']} episodes)")
                print(f"   Score: {anime['score']}, Aired: {anime['aired']['string']}")
                print(f"   Synopsis: {anime['synopsis'][:100]}...\n")
        else:
            print("No recommendations found for this genre.")
    else:
        print("Error fetching data. Please try again.")

def play_trivia():
    questions = [
        {"question": "Which anime features a notebook that kills people?", "answer": "Death Note"},
        {"question": "What is the main character’s name in Naruto?", "answer": "Naruto"},
        {"question": "Which anime is set in the world of alchemy?", "answer": "Fullmetal Alchemist"},
        {"question": "Who is the Pirate King in One Piece?", "answer": "Gol D. Roger"}
    ]
    question = random.choice(questions)
    print("\nTrivia Time!")
    print(question["question"])
    answer = input("Your answer: ").strip()
    if answer.lower() == question["answer"].lower():
        print("Correct! You're a true anime fan!")
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

if __name__ == "__main__":
    main()
