import findspark
findspark.init()

from pyspark import SparkConf, SparkContext

def map_phase(index_number, target):
    index, number = index_number
    return [(min(number, target - number), (index, number))]

def reduce_phase(key, values, target):
    # make sure that we have both the number and its complement
    if len(values) < 2:
        return []
    else:
        # [(0, 2), (1, 7)]
        # so indices are values[0][0] and values[1][0]
        # and values are values[0][1] and values[1][1]
        return [{"indices": (values[0][0], values[1][0]), "values": (values[0][1], values[1][1])}]

def two_sum(nums_rdd, target):
    # Mapping phase
    tuples_rdd = nums_rdd.flatMap(lambda x: map_phase(x, target))

    # Reducing phase
    pairs = tuples_rdd.groupByKey().flatMap(lambda kv: reduce_phase(kv[0], list(kv[1]), target)).collect()



    return pairs

if __name__ == "__main__":
    # set relative tmp path for large datasets
    sparkconf = SparkConf().setAppName("TwoSum").set("spark.local.dir", "tmp")
    sc = SparkContext(conf=sparkconf)

    target = 9  # Example target value
    nums = [2, 7, 12, -4, 16, 164, 3, 6]  # Example dataset
    nums_rdd = sc.parallelize(nums).zipWithIndex().map(lambda x: (x[1], x[0]))  # Get (index, number)

    result = two_sum(nums_rdd, target)
    print(result)  # List of pairs (with their indices) that add up to target

    for res in result:
        print(res["values"][0], "+", res["values"][1], "=", target, "at indices", res["indices"])

    sc.stop()
