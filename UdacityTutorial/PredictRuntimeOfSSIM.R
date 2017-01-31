################################################################################
# Check the runtime to compare all images with ssim
################################################################################
# Author: Sören Schleibaum

# Train dataset
comparison = c(100, 500, 1000)
time = c(1.2072, 30, 118)

# Dataframe is used later to predict the values
test_duration_of_function = data.frame(comparison, time)

# Visualize the data
main = 'Approximation of runtime of ssim'
xlab = 'Number of comparisons'
ylab = 'Time in seconds'
plot(test_duration_of_function,
     main = main,
     xlab = xlab,
     ylab = ylab)

legend(600,20, 
       legend=c('linear', 'quadratic'),
       col=c('red', 'blue'), 
       lty=c(1,1),
       bty = 'n')

# Fit linear model and check accurancy
lin_model = lm(time ~ comparison, data = test_duration_of_function)
summary(lin_model)

# Fit quadratic model and check accurancy
poly_model = lm(time ~ poly(comparison, 2, raw=TRUE), data = test_duration_of_function)
summary(poly_model)

# Draw predicted lines into plot
abline(lin_model, col = "red")
lines(x, predict(poly_model, data.frame(comparison = seq(100,1100,10))), type = 'l', col = 'blue')

# Predict duration of training value
test_data_size = 10000
time_for_train = predict(poly_model, data.frame(comparison = c(test_data_size)))/(60*60)
time_for_train # Approx. 3.2 hours

train_data_size = 200000
time_for_train = predict(poly_model, data.frame(comparison = c(200000)))/(60*60)
time_for_train # Approx. 1284.319 hours
