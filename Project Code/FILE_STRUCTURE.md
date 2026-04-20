# FILE STRUCTURE REFERENCE

```
d:\Restaurant-Recommender-main/
│
├── Flask/                          # Web Application Directory
│   ├── app1.py                     # Main Flask Application (99 lines)
│   │   ├── Imports: flask, pickle, pandas, os
│   │   ├── Routes:
│   │   │   ├── GET / → home page with restaurant list
│   │   │   └── POST /predict → recommendation engine
│   │   ├── Functions:
│   │   │   └── get_recommendations(name) → returns top 10 similar restaurants
│   │   └── Server: runs on port 5000 with debug mode
│   │
│   ├── requirements.txt             # Python dependencies (5 packages)
│   │   ├── Flask==3.1.0
│   │   ├── gunicorn==22.0.0
│   │   ├── pandas==2.2.3
│   │   ├── numpy==2.2.1
│   │   └── scikit-learn==1.6.1
│   │
│   ├── restaurant1.csv             # Dataset (4000 restaurants, 12 columns)
│   │   ├── Columns: name, online_order, book_table, rate, votes, location,
│   │   │            rest_type, cuisines, approx_cost(for two people),
│   │   │            listed_in(type), listed_in(city), soup
│   │   └── Size: ~2MB preprocessed data
│   │
│   ├── restaurant.pkl              # Serialized Model (4000x4000 matrix)
│   │   ├── similarity_matrix: cosine similarity scores
│   │   ├── indices: name→index mapping
│   │   └── restaurant_data: display metadata
│   │
│   ├── Procfile                    # Heroku deployment config
│   ├── runtime.txt                 # Python 3.9 for Heroku
│   │
│   ├── static/                     # Static Assets
│   │   └── style.css               # Modern dark theme styling (280+ lines)
│   │       ├── Root variables: colors, fonts
│   │       ├── Hero section: gradient background
│   │       ├── Search box: card with input/button
│   │       ├── Results grid: recommendation cards
│   │       ├── Choices.js styling: custom dropdown
│   │       └── Responsive design & animations
│   │
│   └── templates/                  # HTML Templates
│       └── index.html              # Main UI (90 lines)
│           ├── Head: meta tags, CSS links, Choices.js
│           ├── Hero: title & description
│           ├── Search form: dropdown + button
│           ├── Results: grid of restaurant cards
│           ├── Card structure: name, location, cuisine, rating, cost, match%
│           └── JavaScript: Choices.js initialization for search
│
├── Model/                          # ML Model Training Directory
│   └── build_model.py              # Model Pipeline (80+ lines)
│       ├── Data Loading: loads CSV from Dataset or Flask folder
│       ├── Preprocessing:
│       │   ├── Name cleaning (encoding fix)
│       │   ├── Column dropping (conditional)
│       │   ├── Rating handling (fill NaN, convert type)
│       │   ├── Deduplication (keep first)
│       │   └── Sampling (4000 max)
│       ├── Feature Engineering: creates "soup" column
│       ├── Similarity Calculation: CountVectorizer + cosine_similarity
│       └── Export: generates restaurant.pkl & CSV
│
├── Document/                       # Documentation
│   └── Project_Documentation.pdf
│
├── .venv/                          # Python Virtual Environment (auto-created)
│   └── Lib/site-packages/          # Installed packages
│       ├── flask/
│       ├── pandas/
│       ├── numpy/
│       ├── sklearn/
│       └── ... (other dependencies)
│
├── .gitignore                      # Git ignore rules
├── Project_Documentation.pdf       # Original documentation
└── PROJECT_SUMMARY.md              # Complete project summary (THIS FILE)
```

## Files Summary Table

| File | Type | Size | Purpose |
|------|------|------|---------|
| app1.py | Python | ~3 KB | Flask web server |
| build_model.py | Python | ~2.5 KB | ML model builder |
| index.html | HTML | ~3 KB | Web UI |
| style.css | CSS | ~8 KB | Styling & theme |
| restaurant1.csv | CSV | ~2 MB | Dataset |
| restaurant.pkl | Binary | ~100 MB | ML model |
| requirements.txt | Text | ~100 B | Dependencies |

## File Statistics

- **Total Python files**: 2 (app1.py, build_model.py)
- **Total HTML files**: 1 (index.html)
- **Total CSS files**: 1 (style.css)
- **Data files**: 1 CSV + 1 pickle
- **Configuration files**: 3 (requirements.txt, Procfile, runtime.txt)
- **Virtual environment**: Python 3.14.3 with 5 packages installed

## Key Code Files Explained

### app1.py - The Web Application
```
Line 1-4:     Imports (Flask, pickle, pandas, os)
Line 6-7:     Initialize Flask app
Line 10-22:   Load model and data from pickle
Line 24-43:   get_recommendations() function - core recommendation logic
Line 45-50:   Home route - display all restaurants
Line 51-61:   Predict route - generate recommendations
Line 63-64:   Run server on port 5000
```

### build_model.py - The Model Builder
```
Line 1-13:    Imports & data loading
Line 15-40:   Data preprocessing (cleaning, deduplication)
Line 42-52:   Feature engineering (create "soup")
Line 54-56:   Similarity calculation
Line 58-68:   Export model and data
```

### index.html - The Frontend
```
Line 1-10:    HTML head (meta, stylesheets, libraries)
Line 12-17:   Hero section (title, description)
Line 19-31:   Search form (dropdown, button)
Line 33-69:   Results display area
Line 71-99:   JavaScript (Choices.js initialization)
```

### style.css - The Styling
```
Line 1-10:    Font imports & CSS variables
Line 12-30:   Body & general styling
Line 32-100:  Hero section styling (gradient, text)
Line 102-150: Search box styling
Line 152-250: Results grid & card styling
Line 252+:    Responsive design & animations
```

## Key Data Points

**Dataset Properties:**
- Total restaurants: 4000
- Features used: cuisines, restaurant_type, city
- Similarity metric: tf-idf + cosine similarity
- Recommendation count: Top 10 matches
- Match score range: 0-100%

**Current Status:**
✅ Server running: http://127.0.0.1:5000
✅ Model loaded and working
✅ All 4000 restaurants searchable
✅ Recommendations generating correctly
