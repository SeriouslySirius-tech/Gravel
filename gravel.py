import random
import time
import numpy as np


maxOnes = 0
rolls = 10**6 # 1 million = 1,000,000,000 = 10**6
start = time.time()
for i in range(rolls):
    n = 4  # No. of moves
    probabilities = np.random.normal(0.25, 0.0001, size=(4))
    if (min(probabilities) < 0): continue
    # print(probabilities)
    probabilities /= sum(probabilities)
    # print(probabilities)
    # print(sum(probabilities))
    # print(probabilities*231)
    probabilities *= 231
    print(f"{i}/{rolls}")
    print(probabilities)
    print(sum(probabilities))
    # print(f"Max Ones on any move (if it's max I just move the paralysis move to it): {int(max(probabilities))}")
    if (not (max(probabilities) >= 231)):
        maxOnes = max(maxOnes, int(max(probabilities)))
        
end = time.time()
print(f"Total Time Taken: {int((end-start)//60)}:{int((end-start)%60)}")
print(f"Max Ones obtained: {maxOnes}")
print(f"No. of rolls done: {rolls}")


