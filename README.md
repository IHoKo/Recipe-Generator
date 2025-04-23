# 🍽️ AI-Powered Recipe Generator

This Python application uses OpenAI’s GPT and DALL·E APIs to create detailed recipes, cultural backgrounds, and high-quality dish images—all based on either a **dish name** or a list of **ingredients** you provide. Perfect for food enthusiasts, hobbyist chefs, and anyone curious about AI-powered creativity in the kitchen.

---

## 🔧 How It Works

1. **User Input**:
   - On running the script, you're prompted:
     ```
     Are you entering a dish name or ingredients? Type 'dish' or 'ingredients':
     ```
   - Based on your choice:
     - **If 'dish'**: Enter the name of a specific dish (e.g., "Mirzaghasemi").
     - **If 'ingredients'**: Enter ingredients one by one (e.g., egg, eggplant, tomato, garlic), finishing with `done`.

2. **Text Generation (via GPT-3.5)**:
   - A custom prompt is generated for GPT-3.5-turbo-instruct to produce:
     - A brief background or cultural origin
     - A recipe title (prefixed with “Recipe Title:”)
     - A numbered list of cooking steps
     - A list of ingredients (if relevant)

3. **Image Generation (via DALL·E)**:
   - A detailed image prompt is constructed from the recipe text and sent to DALL·E.
   - The AI generates a high-quality, food magazine-style image of the final dish.

4. **Output Files**:
   - A `.txt` file with the full recipe
   - A `.jpg` file with the AI-generated dish image

---

## 📂 Example Output
dish
mirzaghasemi

### 📝 Recipe 
![Mirzaghasemi](https://github.com/user-attachments/assets/4cfa7476-8c56-49cc-be6d-0755d56916c8)

[Uploading MirzaghaseBackground: Mirzaghasemi is a popular Persian dish, originating from the Gilan province in Northern Iran. It is a vegetarian dish made with eggplant, tomatoes, and various spices.

Recipe Title: Mirzaghasemi

Common ingredients:
1. Eggplant
2. Tomatoes
3. Garlic
4. Eggs
5. Olive oil
6. Turmeric
7. Salt
8. Black pepper
9. Cumin
10. Red chili flakes
11. Fresh herbs (such as parsley or cilantro)

Recipe:

1. Preheat your oven to 400 degrees Fahrenheit.

2. Wash and dry 2 medium-sized eggplants. Using a fork, prick the eggplants all over.

3. Place the eggplants on a baking sheet and roast them in the oven for 30-40 minutes, until the skin is charred and the eggplants are soft.

4. While the eggplants are roasting, peel and finely chop 4 cloves of garlic.

5. Heat 2 tablespoons of olive oil in a pan over medium heat. Add the chopped garlic and cook for 1-2 minutes, until fragrant.

6. Dice 2 medium-sized tomatoes and add them to the pan with the garlic. Cook for 5-7 minutes, until the tomatoes have softened.

7. Once the eggplants are done roasting, remove them from the oven and let them cool. Once cooled, peel off the charred skin and chop the eggplant flesh into small pieces.

8. Add the chopped eggplant to the pan with the tomatoes and garlic. Mix well and let it cook for another 5 minutes.

9. In a separate bowl, beat 3 eggs with a pinch of salt, black pepper, and a pinch of turmeric.

10. Pour the beaten eggs over the eggplant mixture in the pan. Use a spatula to mix everything together and let it cook for 2-3 minutes.

11. Sprinkle 1 teaspoon of cumin and 1 teaspoon of red chili flakes over the mixture. Mix well and let it cook for another 2-3 minutes.

12. Once the eggs are fully cooked and the mixture is well combined, turn off the heat.

13. Serve the mirzaghasemi hot, garnished with fresh herbs of your choice. It can be enjoyed with bread or rice as a main dish or as a side dish. Enjoy!mi.txt…]()


