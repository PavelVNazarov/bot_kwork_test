# video_manager.py

import json
import os

class VideoManager:
    def __init__(self, data_file='videos.json'):
        self.data_file = data_file
        self.videos = self.load_videos()

    def load_videos(self):
        """Загружает видео из файла JSON."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

    def save_videos(self):
        """Сохраняет видео в файл JSON."""
        with open(self.data_file, 'w') as file:
            json.dump(self.videos, file, indent=4)

    def add_video(self, category, exercise_name, video_url):
        """Добавляет видео в указанную категорию и упражнение."""
        if category not in self.videos:
            self.videos[category] = {}
        self.videos[category][exercise_name] = video_url
        self.save_videos()

    def get_video(self, category, exercise_name):
        """Получает видео по категории и упражнению."""
        return self.videos.get(category, {}).get(exercise_name, None)

    def list_categories(self):
        """Возвращает список категорий."""
        return list(self.videos.keys())

    def list_exercises(self, category):
        """Возвращает список упражнений для указанной категории."""
        return list(self.videos.get(category, {}).keys())

    # EXERCISES = {
    #     # Структура данных для хранения видео
    # }

    # def add_video(category, exercise, video_url):
    #     if category not in EXERCISES:
    #         EXERCISES[category] = {}
    #     EXERCISES[category][exercise] = video_url
    #
    # def get_video(category, exercise):
    #     return EXERCISES.get(category, {}).get(exercise, None)

# Объяснение кода:
# VideoManager: Класс для управления видео.
# load_videos: Загружает видео из файла videos.json, если он существует.
# save_videos: Сохраняет текущие видео в файл videos.json.
# add_video: Добавляет видео в указанную категорию и упражнение, затем сохраняет изменения.
# get_video: Получает URL видео по категории и названию упражнения.
# list_categories: Возвращает список всех категорий.
# list_exercises: Возвращает список всех упражнений для указанной категории.