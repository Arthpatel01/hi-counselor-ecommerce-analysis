import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np
import module1 as t1
import settings
import pandas as pd

def sentiment():
    df = t1.rename_columns()
    analyzer = SentimentIntensityAnalyzer()

    df['sentiment_score'] = df['reviews_text'].apply(lambda text: analyzer.polarity_scores(text))

    df['sentiment'] = df.apply(lambda row: 'positive' if row['sentiment_score']['pos'] > row['sentiment_score']['neg'] else 'negative', axis=1)


    df.drop(['sentiment_score'], axis=1, inplace=True)
    # Create sentiment column
    # Calculate sentiment scores for each review and assign 'positive' or 'negative' based on the scores

    return df

def process_text():
    df = sentiment()
    df['reviews_text'] = df['reviews_text'].apply(nltk.word_tokenize)
    df['reviews_text'] = df['reviews_text'].apply(settings.normalize)

    return df

def export_the_dataset():
    # Call process_text() to get the cleaned dataset with sentiment analysis and tokenization
    df = process_text()
    # Export the cleaned dataset to a new CSV file named 'ecommerce.csv'. use index = False.
    df.to_csv("ecommerce.csv")
    return df



# TASK 4: Load the Cleaned dataset 'ecommerce.csv' to the database provided.
# follow the instruction in the Task 5 description and complete the task as per it.

# check if mysql table is created using "ecommerce"
# Use this final dataset and upload it on the provided database for performing analysis in MySQL
# To run this task click on the terminal and click on the run project



