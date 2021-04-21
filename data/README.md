Spark’s primary abstraction is a distributed collection of items called a Dataset. 
Datasets can be created from Hadoop InputFormats (such as HDFS files) or by transforming other Datasets. 
Due to Python’s dynamic nature, we don’t need the Dataset to be strongly-typed in Python. 
As a result, all Datasets in Python are Dataset[Row], and we call it DataFrame to be consistent with the data frame concept in Pandas and R. 
Let’s make a new DataFrame from the text of the README file in the Spark source directory: