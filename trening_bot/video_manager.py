# video_manager.py
import json

VIDEO_DATA_FILE = 'video_data.json'

def load_video_data():
    try:
        with open(VIDEO_DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_video_data(data):
    with open(VIDEO_DATA_FILE, 'w') as f:
        json.dump(data, f)

def add_video(category, exercise, video_url):
    data = load_video_data()
    if category not in data:
        data[category] = {}
    data[category][exercise] = video_url
    save_video_data(data)

def get_video(category, exercise):
    data = load_video_data()
    return data.get(category, {}).get(exercise)