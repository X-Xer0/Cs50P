# MyAnimeWorld

#### Video Demo:  <URL HERE>

#### Description:
Welcome to **MyAnimeWorld**, a Python-powered application designed for anime enthusiasts! This project serves as a personal hub for anime discovery, watchlist management, and fun interactions like trivia. By leveraging the Jikan API, the app provides real-time access to anime data, making it easier for users to find new shows, get recommendations, and maintain a curated watchlist.

Whether you're new to anime or a seasoned fan, MyAnimeWorld aims to make exploring and organizing your favorite anime titles simple and enjoyable.

---

## Features:
1. **Search for Anime**:
   - Look up anime by title.
   - View essential details such as the number of episodes, type (TV, movie, etc.), score, airing dates, and a brief synopsis.
   - Allows users to explore new or popular shows quickly.

2. **Manage Watchlist**:
   - Add anime to your personal watchlist and store it in a JSON file for persistence.
   - Remove anime from your watchlist with ease.
   - View all the anime titles you've added, ensuring you never lose track of your watchlist.

3. **Get Recommendations**:
   - Generate anime recommendations based on genre.
   - Provides a starting point for exploring anime you might not have heard of.

4. **Play Anime Trivia**:
   - Test your knowledge with random anime-related trivia questions.
   - A fun way to engage with the app and challenge yourself!

5. **User-Friendly Command-Line Interface**:
   - Interactive prompts guide users through each feature seamlessly.

---

## File Structure:

### `project.py`
This is the main Python file containing all core functionality. The file includes:
- `main()`: The entry point of the program. It serves as the central hub that connects all features.
- `search_anime()`: Fetches anime details using the Jikan API and displays search results.
- `manage_watchlist()`: Handles user watchlists, allowing addition, removal, and viewing of anime titles.
- `get_recommendations()`: Fetches anime recommendations based on the user's input genre.
- `play_trivia()`: Implements a simple trivia game for anime enthusiasts.

### `test_project.py`
This file contains tests for the custom functions in `project.py`. It uses the `pytest` framework to ensure all functions behave as expected:
- `test_search_anime()`: Verifies that the `search_anime` function exists and is callable.
- `test_manage_watchlist()`: Verifies the existence and functionality of `manage_watchlist`.
- `test_get_recommendations()`: Ensures `get_recommendations` is callable.
- `test_play_trivia()`: Confirms the functionality of the `play_trivia` function.

### `requirements.txt`
This file lists the dependencies required for the project:
- `requests`: A Python library used to interact with the Jikan API for fetching anime data.

---

## Design Choices:
1. **Use of Jikan API**:
   - The Jikan API provides a vast database of anime details, ensuring accurate and up-to-date information.
   - This choice eliminates the need to maintain a local database, reducing complexity.

2. **Watchlist Storage**:
   - A JSON file is used for persistence. This simple format is human-readable, lightweight, and easy to integrate with Python’s `json` module.

3. **Command-Line Interface**:
   - A CLI was chosen for its simplicity and minimal dependencies, ensuring the project runs on any machine with Python installed.
   - The menu-driven system enhances usability and makes navigation straightforward.

4. **Trivia Game**:
   - Added as a lighthearted feature to increase user engagement and provide a break from the primary functionalities.

---

## Challenges and Future Improvements:
### Challenges:
- Handling API rate limits: The Jikan API has a limit on requests per minute. A caching mechanism or request throttling could be implemented to handle this in future iterations.
- Data parsing: Parsing nested JSON data from the API and ensuring correct formatting required careful handling.

### Future Improvements:
1. **Expand Trivia**:
   - Incorporate more trivia questions and allow users to contribute their own.
   - Fetch questions dynamically from an external source.

2. **Enhanced Recommendations**:
   - Add filters like popularity, year of release, or studios for more tailored recommendations.
   - Enable recommendations based on the user's watchlist history.

3. **Graphical Interface**:
   - Transition from CLI to a GUI using libraries like Tkinter or PyQt for better user experience.

---

## How to Run:
1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the application:
```
python project.py
```

3. To run tests:
```
pytest test_project.py
```

### Enjoy exploring anime with **MyAnimeWorld**!

