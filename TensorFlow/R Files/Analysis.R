
# Load the data
`train1` <- read.csv('~/Documents/TU Clausthal/Neuronale Netze und statistisches Lernen/ConvNet/Resources/OtherResults/train12017-02-02-18:18:33.csv')

# Get an overview of the data
head(train1)
number_of_images = nrow(train1)
# Dataset contains of 25000 values
# 12500 are dogs and 12500 are cats

size = train1['size']
total_size = sum(size)
total_size_in_mb = total_size/1024**2
# The total filesize of all images is: 545.421 MB

avg_size = total_size / number_of_images
avg_size_in_kb = avg_size/1024
# The average filesize is 22.34 KB

# Plot histogram of the filesize
h = hist(train1['size'][[1]]/1024)
h$density = h$count/sum(h$counts)*100
plot(h,
     freq = FALSE,
     main = 'Filesize of the original training images', 
     xlab = 'Filesize in kB', 
     ylab = 'Percent')

# Create histogram of the height
h = hist(train1['height'][[1]])
h$density = h$count/sum(h$counts)*100

# Create histogram of the width
w = hist(train1['width'][[1]])
w$density = w$count/sum(w$counts)*100

par(mfrow=c(1,2))

# Plot histogram of the height
plot(h,
     freq = FALSE,
     main = 'Heigth', 
     xlab = 'Heigth in pixels', 
     ylab = 'Percent')

# Plot histogram of the width
plot(w,
     freq = FALSE,
     main = 'Width', 
     xlab = 'Width in pixels', 
     ylab = 'Percent')

475/375
4/3
# Seems to be that most images are 4:3.

# Boxplot of width
boxplot(train1[['width']],
        horizontal = TRUE)

# Boxplot of height
boxplot(train1[['height']])

names(train1)
