import csv
import operator as op

def In() : 
    reader = csv.reader(open("Phytest.csv"), delimiter = ",")
    my_list = list(reader)
    return my_list

def Remove():
    ilist = In()
    del ilist[0]
    return ilist

def slist():
    dlist = Remove()
    iget0 = op.itemgetter(0)
    
    slist = list(map(iget0, dlist))
    return slist

def flist():
    flist = Remove()
    iget1 = op.itemgetter(1)

    flist = list(map(iget1, flist))
    return flist
    
def convert():
    nlist = flist()
    
    clist = list(map(float, nlist))

    return clist

def merge():
    l1 = slist()
    l2 = convert()

    lmerge = list(list(l) for l in zip(l1, l2))
    
    return lmerge

def sort():
    la = merge()

    sorlist = sorted(la, key = op.itemgetter(1), reverse=True)

    return sorlist


print(sort())