Molecular Property Prediction Using Machine Learning
Overview

This project applies machine learning techniques to predict molecular properties, specifically melting points, from molecular structures. Using Python, RDKit for cheminformatics, and scikit-learn for machine learning, this project demonstrates an end-to-end workflow from data processing to model evaluation.

Prerequisites
Python 3.8+
Libraries: pandas, numpy, scikit-learn, RDKit (for cheminformatics)

Installation
To set up the project environment, install the required libraries using pip:
pip install pandas numpy scikit-learn rdkit

Dataset
The dataset should be in CSV format with the following columns:

SMILES: The SMILES notation of the molecule.
mpC: The melting point of the molecule in Celsius.

Example:
SMILES,mpC
C1=CC=C(C=C1)C=O,60.5
CC(C(=O)O)N,140.7
...

Project Structure
data_preprocessing.py: Contains functions for loading and preprocessing data.
feature_engineering.py: Includes methods to convert SMILES to molecular descriptors.
model.py: Defines, trains, and evaluates the machine learning model.
main.py: The main script that orchestrates data loading, preprocessing, feature engineering, model training, and evaluation.

Usage
Run the main script to execute the project:
python main.py

Model
The project uses a RandomForestRegressor model from scikit-learn. This model was chosen for its robustness and effectiveness in handling complex, non-linear data without extensive hyperparameter tuning.

Evaluation
The model's performance is evaluated using Mean Squared Error (MSE) and R-squared (R²) metrics. These metrics provide insights into the model's accuracy and predictive power.

