'''
https://spark.apache.org/docs/1.1.1/api/python/pyspark.rdd.RDD-class.html
'''

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)

lines = sc.textFile("README.md")
lines = sc.parallelize(["pandas", "i like pandas"])

lines.count()
lines.first()

inputRDD = sc.textFile("txt/foobar.txt")
errorsRDD = inputRDD.filter(lambda x: "error" in x)

book = sc.textFile("books/breakfast_at_tiffanys.txt")

book.take(5)

# ["Breakfast at Tiffany's ",
# 'Truman Capote, 1958 ',
# '',
# 'I am always drawn back to places where I have lived, the houses and their neighborhoods. For ',
# 'instance',
# 'there is a brownstone in the East Seventies where, during the early years of the war, I had ',
# 'my first New York apartment. It was one room crowded with attic furniture, a sofa and fat chairs ',
# 'upholstered in that itchy, particular red velvet that one associates with hot days on a tram. The walls ',
# 'were stucco, and a color rather like tobacco-spit. Everywhere, in the bathroom too, there were prints ',
# 'of Roman ruins freckled brown with age. The single window looked out on a fire escape. Even so, ',
# 'my spirits heightened whenever I felt in my pocket the key to this apartment; with all its gloom, it ',
# 'still was a place of my own, the first, and my books were there, and jars of pencils to sharpen, ',
# 'everything I needed, so I felt, to become the writer I wanted to be. ',
# '',
# 'It never occurred to me in those days to write about Holly Golightly, and probably it would ',
# 'not now except for a conversation I had with Joe Bell that set the whole memory of her in motion ',
# 'again. ', '', "Holly Golightly had been a tenant in the old brownstone; she'd occupied the apartment below ",
# 'mine. As for Joe Bell, he ran a bar around the corner on Lexington Avenue; he still does. Both ',
# 'Holly and I used to go there six, seven times a day, not for a drink, not always, but to make ',
# 'telephone calls: during the war a private telephone was hard to come by. Moreover, Joe Bell was ',
# "good about taking messages, which in Holly's case was no small favor, for she had a tremendous ", 'many. ',
# '',
# "Of course this was a long time ago, and until last week I hadn't seen Joe Bell in several years. "
#            ]

book.count()
book.take(book.count())

a = range(100)
data = sc.parallelize(a)

filter1 = book.filter(lambda x: "her" in x)
filter2 = filter1.filter(lambda x: "Spanish Harlem streets" in x)
filter2.take(filter2.count())

# ['It took weeks of after-work roaming through those Spanish Harlem streets, and there were many ']

errorsRDD = book.filter(lambda x: "damn" in x)
warningsRDD = book.filter(lambda x: "drunk" in x)
badLinesRDD = errorsRDD.union(warningsRDD)

word = book.filter(lambda s: "error" in s)


def containsError(s):
    return "error" in s


word = book.filter(containsError)

nums = sc.parallelize([1, 2, 3, 4])
squared = nums.map(lambda x: x * x).collect() 

'''
Collect (Action) - Return all the elements of the dataset as an array at the driver program. This is usually useful after a filter or other operation that returns a sufficiently small subset of the data.
'''

for num in squared:
    print(num)

lines = sc.parallelize(["hello world", "hi"])
words = lines.flatMap(lambda line: line.split(" "))
words.first() # returns "hello"

# let's make it a list now

a = lines.take(lines.count())
print(type(a))

for i in a:
    print(i)

rdd = sc.parallelize(list(range(25)))
sdd = rdd.reduce(lambda x, y: x + y)
tdd = sdd.take(sdd.count())

# Example 4-4. Simple filter on second element in Python
result = lines.filter(lambda keyValue: len(keyValue[1]) < 20)

# Example 4-7. Per-key average with reduceByKey() and mapValues() in Python
rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

# Example 4-9. Word count in Python
rdd = sc.textFile("s3://...")
words = rdd.flatMap(lambda x: x.split(" "))
result = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

data = [("a", 3), ("b", 4), ("a", 1)]
sc.parallelize(data).reduceByKey(lambda x, y: x + y) # Default parallelism
sc.parallelize(data).reduceByKey(lambda x, y: x + y, 10) # Custom parallelism

