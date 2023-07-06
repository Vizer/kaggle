# https://www.analyticsvidhya.com/blog/2021/06/how-to-load-kaggle-datasets-directly-into-google-colab/
# https://www.youtube.com/watch?v=yEXkEUqK52Q
# https://www.kaggle.com/discussions/general/74235

def load_competition_data(
      competition, 
      drive_path='/content/drive', 
      kaggle_json_path='/content/drive/MyDrive/Docs/kaggle/kaggle.json'):
    import shutil
    import os
    import zipfile 
    from google.colab import drive
    from pathlib import Path

    KAGGLE_DESTINATION = "/root/.kaggle"
    KAGGLE_JSON_DESTINATION = f"{KAGGLE_DESTINATION}/kaggle.json"
    DATA_DESTINATION = f'/content/{competition}'
    
    data_path = Path(f"{competition}.zip")

    if data_path.is_file():
      print('Kaggle competition data is already available at', data_path.absolute())
      return None

    drive.mount(drive_path, readonly=True)

    Path(KAGGLE_DESTINATION).mkdir(parents=True, exist_ok=True)

    shutil.copy(kaggle_json_path, KAGGLE_JSON_DESTINATION)

    os.chmod(KAGGLE_JSON_DESTINATION, 600);

    import kaggle
    kaggle.api.competition_download_cli(competition)

    with zipfile.ZipFile(data_path, 'r') as zip_ref:
      zip_ref.extractall(DATA_DESTINATION)

    drive.flush_and_unmount()

load_competition_data('titanic')

