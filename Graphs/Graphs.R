################################################################################
# Instructions to export the files
################################################################################
# Export files in landscape format and as A5 format

################################################################################
# Total loss graph of standard for 100k
################################################################################

# Read in file
standard100kTotalLossRaw <- read.csv("~/Documents/TU Clausthal/Neuronale Netze und statistisches Lernen/ConvNet/Graphs/run_Standard100K.csv")

# Specify options for plot
x1 = standard100kTotalLossRaw$Step
y1 = standard100kTotalLossRaw$Value
xlab = "Training steps"
ylab = "Loss"
labels = c("0k","20k","40k","60k","80k","100k")

# Plot the function
plot(x1, y1, type='l', xlab = xlab, ylab = ylab, col='gray70', xaxt="n")
axis(1, at=seq(0,100000,20000), labels = labels)

# Add smoothed line
smoothingSpline = smooth.spline(x1, y1, spar=0.35)
lines(smoothingSpline,lwd=2)

################################################################################
# Total loss graph with added conv layer
################################################################################

# Read in file
addedConvLayerTotalLossRaw <- read.csv("~/Documents/TU Clausthal/Neuronale Netze und statistisches Lernen/ConvNet/Graphs/run_AddedConvLayer.csv")

# Specify options for plot
x2 = addedConvLayerTotalLossRaw$Step
y2 = addedConvLayerTotalLossRaw$Value
xlab = "Training steps"
ylab = "Loss"
labels = c("0k","2k","4k","6k","8k","10k","12k","14k")
# xlim = c(0,100000)

# Plot the function
plot(x2, y2, type='l', xlab = xlab, ylab = ylab, col='gray70', xaxt="n")
axis(1, at=seq(0,14000,2000), labels = labels)

# Add smoothed line
smoothingSpline = smooth.spline(x2, y2, spar=0.35)
lines(smoothingSpline,lwd=2)

################################################################################
# Total loss graph standard
################################################################################

# Read in file
standardTotalLossRaw <- read.csv("~/Documents/TU Clausthal/Neuronale Netze und statistisches Lernen/ConvNet/Graphs/run_Standard.csv")

# Specify options for plot
x3 = standardTotalLossRaw$Step
y3 = standardTotalLossRaw$Value
xlab = "Training steps"
ylab = "Loss"
labels = c("0k","10k","20k","30k","40k")
# xlim = c(0,100000)

# Plot the function
plot(x3, y3, type='l', xlab = xlab, ylab = ylab, col='gray70', xaxt="n")
axis(1, at=seq(0,40000,10000), labels = labels)

# Add smoothed line
smoothingSpline = smooth.spline(x3, y3, spar=0.35)
lines(smoothingSpline,lwd=2)

################################################################################
# Total loss graph with 28x28 images
################################################################################

# Read in file
s28x28TotalLossRaw <- read.csv("~/Documents/TU Clausthal/Neuronale Netze und statistisches Lernen/ConvNet/Graphs/run_28x28Images.csv")

# Specify options for plot
x4 = s28x28TotalLossRaw$Step
y4 = s28x28TotalLossRaw$Value
xlab = "Training steps"
ylab = "Loss"
labels = c("0k","10k","20k","30k")
# xlim = c(0,100000)

# Plot the function
plot(x4, y4, type='l', xlab = xlab, ylab = ylab, col='gray70', xaxt="n")
axis(1, at=seq(0,30000,10000), labels = labels)

# Add smoothed line
smoothingSpline = smooth.spline(x4, y4, spar=0.35)
lines(smoothingSpline,lwd=2)

################################################################################
# All together
################################################################################

# Plot the function
plot(x1, y1, type='l', xlab = xlab, ylab = ylab, col='white', xaxt="n", ylim = c(0,1))
labels = c("0k","20k","40k","60k","80k","100k")
axis(1, at=seq(0,100000,20000), labels = labels)

# Add smoothed line of Standard100k
smoothingSpline = smooth.spline(x1, y1, spar=0.35)
lines(smoothingSpline,lwd=2, col='gray70')

# Add smoothed line of AddedConvLayer
smoothingSpline = smooth.spline(x2, y2, spar=0.35)
lines(smoothingSpline,lwd=2, col='deepskyblue')

# Add smoothed line of Standard
smoothingSpline = smooth.spline(x3, y3, spar=0.35)
lines(smoothingSpline,lwd=2, col='firebrick')

# Add smoothed line of 28x28 images
smoothingSpline = smooth.spline(x4, y4, spar=0.35)
lines(smoothingSpline,lwd=2, col='goldenrod1')

# Add a legend to the plot
legend("topright", 
       inset = .05, 
       legend= c("Standard 100k","Additional ConvLayer","Standard 40k","Increased size"),
       lty=c(1,1,1,1),
       lwd=c(2,2,2,2),
       col = c('gray70','deepskyblue','firebrick','goldenrod1'))

