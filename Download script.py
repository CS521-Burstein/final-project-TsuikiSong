#!/usr/bin/env python
# coding: utf-8

# In[13]:


import requests
import shutil
import urllib3
def download_script():
    urllib3.disable_warnings()
    url1 = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    url2 = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    url3 = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names"
    r1 = requests.get(url1, verify=False,stream=True)
    r2 = requests.get(url2, verify=False,stream=True)
    r3 = requests.get(url3, verify=False,stream=True)
    r1.raw.decode_content = True
    r2.raw.decode_content = True
    r3.raw.decode_content = True
    with open("winequality-red.csv", 'wb') as f:
        shutil.copyfileobj(r1.raw, f)
    with open("winequality-white.csv", 'wb') as f:
        shutil.copyfileobj(r2.raw, f)
    with open("winequality.names", 'wb') as f:
        shutil.copyfileobj(r3.raw, f)

if __name__ == '__main__':
    download_script()


# In[ ]:




