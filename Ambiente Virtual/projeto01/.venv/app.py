import os
from tqdm import tqdm
import time
directory = os.listdir('/home/churros/Área de trabalho/Alex - Framework Backend/Ambiente Virtual/projeto01')

for item in tqdm(directory):
    print (item)
    time.sleep(2)
