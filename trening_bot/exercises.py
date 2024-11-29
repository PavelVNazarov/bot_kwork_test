# exercises.py
EXERCISE_CATEGORIES = ["Спина", "Руки", "Грудь", "Ноги", "Плечи"]

def get_exercise_categories():
    return EXERCISE_CATEGORIES

def get_exercise_video(category, exercise):
    from video_manager import get_video
    return get_video(category, exercise)