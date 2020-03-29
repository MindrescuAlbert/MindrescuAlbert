################## TEMA1 SD ##################
import statistics
import time
import random
import sys
sys.setrecursionlimit(1000000000)

########## FunctieSortareCorecta ##########

def test_Sort(lst):
    for i in range (len(lst) - 2):
        if lst[i] > lst[i+1]:
            print ("Nu este sortat corect")
            return
    print("Este sortat corect")


########## BubbleSort ##########

def BubbleSort():
    nr = len(lst)
    ordonat = 0
    while ordonat == 0:
        ordonat = 1
        for i in range(nr-1):
            if lst[i] > lst[i+1]:
                aux = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = aux
                ordonat = 0


########## CountSort ##########

def CountSort():
    if nr == 0:
        maxim = 0
    else:
        maxim = max(lst)
    frecv = [0] * (maxim + 1)
    for i in lst:
        frecv[i] = frecv[i] + 1
    poz = 0
    for i in range(maxim+1):
        while frecv[i] != 0:
            lst[poz] = i
            poz = poz + 1
            frecv[i] = frecv[i] - 1


########## MergeSort ##########

def MergeSort(lst, start, end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(lst, start, mid)
        MergeSort(lst, mid+1, end)
        Merge(lst, start, mid, end)

def Merge(lst, start, mid, end):
    aux = [0] * (end - start + 1)
    i = start
    j = mid + 1
    k = 0
    while i <= mid and j <= end:
        if lst[i] < lst[j]:
            aux[k] = lst[i]
            k = k + 1
            i = i + 1
        else:
            aux[k] = lst[j]
            k = k + 1
            j = j + 1
    while i <= mid:
        aux[k] = lst[i]
        k = k + 1
        i = i + 1
    while j <= end:
        aux[k] = lst[j]
        k = k + 1
        j = j + 1
    k = 0
    for i in range(start, end):
        lst[i] = aux[k]
        k = k + 1

########## QuickSort ##########

def MedianaDinTrei(lst, s, d):
    mij = (s + d) // 2
    if lst[s] > lst[mij]:
        aux = lst[s]
        lst[s] = lst[mij]
        lst[mij] = aux

    if lst[s] > lst[d]:
        aux = lst[s]
        lst[s] = lst[d]
        lst[d] = aux

    if lst[mij] > lst[d]:
        aux = lst[mij]
        lst[mij] = lst[d]
        lst[d] = aux

def MedianaDinCinci(lst, s, d):
    mij = (s + d) // 2
    mij1 = (mij + s) // 2
    mij2 = (mij + d) // 2
    l = [lst[s], lst[mij1], lst[mij], lst[mij2], lst[d]]
    l.sort()
    lst[s] = l[0]
    lst[mij1] = l[1]
    lst[mij] = l[2]
    lst[mij2] = l[3]
    lst[d] = l[4]

def Pivot(lst, s, d):
    MedianaDinTrei(lst, s, d)
    i = s - 1
    p = (s + d) // 2
    aux = lst[p]
    lst[p] = lst[d]
    lst[d] = aux
    for j in range(s,d):
        if lst[j] < lst[d]:
            i = i + 1
            aux = lst[i]
            lst[i] = lst[j]
            lst[j] = aux
    aux = lst[i+1]
    lst[i+1] = lst[d]
    lst[d] = aux
    return i+1

def QuickSortM3(lst, s, d):
    if s < d:
        p = Pivot(lst, s, d)
        QuickSortM3(lst, s, p - 1)
        QuickSortM3(lst, p + 1, d)

def Pivot2(lst, s, d):
    MedianaDinCinci(lst, s, d)
    i = s - 1
    p = (s + d) // 2
    aux = lst[p]
    lst[p] = lst[d]
    lst[d] = aux
    for j in range(s,d):
        if lst[j] < lst[d]:
            i = i + 1
            aux = lst[i]
            lst[i] = lst[j]
            lst[j] = aux
    aux = lst[i+1]
    lst[i+1] = lst[d]
    lst[d] = aux
    return i+1

def QuickSortM5(lst, s, d):
    if s < d:
        p = Pivot2(lst, s, d)
        QuickSortM5(lst, s, p - 1)
        QuickSortM5(lst, p + 1, d)

def RadixSort(lst):
    Maxim = max(lst)

    nr = 1
    while Maxim > 0:
        l = [[] for i in range(10)]
        for i in lst:
            l[(i // nr)  % 10] += [i]
        lst = []
        for i in l:
            for j in i:
                if j != []:
                    lst += [j]
        Maxim = Maxim // 10
        nr = nr * 10

    return lst

def RadixSort4(list):
    x = 1
    for i in range(16):
        l = [ [] for k in range(4) ]
        for k in list:
            l[ (k//x)  % 4] += [k]
        list = []
        for k in l:
            for j in k:
                if j != []:
                    list += [j]
        x = x * 4
    return list


# Citire

f = open("input.in", 'r')
n = int(f.readline())
for x in f:
    l = x.split()
    lst = [random.randrange(0, int(l[1]), 1) for i in range(int(l[0])) ]
    nr = len(lst)
    print("N = ", int(l[0]), ", Max = ", int(l[1]))

    start = time.time()
    BubbleSort()
    end = time.time()
    print("Bubble Sort: ", end-start, end = " ")
    test_Sort(lst)

    start = time.time()
    CountSort()
    end = time.time()
    print("Count Sort: ", end-start, end = " ")
    test_Sort(lst)

    start = time.time()
    MergeSort(lst, 0, len(lst)-1)
    end = time.time()
    print("Merge Sort: ", end - start, end=" ")
    test_Sort(lst)

    start = time.time()
    QuickSortM3(lst, 0, len(lst) - 1)
    end = time.time()
    print("Quick Sort M3: ", end - start, end=" ")
    test_Sort(lst)

    start = time.time()
    QuickSortM5(lst, 0, len(lst) - 1)
    end = time.time()
    print("Quick Sort M5: ", end - start, end=" ")
    test_Sort(lst)
    print()

    start = time.time()
    l = RadixSort(lst)
    end = time.time()
    print("Radix Sort: ", end - start, end=" ")
    test_Sort(l)

    start = time.time()
    l = RadixSort4(lst)
    end = time.time()
    print("Radix Sort4: ", end - start, end=" ")
    test_Sort(l)
