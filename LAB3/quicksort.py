def compare_integers(a, b):
    return a<=b

def compare_strings(a,b):
    return a.lower() <= b.lower()

def partition(lst, p, r, compare_fun):
    pivot = lst[r]
    i=p-1
    j=p
    while j < r:

#everything on the left of i is smaller than the pivot
        if compare_fun(lst[j], pivot):
            i += 1
            k = lst[i]
            lst[i] = lst[j]
            lst[j] = k
            j += 1
        else:
            j+=1
    #swapping the pivot with list[i+1]
    t = lst[r]
    lst[r] = lst[i+1]
    lst[i+1] = t

    return i+1

def quicksort(the_list, p, r, compare_fun):
    if p<r:
        q= partition(the_list, p, r, compare_fun)
        quicksort(the_list, p, q-1, compare_fun)
        quicksort(the_list, q+1, r, compare_fun)
    return the_list

def sort(the_list, compare_fun):
    return quicksort(the_list, 0, len(the_list)-1, compare_fun= compare_fun)


