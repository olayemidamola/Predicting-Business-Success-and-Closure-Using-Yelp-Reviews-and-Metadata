# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# Load Data
files = {
    "business": "C:\Data Analysis\ML\capstone\yelp\yelp_academic_dataset_business.json",
    "checkin": "C:\Data Analysis\ML\capstone\yelp\yelp_academic_dataset_checkin.json",
    "photos": "C:\Data Analysis\ML\capstone\yelp\photos.json",
    "review": "C:\Data Analysis\ML\capstone\yelp\yelp_academic_dataset_review.json",
    "tip": "C:\Data Analysis\ML\capstone\yelp\yelp_academic_dataset_tip.json",
    "user": "C:\Data Analysis\ML\capstone\yelp\yelp_academic_dataset_user.json"
}

limit = 150000 # limit the number of rows

datasets = {}
for name, path in files.items():
    df = pd.read_json(path, lines=True, nrows=limit)
    datasets[name] = df
    print(f"{name}: {len(df)} rows read")

business = datasets["business"]
checkin = datasets["checkin"]
photos = datasets["photos"]
review = datasets["review"]
tip = datasets["tip"]
user = datasets["user"]