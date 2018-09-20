def matrixChainOrder( p ):
    lenp, n = len(p), len(p) - 1
    m = lenp*[lenp*[1e9]]
    s = lenp*[lenp*[-1]]
    for i in xrange(1,n+1):
        m[i][i]=0
    for l in xrange(2,n+1):
        for i in xrange(1,n-l+2):
            j = i+l-1
            for k in xrange(i,j):
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m,s

p = [ 30, 35, 15, 5, 10, 20, 25 ]
m,s = matrixChainOrder(p)

        
