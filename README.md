# Movie Recommendation System

## Overview
The **Movie Recommendation System** is a **Flask-based web application** that provides personalized movie recommendations using **collaborative filtering techniques**. The system supports both **user-based** and **item-based collaborative filtering** and presents recommendations through an intuitive web interface.

---

## Features
- **User-Based Collaborative Filtering**: Suggests movies based on the preferences of similar users.
- **Item-Based Collaborative Filtering**: Recommends movies that are similar to those the user has already liked.
- **Handling Sparsity**: Uses **imputation techniques** to manage missing data in the user-item interaction matrix.
- **Interactive Web Interface**: Built with **Flask** and **Bootstrap** for a modern and responsive UI.
- **Movie Posters Integration**: Fetches and displays movie posters from the **TMDb API** (optional).

---


### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Scipy
- Requests (optional, for TMDb API integration)

### Steps to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd movie-recommendation-system
   ```
3. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Download the MovieLens Dataset**:
   - Place `ratings.csv` and `movies.csv` in the project directory.

5. **Run the Flask Application**:
   ```bash
   python app.py
   ```
6. **Access the Application**:
   Open your browser and go to `http://127.0.0.1:5000/`.

---

## How It Works
### 1. User-Based Collaborative Filtering
- Identifies users with similar movie preferences.
- Recommends movies that similar users have highly rated but the target user has not seen.

### 2. Item-Based Collaborative Filtering
- Identifies movies that are similar to those the user has previously liked.
- Recommends movies with characteristics closely matching the user’s interests.

### 3. Handling Sparsity
- Fills missing values in the user-item interaction matrix using the average rating of each user.
- Ensures accurate similarity calculations.

---

## Code Structure
```
movie-recommendation-system/
├── app.py                  # Flask application
├── ratings.csv             # MovieLens ratings dataset
├── movies.csv              # MovieLens movies dataset
├── templates/              # HTML templates
│   ├── index.html          # Home page
│   └── recommendations.html # Recommendations page
├── static/                 # Static files (CSS, images)
│   └── styles.css          # Custom CSS
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

---

## Usage
### **Home Page**
1. Enter a **User ID**.
2. Select an algorithm (**User-Based** or **Item-Based** Collaborative Filtering).
3. Click **Get Recommendations**.

### **Recommendations Page**
- Displays a list of recommended movies along with:
  - **Titles**
  - **Genres**
  - **Posters** (if available)
- Click **Back to Home** to return.

---

## Dataset
The system utilizes the **MovieLens dataset**, which includes:
- `ratings.csv`: Contains user ratings for movies (`userId`, `movieId`, `rating`, `timestamp`).
- `movies.csv`: Provides movie metadata (`movieId`, `title`, `genres`).

---

## Dependencies
- **Flask** - Web framework
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning algorithms
- **Scipy** - Scientific computing
- **Requests** - (Optional) Fetch movie posters from the TMDb API

---

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## Contributing
Contributions are welcome! If you find any bugs or have suggestions, please **open an issue** or **submit a pull request**.

---

## Acknowledgments
- **MovieLens** for the dataset.
- **TMDb** for the movie poster API.
- **Flask** for the web framework.
- **Bootstrap** for frontend design.

---

Enjoy using the **Movie Recommendation System**! 🎬🍿

