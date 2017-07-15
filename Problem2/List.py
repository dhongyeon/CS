import numpy as np
import pandas as pd
import csv

def Import():
    with open('Phytest.csv',newline='') as f:
        reader = csv.reader(f)
        Phylist = list(reader)
 

