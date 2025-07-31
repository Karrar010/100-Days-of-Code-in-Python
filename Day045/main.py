# ## 100 Movies that You Must Watch

# # Objective

# Scrape the top 100 movies of all time from a website. Generate a text file called `movies.txt` that lists the movie titles in ascending order (starting from 1). 
# The result should look something like this:

# ```
# 1) The Godfather
# 2) The Empire Strikes Back
# 3) The Dark Knight
# 4) The Shawshank Redemption
# ... and so on
# ```
# The central idea behind this project is to be able to use BeautifulSoup to obtain some data - like movie titles - from a website like Empire's (or from, say Timeout or Stacker that have curated similar lists). 

# ### ⚠️ Important: Use the Internet Archive's URL

# Since websites change very frequently, **use this link** 
# ```
# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# ```
# from the Internet Archive's Wayback machine. That way your work will match the solution video.

# (Do *not* use https://www.empireonline.com/movies/features/best-movies-2/ which I've used in the screen recording)

# # Solution

# You can find the code from my walkthrough and solution as a downloadable .zip file in the course resources for this lesson. 


import requests
from bs4 import BeautifulSoup

# Use the archived version of the page
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Get the HTML of the page
response = requests.get(URL)
website_html = response.text

# Parse with BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")

# Find all movie title elements
all_movies = soup.find_all(name="h3", class_="title")

# Extract text from each <h3> tag
movie_titles = [movie.getText() for movie in all_movies]

# Reverse the list so movie 1 is at the top
movies = movie_titles[::-1]

# Write to a text file with UTF-8 encoding
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for index, movie in enumerate(movies, start=1):
        file.write(f"{index}) {movie}\n")




# print("✅ movies.txt generated successfully!")


'''
FAQ: Empire's website has changed!

When this lesson was created, I used this URL for the project: 
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

However, Empire has since changed their website. You can see this when you inspect the movie title elements. 
You'll see that the h3 with the class "title" is no longer there. 
To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.

'''