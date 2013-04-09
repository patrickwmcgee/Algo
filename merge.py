def merge_sort(A,p,r):
    while p < r:
        q = ((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,q,p,r)


def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    # copy A[p..q] into L
    for i in xrange(n1):
        L.append(A[p + i - 1])
    # copy A[q + 1 ..r] into R
    for j in xrange(n2):
        R.append(A[q + j])

    i = 1
    j = 1
    for k in xrange(p,r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        elif A[k] == R[j]:
            j+=1

