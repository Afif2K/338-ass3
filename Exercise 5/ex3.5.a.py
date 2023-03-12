import time
import random
import numpy as np
import matplotlib.pyplot as plt

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
 
    return -1

def experiment():
    sizes = [1000, 10000, 100000]
    measurements = 100
    results = {}
    for size in sizes:
        arr = [random.randint(0, size) for _ in range(size)]
        arr.sort()
        x = random.randint(0, size)
        linear_times = []
        binary_times = []
        for _ in range(measurements):
            start_time = time.time()
            linear_search(arr, x)
            end_time = time.time()
            linear_times.append(end_time - start_time)
            
            start_time = time.time()
            binary_search(arr, x)
            end_time = time.time()
            binary_times.append(end_time - start_time)
            
        results[size] = {'linear': np.mean(linear_times), 'binary': np.mean(binary_times)}
        
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))
        
        for i, size in enumerate(sizes):
            axs[i].hist(linear_times, alpha=0.5, label='linear')
            axs[i].hist(binary_times, alpha=0.5, label='binary')
            axs[i].set_title(f'Size {size}')
            axs[i].legend(loc='upper right')
        plt.show()
    return results

experiment()
