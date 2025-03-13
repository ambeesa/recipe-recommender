# test_api.py
from api_helper import get_recipes_by_ingredients, get_recipe_information

# Test the get_recipes_by_ingredients function
print("Testing recipe search by ingredients...")
ingredients = ["chicken", "pasta", "tomato"]
recipes = get_recipes_by_ingredients(ingredients, number=3)

if recipes:
    print(f"Found {len(recipes)} recipes")
    
    # Print basic info about each recipe
    for recipe in recipes:
        print(f"\nRecipe: {recipe['title']}")
        print(f"Used ingredients: {[ing['name'] for ing in recipe['usedIngredients']]}")
        print(f"Missing ingredients: {[ing['name'] for ing in recipe['missedIngredients']]}")
    
    # Test the get_recipe_information function with the first recipe
    if recipes:
        recipe_id = recipes[0]['id']
        print(f"\nGetting detailed information for recipe {recipe_id}...")
        recipe_info = get_recipe_information(recipe_id)
        
        if recipe_info:
            print(f"Recipe: {recipe_info['title']}")
            print(f"Ready in {recipe_info['readyInMinutes']} minutes")
            print(f"Servings: {recipe_info['servings']}")
            print(f"Source: {recipe_info['sourceUrl']}")
        else:
            print("Failed to get recipe information")
else:
    print("No recipes found or API error occurred")