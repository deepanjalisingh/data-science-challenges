import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        csv_path='/Users/himanshu/code/deepanjalisingh/data-challenges/04-Decision-Science/data/csv'

        all_files = os.listdir(csv_path)
        file_names = list(filter(lambda f: f.endswith('.csv'), all_files))

        key_names={}
        for file_name in file_names:
            key=file_name.replace('_dataset.csv',"")
            key=key.replace('.csv',"")
            key=key.replace('olist_',"")
            key_names[key]=file_name

        data = {}

        for key, value in key_names.items():
            df=pd.read_csv(os.path.join(csv_path, value))
            data[key] = df

        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
