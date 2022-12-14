from asyncio import base_tasks
import math
import time
import random
import matplotlib.pyplot as plt

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)
    
    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(u, b, a):
    k = math.ceil(math.log(u)/math.log(b))
    i = 0
    n = len(a)

    while i < n:
        v_prime = BC((a[i])[0], b, k)
        a[i].append(v_prime)
        i+=1

    j = 0

    while j < k:
        for l in a:
            k_prime = (l[2])[j]
            l[0] = k_prime
        a = countSort(b, a)
        j+=1
    
    for ll in a:
        k_count = 0
        b_count = 0
        k_k = 0

        while k_count < k:
            k_k = k_k + ((ll[2])[k_count]*(b**b_count))
            b_count+=1
            k_count+=1
        
        ll.remove(ll[2])
        ll[0] = k_k
        
    return a

# In order to run your experiments, you may find the functions random.randint() and time.time() useful.
def RA(n, U):
    random_array = []
    random_c = 0

    while random_c < n:
        random_array.append([random.randint(0, U-1), random.randint(0, U-1)])
        random_c+=1
    
    return random_array

def experiment(n, U):
    # n = random.randint(-1, 2**16)
    # U = random.randint(-1, 2**20)
    a = RA(n, U)

    c_times = []
    m_times = []
    r_times = []

    avg = 0

    avg_times = []

    for i in range(3):
        ## CountSort
        startC = time.time()
        countSort(U, a)
        endC = time.time()
        c_times.append(endC - startC)

        ## MergeSort
        startM = time.time()
        mergeSort(a)
        endM = time.time()
        m_times.append(endM - startM)

        ## RadixSort
        startR = time.time()
        radixSort(U, n, a)
        endR = time.time()
        r_times.append(endR - startR)
    
    for t in c_times:
        avg = avg + t
    avg_times.append(avg / 3)

    avg = 0

    for t in m_times:
        avg = avg + t
    avg_times.append(avg / 3)

    avg = 0

    for t in r_times:
        avg = avg + t
    avg_times.append(avg / 3)

    min_index = avg_times.index(min(avg_times)) 
    
    index_map = {
        0: "red", ## count
        1: "blue", ## merge
        2: "green" ## radix
    }

    return index_map[min_index]


for U in range(1, 21):
    for n in range(1, 17):
        sort = experiment(pow(2,n), pow(2,U))
        plt.scatter(pow(2,n), pow(2,U), color = sort)

plt.xscale('log')
plt.yscale('log')
plt.show()
 