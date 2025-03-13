# AI Recipe Recommender

An intelligent recipe recommendation system that suggests recipes based on ingredients you already have at home, powered by machine learning.

## Features

- Enter ingredients you already have in your kitchen
- Get AI-ranked recipes that best match your available ingredients
- See which ingredients you have and which you need to buy
- View detailed recipe information including instructions
- Machine learning-based ranking using TF-IDF and cosine similarity

## Technologies Used

- **Python Flask**: Web framework for the application
- **Scikit-learn**: TF-IDF vectorization and cosine similarity
- **Spoonacular API**: Recipe data source
- **Bootstrap**: Frontend styling

## How It Works

The system uses a machine learning approach to recommend recipes:

1. **Data Collection**: Fetches recipe data from the Spoonacular API based on user ingredients
2. **Feature Extraction**: Converts ingredient lists into TF-IDF vectors
3. **Similarity Calculation**: Uses cosine similarity to measure how well recipes match user ingredients
4. **Ranking**: Sorts recipes by similarity score to show the best matches first
5. **Visualization**: Clearly marks which ingredients the user has and which they need

## Installation

1. Clone the repository
   ```
   git clone https://github.com/yourusername/recipe-recommender.git
   cd recipe-recommender
   ```

2. Create a virtual environment
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your Spoonacular API key
   ```
   SPOONACULAR_API_KEY=your_api_key_here
   ```

5. Run the application
   ```
   python app.py
   ```

6. Open your browser and go to http://127.0.0.1:5000/

## Project Structure

- **app.py**: Main Flask application
- **api_helper.py**: Functions for interacting with the Spoonacular API
- **ml_model.py**: Machine learning model for recipe recommendations
- **templates/**: HTML templates for the web interface
- **static/**: CSS and JavaScript files

## Future Improvements

- Dietary restrictions filtering
- Ingredient substitution suggestions
- User accounts to save favorite recipes
- More sophisticated NLP for ingredient matching
- Mobile app version

## Screenshot

[Insert screenshot of application here]

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Spoonacular API](https://spoonacular.com/food-api) for providing recipe data
- Scikit-learn for machine learning tools
- Flask for the web framework
