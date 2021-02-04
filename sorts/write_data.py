from timeit import default_timer as timer
from bubble_sort import bubble_sort
from insertin_sort import insertion_sort
from merge_sort import mergeSort
from quick_sort import quick_sort
from get_data import get_column_data
import pandas as pd

id_obj,name_obj,gender_obj,date_obj=get_column_data()

def write__(sorted_data):
    df = pd.DataFrame({'Id':sorted_data,'First Name':name_obj,'Gender':gender_obj,'Date':date_obj})
    df.to_excel('file_example_XLS_1000.xls')
    return True

def _timer_(algo,algo_name):
    start= timer()
    sorted_data = algo(id_obj)
    write__(sorted_data)
    end = timer()
    return print("Time taken to run "+algo_name+":", end-start)

_timer_(algo=bubble_sort,algo_name='Bubble Sort')  #O(n2)
_timer_(algo=insertion_sort,algo_name='Insertion Sort')  #O(n2)
_timer_(algo=mergeSort,algo_name='Merge Sort')  #O(n log2n)
_timer_(algo=quick_sort,algo_name='Quick Sort')  #O(n log2n) 

