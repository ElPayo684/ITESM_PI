from pathlib import Path
import zipfile
import gdown

GDRIVE_FILE_ID = "FILE_ID"

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw"
ZIP_PATH = DATA_RAW_DIR / "dataset.zip"

def download_data():
    DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)

    if ZIP_PATH.exists():
        print("Dataset already downloaded.")
        return

    url = f"https://drive.google.com/uc?id={GDRIVE_FILE_ID}"
    print("Downloading dataset from Google Drive...")
    gdown.download(url, str(ZIP_PATH), quiet=False)

    print("Extracting dataset...")
    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall(DATA_RAW_DIR)

    print("Dataset ready in data/raw/")

if __name__ == "__main__":
    download_data()