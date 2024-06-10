from openai import OpenAI
import pandas as pd
from PIL import Image
import requests
from io import BytesIO
from src.exception import CustomException
from src.logger import logging
from src.constants import *


class TouristInfoCollector:
    def __init__(self, country, city, attractions):
        self.country = country
        self.city = city
        self.attractions = attractions

    def get_chatgpt_description(self, attraction):
        prompt = f"Provide a detailed description of the tourist attraction: {attraction}"
        response = client.chat.completions.create(
            model= GPT_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content 


    def generate_ai_image(self, attraction):
        response = client.images.generate(
            prompt=f"Create an image of the tourist attraction: {attraction}",
            model = GPT_VISION_MODEL,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url = response['data'][0]['url']
        return image_url

    def save_image(self, image_url, image_path):
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.save(image_path)

    def gather_tourist_info(self):
        data = []

        for attraction in self.attractions:
            chatgpt_desc = self.get_chatgpt_description(attraction)
            # gemini_desc = self.get_gemini_description(attraction)
            # combined_desc = self.combine_descriptions(chatgpt_desc, gemini_desc)
            image_url = self.generate_ai_image(attraction)
            image_path = f"images/{attraction}.png"
            self.save_image(image_url, image_path)

            data.append([self.country, self.city, attraction, chatgpt_desc, image_path])

        df = pd.DataFrame(data, columns=["Country", "City", "Attraction Name", "ChatGPT Description", "Image Path"])
        df.to_excel("tourist_attractions.xlsx", index=False)


# Main function to gather information and save to Excel
if __name__ == "__main__":
    client = OpenAI()
    country = "France"
    city = "Paris"
    attractions = ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"]

    collector = TouristInfoCollector(country, city, attractions)
    collector.gather_tourist_info()
