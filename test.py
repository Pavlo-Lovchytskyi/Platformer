import os
import re
#personnel = os.listdir('data/player/running')
personnel = sorted(os.listdir('data/player/holding/left'), key=lambda x: int(re.search(r'\d+', x).group()))
print(personnel)