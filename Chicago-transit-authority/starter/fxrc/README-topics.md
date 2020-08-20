<!-- # producer
* direct:
    * station: TOPIC_NAME = "chicago-transit.station.arrivals"
    * turnstile: TOPIC_NAME = "chicago-transit.station.tunstiles"

* REST:
    * weather: TOPIC_NAME = "chicago-transit.weather"
* connector:
    * stations from postgres: "topic.prefix": "chicago-transit.connect-", CONNECTOR_NAME: "stations"

# consumer
* faust_stream:
    * topic (input, read from Connect stations topic): "chicago-transit.connect-stations"
    * out_topic: "chicago-transit.stations.table"
    * to filter line with valid color

* ksql
    * table: turnstile (topic: "chicago-transit.station.tunstiles")
    * table: turnstile_summary (this is query from turnstile table) -->

# Notice
* actually, server.py had already defined all the topics. So I have to follow its naming.

# Max retries exceeded with url
* solution:
    * ulimit -n 4096 (this command is only affect current tab/terminal, rather global)
    * as in course forum: https://knowledge.udacity.com/questions/149305
* Symptom
```
# fxrc @ pop in ~/Learn/UdacityNanodegree/mirror-Mehak97-udacity-kafka-streams/Chicago-transit-authority/starter/producers on git:master x [20:33:54] C:1
$ python simulation.py
2020-08-19 20:34:41,724 models.producer INFO     Creating topic org.chicago.cta.station.arrivals.v1
2020-08-19 20:34:43,726 models.producer CRITICAL failed to create topic org.chicago.cta.station.arrivals.v1: KafkaError{code=TOPIC_ALREADY_EXISTS,val=36,str="Topic 'org.chicago.cta.station.arrivals.v1' already exists."}
2020-08-19 20:34:43,727 models.producer INFO     Creating topic org.chicago.cta.station.turnstile.v1
2020-08-19 20:34:45,730 models.producer CRITICAL failed to create topic org.chicago.cta.station.turnstile.v1: KafkaError{code=TOPIC_ALREADY_EXISTS,val=36,str="Topic 'org.chicago.cta.station.turnstile.v1' already exists."}
2020-08-19 20:34:46,338 models.station CRITICAL HTTPConnectionPool(host='localhost', port=8081): Max retries exceeded with url: /subjects/org.chicago.cta.station.arrivals.v1-value/versions (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f86584c30a0>: Failed to establish a new connection: [Errno 16] Device or resource busy'))
Traceback (most recent call last):
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/urllib3/connection.py", line 159, in _new_conn
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/urllib3/util/connection.py", line 61, in create_connection
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/socket.py", line 918, in getaddrinfo
OSError: [Errno 16] Device or resource busy

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/urllib3/connectionpool.py", line 670, in urlopen
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/urllib3/connectionpool.py", line 392, in _make_request
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/http/client.py", line 1240, in request
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/http/client.py", line 1286, in _send_request
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/http/client.py", line 1235, in endheaders
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/http/client.py", line 1006, in _send_output
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/http/client.py", line 946, in send
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/urllib3/connection.py", line 187, in connect
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/urllib3/connection.py", line 171, in _new_conn
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x7f86584c30a0>: Failed to establish a new connection: [Errno 16] Device or resource busy

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/requests/adapters.py", line 439, in send
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/urllib3/connectionpool.py", line 724, in urlopen
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/urllib3/util/retry.py", line 439, in increment
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=8081): Max retries exceeded with url: /subjects/org.chicago.cta.station.arrivals.v1-value/versions (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f86584c30a0>: Failed to establish a new connection: [Errno 16] Device or resource busy'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "simulation.py", line 83, in <module>
  File "simulation.py", line 54, in __init__
  File "/home/fxrc/Learn/UdacityNanodegree/mirror-Mehak97-udacity-kafka-streams/Chicago-transit-authority/starter/producers/models/line.py", line 24, in __init__
  File "/home/fxrc/Learn/UdacityNanodegree/mirror-Mehak97-udacity-kafka-streams/Chicago-transit-authority/starter/producers/models/line.py", line 61, in _build_trains
  File "/home/fxrc/Learn/UdacityNanodegree/mirror-Mehak97-udacity-kafka-streams/Chicago-transit-authority/starter/producers/models/station.py", line 83, in arrive_b
  File "/home/fxrc/Learn/UdacityNanodegree/mirror-Mehak97-udacity-kafka-streams/Chicago-transit-authority/starter/producers/models/station.py", line 60, in run
  File "/home/fxrc/Learn/UdacityNanodegree/mirror-Mehak97-udacity-kafka-streams/Chicago-transit-authority/starter/producers/models/station.py", line 45, in run
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/confluent_kafka/avro/__init__.py", line 80, in produce
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/confluent_kafka/avro/serializer/message_serializer.py", line 107, in encode_record_with_schema
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/confluent_kafka/avro/cached_schema_registry_client.py", line 218, in register
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/confluent_kafka/avro/cached_schema_registry_client.py", line 167, in _send_request
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/requests/sessions.py", line 530, in request
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/requests/sessions.py", line 643, in send
  File "/home/fxrc/miniconda3/envs/mypy3/lib/python3.8/site-packages/requests/adapters.py", line 516, in send
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=8081): Max retries exceeded with url: /subjects/org.chicago.cta.station.arrivals.v1-value/versions (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f86584c30a0>: Failed to establish a new connection: [Errno 16] Device or resource busy'))
(mypy3)

```