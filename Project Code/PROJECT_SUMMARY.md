# Restaurant Recommender Project - Completion Summary

## Project Overview
This is a **Content-Based Restaurant Recommendation System** built with Flask and scikit-learn. It analyzes restaurant attributes (cuisines, types, locations) to recommend similar restaurants to users.

## Project Structure
```
Restaurant-Recommender-main/
├── Flask/
│   ├── app1.py                 # Main Flask application
│   ├── restaurant1.csv         # Preprocessed restaurant dataset (4000 records)
│   ├── restaurant.pkl          # Serialized model (similarity matrix & indices)
│   ├── requirements.txt        # Python dependencies
│   ├── Procfile               # Heroku deployment config
│   ├── runtime.txt            # Python runtime version
│   ├── static/
│   │   └── style.css          # Modern dark-themed styling with Glassmorphism
│   └── templates/
│       └── index.html         # Interactive UI with restaurant search & recommendations
├── Model/
│   └── build_model.py         # Model building pipeline
├── Document/
│   └── Project_Documentation.pdf
└── PROJECT_SUMMARY.md         # This file
```

## All Project Files

### Backend Files
1. **app1.py** - Flask web server
   - Routes: GET `/` (home page), POST `/predict` (recommendations)
   - Loads pre-trained model from pickle file
   - Generates top 10 restaurant recommendations based on cosine similarity
   - Returns match scores (0-100%)

2. **build_model.py** - Model training pipeline
   - Loads restaurant dataset (handles missing Dataset folder gracefully)
   - Data preprocessing: cleaning names, handling missing values, deduplication
   - Feature engineering: creates "soup" from cuisines + restaurant type + city
   - Generates cosine similarity matrix using CountVectorizer
   - Exports: restaurant1.csv and restaurant.pkl to Flask folder

3. **requirements.txt** - Dependencies
   - Flask==3.1.0 (Web framework)
   - gunicorn==22.0.0 (Production server)
   - pandas==2.2.3 (Data manipulation)
   - numpy==2.2.1 (Numerical computing)
   - scikit-learn==1.6.1 (ML algorithms)

4. **Procfile** - Heroku deployment configuration
5. **runtime.txt** - Python version specification

### Frontend Files
1. **index.html** - Interactive UI with:
   - Hero section with project description
   - Dropdown search for 4000 restaurants (using Choices.js library)
   - Results grid displaying recommendations with:
     - Restaurant name & location
     - Cuisine types
     - Rating & cost estimate
     - Match percentage score

2. **style.css** - Modern dark theme styling featuring:
   - Dark gradient background (#0f172a)
   - Glassmorphism effects (semi-transparent panels)
   - Responsive grid layout for recommendation cards
   - Smooth transitions and hover effects
   - Color scheme: Rose accent (#f43f5e) on dark background

### Data Files
1. **restaurant1.csv** - Preprocessed dataset with 4000 restaurants
   - Columns: name, online_order, book_table, rate, votes, location, rest_type, cuisines, approx_cost(for two people), listed_in(type), listed_in(city), soup
   
2. **restaurant.pkl** - Serialized model containing:
   - `similarity_matrix`: Cosine similarity scores between all restaurants
   - `indices`: Mapping of restaurant names to their dataframe indices
   - `restaurant_data`: Restaurant metadata for display (name, cuisines, location, rate, cost)

## How It Works

1. **Model Generation** (build_model.py):
   - Loads 4000 restaurant records
   - Creates feature vectors from: cuisines + restaurant_type + city
   - Computes pairwise cosine similarity matrix
   - Saves model to pickle for quick loading

2. **User Interaction** (Flask app):
   - User selects a restaurant from dropdown
   - Flask retrieves similarity scores for that restaurant
   - Returns top 10 most similar restaurants
   - Displays results with match percentages and metadata

3. **Recommendation Algorithm**:
   - Content-based filtering using cosine similarity
   - Feature space: combined text of cuisines, restaurant type, and city
   - Similarity range: 0-100% match score

## Running the Project

### Prerequisites
- Python 3.11+ (already configured in .venv)
- All dependencies installed via requirements.txt

### Steps to Run

1. **Build the model** (if not already done):
   ```bash
   cd Model
   python build_model.py
   ```

2. **Start the Flask app**:
   ```bash
   cd Flask
   python app1.py
   ```

3. **Access the application**:
   - Open browser: http://127.0.0.1:5000
   - Select a restaurant from the dropdown
   - Click "Find Recommendations"
   - View similar restaurant suggestions

## Project Status: ✅ COMPLETE

### Completed Components:
✅ Flask web application running successfully  
✅ Model generated and loaded (restaurant.pkl created)  
✅ Frontend UI with interactive search and results display  
✅ Backend recommendation engine functional  
✅ All dependencies installed and configured  
✅ Data preprocessing pipeline working  

### Features Implemented:
✅ Restaurant search dropdown (4000 entries)  
✅ Content-based recommendation system  
✅ Match score calculation (0-100%)  
✅ Restaurant metadata display (location, cuisine, rating, cost)  
✅ Responsive dark-themed UI  
✅ Search-enabled dropdown with Choices.js  
✅ Error handling for missing model files  

### Application is Currently Running:
- Server: http://127.0.0.1:5000
- Status: 🟢 Online
- Model: ✅ Loaded
- Database: ✅ Ready (4000 restaurants)

## Deployment Notes
- The `Procfile` and `runtime.txt` are configured for Heroku deployment
- In production, replace `debug=True` with production WSGI server (e.g., Gunicorn)
- The model file (restaurant.pkl) needs to be included in deployments

## Testing the System
1. Select "Cupcake Bliss" restaurant
2. Get 10 recommendations similar to bakery/delivery places in Bangalore area
3. Try "NH8" restaurant (Casual dining)
4. Observe different restaurant types being recommended

## Technical Highlights
- **Efficient**: Pre-computed cosine similarity matrix for O(1) recommendation lookup
- **Scalable**: Works with 4000+ restaurants, easily extendable
- **User-Friendly**: Clean UI with real-time search and visual match scores
- **Robust**: Handles missing columns, encoding issues, and data cleaning automatically
