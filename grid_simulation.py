import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

my_arr = np.zeros((101, 101))
arr_timeline = np.zeros((101, 2))

fig, axs = plt.subplots(5, 2, figsize=(15, 30))

for j in range(5):
    strength = 100
    posnx = 51
    posny = 51
    T = 0
    while strength > 0:
        r = random.choice([1, 2, 3, 4])
        if r == 1:
            posnx += 1
        elif r ==2:
            posnx -= 1
        elif r == 3:
            posny += 1
        elif r == 4:
            posny -= 1
            
        strength -= 1
        my_arr[posnx][posny] = my_arr[posnx][posny] + 1
        T += 1
        arr_timeline[T][0] = posnx
        arr_timeline[T][1] = posny

    sns.heatmap(my_arr, ax = axs[j, 0])
    axs[j, 0].set_xticks([])
    axs[j, 0].set_yticks([])
    axs[j//2, 0].set_title('Grid')
    
    axs[j, 1].plot(arr_timeline[1:, 0], arr_timeline[1:, 1], '-o')
    axs[j, 1].set_title('Time')    
    
plt.tight_layout()
plt.show()