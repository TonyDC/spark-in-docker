def handler(spark, file):
    file = spark.textFile(f'file:///opt/data/{file}')
    word_count = file.flatMap(lambda line: line.split(' ')) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)
    
    print(word_count)
