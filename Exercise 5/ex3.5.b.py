import time
import random
import heapq
import numpy as np
import matplotlib.pyplot as plt

def inefficient_insertion(queue, x):
    queue.append(x)
    queue.sort()

def inefficient_extraction(queue):
    return queue.pop(0)

def efficient_insertion(queue, x):
    heapq.heappush(queue, x)

def efficient_extraction(queue):
    return heapq.heappop(queue)

def experiment():
    sizes = [1000, 10000, 100000]
    measurements = 100
    results = {}
    for size in sizes:
        inefficient_times = {'insertion': [], 'extraction': []}
        efficient_times = {'insertion': [], 'extraction': []}
        for _ in range(measurements):
            inefficient_queue = []
            efficient_queue = []
            for i in range(size):
                x = random.randint(0, size)
                
                start_time = time.time()
                inefficient_insertion(inefficient_queue, x)
                end_time = time.time()
                inefficient_times['insertion'].append(end_time - start_time)
                
                start_time = time.time()
                efficient_insertion(efficient_queue, x)
                end_time = time.time()
                efficient_times['insertion'].append(end_time - start_time)
                
            inefficient_extraction_times = []
            efficient_extraction_times = []
            for i in range(size):
                start_time = time.time()
                inefficient_extraction(inefficient_queue)
                end_time = time.time()
                inefficient_extraction_times.append(end_time - start_time)
                
                start_time = time.time()
                efficient_extraction(efficient_queue)
                end_time = time.time()
                efficient_extraction_times.append(end_time - start_time)
                
            inefficient_times['extraction'].append(np.mean(inefficient_extraction_times))
            efficient_times['extraction'].append(np.mean(efficient_extraction_times))
        
        results[size] = {'inefficient': inefficient_times, 'efficient': efficient_times}
        
        fig, axs = plt.subplots(2, 3, figsize=(15, 10))
        for i, size in enumerate(sizes):
            axs[0, i].hist(inefficient_times['insertion'], alpha=0.5, label='inefficient')
            axs[0, i].hist(efficient_times['insertion'], alpha=0.5, label='efficient')
            axs[0, i].set_title(f'Size {size} Insertion')
            axs[0, i].legend(loc='upper right')
            
            axs[1, i].hist(inefficient_times['extraction'], alpha=0.5, label='inefficient')
            axs[1, i].hist(efficient_times['extraction'], alpha=0.5, label='efficient')
            axs[1, i].set_title(f'Size {size} Extraction')
            axs[1, i].legend(loc='upper right')
        plt.show()
    return results

experiment()
