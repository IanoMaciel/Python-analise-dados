import pandas as pd
import numpy as np

familyData = {
    'Name': [
        'Iane Neto',
        'Iano Maciel',
        'Iana Maciel', 
        'Raiza Benedito',
        'Raimunda Maria',
        'Iane Maciel'
    ],
    'Gender': ['M', 'M', 'F', 'F', 'F', 'M'],
    'Age': [5, 22, 24, 29, 49, 50]
}

df = pd.DataFrame(data=familyData)

df