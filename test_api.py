import requests

def test_github_api_root():
    # Skicka ett GET-anrop till GitHubs öppna API
    response = requests.get("https://api.github.com")

    # 1) API:t ska svara med HTTP-status 200 (OK)
    assert response.status_code == 200

    # 2) Svaret ska innehålla nyckeln "current_user_url" i JSON-datat
    data = response.json()
    assert "current_user_url" in data
