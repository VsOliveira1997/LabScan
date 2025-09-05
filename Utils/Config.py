import os
import requests


class Config:
    def __init__(self, path):
        self.path = path

    def get_path(self):
        try:
            if self.path is None:
                self.path = ".."
            with open(".env", "w") as f:
                f.write(f"DIR_SAVE={self.path}\n")
        except Exception as e:
            print(e)
