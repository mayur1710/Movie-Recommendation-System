# Movie Recommendation System
![image](https://github.com/user-attachments/assets/239c39d4-f789-4600-a62a-bf5bb28c6820)


This project is a simple **Movie Recommendation System** that suggests movies based on user input. The system uses a similarity matrix generated from the movie metadata dataset and fetches movie posters using the TMDB API.

---

## Features

- Recommends five movies similar to the user's selected movie.
- Displays posters of the recommended movies for better user experience.
- User-friendly interface built with Streamlit.

---

## Dataset

The dataset used for this project is from [Kaggle's TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

### Steps to Prepare the Dataset:

1. Download the dataset from [this link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
2. Preprocess the dataset as needed (e.g., extracting necessary columns).
3. Generate a similarity matrix using features like genres, keywords, cast, etc.
4. Save the processed data and similarity matrix into `.pkl` files:
   - `movie_dict.pkl`: Contains movie data.
   - `similarity.pkl`: Contains the precomputed similarity matrix.

---

## Setup Instructions

### Prerequisites

Ensure you have Python installed on your system. Install the required libraries using the `requirements.txt` file.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd movie-recommendation-system
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your TMDB API key in the `fetch_poster` function (replace `b7e0da4255863382860eb7727db6fa4f` with your API key).

### Running the App

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open the provided local URL in your browser.

---

## File Descriptions

- **app.py**: The main script to run the Streamlit application.
- **movie\_dict.pkl**: Serialized dictionary containing movie metadata.
- **similarity.pkl**: Serialized similarity matrix for movie recommendations.
- **requirements.txt**: List of required Python libraries.

---

## Usage

1. Open the app and select a movie from the dropdown menu.
2. Click on the "Recommend" button.
3. View the recommended movies along with their posters.

---

## Example



---

## Acknowledgments

- Dataset: [TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- API: [TMDB API](https://www.themoviedb.org/documentation/api)
- Streamlit for an easy-to-build interactive user interface.

---


