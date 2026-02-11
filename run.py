from src.data_loader import load_power_rankings, load_current_table
from src.pipeline import run_simulation_pipeline
import pandas as pd


def main():
    season = "2526"
    ratings = load_power_rankings(season)
    current_table = load_current_table(season)
    
    #FETCH REMAINING FIXTURES NOW
    fixtures_df = pd.read_csv(f"data/remaining_fixtures{season}.csv")
    
    # Run simulation
    results = run_simulation_pipeline(
        fixtures_df,
        ratings,
        current_table,
        season=season
    )
    
    print("Simulation complete.\n")
    print(results)


if __name__ == "__main__":
    main()