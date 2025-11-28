# Welcome to my Movie Recommender using the Movie Lens 100k dataset

## Project Overview

This jupyter Notebook implements data analysis and machine learning workflow using the MovieLens 100k dataset. Included is data loading, preprocessing, exploratory data analysis, model building, evaluation, and visualization. 

This enitire project follows Jill Cates walkthrough on Creating a Recommendation System and references the tutorial provided by topspinj on github available **[here](https://github.com/topspinj/tmls-2020-recommender-workshop)**.

## Key Features

- Data cleaning and preprocessing.
- Exploratory Data Analysis with visualizations.
- Implementation of a k-Nearest Neighbor recommendation algorithm. 
- Terminal based results and similarity outputs.

## Dependencies

The notebook uses the following Python libraries. You can install them via pip install <insert_library>:

- pandas
- numpy
- matplotlib
- seaborn
- scipy
- sklearn

## Files / Data

The following data files were referenced from the m1-100k download:

- `ml-100k/u.data`
- `ml-100k/u.item`
- `ml-100k/u.genre`

## What this notebook accomplishes

1. **Loads the dataset** into pandas.
2. **Cleans and preprocesses** the ratings and movie metadata.
3. **Explores patterns** using plots and summary statistics.
4. **Builds a kNN model** for movie to movie similarity recommendations.
5. **Displays results** directly in the notebook and terminal.

## How to Run

1. Clone the repository.
    `git clone <https://github.com/ndegryse/movie_recommender>`
2. Optional - Create a virtual enviornment through bash.
    `python -m venv venv`
    `source venv/bin/activate`
3. Install dependencies.
    `pip install pandas numpy matplotlib seaborn scipy sklearn`
3. Start Jupyter and open the notebook with your preferred interpreter.
4. **Run the cells in order from top to bottom** for best consistency and visualization. 


