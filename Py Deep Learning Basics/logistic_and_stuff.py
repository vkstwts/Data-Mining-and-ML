import theano.tensor as T
from theano import function
from theano import pp
import numpy

'''
Basic Logistic function demo.
'''
x = T.dmatrix("x")
s = 1/(1+T.exp(-x))
logistic = function([x],s)
print logistic([[0,1],[-1,-2]])
#print pp(s)

'''
Similar to logit function is the tanh
'''
s2 = (1+T.tanh(x/2))/2
tan = function([x], s2)
print tan([[0,1],[-1,-2]])

'''
Executing multiple functions
'''
a,b = T.dmatrices('a','b')
diff = a-b
abs_diff = abs(a-b)
diff_sq = diff**2
mult = function([a,b],[diff,abs_diff,diff_sq])
print mult([[0,1],[1,2]],[[-1,2],[5,7]])
#print pp(diff)
#print pp(abs_diff)
