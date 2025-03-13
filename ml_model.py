import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer #converts texts to numerical feature vectors
from sklearn.metrics.pairwise import cosine_similarity #calculates similarity between vectors

class RecipeRecommender:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english') # removes common english words
        # stores the recipe vectors and recipe data
        self.recipe_vectors = None
        self.recipes = None 

    def extract_features(self,recipes):
        """
        Extract features from recipes using TF-IDF on ingredients
        Uses TF-IDF Vectorizer to convert our ingredient lists into numerical vectors
        Stores these vectors for later use
        Returns the vectors
        """
        self.recipes = recipes

        #extract ingredients and create docs for vectorization
        documents = []
        """ Stores the recipes in the class, creates a list of documents where each document is a string of all ingredients 
            in a recipe
            Uses .get() with default values in case keys dont exist
        """
        for recipe in recipes:
            #join all ingredients into one string
            ingredients_text = " ".join([item.get('name', '')
                                            for item in recipe.get('missedIngredients', []) +
                                            recipe.get('usedIngredients', [])])
            documents.append(ingredients_text)

        #fit vectorizer and trransform docs to TD-IDF Vectors
        self.recipe_vectors = self.vectorizer.fit_transform(documents)
        return self.recipe_vectors
    
    def rank_recipes(self, user_ingredients):
        """
        Rank recipes based o n similarity to user ingredients
        Checks if we have recipe vectors - returns empty list if not
        Joins the users ingreidents into a single string
        Transforms the string into vector using the same vectorizer
        """
        if self.recipe_vectors is None or self.recipes is None:
            return []
        #create a vector for user ingredients
        user_text = " ".join(user_ingredients)
        user_vector = self.vectorizer.transform([user_text])
        
        #calculate similarities between user ingredients and recipes
        similarities = cosine_similarity(user_vector, self.recipe_vectors).flatten()

        #create a list of recipe, similarity tuples
        recipe_scores = []
        for i in range(len(self.recipes)):
            recipe = self.recipes[i]
            similarity = similarities[i]
            recipe_scores.append((recipe, similarity))

        # sort by similarity(descending) - using bubble soirt
            
        for i in range(len(recipe_scores)):
            for j in range(0, len(recipe_scores)- i - 1):
                #if the similarity of the current pair is < next pair, swap
                if recipe_scores[j][1] < recipe_scores[j+1][1]:
                    temp = recipe_scores[j]
                    recipe_scores[j] = recipe_scores[j+1]
                    recipe_scores[j+1] = temp
        return recipe_scores   