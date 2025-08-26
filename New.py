import streamlit as st import requests from datetime import datetime, timedelta

============================

YouTube API Config

============================

API_KEY = "AIzaSyBS5xHngDjrzvaBufjxn88wFxEzq8mJG8o" YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search" YOUTUBE_VIDEO_URL = "https://www.googleapis.com/youtube/v3/videos"

============================

Keywords for Movie Explanation

============================

KEYWORDS = [ "Movie explanation", "Movies explanation", "Movie explanation shorts", "Movie explanation video", "New movie explanation shorts", "Movie review", "Movie recap", "Movie reviews", "Movie explained in hindi", "Movie explained India", "Movie explained in Urdu", "Movie explained hindi", "Movie explanation in hindi", "Movie explanation in urdu", "Movie explanation video", "New movie explanation video", "New movie explained video", "Movie in simple language", "New movie explanation", "Trending movie explanation", "Hot movie explanation" ]

============================

Function: Search YouTube Videos

============================

def search_youtube(query, max_results=10): params = { "part": "snippet", "q": query, "type": "video", "key": API_KEY, "maxResults": max_results, "order": "date" } response = requests.get(YOUTUBE_SEARCH_URL, params=params) if response.status_code == 200: return response.json().get("items", []) else: return []

============================

Function: Get Video Details

============================

def get_video_details(video_ids): params = { "part": "snippet,statistics,contentDetails", "id": ",".join(video_ids), "key": API_KEY } response = requests.get(YOUTUBE_VIDEO_URL, params=params) if response.status_code == 200: return response.json().get("items", []) else: return []

============================

Streamlit UI

============================

st.set_page_config(page_title="YouTube Movie Explanation Finder", layout="wide") st.title("🎬 Movie Explanation YouTube Videos Finder")

Select keyword from dropdown

selected_keyword = st.selectbox("🔍 Select a keyword to search:", KEYWORDS)

Number of results

max_results = st.slider("Number of results:", 5, 30, 10)

if st.button("Search Videos"): with st.spinner("Fetching videos from YouTube..."): videos = search_youtube(selected_keyword, max_results)

if videos:
        video_ids = [v["id"]["videoId"] for v in videos]
        details = get_video_details(video_ids)

        for video in details:
            snippet = video["snippet"]
            stats = video.get("statistics", {})
            video_id = video["id"]

            st.subheader(snippet["title"])
            st.video(f"https://www.youtube.com/watch?v={video_id}")
            st.write(f"**Channel:** {snippet['channelTitle']}")
            st.write(f"**Published at:** {snippet['publishedAt']}")
            st.write(f"**Views:** {stats.get('viewCount', 'N/A')}")
            st.write("---")
    else:
        st.warning("No videos found. Try another keyword or check API key.")

