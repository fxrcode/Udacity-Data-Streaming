# Step 3
## 1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
* by changing sparksession configurations, such as tuning level of parallelism or tuning maximum rate at which data read from each Kafka partition, can affect thoughput and latency.

## 2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
* by search on tuning tips, I found dataframe performance can improve by `spark.sql.shuffle.partitions`, and data read throughput can be tuned by `spark.streaming.kafka.maxRatePerPartition`.
* by monitoring htop, and progress report's `processedRowsPerSecond`. I found the optimial sets are, and `processedRowsPerSecond` can above 100.
    * `spark.sql.shuffle.partitions = 20`
    * `spark.streaming.kafka.maxRatePerPartition = 50`