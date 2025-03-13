#imported libraries
import os
import json
import requests
from pathlib import Path 
from dotenv import load_dotenv

#load environment variables from env file
load_dotenv()
#get api key from environment variables
API_KEY = os.getenv("SPOONACULAR_API_KEY")

#create a cache directory to store api responses
#this prervents unnecessary API calls during developpment

CACHE_DIR = Path("cache")
CACHE_DIR.mkdir(exist_ok=True)

def get_recipes_by_ingredients(ingredients, number = 10):
    #Get recipies that use the provided ingredients. 
    #Cache results to avoid repeated API Calls while developing.

    #create a cache filename based on the ingredients

    ingredients_str = ",".join(sorted(ingredients))
    cache_file = CACHE_DIR / f"{hash(ingredients_str)}.json"

    #check if we cached results
    if cache_file.exists():
        with open(cache_file, "r") as f:
            return json.load(f)
    #make API Request
    
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "apiKey": API_KEY,
        "ingredients": ingredients_str,
        "number": number,
        "ranking": 2,  #maximize used ingredients
        "ignorePantry": False
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        #cache the results

        with open(cache_file, "w") as f:
            json.dump(data, f)
        return data
    else:
        print(f"Error: {response.status_code}")
        return []

def get_recipe_information(recipe_id):
    """Get detailed information abotu a recipe by its ID."""
    cache_file = CACHE_DIR / f"recipe_{recipe_id}.json"

    #check cache first

    if cache_file.exists():
        with open(cache_file, "r") as f:
            return json.load(f)
    
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {
        "apiKey": API_KEY,
        "includeNutrition": False
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        #cache the results

        with open(cache_file, "w") as f:
            json.dump(data,f)
        return data
    else:
        print(f"Error: {response.status_code}")
        return {}