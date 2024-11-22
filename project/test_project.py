from project import search_anime, manage_watchlist, get_recommendations, play_trivia

def test_search_anime():
    assert callable(search_anime)

def test_manage_watchlist():
    assert callable(manage_watchlist)

def test_get_recommendations():
    assert callable(get_recommendations)

def test_play_trivia():
    assert callable(play_trivia)
