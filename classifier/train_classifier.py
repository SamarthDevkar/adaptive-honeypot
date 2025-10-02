# train_classifier.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Load data
df = pd.read_csv("labeled_commands.csv", names=["command", "label"])

# Train classifier
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(df["command"], df["label"])

# Save model
joblib.dump(model, "command_classifier.joblib")
