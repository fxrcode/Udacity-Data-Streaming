$ curl -X POST -H 'Content-Type: application/json' -d '{
    "name": "stations",
    "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "key.converter": "org.apache.kafka.connect.json.JsonConverter",
        "key.converter.schemas.enable": "false",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter.schemas.enable": "false",
        "batch.max.rows": "500",
        "connection.url": "jdbc:postgresql://postgres:5432/cta",
        "connection.user": "cta_admin",
        "connection.password": "chicago",
        "table.whitelist": "stations",
        "mode": "incrementing",
        "incrementing.column.name": "stop_id",
        "topic.prefix": "chicago-transit.",
        "poll.interval.ms": "3600000"
    }
  }' \
  http://localhost:8083/connectors

{"name":"stations","config":{"connector.class":"io.confluent.connect.jdbc.JdbcSourceConnector","key.converter":"org.apache.kafka.connect.json.JsonConverter","key.converter.schemas.enable":"false","value.converter":"org.apache.kafka.connect.json.JsonConverter","value.converter.schemas.enable":"false","batch.max.rows":"500","connection.url":"jdbc:postgresql://postgres:5432/cta","connection.user":"cta_admin","connection.password":"chicago","table.whitelist":"stations","mode":"incrementing","incrementing.column.name":"stop_id","topic.prefix":"chicago-transit.","poll.interval.ms":"3600000","name":"stations"},"tasks":[{"connector":"stations","task":0}],"type":"source"}%


# fxrc @ pop in ~/Learn/UdacityNanodegree/mirror-Mehak97-udacity-kafka-streams/Chicago-transit-authority/starter/producers on git:master x [1:28:49] C:1
$ curl -X POST -H 'Content-Type: application/json' -d '{
    "name": "stations",
    "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "key.converter": "org.apache.kafka.connect.json.JsonConverter",
        "key.converter.schemas.enable": "false",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter.schemas.enable": "false",
        "batch.max.rows": "500",
        "connection.url": "jdbc:postgresql://postgres:5432/cta",
        "connection.user": "cta_admin",
        "connection.password": "chicago",
        "table.whitelist": "stations",
        "mode": "incrementing",
        "incrementing.column.name": "stop_id",
        "topic.prefix": "chicago-transit.",
        "poll.interval.ms": "3600000",
    }
  }' \
  http://localhost:8083/connectors

{"error_code":500,"message":"Unexpected character ('}' (code 125)): was expecting double-quote to start field name\n at [Source: (org.glassfish.jersey.message.internal.ReaderInterceptorExecutor$UnCloseableInputStream); line: 17, column: 29] (through reference chain: org.apache.kafka.connect.runtime.rest.entities.CreateConnectorRequest[\"config\"])"}%


$ curl -X POST -H 'Content-Type: application/json' -d '{
    "name": "stations",
    "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "key.converter": "org.apache.kafka.connect.json.JsonConverter",
        "key.converter.schemas.enable": "false",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter.schemas.enable": "false",
        "batch.max.rows": "500",
        "connection.url": "jdbc:postgresql://localhost:5432/cta",
        "connection.user": "cta_admin",
        "connection.password": "chicago",
        "table.whitelist": "stations",
        "mode": "incrementing",
        "incrementing.column.name": "stop_id",
        "topic.prefix": "chicago-transit.",
        "poll.interval.ms": "3600000"
    }
  }' \
  http://localhost:8083/connectors

{"error_code":400,"message":"Connector configuration is invalid and contains the following 2 error(s):\nInvalid value org.postgresql.util.PSQLException: Connection to localhost:5432 refused. Check that the hostname and port are correct and that the postmaster is accepting TCP/IP connections. for configuration Couldn't open connection to jdbc:postgresql://localhost:5432/cta\nInvalid value org.postgresql.util.PSQLException: Connection to localhost:5432 refused. Check that the hostname and port are correct and that the postmaster is accepting TCP/IP connections. for configuration Couldn't open connection to jdbc:postgresql://localhost:5432/cta\nYou can also find the above list of errors at the endpoint `/{connectorType}/config/validate`"}%