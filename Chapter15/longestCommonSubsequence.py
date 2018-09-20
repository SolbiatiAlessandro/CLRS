A, B = "ABCBDAB","BDCABA"
lcs = [ len(B)*[-1] for _ in range(len(A)) ]

def getLCS( a, b ):
    if lcs[a][b] == -1:
        lcs[a][b] = LCS( a, b )
    return lcs[a][b]

def LCS( a, b ):
    if a < 0 or  b < 0:
        return 0
    if A[a] == B[b]:
        return 1 + getLCS( a-1, b-1 )
    return max( getLCS( a-1, b ), getLCS( a, b-1 ) )

print LCS(len(A)-1,len(B)-1)
