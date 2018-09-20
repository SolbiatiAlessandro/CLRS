f1, f2 = [], []

def fastestWay( a, t, e, x, n ):
    """
    ref CLRS pg326, solution to the basic supply chain problem using the book notation for variables name
    """
    import pdb;pdb.set_trace() 
    f1.append( ( e[0] , 1 ) )
    f2.append( ( e[1] , 2 ) )
    for i in xrange(n):
        f11 = f1[i][0]+a[0][i]
        f12 = f2[i][0]+a[1][i]+t[1][i+1]
        f22 = f2[i][0]+a[1][i]
        f21 = f1[i][0]+a[0][i]+t[0][i+1]

        f1.append( ( min( f11, f12 ), 1 ) if f11 < f12 else ( min( f11, f12 ), 2 ) )
        f2.append( ( min( f21, f22 ), 2 ) if f22 < f21 else ( min( f22, f21 ), 1 ) )

    f1x, f2x = f1[n][0]+x[0], f2[n][0]+x[1] 
    return ( min( f1x, f2x ) , f1 ) if f1x < f2x else ( min( f1x, f2x ), f2 ) 
        

"""
values from example in CLRS page 326 
"""
e = [2,4]
a = [[7,9,3,4,8,4],[8,5,6,4,5,7]]
t = [[0,0,2,3,1,3,4],[0,0,2,1,2,2,1]]
x = [3,2]

res = fastestWay(a,t,e,x,6) 
print "min cost = {}".format( res[0] ) 
for station, line in enumerate( res[1] ):
    print "line {}, station {}".format( line, station )
    

