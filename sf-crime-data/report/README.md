# SF Crime Statistics with Spark Streaming

## Project Directions

## Local development environment setup
* Download Spark from https://spark.apache.org/downloads.html. Choose "Prebuilt for Apache Hadoop 2.7 and later."
* Unpack into (`/home/fxrc/tools`)
* Download binary for Kafka from https://kafka.apache.org/downloads, and modify config: `zookeeper.properties` and `server.properties`
* Downloaad Scala from official.
```log
# fxrc @ pop in ~/Tools [0:13:01] 
$ sdk install scala               
==== BROADCAST =================================================================
* 2020-08-18: Jbang 0.38.0 released on SDKMAN! Checkout https://github.com/jbangdev/jbang/releases/tag/v0.38.0. Follow @jbangdev #jbang
* 2020-08-17: Jbang 0.37.0 released on SDKMAN! Checkout https://github.com/jbangdev/jbang/releases/tag/v0.37.0. Follow @jbangdev #jbang
* 2020-08-17: Kotlin 1.4.0 released on SDKMAN! #kotlin
================================================================================

Downloading: scala 2.13.3

In progress...

####################################################################################################################################################### 100.0%

Installing: scala 2.13.3
Done installing!


Setting scala 2.13.3 as default.
(base) 
# fxrc @ pop in ~/Tools [0:14:42] 
$ scala -version   
Scala code runner version 2.13.3 -- Copyright 2002-2020, LAMP/EPFL and Lightbend, Inc.
$ java -version
openjdk version "11.0.8" 2020-07-14
OpenJDK Runtime Environment AdoptOpenJDK (build 11.0.8+10)
OpenJDK 64-Bit Server VM AdoptOpenJDK (build 11.0.8+10, mixed mode)
```