print("========================")
print("    Selection Sorting   ")
print("------------------------")

def SelectionSort(val):
    for i in range(len(val)-1,0,-1):
        Max=0
        for l in range(1,i+1):
            if val[l]>val[Max]:
                Max = l
        temp = val[i]
        val[i] = val[Max]
        val[Max] = temp
Angka = [22,10,15,3,8,2]
SelectionSort(Angka)
print(Angka)

print("========================")
print("     Bubble sorting     ")
print("------------------------")

def BubbleSort(X):
    for i in range(len(X)-1,0,-1):
        Max=0
        for l in range(1,i+1):
            if X[l]>X[Max]:
                Max = l
        temp = X[i]
        X[i] = X[Max]
        X[Max] = temp
Hasil = [22,10,15,3,8,2]
BubbleSort(Hasil)
print(Hasil)

print("========================")
print("   Insertion sorting    ")
print("------------------------")

def InsertionSort(val):
    for index in range(1,len(val)):
        a = val[index]
        b = index
        while b>0 and val[b-1]>a:
            val[b]=val[b-1]
            b = b-1
        val[b]=a
Angka = [22,10,15,3,8,2]
InsertionSort(Angka)
print(Angka)

print("========================")
