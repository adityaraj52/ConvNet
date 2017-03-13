################################################################################
# Instructions to export the files
################################################################################
# Export files in landscape format and as A5 format

################################################################################
# Total loss graph of 100k
################################################################################

# Read in file
s100kTotalLossRaw <- read.csv("~/Documents/TU Clausthal/Neuronale Netze und statistisches Lernen/ConvNet/Graphs/run_Standard100K,tag_total_loss (raw).csv")

# Specify options for plot
x = s100kTotalLossRaw$Step
y = s100kTotalLossRaw$Value
xlab = "Training steps "
ylab = "Loss"
labels = c("0k","20k","40k","60k","80k","100k")

# Plot the function
plot(x, y, type='l', xlab = xlab, ylab = ylab, col='gray70', xaxt="n")
axis(1, at=seq(0,100000,20000), labels = labels)

# Add smoothed line
smoothingSpline = smooth.spline(x, y, spar=0.35)
lines(smoothingSpline,lwd=2)

################################################################################
# Total loss graph with added conv layer
################################################################################

# Read in file
ACLTotalLossRaw <- read.csv("~/Documents/TU Clausthal/Neuronale Netze und statistisches Lernen/ConvNet/Graphs/run_AddedConvLayer,tag_total_loss (raw).csv")

# Specify options for plot
x = ACLTotalLossRaw$Step
y = ACLTotalLossRaw$Value
xlab = "Training steps "
ylab = "Loss"
labels = c("0k","2k","4k","6k","8k","10k","12k","14k")
# xlim = c(0,100000)

# Plot the function
plot(x, y, type='l', xlab = xlab, ylab = ylab, col='gray70', xaxt="n")
axis(1, at=seq(0,14000,2000), labels = labels)

# Add smoothed line
smoothingSpline = smooth.spline(x, y, spar=0.35)
lines(smoothingSpline,lwd=2)
