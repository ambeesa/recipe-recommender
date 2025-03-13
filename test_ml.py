from api_helper import get_recipes_by_ingredients
from ml_model import RecipeRecommender

# Get some recipes using the API
print("Fetching recipes from API...")
ingredients = ["chicken", "pasta", "tomato"]
recipes = get_recipes_by_ingredients(ingredients, number=5)

# Initialize the recommender
recommender = RecipeRecommender()

# Extract features from recipes
print("\nExtracting features from recipes...")
recommender.extract_features(recipes)

# Rank recipes based on user ingredients
# Let's try with slightly different ingredients
print("\nRanking recipes based on user ingredients...")
user_ingredients = ["chicken", "tomato", "garlic", "basil"]
ranked_recipes = recommender.rank_recipes(user_ingredients)

# Print the ranked recipes with scores
print("\nRanked Recipes:")
for recipe, score in ranked_recipes:
    print(f"{recipe['title']}: {score:.4f}")