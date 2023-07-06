# https://www.analyticsvidhya.com/blog/2021/06/how-to-load-kaggle-datasets-directly-into-google-colab/
# https://www.youtube.com/watch?v=yEXkEUqK52Q
# https://www.kaggle.com/discussions/general/74235

def load_competition_data(
      competition, 
      drive_path='/content/drive', 
      kaggle_json_path='/content/drive/MyDrive/Docs/kaggle/kaggle.json'):
    import shutil
    import os
    import kaggle
    import zipfile 
    from google.colab import drive
    from pathlib import Path
    
    data_path = Path(f"{competition}.zip")

    if data_path.is_file():
      print('Kaggle competition data ise already availabel at', data_path.absolute())
      return None

    drive.mount(drive_path)

    Path("/root/.kaggle").mkdir(parents=True, exist_ok=True)

    shutil.copy(kaggle_json_path, '/root/.kaggle/kaggle.json')

    os.chmod('/root/.kaggle/kaggle.json', 600);

    
    kaggle.api.competition_download_cli(competition)


    with zipfile.ZipFile(data_path, 'r') as zip_ref:
      zip_ref.extractall(f'/content/{competition}')

    drive.flush_and_unmount()

load_competition_data('titanic')

