#import needed libraries
from flask import Flask, render_template, request, redirect, url_for
from api_helper import get_recipes_by_ingredients, get_recipe_information
from ml_model import RecipeRecommender

#create flask app
app = Flask(__name__)
recommender = RecipeRecommender()

#define the homepage route
@app.route('/')
def index():
    """Show the homepage with the ingredient input form"""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """processes the ingredient form and redirect to food item"""
    ingredients = request.form.get('ingredients', '')
    if not ingredients:
        return redirect(url_for('index'))
    
    #splits ingreidents by comma
    ingredients_split = ingredients.split(',')
    
    #clean up ingredients
    ingredients_list = []
    for ingredient in ingredients_split:
        #removewhitespace
        ingredient = ingredient.strip()
        #only add nonempty ingredients
        if ingredient:
            ingredients_list.append(ingredient)
    
    #join ingredients back with commas
    ingredients_joined = ','.join(ingredients_list)

    #redirect to results page with ingredients as parameters
    return redirect(url_for('results', ingredients=ingredients_joined))

@app.route('/results')
def results():
    """show recipe results"""
    #get ingredients from url parameters
    ingredients_param = request.args.get('ingredients', '')
    if not ingredients_param:
        return redirect(url_for('index'))
    ingredients_list = ingredients_param.split(',')

    #get recipes from api call

    recipes = get_recipes_by_ingredients(ingredients_list)

    if not recipes:
        return render_template('results.html',
                               ingredients=ingredients_list,
                               recipes=[],
                               message = "no recipes found with those ingredients. try again")
    
    #use ml model for ranking recipes
    recommender.extract_features(recipes)
    ranked_recipes = recommender.rank_recipes(ingredients_list)

    # a formatted score percentage to each recipe

    for i in range(len(ranked_recipes)):
        recipe = ranked_recipes[i][0]
        score = ranked_recipes[i][1]
        recipe['match_score'] = f"{score * 100:.1f}%"
    #create listr of just recipes without score
    recipes_only = []
    for i in range(len(ranked_recipes)):
        recipes_only.append(ranked_recipes[i][0])

    #send data to template
    return render_template('results.html',
                           ingredients=ingredients_list,
                           recipes=recipes_only,
                           message=None)
#recipe detail route
@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    """shows detasiled information about a specific recipe"""
    #get ingredients for highlighting
    ingredients_param = request.args.get('ingredients', '')

    #create ingredient list
    if ingredients_param:
        ingredients_list = ingredients_param.split(',')
    else:
        ingredients_list = []

    # get detailed recipe information
    recipe_info = get_recipe_information(recipe_id)

    if not recipe_info:
        return redirect(url_for('index'))
    
    #mark which ingredients the user has
    if len(ingredients_list) > 0:
        user_ingredients_lower = []
        for ing in ingredients_list:
            user_ingredients_lower.append(ing.lower())

            #checks each recipe ingredients
        extended_ingredients = recipe_info.get('extendedIngredients', [])
        for ingredient in extended_ingredients:
            name = ingredient.get('name', '')
            if name:
                name = name.lower()

            #checks if the user has this ingrident
            user_has_ingreident = False
            for user_ing in user_ingredients_lower:
                if user_ing in name:
                    user_has_ingreident = True
                    break
            #mark the ingredient
            ingredient['user_has'] = user_has_ingreident
    return render_template('recipe.html', recipe=recipe_info, ingredients = ingredients_list)
                

# Run the application 
if __name__ == '__main__':
    app.run(debug=True)