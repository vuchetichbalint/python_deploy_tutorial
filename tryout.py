from __future__ import print
import pandas as pd

df = pd.DataFrame([[1,2], [3,4]])

if df.sum()[0] == 4:
	print('Az elet szep! ;)')