nonlin = function(x){
  out = 1/(1+exp(-x))
  return(out)
}

deriv = function(x){
  return(x*(1-x))
}

calcderiv = function(x){
  
  a = exp(-x)
  b = (a + 1)**2
  # The addition is done to see the two different functions within
  # the graph. It does not belong to the claculation.
  out = (a/b)+0.001
  
  return(out)
}

a = seq(-5,5,0.01)
nl = nonlin(a)

par(mfrow = c(2,1))

plot(a,nonlin(a), type = 'l', 
     main = 'Distribution',
     xlab = '',
     ylab = '')

# The following two plots seem to be equal
plot(a,deriv(nonlin(a)),col=2, type = 'l', 
     main = 'Derivative ',
     xlab = '',
     ylab = '')
points(a, calcderiv(a), col=3, type = 'l')

# The following code fills the area under the curve.
# This code is optional and should not be used if 
# the similarity of the two curves above should be shown.
b = 5
cord.x <- c(-b,seq(-b,b,0.01),b) 
cord.y <- c(0,deriv(nonlin(a)),0) 
curve(deriv(nonlin(x)),xlim=c(-b,b))
polygon(cord.x,cord.y,col='lightgrey')
