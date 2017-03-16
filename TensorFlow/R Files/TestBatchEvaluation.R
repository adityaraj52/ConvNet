library(readr)

test_batch <- read_csv("~/Documents/Projects/ConvNet/Resources/EvaluateImageResults/test_batch.txt", 
                       col_names = FALSE)
unmatching_files <- test_batch[which(test_batch$X2 != test_batch$X3),]

View(unmatching_files)