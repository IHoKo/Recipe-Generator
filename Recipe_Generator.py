import os
import re
import shutil
import openai
import requests

openai.api_key = os.getenv("OPENAI_API_KEY")


class RecipeWithImageGenerator:
    def __init__(self):
        self.recipe = None
        self.title = None
        self.background = None
        self.instruction = None

    def run(self):
        result = self.ask_for_ingredients_or_dish()
        if not result:
            return

        prompt = self.create_recipe_prompt(result)
        response = self.get_text_response(prompt)

        self.recipe = response.get("choices", [{}])[0].get("text", "").strip()
        if not self.recipe:
            print("No recipe was generated.")
            return

        self.title = self.extract_title()
        self.background = self.extract_background()

        print(self.recipe)
        self.save_to_file(f"{self.title}.txt", self.recipe)

        image_prompt = self.create_image_prompt()
        image_url = self.get_image_url(image_prompt)
        if image_url:
            self.save_image(image_url, f"{self.title}.jpg")

    @staticmethod
    def ask_for_ingredients_or_dish():
        mode = input("Are you entering a dish name or ingredients? Type 'dish' or 'ingredients': ").strip().lower()

        if mode == 'dish':
            dish = input("Enter the name of the dish: ").strip()
            return {'type': 'dish', 'value': dish}
        elif mode == 'ingredients':
            ingredients = []
            while True:
                ingredient = input("Enter an ingredient (or type 'done' to finish): ").strip()
                if ingredient.lower() == 'done':
                    break
                ingredients.append(ingredient)
            return {'type': 'ingredients', 'value': ingredients}
        else:
            print("Invalid input.")
            return None

    @staticmethod
    def create_recipe_prompt(result):
        if result['type'] == 'dish':
            return (
                f"Give a short background on the dish and mention its country or region of origin of the {result['value']}.\n"
                f"Provide the name of the dish starting with 'Recipe Title: '.\n"
                f"List the common ingredients.\n"
                f"Then write a numbered recipe on how to prepare it.\n"
            )
        else:
            ingredients = ', '.join(result['value'])
            return (
                f"I have a list of ingredients: {ingredients}.\n"
                f"Create a unique dish using them (assume pantry basics are available).\n"
                f"Name the dish starting with 'Recipe Title: '.\n"
                f"Describe its origin or what cuisine it’s similar to.\n"
                f"Write a numbered recipe to prepare it.\n"
            )

    @staticmethod
    def get_text_response(prompt):
        try:
            return openai.Completion.create(
                engine='gpt-3.5-turbo-instruct',
                prompt=prompt,
                max_tokens=1024,
                temperature=0.7
            )
        except Exception as e:
            print(f"Error during OpenAI text completion: {e}")
            return {}

    def extract_title(self):
        match = re.search(r"Recipe Title:\s*(.*)", self.recipe)
        if not match:
            raise ValueError("Recipe title not found.")
        return match.group(1).strip()

    def extract_background(self):
        match = re.search(r"Background:\s*(.*)", self.recipe)
        if not match:
            return "a regional dish"
        return match.group(1).strip()

    def extract_instruction(self):
        match = re.search(r"Instruction:\s*(.*)", self.recipe)
        if not match:
            return "Instruction not found."
        return match.group(1).strip()

    def create_image_prompt(self):
        return (
            f"Generate a professional food photograph of {self.title}. The finished dish described in the following recipe. The photo should focus on realistic textures, lighting, and presentation, as if styled for a high-end food magazine.\n"\
            + f"{self.instruction}\n"\
            + f"Based on the recipe above, show the final plated dish. The image should emphasize the colors, textures, and overall appearance of the finished meal."
        )

    @staticmethod
    def get_image_url(prompt):
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            return response['data'][0]['url']
        except Exception as e:
            print(f"Error generating image: {e}")
            return None

    @staticmethod
    def save_image(url, file_name):
        try:
            res = requests.get(url, stream=True)
            if res.status_code == 200:
                with open(file_name, 'wb') as f:
                    shutil.copyfileobj(res.raw, f)
                print(f"Image saved to {file_name}")
            else:
                print(f"Failed to download image: {res.status_code}")
        except Exception as e:
            print(f"Error saving image: {e}")

    @staticmethod
    def save_to_file(file_name, content):
        try:
            with open(file_name, "w") as f:
                f.write(content)
            print(f"Recipe saved to {file_name}")
        except Exception as e:
            print(f"Error saving file: {e}")


if __name__ == "__main__":
    generator = RecipeWithImageGenerator()
    generator.run()