from data_loader import DATA_DIR
import os

print(f"DATA_DIR resolves to: {DATA_DIR}")
print(f"Does it exist? {os.path.exists(DATA_DIR)}")
print(f"\nFiles in DATA_DIR:")
if os.path.exists(DATA_DIR):
    print(os.listdir(DATA_DIR))