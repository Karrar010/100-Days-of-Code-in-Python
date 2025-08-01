import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re

# Function to validate date format
def validate_date(date):
    # Check if the date is in the correct format YYYY-MM-DD
    return bool(re.match(r"\d{4}-\d{2}-\d{2}", date))

# Get and validate the date input
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
if not validate_date(date):
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    exit()

# Scrape Billboard 100 for the given date
try:
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
    response.raise_for_status()  # Check for request errors (e.g., 404 or 500)
except requests.exceptions.RequestException as e:
    print(f"Error fetching the Billboard Hot 100 chart: {e}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
if not song_names_spans:
    print("No songs found for this date on the Billboard chart.")
    exit()

song_names = [song.getText() for song in song_names_spans]
print(f"Found {len(song_names)} songs from the Billboard Hot 100 on {date}.")

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id="YOUR CLIENT ID",  # Replace with your actual client ID
    client_secret="YOUR CLIENT SECRET",  # Replace with your actual client secret
    show_dialog=True,
    cache_path="token.txt"
))

# Get the current user's ID
try:
    user_id = sp.current_user()["id"]
except spotipy.exceptions.SpotifyException as e:
    print(f"Error fetching user ID: {e}")
    exit()

print(f"Authenticated successfully. User ID: {user_id}")

# Searching for songs in Spotify by title and adding to a list
song_uris = []
year = date.split("-")[0]
for song in song_names:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        if result["tracks"]["items"]:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
            print(f"Found '{song}' on Spotify and added to the list.")
        else:
            print(f"'{song}' not found on Spotify. Skipped.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error searching for '{song}': {e}")

# Creating a new private playlist on Spotify
try:
    playlist = sp.user_playlist_create(user=user_id, name=f"Billboard 100 {date}", public=False)
    print(f"Playlist '{playlist['name']}' created successfully.")
except spotipy.exceptions.SpotifyException as e:
    print(f"Error creating playlist: {e}")
    exit()

# Adding songs to the newly created playlist
if song_uris:
    try:
        sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
        print(f"Successfully added {len(song_uris)} songs to the playlist.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error adding songs to the playlist: {e}")
else:
    print("No songs to add to the playlist.")
