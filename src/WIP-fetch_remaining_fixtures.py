import requests
import pandas as pd
from datetime import datetime


def fetch_fixtures():
    #scrape bbc sport or premier league API
    
    #replace below with actual scraping logic
    fixtures = []
    
    # Save to CSV
    df = pd.DataFrame(fixtures, columns=['HomeTeam', 'AwayTeam', 'Date'])
    df.to_csv('data/remaining_fixtures2526.csv', index=False)
    
fetch_fixtures()