import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_power_rankings(season="2526"):
    """Load Elo ratings from power_rankings CSV"""
    path = os.path.join(DATA_DIR, f"power_rankings_{season}.csv")
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Cannot find: {path}")
    
    df = pd.read_csv(path)
    df["Team"] = df["Team"].str.strip()
    
    ratings = dict(zip(df["Team"], df["EloRating"]))
    return ratings


def load_current_table(season="2526"):
    """Load current league standings from summary_table CSV"""
    path = os.path.join(DATA_DIR, f"summary_table{season}.csv")
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Cannot find: {path}")
    
    df = pd.read_csv(path)
    df["Team"] = df["Team"].str.strip()
    
    table = {}
    for _, row in df.iterrows():
        table[row["Team"]] = {
            "points": row["Pts"],
            "played": row["MP"],
            "wins": row["W"],
            "draws": row["D"],
            "losses": row["L"]
        }
    
    return table