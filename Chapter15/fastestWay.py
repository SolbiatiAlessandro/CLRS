f1, f2 = [], []

def fastestWay( a, t, e, x, n ):
    """
    ref CLRS pg326, solution to the basic supply chain problem using the book notation for variables name
    """
    f1.append( e[0] )
    f2.append( e[1] )
    for i in xrange(n):
        f11 = f1[i]+a[0][i]
        f12 = f2[i]+a[1][i]+t[1][i+1]
        f22 = f2[i]+a[1][i]
        f21 = f1[i]+a[0][i]+t[0][i+1]

        f1.append( min( f11, f12 ) )
        f2.append( min( f21, f22 ) )

    return min( f1[n]+x[0], f2[n]+x[1] )
        

"""
values from example in CLRS page 326 
"""
e = [2,4]
a = [[7,9,3,4,8,4],[8,5,6,4,5,7]]
t = [[0,0,2,3,1,3,4],[0,0,2,1,2,2,1]]
x = [3,2]

print( fastestWay(a,t,e,x,6) )

