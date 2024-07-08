#!/bin/python3

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        meme_large = data["preview"][-2]
        subreddit = data["subreddit"]
        return meme_large, subreddit
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None, None
    except (KeyError, IndexError) as e:
        print(f"Error processing response: {e}")
        return None, None

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    if meme_pic and subreddit:
        return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)
    else:
        return "Failed to load meme", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
