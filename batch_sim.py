import pandas as pd
import time
from git import Repo

class BatchLoader:
    def __init__(self, data_file, batch_size) -> None:
        self.data_file = data_file
        self.data = None
        self.batch_size = batch_size
        self.idx=0
    def generate(self):
        if self.data is None:
            self.data = pd.read_csv(self.data_file)
        min_idx = min([self.idx+self.batch_size, self.data.shape[0]])
        selected = self.data.iloc[self.idx:min_idx]
        self.idx = min_idx

        with open("batch.csv", "w") as f:
            selected.to_csv(f)

PATH_OF_GIT_REPO = r'./.git'
COMMIT_MESSAGE = 'new batch'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

if __name__ == "__main__":
    bl = BatchLoader("imdb_top_1000.csv", 10)
    while bl.idx < 20:
        bl.generate()
        time.sleep(3)

    