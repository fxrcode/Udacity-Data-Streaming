Attaching to starter_connect_1
[36mconnect_1             |[0m ===> User
[36mconnect_1             |[0m uid=0(root) gid=0(root) groups=0(root)
[36mconnect_1             |[0m ===> Configuring ...
[36mconnect_1             |[0m ===> Running preflight checks ... 
[36mconnect_1             |[0m ===> Check if Kafka is healthy ...
[36mconnect_1             |[0m [main] INFO org.apache.kafka.clients.admin.AdminClientConfig - AdminClientConfig values: 
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = 
[36mconnect_1             |[0m 	connections.max.idle.ms = 300000
[36mconnect_1             |[0m 	default.api.timeout.ms = 60000
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	receive.buffer.bytes = 65536
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 30000
[36mconnect_1             |[0m 	retries = 2147483647
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m 
[36mconnect_1             |[0m [main] INFO org.apache.kafka.common.utils.AppInfoParser - Kafka version: 5.5.1-ccs
[36mconnect_1             |[0m [main] INFO org.apache.kafka.common.utils.AppInfoParser - Kafka commitId: cb1873c1fdf5f5f9
[36mconnect_1             |[0m [main] INFO org.apache.kafka.common.utils.AppInfoParser - Kafka startTimeMs: 1597885655887
[36mconnect_1             |[0m ===> Launching ... 
[36mconnect_1             |[0m ===> Launching kafka-connect ... 
[36mconnect_1             |[0m [2020-08-20 01:07:39,052] INFO WorkerInfo values: 
[36mconnect_1             |[0m 	jvm.args = -Xms256M, -Xmx2G, -XX:+UseG1GC, -XX:MaxGCPauseMillis=20, -XX:InitiatingHeapOccupancyPercent=35, -XX:+ExplicitGCInvokesConcurrent, -XX:MaxInlineLevel=15, -Djava.awt.headless=true, -Dcom.sun.management.jmxremote=true, -Dcom.sun.management.jmxremote.authenticate=false, -Dcom.sun.management.jmxremote.ssl=false, -Dkafka.logs.dir=/var/log/kafka, -Dlog4j.configuration=file:/etc/kafka/connect-log4j.properties
[36mconnect_1             |[0m 	jvm.spec = Azul Systems, Inc., OpenJDK 64-Bit Server VM, 1.8.0_212, 25.212-b04
[36mconnect_1             |[0m 	jvm.classpath = /etc/kafka-connect/jars/*:/usr/share/java/kafka/kafka_2.12-5.5.1-ccs-test-sources.jar:/usr/share/java/kafka/jaxb-api-2.3.0.jar:/usr/share/java/kafka/commons-compress-1.19.jar:/usr/share/java/kafka/jakarta.ws.rs-api-2.1.5.jar:/usr/share/java/kafka/kafka_2.12-5.5.1-ccs-scaladoc.jar:/usr/share/java/kafka/javassist-3.26.0-GA.jar:/usr/share/java/kafka/snappy-java-1.1.7.3.jar:/usr/share/java/kafka/jetty-servlet-9.4.24.v20191120.jar:/usr/share/java/kafka/kafka_2.12-5.5.1-ccs-javadoc.jar:/usr/share/java/kafka/kafka-streams-examples-5.5.1-ccs.jar:/usr/share/java/kafka/scala-library-2.12.10.jar:/usr/share/java/kafka/jetty-http-9.4.24.v20191120.jar:/usr/share/java/kafka/netty-transport-native-epoll-4.1.48.Final.jar:/usr/share/java/kafka/commons-cli-1.4.jar:/usr/share/java/kafka/kafka_2.12-5.5.1-ccs-test.jar:/usr/share/java/kafka/kafka_2.12-5.5.1-ccs-sources.jar:/usr/share/java/kafka/kafka-streams-test-utils-5.5.1-ccs.jar:/usr/share/java/kafka/kafka-log4j-appender-5.5.1-ccs.jar:/usr/share/java/kafka/support-metrics-common-5.5.1-ccs.jar:/usr/share/java/kafka/netty-handler-4.1.48.Final.jar:/usr/share/java/kafka/rocksdbjni-5.18.3.jar:/usr/share/java/kafka/javassist-3.22.0-CR2.jar:/usr/share/java/kafka/kafka_2.12-5.5.1-ccs.jar:/usr/share/java/kafka/jackson-module-paranamer-2.10.2.jar:/usr/share/java/kafka/jakarta.activation-api-1.2.1.jar:/usr/share/java/kafka/kafka-tools-5.5.1-ccs.jar:/usr/share/java/kafka/jackson-module-jaxb-annotations-2.10.2.jar:/usr/share/java/kafka/connect-mirror-client-5.5.1-ccs.jar:/usr/share/java/kafka/jakarta.inject-2.5.0.jar:/usr/share/java/kafka/httpcore-4.4.13.jar:/usr/share/java/kafka/connect-basic-auth-extension-5.5.1-ccs.jar:/usr/share/java/kafka/jersey-server-2.28.jar:/usr/share/java/kafka/hk2-locator-2.5.0.jar:/usr/share/java/kafka/jetty-io-9.4.24.v20191120.jar:/usr/share/java/kafka/jackson-dataformat-csv-2.10.2.jar:/usr/share/java/kafka/kafka-clients-5.5.1-ccs.jar:/usr/share/java/kafka/httpmime-4.5.11.jar:/usr/share/java/kafka/connect-file-5.5.1-ccs.jar:/usr/share/java/kafka/commons-codec-1.11.jar:/usr/share/java/kafka/jackson-datatype-jdk8-2.10.2.jar:/usr/share/java/kafka/javax.ws.rs-api-2.1.1.jar:/usr/share/java/kafka/jetty-util-9.4.24.v20191120.jar:/usr/share/java/kafka/slf4j-log4j12-1.7.30.jar:/usr/share/java/kafka/jackson-jaxrs-base-2.10.2.jar:/usr/share/java/kafka/slf4j-api-1.7.30.jar:/usr/share/java/kafka/metrics-core-2.2.0.jar:/usr/share/java/kafka/jopt-simple-5.0.4.jar:/usr/share/java/kafka/zstd-jni-1.4.4-7.jar:/usr/share/java/kafka/jersey-container-servlet-core-2.28.jar:/usr/share/java/kafka/jersey-client-2.28.jar:/usr/share/java/kafka/argparse4j-0.7.0.jar:/usr/share/java/kafka/httpclient-4.5.11.jar:/usr/share/java/kafka/commons-lang3-3.8.1.jar:/usr/share/java/kafka/netty-transport-4.1.48.Final.jar:/usr/share/java/kafka/paranamer-2.8.jar:/usr/share/java/kafka/maven-artifact-3.6.3.jar:/usr/share/java/kafka/hk2-utils-2.5.0.jar:/usr/share/java/kafka/audience-annotations-0.5.0.jar:/usr/share/java/kafka/avro-1.9.2.jar:/usr/share/java/kafka/kafka-streams-5.5.1-ccs.jar:/usr/share/java/kafka/connect-json-5.5.1-ccs.jar:/usr/share/java/kafka/jetty-security-9.4.24.v20191120.jar:/usr/share/java/kafka/scala-logging_2.12-3.9.2.jar:/usr/share/java/kafka/scala-reflect-2.12.10.jar:/usr/share/java/kafka/connect-api-5.5.1-ccs.jar:/usr/share/java/kafka/jakarta.xml.bind-api-2.3.2.jar:/usr/share/java/kafka/connect-runtime-5.5.1-ccs.jar:/usr/share/java/kafka/jersey-container-servlet-2.28.jar:/usr/share/java/kafka/support-metrics-client-5.5.1-ccs.jar:/usr/share/java/kafka/plexus-utils-3.2.1.jar:/usr/share/java/kafka/validation-api-2.0.1.Final.jar:/usr/share/java/kafka/jetty-continuation-9.4.24.v20191120.jar:/usr/share/java/kafka/jackson-module-scala_2.12-2.10.2.jar:/usr/share/java/kafka/netty-codec-4.1.48.Final.jar:/usr/share/java/kafka/commons-logging-1.2.jar:/usr/share/java/kafka/jackson-annotations-2.10.2.jar:/usr/share/java/kafka/activation-1.1.1.jar:/usr/share/java/kafka/connect-mirror-5.5.1-ccs.jar:/usr/share/java/kafka/scala-java8-compat_2.12-0.9.0.jar:/usr/share/java/kafka/jetty-servlets-9.4.24.v20191120.jar:/usr/share/java/kafka/zookeeper-jute-3.5.8.jar:/usr/share/java/kafka/hk2-api-2.5.0.jar:/usr/share/java/kafka/scala-collection-compat_2.12-2.1.3.jar:/usr/share/java/kafka/jakarta.annotation-api-1.3.4.jar:/usr/share/java/kafka/reflections-0.9.12.jar:/usr/share/java/kafka/netty-common-4.1.48.Final.jar:/usr/share/java/kafka/kafka.jar:/usr/share/java/kafka/jackson-jaxrs-json-provider-2.10.2.jar:/usr/share/java/kafka/kafka-streams-scala_2.12-5.5.1-ccs.jar:/usr/share/java/kafka/jackson-databind-2.10.2.jar:/usr/share/java/kafka/zookeeper-3.5.8.jar:/usr/share/java/kafka/osgi-resource-locator-1.0.1.jar:/usr/share/java/kafka/netty-transport-native-unix-common-4.1.48.Final.jar:/usr/share/java/kafka/javax.servlet-api-3.1.0.jar:/usr/share/java/kafka/jersey-hk2-2.28.jar:/usr/share/java/kafka/netty-buffer-4.1.48.Final.jar:/usr/share/java/kafka/log4j-1.2.17.jar:/usr/share/java/kafka/jetty-client-9.4.24.v20191120.jar:/usr/share/java/kafka/connect-transforms-5.5.1-ccs.jar:/usr/share/java/kafka/lz4-java-1.7.1.jar:/usr/share/java/kafka/jersey-media-jaxb-2.28.jar:/usr/share/java/kafka/netty-resolver-4.1.48.Final.jar:/usr/share/java/kafka/jackson-core-2.10.2.jar:/usr/share/java/kafka/aopalliance-repackaged-2.5.0.jar:/usr/share/java/kafka/jetty-server-9.4.24.v20191120.jar:/usr/share/java/kafka/jersey-common-2.28.jar:/usr/share/java/kafka/confluent-metrics-5.5.1-ce.jar:/usr/share/java/confluent-common/common-config-5.5.1.jar:/usr/share/java/confluent-common/common-utils-5.5.1.jar:/usr/share/java/confluent-common/build-tools-5.5.1.jar:/usr/share/java/confluent-common/common-metrics-5.5.1.jar:/usr/share/java/confluent-common/slf4j-api-1.7.26.jar:/usr/share/java/kafka-serde-tools/okio-2.5.0.jar:/usr/share/java/kafka-serde-tools/mbknor-jackson-jsonschema_2.12-1.0.39.jar:/usr/share/java/kafka-serde-tools/commons-compress-1.19.jar:/usr/share/java/kafka-serde-tools/kotlin-stdlib-1.3.71.jar:/usr/share/java/kafka-serde-tools/kotlinx-coroutines-core-1.1.1.jar:/usr/share/java/kafka-serde-tools/jackson-datatype-jsr310-2.10.2.jar:/usr/share/java/kafka-serde-tools/kafka-connect-avro-data-5.5.1.jar:/usr/share/java/kafka-serde-tools/wire-schema-3.2.2.jar:/usr/share/java/kafka-serde-tools/kotlin-scripting-compiler-impl-embeddable-1.3.50.jar:/usr/share/java/kafka-serde-tools/scala-library-2.12.10.jar:/usr/share/java/kafka-serde-tools/wire-runtime-3.2.2.jar:/usr/share/java/kafka-serde-tools/joda-time-2.9.9.jar:/usr/share/java/kafka-serde-tools/kotlin-stdlib-common-1.3.71.jar:/usr/share/java/kafka-serde-tools/kotlin-stdlib-jdk8-1.3.71.jar:/usr/share/java/kafka-serde-tools/classgraph-4.8.21.jar:/usr/share/java/kafka-serde-tools/kotlin-script-runtime-1.3.50.jar:/usr/share/java/kafka-serde-tools/rocksdbjni-5.18.3.jar:/usr/share/java/kafka-serde-tools/annotations-13.0.jar:/usr/share/java/kafka-serde-tools/kafka-protobuf-provider-5.5.1.jar:/usr/share/java/kafka-serde-tools/animal-sniffer-annotations-1.14.jar:/usr/share/java/kafka-serde-tools/kafka-json-schema-provider-5.5.1.jar:/usr/share/java/kafka-serde-tools/osgi-resource-locator-1.0.3.jar:/usr/share/java/kafka-serde-tools/kafka-schema-serializer-5.5.1.jar:/usr/share/java/kafka-serde-tools/kafka-streams-protobuf-serde-5.5.1.jar:/usr/share/java/kafka-serde-tools/commons-collections-3.2.2.jar:/usr/share/java/kafka-serde-tools/jsr305-1.3.9.jar:/usr/share/java/kafka-serde-tools/org.everit.json.schema-1.12.1.jar:/usr/share/java/kafka-serde-tools/json-20190722.jar:/usr/share/java/kafka-serde-tools/jackson-datatype-jdk8-2.10.2.jar:/usr/share/java/kafka-serde-tools/kafka-avro-serializer-5.5.1.jar:/usr/share/java/kafka-serde-tools/error_prone_annotations-2.3.4.jar:/usr/share/java/kafka-serde-tools/kotlin-scripting-compiler-embeddable-1.3.50.jar:/usr/share/java/kafka-serde-tools/javax.ws.rs-api-2.1.1.jar:/usr/share/java/kafka-serde-tools/jakarta.annotation-api-1.3.5.jar:/usr/share/java/kafka-serde-tools/jackson-module-parameter-names-2.10.2.jar:/usr/share/java/kafka-serde-tools/kafka-connect-json-schema-converter-5.5.1.jar:/usr/share/java/kafka-serde-tools/kotlin-scripting-common-1.3.50.jar:/usr/share/java/kafka-serde-tools/protobuf-java-3.11.4.jar:/usr/share/java/kafka-serde-tools/kotlin-reflect-1.3.50.jar:/usr/share/java/kafka-serde-tools/kafka-json-schema-serializer-5.5.1.jar:/usr/share/java/kafka-serde-tools/kafka-protobuf-serializer-5.5.1.jar:/usr/share/java/kafka-serde-tools/kafka-schema-registry-client-5.5.1.jar:/usr/share/java/kafka-serde-tools/avro-1.9.2.jar:/usr/share/java/kafka-serde-tools/kafka-streams-5.5.1-ccs.jar:/usr/share/java/kafka-serde-tools/kafka-json-serializer-5.5.1.jar:/usr/share/java/kafka-serde-tools/kafka-connect-avro-converter-5.5.1.jar:/usr/share/java/kafka-serde-tools/re2j-1.3.jar:/usr/share/java/kafka-serde-tools/gson-2.8.5.jar:/usr/share/java/kafka-serde-tools/jersey-common-2.30.jar:/usr/share/java/kafka-serde-tools/kafka-connect-protobuf-converter-5.5.1.jar:/usr/share/java/kafka-serde-tools/validation-api-2.0.1.Final.jar:/usr/share/java/kafka-serde-tools/commons-logging-1.2.jar:/usr/share/java/kafka-serde-tools/jackson-annotations-2.10.2.jar:/usr/share/java/kafka-serde-tools/checker-compat-qual-2.0.0.jar:/usr/share/java/kafka-serde-tools/protobuf-java-util-3.11.4.jar:/usr/share/java/kafka-serde-tools/kafka-streams-json-schema-serde-5.5.1.jar:/usr/share/java/kafka-serde-tools/jackson-datatype-guava-2.10.2.jar:/usr/share/java/kafka-serde-tools/guava-24.0-jre.jar:/usr/share/java/kafka-serde-tools/swagger-annotations-1.6.0.jar:/usr/share/java/kafka-serde-tools/kafka-streams-avro-serde-5.5.1.jar:/usr/share/java/kafka-serde-tools/kotlinx-coroutines-core-common-1.1.1.jar:/usr/share/java/kafka-serde-tools/jakarta.ws.rs-api-2.1.6.jar:/usr/share/java/kafka-serde-tools/jackson-databind-2.10.2.jar:/usr/share/java/kafka-serde-tools/handy-uri-templates-2.1.8.jar:/usr/share/java/kafka-serde-tools/kotlin-scripting-jvm-1.3.50.jar:/usr/share/java/kafka-serde-tools/jakarta.inject-2.6.1.jar:/usr/share/java/kafka-serde-tools/commons-digester-1.8.1.jar:/usr/share/java/kafka-serde-tools/commons-validator-1.6.jar:/usr/share/java/kafka-serde-tools/kotlin-stdlib-jdk7-1.3.71.jar:/usr/share/java/kafka-serde-tools/jackson-datatype-joda-2.10.2.jar:/usr/share/java/kafka-serde-tools/jackson-core-2.10.2.jar:/usr/share/java/kafka-serde-tools/j2objc-annotations-1.1.jar:/usr/share/java/monitoring-interceptors/monitoring-interceptors-5.5.1.jar:/usr/bin/../share/java/kafka/kafka_2.12-5.5.1-ccs-test-sources.jar:/usr/bin/../share/java/kafka/jaxb-api-2.3.0.jar:/usr/bin/../share/java/kafka/commons-compress-1.19.jar:/usr/bin/../share/java/kafka/jakarta.ws.rs-api-2.1.5.jar:/usr/bin/../share/java/kafka/kafka_2.12-5.5.1-ccs-scaladoc.jar:/usr/bin/../share/java/kafka/javassist-3.26.0-GA.jar:/usr/bin/../share/java/kafka/snappy-java-1.1.7.3.jar:/usr/bin/../share/java/kafka/jetty-servlet-9.4.24.v20191120.jar:/usr/bin/../share/java/kafka/kafka_2.12-5.5.1-ccs-javadoc.jar:/usr/bin/../share/java/kafka/kafka-streams-examples-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/scala-library-2.12.10.jar:/usr/bin/../share/java/kafka/jetty-http-9.4.24.v20191120.jar:/usr/bin/../share/java/kafka/netty-transport-native-epoll-4.1.48.Final.jar:/usr/bin/../share/java/kafka/commons-cli-1.4.jar:/usr/bin/../share/java/kafka/kafka_2.12-5.5.1-ccs-test.jar:/usr/bin/../share/java/kafka/kafka_2.12-5.5.1-ccs-sources.jar:/usr/bin/../share/java/kafka/kafka-streams-test-utils-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/kafka-log4j-appender-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/support-metrics-common-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/netty-handler-4.1.48.Final.jar:/usr/bin/../share/java/kafka/rocksdbjni-5.18.3.jar:/usr/bin/../share/java/kafka/javassist-3.22.0-CR2.jar:/usr/bin/../share/java/kafka/kafka_2.12-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/jackson-module-paranamer-2.10.2.jar:/usr/bin/../share/java/kafka/jakarta.activation-api-1.2.1.jar:/usr/bin/../share/java/kafka/kafka-tools-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/jackson-module-jaxb-annotations-2.10.2.jar:/usr/bin/../share/java/kafka/connect-mirror-client-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/jakarta.inject-2.5.0.jar:/usr/bin/../share/java/kafka/httpcore-4.4.13.jar:/usr/bin/../share/java/kafka/connect-basic-auth-extension-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/jersey-server-2.28.jar:/usr/bin/../share/java/kafka/hk2-locator-2.5.0.jar:/usr/bin/../share/java/kafka/jetty-io-9.4.24.v20191120.jar:/usr/bin/../share/java/kafka/jackson-dataformat-csv-2.10.2.jar:/usr/bin/../share/java/kafka/kafka-clients-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/httpmime-4.5.11.jar:/usr/bin/../share/java/kafka/connect-file-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/commons-codec-1.11.jar:/usr/bin/../share/java/kafka/jackson-datatype-jdk8-2.10.2.jar:/usr/bin/../share/java/kafka/javax.ws.rs-api-2.1.1.jar:/usr/bin/../share/java/kafka/jetty-util-9.4.24.v20191120.jar:/usr/bin/../share/java/kafka/slf4j-log4j12-1.7.30.jar:/usr/bin/../share/java/kafka/jackson-jaxrs-base-2.10.2.jar:/usr/bin/../share/java/kafka/slf4j-api-1.7.30.jar:/usr/bin/../share/java/kafka/metrics-core-2.2.0.jar:/usr/bin/../share/java/kafka/jopt-simple-5.0.4.jar:/usr/bin/../share/java/kafka/zstd-jni-1.4.4-7.jar:/usr/bin/../share/java/kafka/jersey-container-servlet-core-2.28.jar:/usr/bin/../share/java/kafka/jersey-client-2.28.jar:/usr/bin/../share/java/kafka/argparse4j-0.7.0.jar:/usr/bin/../share/java/kafka/httpclient-4.5.11.jar:/usr/bin/../share/java/kafka/commons-lang3-3.8.1.jar:/usr/bin/../share/java/kafka/netty-transport-4.1.48.Final.jar:/usr/bin/../share/java/kafka/paranamer-2.8.jar:/usr/bin/../share/java/kafka/maven-artifact-3.6.3.jar:/usr/bin/../share/java/kafka/hk2-utils-2.5.0.jar:/usr/bin/../share/java/kafka/audience-annotations-0.5.0.jar:/usr/bin/../share/java/kafka/avro-1.9.2.jar:/usr/bin/../share/java/kafka/kafka-streams-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/connect-json-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/jetty-security-9.4.24.v20191120.jar:/usr/bin/../share/java/kafka/scala-logging_2.12-3.9.2.jar:/usr/bin/../share/java/kafka/scala-reflect-2.12.10.jar:/usr/bin/../share/java/kafka/connect-api-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/jakarta.xml.bind-api-2.3.2.jar:/usr/bin/../share/java/kafka/connect-runtime-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/jersey-container-servlet-2.28.jar:/usr/bin/../share/java/kafka/support-metrics-client-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/plexus-utils-3.2.1.jar:/usr/bin/../share/java/kafka/validation-api-2.0.1.Final.jar:/usr/bin/../share/java/kafka/jetty-continuation-9.4.24.v20191120.jar:/usr/bin/../share/java/kafka/jackson-module-scala_2.12-2.10.2.jar:/usr/bin/../share/java/kafka/netty-codec-4.1.48.Final.jar:/usr/bin/../share/java/kafka/commons-logging-1.2.jar:/usr/bin/../share/java/kafka/jackson-annotations-2.10.2.jar:/usr/bin/../share/java/kafka/activation-1.1.1.jar:/usr/bin/../share/java/kafka/connect-mirror-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/scala-java8-compat_2.12-0.9.0.jar:/usr/bin/../share/java/kafka/jetty-servlets-9.4.24.v20191120.jar:/usr/bin/../share/java/kafka/zookeeper-jute-3.5.8.jar:/usr/bin/../share/java/kafka/hk2-api-2.5.0.jar:/usr/bin/../share/java/kafka/scala-collection-compat_2.12-2.1.3.jar:/usr/bin/../share/java/kafka/jakarta.annotation-api-1.3.4.jar:/usr/bin/../share/java/kafka/reflections-0.9.12.jar:/usr/bin/../share/java/kafka/netty-common-4.1.48.Final.jar:/usr/bin/../share/java/kafka/kafka.jar:/usr/bin/../share/java/kafka/jackson-jaxrs-json-provider-2.10.2.jar:/usr/bin/../share/java/kafka/kafka-streams-scala_2.12-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/jackson-databind-2.10.2.jar:/usr/bin/../share/java/kafka/zookeeper-3.5.8.jar:/usr/bin/../share/java/kafka/osgi-resource-locator-1.0.1.jar:/usr/bin/../share/java/kafka/netty-transport-native-unix-common-4.1.48.Final.jar:/usr/bin/../share/java/kafka/javax.servlet-api-3.1.0.jar:/usr/bin/../share/java/kafka/jersey-hk2-2.28.jar:/usr/bin/../share/java/kafka/netty-buffer-4.1.48.Final.jar:/usr/bin/../share/java/kafka/log4j-1.2.17.jar:/usr/bin/../share/java/kafka/jetty-client-9.4.24.v20191120.jar:/usr/bin/../share/java/kafka/connect-transforms-5.5.1-ccs.jar:/usr/bin/../share/java/kafka/lz4-java-1.7.1.jar:/usr/bin/../share/java/kafka/jersey-media-jaxb-2.28.jar:/usr/bin/../share/java/kafka/netty-resolver-4.1.48.Final.jar:/usr/bin/../share/java/kafka/jackson-core-2.10.2.jar:/usr/bin/../share/java/kafka/aopalliance-repackaged-2.5.0.jar:/usr/bin/../share/java/kafka/jetty-server-9.4.24.v20191120.jar:/usr/bin/../share/java/kafka/jersey-common-2.28.jar:/usr/bin/../share/java/kafka/confluent-metrics-5.5.1-ce.jar:/usr/bin/../support-metrics-client/build/dependant-libs-2.12/*:/usr/bin/../support-metrics-client/build/libs/*:/usr/share/java/support-metrics-client/*
[36mconnect_1             |[0m 	os.spec = Linux, amd64, 5.4.0-7634-generic
[36mconnect_1             |[0m 	os.vcpus = 4
[36mconnect_1             |[0m  (org.apache.kafka.connect.runtime.WorkerInfo)
[36mconnect_1             |[0m [2020-08-20 01:07:39,128] INFO Scanning for plugin classes. This might take a moment ... (org.apache.kafka.connect.cli.ConnectDistributed)
[36mconnect_1             |[0m [2020-08-20 01:07:39,237] INFO Loading plugin from: /usr/share/java/kafka-connect-jdbc (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:40,596] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/kafka-connect-jdbc/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:40,596] INFO Added plugin 'io.confluent.connect.jdbc.JdbcSinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:40,598] INFO Added plugin 'io.confluent.connect.jdbc.JdbcSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:40,598] INFO Added plugin 'org.apache.kafka.connect.connector.policy.AllConnectorClientConfigOverridePolicy' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:40,598] INFO Added plugin 'org.apache.kafka.connect.connector.policy.PrincipalConnectorClientConfigOverridePolicy' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:40,599] INFO Added plugin 'org.apache.kafka.connect.connector.policy.NoneConnectorClientConfigOverridePolicy' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:40,648] INFO Loading plugin from: /usr/share/java/kafka-connect-jms (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:43,551] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/kafka-connect-jms/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:43,557] INFO Added plugin 'io.confluent.connect.jms.JmsSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:43,560] INFO Loading plugin from: /usr/share/java/kafka-connect-s3 (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:50,927] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/kafka-connect-s3/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:50,927] INFO Added plugin 'io.confluent.connect.s3.S3SinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:50,927] INFO Added plugin 'io.confluent.connect.storage.tools.SchemaSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:50,928] INFO Added plugin 'io.confluent.connect.avro.AvroConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:50,928] INFO Added plugin 'org.apache.kafka.common.config.provider.FileConfigProvider' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:50,928] INFO Loading plugin from: /usr/share/java/kafka-connect-activemq (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:51,534] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/kafka-connect-activemq/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:51,534] INFO Added plugin 'io.confluent.connect.activemq.ActiveMQSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:51,539] INFO Loading plugin from: /usr/share/java/kafka-connect-elasticsearch (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:51,834] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/kafka-connect-elasticsearch/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:51,834] INFO Added plugin 'io.confluent.connect.elasticsearch.ElasticsearchSinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:51,835] INFO Loading plugin from: /usr/share/java/kafka-connect-ibmmq (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:52,181] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/kafka-connect-ibmmq/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:52,181] INFO Added plugin 'io.confluent.connect.ibm.mq.IbmMQSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:52,182] INFO Loading plugin from: /usr/share/java/kafka-connect-storage-common (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:53,581] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/kafka-connect-storage-common/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:53,582] INFO Loading plugin from: /usr/share/java/monitoring-interceptors (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:53,823] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/monitoring-interceptors/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:53,823] INFO Loading plugin from: /usr/share/java/confluent-rebalancer (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,736] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/confluent-rebalancer/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,737] INFO Added plugin 'org.apache.kafka.connect.tools.VerifiableSinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,737] INFO Added plugin 'org.apache.kafka.connect.tools.VerifiableSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,737] INFO Added plugin 'org.apache.kafka.connect.tools.MockSinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,737] INFO Added plugin 'org.apache.kafka.connect.tools.MockConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,737] INFO Added plugin 'org.apache.kafka.connect.tools.MockSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,737] INFO Added plugin 'org.apache.kafka.connect.tools.SchemaSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,737] INFO Added plugin 'org.apache.kafka.connect.converters.FloatConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,737] INFO Added plugin 'org.apache.kafka.connect.converters.DoubleConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,737] INFO Added plugin 'org.apache.kafka.connect.converters.ByteArrayConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,737] INFO Added plugin 'org.apache.kafka.connect.converters.LongConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,737] INFO Added plugin 'org.apache.kafka.connect.converters.IntegerConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,738] INFO Added plugin 'org.apache.kafka.connect.json.JsonConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,738] INFO Added plugin 'org.apache.kafka.connect.storage.StringConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,738] INFO Added plugin 'org.apache.kafka.connect.converters.ShortConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,738] INFO Added plugin 'org.apache.kafka.connect.storage.SimpleHeaderConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,738] INFO Added plugin 'org.apache.kafka.connect.transforms.ReplaceField$Value' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,738] INFO Added plugin 'org.apache.kafka.connect.transforms.SetSchemaMetadata$Value' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,738] INFO Added plugin 'org.apache.kafka.connect.transforms.ReplaceField$Key' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,738] INFO Added plugin 'org.apache.kafka.connect.transforms.InsertField$Value' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,738] INFO Added plugin 'org.apache.kafka.connect.transforms.TimestampConverter$Key' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,738] INFO Added plugin 'org.apache.kafka.connect.transforms.MaskField$Value' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,738] INFO Added plugin 'org.apache.kafka.connect.transforms.TimestampRouter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,739] INFO Added plugin 'org.apache.kafka.connect.transforms.RegexRouter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,739] INFO Added plugin 'org.apache.kafka.connect.transforms.HoistField$Value' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,739] INFO Added plugin 'org.apache.kafka.connect.transforms.ValueToKey' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,739] INFO Added plugin 'org.apache.kafka.connect.transforms.MaskField$Key' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,739] INFO Added plugin 'org.apache.kafka.connect.transforms.Cast$Key' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,739] INFO Added plugin 'org.apache.kafka.connect.transforms.Cast$Value' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,739] INFO Added plugin 'org.apache.kafka.connect.transforms.ExtractField$Key' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,739] INFO Added plugin 'org.apache.kafka.connect.transforms.Flatten$Value' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,739] INFO Added plugin 'org.apache.kafka.connect.transforms.InsertField$Key' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,739] INFO Added plugin 'org.apache.kafka.connect.transforms.Flatten$Key' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,739] INFO Added plugin 'org.apache.kafka.connect.transforms.SetSchemaMetadata$Key' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,740] INFO Added plugin 'org.apache.kafka.connect.transforms.ExtractField$Value' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,740] INFO Added plugin 'org.apache.kafka.connect.transforms.TimestampConverter$Value' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,740] INFO Added plugin 'org.apache.kafka.connect.transforms.HoistField$Key' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,740] INFO Loading plugin from: /usr/share/java/confluent-hub-client (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,992] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/confluent-hub-client/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:07:56,992] INFO Loading plugin from: /usr/share/java/acl (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:00,812] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/acl/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:00,812] INFO Added plugin 'io.confluent.connect.json.JsonSchemaConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:00,812] INFO Added plugin 'io.confluent.connect.protobuf.ProtobufConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:00,813] INFO Added plugin 'io.confluent.kafka.secretregistry.client.config.provider.SecretConfigProvider' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:00,813] INFO Added plugin 'io.confluent.connect.security.ConnectSecurityExtension' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:00,813] INFO Loading plugin from: /usr/share/java/rest-utils (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:01,204] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/rest-utils/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:01,205] INFO Loading plugin from: /usr/share/java/schema-registry (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:02,253] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/schema-registry/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:02,253] INFO Loading plugin from: /usr/share/java/confluent-common (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:02,259] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/confluent-common/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:02,260] INFO Loading plugin from: /usr/share/java/kafka-serde-tools (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:02,890] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/kafka-serde-tools/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:02,890] INFO Loading plugin from: /usr/share/java/kafka (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:04,583] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/kafka/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:04,584] INFO Added plugin 'org.apache.kafka.connect.mirror.MirrorSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:04,584] INFO Added plugin 'org.apache.kafka.connect.file.FileStreamSinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:04,584] INFO Added plugin 'org.apache.kafka.connect.file.FileStreamSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:04,584] INFO Added plugin 'org.apache.kafka.connect.mirror.MirrorCheckpointConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:04,584] INFO Added plugin 'org.apache.kafka.connect.mirror.MirrorHeartbeatConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:04,584] INFO Added plugin 'org.apache.kafka.connect.rest.basic.auth.extension.BasicAuthSecurityRestExtension' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:04,585] INFO Loading plugin from: /usr/share/java/confluent-control-center (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:07,961] INFO Registered loader: PluginClassLoader{pluginLocation=file:/usr/share/java/confluent-control-center/} (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,167] INFO Registered loader: sun.misc.Launcher$AppClassLoader@764c12b6 (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,168] INFO Added aliases 'ActiveMQSourceConnector' and 'ActiveMQSource' to plugin 'io.confluent.connect.activemq.ActiveMQSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,168] INFO Added aliases 'ElasticsearchSinkConnector' and 'ElasticsearchSink' to plugin 'io.confluent.connect.elasticsearch.ElasticsearchSinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,169] INFO Added aliases 'IbmMQSourceConnector' and 'IbmMQSource' to plugin 'io.confluent.connect.ibm.mq.IbmMQSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,169] INFO Added aliases 'JdbcSinkConnector' and 'JdbcSink' to plugin 'io.confluent.connect.jdbc.JdbcSinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,169] INFO Added aliases 'JdbcSourceConnector' and 'JdbcSource' to plugin 'io.confluent.connect.jdbc.JdbcSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,169] INFO Added aliases 'JmsSourceConnector' and 'JmsSource' to plugin 'io.confluent.connect.jms.JmsSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,169] INFO Added aliases 'S3SinkConnector' and 'S3Sink' to plugin 'io.confluent.connect.s3.S3SinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,170] INFO Added aliases 'FileStreamSinkConnector' and 'FileStreamSink' to plugin 'org.apache.kafka.connect.file.FileStreamSinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,170] INFO Added aliases 'FileStreamSourceConnector' and 'FileStreamSource' to plugin 'org.apache.kafka.connect.file.FileStreamSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,170] INFO Added aliases 'MirrorCheckpointConnector' and 'MirrorCheckpoint' to plugin 'org.apache.kafka.connect.mirror.MirrorCheckpointConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,170] INFO Added aliases 'MirrorHeartbeatConnector' and 'MirrorHeartbeat' to plugin 'org.apache.kafka.connect.mirror.MirrorHeartbeatConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,170] INFO Added aliases 'MirrorSourceConnector' and 'MirrorSource' to plugin 'org.apache.kafka.connect.mirror.MirrorSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,170] INFO Added aliases 'MockConnector' and 'Mock' to plugin 'org.apache.kafka.connect.tools.MockConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,170] INFO Added aliases 'MockSinkConnector' and 'MockSink' to plugin 'org.apache.kafka.connect.tools.MockSinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,171] INFO Added aliases 'MockSourceConnector' and 'MockSource' to plugin 'org.apache.kafka.connect.tools.MockSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,171] INFO Added aliases 'VerifiableSinkConnector' and 'VerifiableSink' to plugin 'org.apache.kafka.connect.tools.VerifiableSinkConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,171] INFO Added aliases 'VerifiableSourceConnector' and 'VerifiableSource' to plugin 'org.apache.kafka.connect.tools.VerifiableSourceConnector' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,171] INFO Added aliases 'AvroConverter' and 'Avro' to plugin 'io.confluent.connect.avro.AvroConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,171] INFO Added aliases 'JsonSchemaConverter' and 'JsonSchema' to plugin 'io.confluent.connect.json.JsonSchemaConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,171] INFO Added aliases 'ProtobufConverter' and 'Protobuf' to plugin 'io.confluent.connect.protobuf.ProtobufConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,172] INFO Added aliases 'ByteArrayConverter' and 'ByteArray' to plugin 'org.apache.kafka.connect.converters.ByteArrayConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,172] INFO Added aliases 'DoubleConverter' and 'Double' to plugin 'org.apache.kafka.connect.converters.DoubleConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,172] INFO Added aliases 'FloatConverter' and 'Float' to plugin 'org.apache.kafka.connect.converters.FloatConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,172] INFO Added aliases 'IntegerConverter' and 'Integer' to plugin 'org.apache.kafka.connect.converters.IntegerConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,172] INFO Added aliases 'LongConverter' and 'Long' to plugin 'org.apache.kafka.connect.converters.LongConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,172] INFO Added aliases 'ShortConverter' and 'Short' to plugin 'org.apache.kafka.connect.converters.ShortConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,172] INFO Added aliases 'JsonConverter' and 'Json' to plugin 'org.apache.kafka.connect.json.JsonConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,172] INFO Added aliases 'StringConverter' and 'String' to plugin 'org.apache.kafka.connect.storage.StringConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,172] INFO Added aliases 'ByteArrayConverter' and 'ByteArray' to plugin 'org.apache.kafka.connect.converters.ByteArrayConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,173] INFO Added aliases 'DoubleConverter' and 'Double' to plugin 'org.apache.kafka.connect.converters.DoubleConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,173] INFO Added aliases 'FloatConverter' and 'Float' to plugin 'org.apache.kafka.connect.converters.FloatConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,173] INFO Added aliases 'IntegerConverter' and 'Integer' to plugin 'org.apache.kafka.connect.converters.IntegerConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,174] INFO Added aliases 'LongConverter' and 'Long' to plugin 'org.apache.kafka.connect.converters.LongConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,174] INFO Added aliases 'ShortConverter' and 'Short' to plugin 'org.apache.kafka.connect.converters.ShortConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,175] INFO Added aliases 'JsonConverter' and 'Json' to plugin 'org.apache.kafka.connect.json.JsonConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,175] INFO Added alias 'SimpleHeaderConverter' to plugin 'org.apache.kafka.connect.storage.SimpleHeaderConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,175] INFO Added aliases 'StringConverter' and 'String' to plugin 'org.apache.kafka.connect.storage.StringConverter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,176] INFO Added alias 'RegexRouter' to plugin 'org.apache.kafka.connect.transforms.RegexRouter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,176] INFO Added alias 'TimestampRouter' to plugin 'org.apache.kafka.connect.transforms.TimestampRouter' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,176] INFO Added alias 'ValueToKey' to plugin 'org.apache.kafka.connect.transforms.ValueToKey' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,176] INFO Added alias 'ConnectSecurityExtension' to plugin 'io.confluent.connect.security.ConnectSecurityExtension' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,177] INFO Added alias 'BasicAuthSecurityRestExtension' to plugin 'org.apache.kafka.connect.rest.basic.auth.extension.BasicAuthSecurityRestExtension' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,177] INFO Added aliases 'AllConnectorClientConfigOverridePolicy' and 'All' to plugin 'org.apache.kafka.connect.connector.policy.AllConnectorClientConfigOverridePolicy' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,177] INFO Added aliases 'NoneConnectorClientConfigOverridePolicy' and 'None' to plugin 'org.apache.kafka.connect.connector.policy.NoneConnectorClientConfigOverridePolicy' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,177] INFO Added aliases 'PrincipalConnectorClientConfigOverridePolicy' and 'Principal' to plugin 'org.apache.kafka.connect.connector.policy.PrincipalConnectorClientConfigOverridePolicy' (org.apache.kafka.connect.runtime.isolation.DelegatingClassLoader)
[36mconnect_1             |[0m [2020-08-20 01:08:11,263] INFO DistributedConfig values: 
[36mconnect_1             |[0m 	access.control.allow.methods = 
[36mconnect_1             |[0m 	access.control.allow.origin = 
[36mconnect_1             |[0m 	admin.listeners = null
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = 
[36mconnect_1             |[0m 	config.providers = []
[36mconnect_1             |[0m 	config.storage.replication.factor = 1
[36mconnect_1             |[0m 	config.storage.topic = connect-config
[36mconnect_1             |[0m 	connect.protocol = sessioned
[36mconnect_1             |[0m 	connections.max.idle.ms = 540000
[36mconnect_1             |[0m 	connector.client.config.override.policy = None
[36mconnect_1             |[0m 	group.id = connect
[36mconnect_1             |[0m 	header.converter = class org.apache.kafka.connect.storage.SimpleHeaderConverter
[36mconnect_1             |[0m 	heartbeat.interval.ms = 3000
[36mconnect_1             |[0m 	inter.worker.key.generation.algorithm = HmacSHA256
[36mconnect_1             |[0m 	inter.worker.key.size = null
[36mconnect_1             |[0m 	inter.worker.key.ttl.ms = 3600000
[36mconnect_1             |[0m 	inter.worker.signature.algorithm = HmacSHA256
[36mconnect_1             |[0m 	inter.worker.verification.algorithms = [HmacSHA256]
[36mconnect_1             |[0m 	internal.key.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m 	internal.value.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m 	key.converter = class io.confluent.connect.avro.AvroConverter
[36mconnect_1             |[0m 	listeners = null
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	offset.flush.interval.ms = 60000
[36mconnect_1             |[0m 	offset.flush.timeout.ms = 5000
[36mconnect_1             |[0m 	offset.storage.partitions = 25
[36mconnect_1             |[0m 	offset.storage.replication.factor = 1
[36mconnect_1             |[0m 	offset.storage.topic = connect-offset
[36mconnect_1             |[0m 	plugin.path = [/usr/share/java]
[36mconnect_1             |[0m 	rebalance.timeout.ms = 60000
[36mconnect_1             |[0m 	receive.buffer.bytes = 32768
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 40000
[36mconnect_1             |[0m 	rest.advertised.host.name = connect
[36mconnect_1             |[0m 	rest.advertised.listener = null
[36mconnect_1             |[0m 	rest.advertised.port = null
[36mconnect_1             |[0m 	rest.extension.classes = []
[36mconnect_1             |[0m 	rest.host.name = null
[36mconnect_1             |[0m 	rest.port = 8083
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	scheduled.rebalance.max.delay.ms = 300000
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	session.timeout.ms = 10000
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.client.auth = none
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m 	status.storage.partitions = 5
[36mconnect_1             |[0m 	status.storage.replication.factor = 1
[36mconnect_1             |[0m 	status.storage.topic = connect-status
[36mconnect_1             |[0m 	task.shutdown.graceful.timeout.ms = 5000
[36mconnect_1             |[0m 	topic.tracking.allow.reset = true
[36mconnect_1             |[0m 	topic.tracking.enable = true
[36mconnect_1             |[0m 	value.converter = class io.confluent.connect.avro.AvroConverter
[36mconnect_1             |[0m 	worker.sync.timeout.ms = 3000
[36mconnect_1             |[0m 	worker.unsync.backoff.ms = 300000
[36mconnect_1             |[0m  (org.apache.kafka.connect.runtime.distributed.DistributedConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,264] INFO Worker configuration property 'internal.key.converter' is deprecated and may be removed in an upcoming release. The specified value 'org.apache.kafka.connect.json.JsonConverter' matches the default, so this property can be safely removed from the worker configuration. (org.apache.kafka.connect.runtime.WorkerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,264] INFO Worker configuration property 'internal.key.converter.schemas.enable' (along with all configuration for 'internal.key.converter') is deprecated and may be removed in an upcoming release. The specified value 'false' matches the default, so this property can be safely removed from the worker configuration. (org.apache.kafka.connect.runtime.WorkerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,264] INFO Worker configuration property 'internal.value.converter' is deprecated and may be removed in an upcoming release. The specified value 'org.apache.kafka.connect.json.JsonConverter' matches the default, so this property can be safely removed from the worker configuration. (org.apache.kafka.connect.runtime.WorkerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,264] INFO Worker configuration property 'internal.value.converter.schemas.enable' (along with all configuration for 'internal.value.converter') is deprecated and may be removed in an upcoming release. The specified value 'false' matches the default, so this property can be safely removed from the worker configuration. (org.apache.kafka.connect.runtime.WorkerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,266] INFO Creating Kafka admin client (org.apache.kafka.connect.util.ConnectUtils)
[36mconnect_1             |[0m [2020-08-20 01:08:11,269] INFO AdminClientConfig values: 
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = 
[36mconnect_1             |[0m 	connections.max.idle.ms = 300000
[36mconnect_1             |[0m 	default.api.timeout.ms = 60000
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	receive.buffer.bytes = 65536
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 30000
[36mconnect_1             |[0m 	retries = 2147483647
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m  (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,374] WARN The configuration 'config.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,374] WARN The configuration 'rest.advertised.host.name' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'status.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'group.id' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'plugin.path' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'internal.key.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'config.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'rest.port' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'internal.key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'value.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'internal.value.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'status.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'internal.value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'offset.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'offset.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,375] WARN The configuration 'key.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:11,376] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:11,376] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:11,376] INFO Kafka startTimeMs: 1597885691375 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:11,774] INFO Kafka cluster ID: 40eSduN2R46UaeWXQ6fOrQ (org.apache.kafka.connect.util.ConnectUtils)
[36mconnect_1             |[0m [2020-08-20 01:08:11,796] INFO Logging initialized @34570ms to org.eclipse.jetty.util.log.Slf4jLog (org.eclipse.jetty.util.log)
[36mconnect_1             |[0m [2020-08-20 01:08:11,856] INFO Added connector for http://:8083 (org.apache.kafka.connect.runtime.rest.RestServer)
[36mconnect_1             |[0m [2020-08-20 01:08:11,856] INFO Initializing REST server (org.apache.kafka.connect.runtime.rest.RestServer)
[36mconnect_1             |[0m [2020-08-20 01:08:11,863] INFO jetty-9.4.24.v20191120; built: 2019-11-20T21:37:49.771Z; git: 363d5f2df3a8a28de40604320230664b9c793c16; jvm 1.8.0_212-b04 (org.eclipse.jetty.server.Server)
[36mconnect_1             |[0m [2020-08-20 01:08:11,894] INFO Started http_8083@77db957b{HTTP/1.1,[http/1.1]}{0.0.0.0:8083} (org.eclipse.jetty.server.AbstractConnector)
[36mconnect_1             |[0m [2020-08-20 01:08:11,895] INFO Started @34669ms (org.eclipse.jetty.server.Server)
[36mconnect_1             |[0m [2020-08-20 01:08:11,921] INFO Advertised URI: http://connect:8083/ (org.apache.kafka.connect.runtime.rest.RestServer)
[36mconnect_1             |[0m [2020-08-20 01:08:11,921] INFO REST server listening at http://172.18.0.9:8083/, advertising URL http://connect:8083/ (org.apache.kafka.connect.runtime.rest.RestServer)
[36mconnect_1             |[0m [2020-08-20 01:08:11,923] INFO Advertised URI: http://connect:8083/ (org.apache.kafka.connect.runtime.rest.RestServer)
[36mconnect_1             |[0m [2020-08-20 01:08:11,923] INFO REST admin endpoints at http://connect:8083/ (org.apache.kafka.connect.runtime.rest.RestServer)
[36mconnect_1             |[0m [2020-08-20 01:08:11,924] INFO Advertised URI: http://connect:8083/ (org.apache.kafka.connect.runtime.rest.RestServer)
[36mconnect_1             |[0m [2020-08-20 01:08:11,932] INFO Setting up None Policy for ConnectorClientConfigOverride. This will disallow any client configuration to be overridden (org.apache.kafka.connect.connector.policy.NoneConnectorClientConfigOverridePolicy)
[36mconnect_1             |[0m [2020-08-20 01:08:11,945] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:11,945] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:11,945] INFO Kafka startTimeMs: 1597885691945 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:12,109] INFO JsonConverterConfig values: 
[36mconnect_1             |[0m 	converter.type = key
[36mconnect_1             |[0m 	decimal.format = BASE64
[36mconnect_1             |[0m 	schemas.cache.size = 1000
[36mconnect_1             |[0m 	schemas.enable = false
[36mconnect_1             |[0m  (org.apache.kafka.connect.json.JsonConverterConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,111] INFO JsonConverterConfig values: 
[36mconnect_1             |[0m 	converter.type = value
[36mconnect_1             |[0m 	decimal.format = BASE64
[36mconnect_1             |[0m 	schemas.cache.size = 1000
[36mconnect_1             |[0m 	schemas.enable = false
[36mconnect_1             |[0m  (org.apache.kafka.connect.json.JsonConverterConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,173] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:12,173] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:12,173] INFO Kafka startTimeMs: 1597885692173 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:12,177] INFO Kafka Connect distributed worker initialization took 33048ms (org.apache.kafka.connect.cli.ConnectDistributed)
[36mconnect_1             |[0m [2020-08-20 01:08:12,177] INFO Kafka Connect starting (org.apache.kafka.connect.runtime.Connect)
[36mconnect_1             |[0m [2020-08-20 01:08:12,179] INFO Initializing REST resources (org.apache.kafka.connect.runtime.rest.RestServer)
[36mconnect_1             |[0m [2020-08-20 01:08:12,179] INFO [Worker clientId=connect-1, groupId=connect] Herder starting (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:08:12,180] INFO Worker starting (org.apache.kafka.connect.runtime.Worker)
[36mconnect_1             |[0m [2020-08-20 01:08:12,180] INFO Starting KafkaOffsetBackingStore (org.apache.kafka.connect.storage.KafkaOffsetBackingStore)
[36mconnect_1             |[0m [2020-08-20 01:08:12,180] INFO Starting KafkaBasedLog with topic connect-offset (org.apache.kafka.connect.util.KafkaBasedLog)
[36mconnect_1             |[0m [2020-08-20 01:08:12,181] INFO AdminClientConfig values: 
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = 
[36mconnect_1             |[0m 	connections.max.idle.ms = 300000
[36mconnect_1             |[0m 	default.api.timeout.ms = 60000
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	receive.buffer.bytes = 65536
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 30000
[36mconnect_1             |[0m 	retries = 2147483647
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m  (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,188] WARN The configuration 'config.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,188] WARN The configuration 'rest.advertised.host.name' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,188] WARN The configuration 'status.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,188] WARN The configuration 'group.id' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,188] WARN The configuration 'plugin.path' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,188] WARN The configuration 'internal.key.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,188] WARN The configuration 'config.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,188] WARN The configuration 'rest.port' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,188] WARN The configuration 'internal.key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,189] WARN The configuration 'value.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,189] WARN The configuration 'internal.value.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,189] WARN The configuration 'status.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,189] WARN The configuration 'internal.value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,189] WARN The configuration 'offset.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,189] WARN The configuration 'offset.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,189] WARN The configuration 'value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,189] WARN The configuration 'key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,189] WARN The configuration 'key.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:12,191] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:12,192] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:12,192] INFO Kafka startTimeMs: 1597885692191 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:12,292] INFO Adding admin resources to main listener (org.apache.kafka.connect.runtime.rest.RestServer)
[36mconnect_1             |[0m [2020-08-20 01:08:12,562] INFO DefaultSessionIdManager workerName=node0 (org.eclipse.jetty.server.session)
[36mconnect_1             |[0m [2020-08-20 01:08:12,562] INFO No SessionScavenger set, using defaults (org.eclipse.jetty.server.session)
[36mconnect_1             |[0m [2020-08-20 01:08:12,564] INFO node0 Scavenging every 600000ms (org.eclipse.jetty.server.session)
[36mconnect_1             |[0m [2020-08-20 01:08:13,175] INFO Created topic (name=connect-offset, numPartitions=25, replicationFactor=1, replicasAssignments=null, configs={cleanup.policy=compact}) on brokers at PLAINTEXT://kafka0:19092 (org.apache.kafka.connect.util.TopicAdmin)
[36mconnect_1             |[0m [2020-08-20 01:08:13,195] INFO ProducerConfig values: 
[36mconnect_1             |[0m 	acks = -1
[36mconnect_1             |[0m 	batch.size = 16384
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	buffer.memory = 33554432
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = producer-1
[36mconnect_1             |[0m 	compression.type = none
[36mconnect_1             |[0m 	connections.max.idle.ms = 540000
[36mconnect_1             |[0m 	delivery.timeout.ms = 2147483647
[36mconnect_1             |[0m 	enable.idempotence = false
[36mconnect_1             |[0m 	interceptor.classes = []
[36mconnect_1             |[0m 	key.serializer = class org.apache.kafka.common.serialization.ByteArraySerializer
[36mconnect_1             |[0m 	linger.ms = 0
[36mconnect_1             |[0m 	max.block.ms = 60000
[36mconnect_1             |[0m 	max.in.flight.requests.per.connection = 1
[36mconnect_1             |[0m 	max.request.size = 1048576
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metadata.max.idle.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	partitioner.class = class org.apache.kafka.clients.producer.internals.DefaultPartitioner
[36mconnect_1             |[0m 	receive.buffer.bytes = 32768
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 30000
[36mconnect_1             |[0m 	retries = 2147483647
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m 	transaction.timeout.ms = 60000
[36mconnect_1             |[0m 	transactional.id = null
[36mconnect_1             |[0m 	value.serializer = class org.apache.kafka.common.serialization.ByteArraySerializer
[36mconnect_1             |[0m  (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'group.id' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'plugin.path' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'internal.key.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'status.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'offset.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'config.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'rest.advertised.host.name' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'status.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'config.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'rest.port' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'internal.key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'value.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'internal.value.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'internal.value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'offset.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,243] WARN The configuration 'key.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,244] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,244] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,244] INFO Kafka startTimeMs: 1597885693244 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,252] INFO ConsumerConfig values: 
[36mconnect_1             |[0m 	allow.auto.create.topics = true
[36mconnect_1             |[0m 	auto.commit.interval.ms = 5000
[36mconnect_1             |[0m 	auto.offset.reset = earliest
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	check.crcs = true
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = 
[36mconnect_1             |[0m 	client.rack = 
[36mconnect_1             |[0m 	connections.max.idle.ms = 540000
[36mconnect_1             |[0m 	default.api.timeout.ms = 60000
[36mconnect_1             |[0m 	enable.auto.commit = false
[36mconnect_1             |[0m 	exclude.internal.topics = true
[36mconnect_1             |[0m 	fetch.max.bytes = 52428800
[36mconnect_1             |[0m 	fetch.max.wait.ms = 500
[36mconnect_1             |[0m 	fetch.min.bytes = 1
[36mconnect_1             |[0m 	group.id = connect
[36mconnect_1             |[0m 	group.instance.id = null
[36mconnect_1             |[0m 	heartbeat.interval.ms = 3000
[36mconnect_1             |[0m 	interceptor.classes = []
[36mconnect_1             |[0m 	internal.leave.group.on.close = true
[36mconnect_1             |[0m 	isolation.level = read_uncommitted
[36mconnect_1             |[0m 	key.deserializer = class org.apache.kafka.common.serialization.ByteArrayDeserializer
[36mconnect_1             |[0m 	max.partition.fetch.bytes = 1048576
[36mconnect_1             |[0m 	max.poll.interval.ms = 300000
[36mconnect_1             |[0m 	max.poll.records = 500
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	partition.assignment.strategy = [class org.apache.kafka.clients.consumer.RangeAssignor]
[36mconnect_1             |[0m 	receive.buffer.bytes = 65536
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 30000
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	session.timeout.ms = 10000
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m 	value.deserializer = class org.apache.kafka.common.serialization.ByteArrayDeserializer
[36mconnect_1             |[0m  (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,288] INFO [Producer clientId=producer-1] Cluster ID: 40eSduN2R46UaeWXQ6fOrQ (org.apache.kafka.clients.Metadata)
[36mconnect_1             |[0m [2020-08-20 01:08:13,313] WARN The configuration 'config.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,320] WARN The configuration 'rest.advertised.host.name' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,320] WARN The configuration 'status.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,320] WARN The configuration 'plugin.path' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,320] WARN The configuration 'internal.key.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,320] WARN The configuration 'config.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,320] WARN The configuration 'rest.port' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,320] WARN The configuration 'internal.key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,320] WARN The configuration 'value.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,321] WARN The configuration 'internal.value.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,321] WARN The configuration 'status.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,321] WARN The configuration 'internal.value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,321] WARN The configuration 'offset.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,321] WARN The configuration 'offset.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,321] WARN The configuration 'value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,321] WARN The configuration 'key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,321] WARN The configuration 'key.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,321] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,322] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,322] INFO Kafka startTimeMs: 1597885693321 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,339] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Cluster ID: 40eSduN2R46UaeWXQ6fOrQ (org.apache.kafka.clients.Metadata)
[36mconnect_1             |[0m Aug 20, 2020 1:08:13 AM org.glassfish.jersey.internal.inject.Providers checkProviderRuntime
[36mconnect_1             |[0m WARNING: A provider org.apache.kafka.connect.runtime.rest.resources.LoggingResource registered in SERVER runtime does not implement any provider interfaces applicable in the SERVER runtime. Due to constraint configuration problems the provider org.apache.kafka.connect.runtime.rest.resources.LoggingResource will be ignored. 
[36mconnect_1             |[0m Aug 20, 2020 1:08:13 AM org.glassfish.jersey.internal.inject.Providers checkProviderRuntime
[36mconnect_1             |[0m WARNING: A provider org.apache.kafka.connect.runtime.rest.resources.RootResource registered in SERVER runtime does not implement any provider interfaces applicable in the SERVER runtime. Due to constraint configuration problems the provider org.apache.kafka.connect.runtime.rest.resources.RootResource will be ignored. 
[36mconnect_1             |[0m Aug 20, 2020 1:08:13 AM org.glassfish.jersey.internal.inject.Providers checkProviderRuntime
[36mconnect_1             |[0m WARNING: A provider org.apache.kafka.connect.runtime.rest.resources.ConnectorPluginsResource registered in SERVER runtime does not implement any provider interfaces applicable in the SERVER runtime. Due to constraint configuration problems the provider org.apache.kafka.connect.runtime.rest.resources.ConnectorPluginsResource will be ignored. 
[36mconnect_1             |[0m Aug 20, 2020 1:08:13 AM org.glassfish.jersey.internal.inject.Providers checkProviderRuntime
[36mconnect_1             |[0m WARNING: A provider org.apache.kafka.connect.runtime.rest.resources.ConnectorsResource registered in SERVER runtime does not implement any provider interfaces applicable in the SERVER runtime. Due to constraint configuration problems the provider org.apache.kafka.connect.runtime.rest.resources.ConnectorsResource will be ignored. 
[36mconnect_1             |[0m [2020-08-20 01:08:13,402] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Subscribed to partition(s): connect-offset-0, connect-offset-5, connect-offset-10, connect-offset-20, connect-offset-15, connect-offset-9, connect-offset-11, connect-offset-4, connect-offset-16, connect-offset-17, connect-offset-3, connect-offset-24, connect-offset-23, connect-offset-13, connect-offset-18, connect-offset-22, connect-offset-2, connect-offset-8, connect-offset-12, connect-offset-19, connect-offset-14, connect-offset-1, connect-offset-6, connect-offset-7, connect-offset-21 (org.apache.kafka.clients.consumer.KafkaConsumer)
[36mconnect_1             |[0m [2020-08-20 01:08:13,409] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-0 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,410] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-5 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,415] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-10 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,415] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-20 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,415] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-15 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,416] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-9 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,416] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-11 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,416] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-4 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,416] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-16 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,416] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-17 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,416] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-3 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,417] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-24 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,417] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-23 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,417] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-13 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,417] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-18 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,417] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-22 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,417] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-2 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,418] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-8 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,418] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-12 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,418] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-19 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,418] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-14 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,418] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-1 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,418] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-6 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,419] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-7 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,419] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Seeking to EARLIEST offset of partition connect-offset-21 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,512] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-0 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,513] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-2 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,513] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-4 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,513] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-6 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-16 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-18 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-20 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-22 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-8 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-10 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-12 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-14 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-1 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-3 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-5 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-7 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,514] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-24 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,515] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-17 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,515] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-19 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,515] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-21 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,515] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-23 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,515] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-9 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,515] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-11 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,515] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-13 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,515] INFO [Consumer clientId=consumer-connect-1, groupId=connect] Resetting offset for partition connect-offset-15 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,522] INFO Finished reading KafkaBasedLog for topic connect-offset (org.apache.kafka.connect.util.KafkaBasedLog)
[36mconnect_1             |[0m [2020-08-20 01:08:13,522] INFO Started KafkaBasedLog for topic connect-offset (org.apache.kafka.connect.util.KafkaBasedLog)
[36mconnect_1             |[0m [2020-08-20 01:08:13,522] INFO Finished reading offsets topic and starting KafkaOffsetBackingStore (org.apache.kafka.connect.storage.KafkaOffsetBackingStore)
[36mconnect_1             |[0m [2020-08-20 01:08:13,529] INFO Worker started (org.apache.kafka.connect.runtime.Worker)
[36mconnect_1             |[0m [2020-08-20 01:08:13,529] INFO Starting KafkaBasedLog with topic connect-status (org.apache.kafka.connect.util.KafkaBasedLog)
[36mconnect_1             |[0m [2020-08-20 01:08:13,529] INFO AdminClientConfig values: 
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = 
[36mconnect_1             |[0m 	connections.max.idle.ms = 300000
[36mconnect_1             |[0m 	default.api.timeout.ms = 60000
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	receive.buffer.bytes = 65536
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 30000
[36mconnect_1             |[0m 	retries = 2147483647
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m  (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'config.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'rest.advertised.host.name' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'status.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'group.id' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'plugin.path' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'internal.key.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'config.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'rest.port' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'internal.key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'value.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'internal.value.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'status.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'internal.value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'offset.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'offset.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] WARN The configuration 'key.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,536] INFO Kafka startTimeMs: 1597885693536 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,784] INFO Created topic (name=connect-status, numPartitions=5, replicationFactor=1, replicasAssignments=null, configs={cleanup.policy=compact}) on brokers at PLAINTEXT://kafka0:19092 (org.apache.kafka.connect.util.TopicAdmin)
[36mconnect_1             |[0m [2020-08-20 01:08:13,789] INFO ProducerConfig values: 
[36mconnect_1             |[0m 	acks = -1
[36mconnect_1             |[0m 	batch.size = 16384
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	buffer.memory = 33554432
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = producer-2
[36mconnect_1             |[0m 	compression.type = none
[36mconnect_1             |[0m 	connections.max.idle.ms = 540000
[36mconnect_1             |[0m 	delivery.timeout.ms = 120000
[36mconnect_1             |[0m 	enable.idempotence = false
[36mconnect_1             |[0m 	interceptor.classes = []
[36mconnect_1             |[0m 	key.serializer = class org.apache.kafka.common.serialization.StringSerializer
[36mconnect_1             |[0m 	linger.ms = 0
[36mconnect_1             |[0m 	max.block.ms = 60000
[36mconnect_1             |[0m 	max.in.flight.requests.per.connection = 1
[36mconnect_1             |[0m 	max.request.size = 1048576
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metadata.max.idle.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	partitioner.class = class org.apache.kafka.clients.producer.internals.DefaultPartitioner
[36mconnect_1             |[0m 	receive.buffer.bytes = 32768
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 30000
[36mconnect_1             |[0m 	retries = 0
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m 	transaction.timeout.ms = 60000
[36mconnect_1             |[0m 	transactional.id = null
[36mconnect_1             |[0m 	value.serializer = class org.apache.kafka.common.serialization.ByteArraySerializer
[36mconnect_1             |[0m  (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,805] WARN The configuration 'group.id' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,805] WARN The configuration 'plugin.path' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,806] WARN The configuration 'internal.key.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,806] WARN The configuration 'status.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,807] WARN The configuration 'offset.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,807] WARN The configuration 'value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,807] WARN The configuration 'key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,808] WARN The configuration 'config.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,808] WARN The configuration 'rest.advertised.host.name' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,808] WARN The configuration 'status.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,809] WARN The configuration 'config.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,809] WARN The configuration 'rest.port' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,809] WARN The configuration 'internal.key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,810] WARN The configuration 'value.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,810] WARN The configuration 'internal.value.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,810] WARN The configuration 'internal.value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,811] WARN The configuration 'offset.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,811] WARN The configuration 'key.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,812] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,812] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,813] INFO Kafka startTimeMs: 1597885693812 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,818] INFO ConsumerConfig values: 
[36mconnect_1             |[0m 	allow.auto.create.topics = true
[36mconnect_1             |[0m 	auto.commit.interval.ms = 5000
[36mconnect_1             |[0m 	auto.offset.reset = earliest
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	check.crcs = true
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = 
[36mconnect_1             |[0m 	client.rack = 
[36mconnect_1             |[0m 	connections.max.idle.ms = 540000
[36mconnect_1             |[0m 	default.api.timeout.ms = 60000
[36mconnect_1             |[0m 	enable.auto.commit = false
[36mconnect_1             |[0m 	exclude.internal.topics = true
[36mconnect_1             |[0m 	fetch.max.bytes = 52428800
[36mconnect_1             |[0m 	fetch.max.wait.ms = 500
[36mconnect_1             |[0m 	fetch.min.bytes = 1
[36mconnect_1             |[0m 	group.id = connect
[36mconnect_1             |[0m 	group.instance.id = null
[36mconnect_1             |[0m 	heartbeat.interval.ms = 3000
[36mconnect_1             |[0m 	interceptor.classes = []
[36mconnect_1             |[0m 	internal.leave.group.on.close = true
[36mconnect_1             |[0m 	isolation.level = read_uncommitted
[36mconnect_1             |[0m 	key.deserializer = class org.apache.kafka.common.serialization.StringDeserializer
[36mconnect_1             |[0m 	max.partition.fetch.bytes = 1048576
[36mconnect_1             |[0m 	max.poll.interval.ms = 300000
[36mconnect_1             |[0m 	max.poll.records = 500
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	partition.assignment.strategy = [class org.apache.kafka.clients.consumer.RangeAssignor]
[36mconnect_1             |[0m 	receive.buffer.bytes = 65536
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 30000
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	session.timeout.ms = 10000
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m 	value.deserializer = class org.apache.kafka.common.serialization.ByteArrayDeserializer
[36mconnect_1             |[0m  (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,831] INFO [Producer clientId=producer-2] Cluster ID: 40eSduN2R46UaeWXQ6fOrQ (org.apache.kafka.clients.Metadata)
[36mconnect_1             |[0m [2020-08-20 01:08:13,860] WARN The configuration 'config.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,863] WARN The configuration 'rest.advertised.host.name' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,864] WARN The configuration 'status.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,864] WARN The configuration 'plugin.path' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,864] WARN The configuration 'internal.key.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,865] WARN The configuration 'config.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,865] WARN The configuration 'rest.port' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,866] WARN The configuration 'internal.key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,866] WARN The configuration 'value.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,867] WARN The configuration 'internal.value.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,867] WARN The configuration 'status.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,867] WARN The configuration 'internal.value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,868] WARN The configuration 'offset.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,868] WARN The configuration 'offset.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,869] WARN The configuration 'value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,869] WARN The configuration 'key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,870] WARN The configuration 'key.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,870] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,871] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,871] INFO Kafka startTimeMs: 1597885693870 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m Aug 20, 2020 1:08:13 AM org.glassfish.jersey.internal.Errors logErrors
[36mconnect_1             |[0m WARNING: The following warnings have been detected: WARNING: The (sub)resource method listLoggers in org.apache.kafka.connect.runtime.rest.resources.LoggingResource contains empty path annotation.
[36mconnect_1             |[0m WARNING: The (sub)resource method listConnectors in org.apache.kafka.connect.runtime.rest.resources.ConnectorsResource contains empty path annotation.
[36mconnect_1             |[0m WARNING: The (sub)resource method createConnector in org.apache.kafka.connect.runtime.rest.resources.ConnectorsResource contains empty path annotation.
[36mconnect_1             |[0m WARNING: The (sub)resource method listConnectorPlugins in org.apache.kafka.connect.runtime.rest.resources.ConnectorPluginsResource contains empty path annotation.
[36mconnect_1             |[0m WARNING: The (sub)resource method serverInfo in org.apache.kafka.connect.runtime.rest.resources.RootResource contains empty path annotation.
[36mconnect_1             |[0m 
[36mconnect_1             |[0m [2020-08-20 01:08:13,879] INFO Started o.e.j.s.ServletContextHandler@5e8372b8{/,null,AVAILABLE} (org.eclipse.jetty.server.handler.ContextHandler)
[36mconnect_1             |[0m [2020-08-20 01:08:13,879] INFO REST resources initialized; server is started and ready to handle requests (org.apache.kafka.connect.runtime.rest.RestServer)
[36mconnect_1             |[0m [2020-08-20 01:08:13,879] INFO Kafka Connect started (org.apache.kafka.connect.runtime.Connect)
[36mconnect_1             |[0m [2020-08-20 01:08:13,888] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Cluster ID: 40eSduN2R46UaeWXQ6fOrQ (org.apache.kafka.clients.Metadata)
[36mconnect_1             |[0m [2020-08-20 01:08:13,908] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Subscribed to partition(s): connect-status-0, connect-status-4, connect-status-1, connect-status-2, connect-status-3 (org.apache.kafka.clients.consumer.KafkaConsumer)
[36mconnect_1             |[0m [2020-08-20 01:08:13,908] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Seeking to EARLIEST offset of partition connect-status-0 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,909] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Seeking to EARLIEST offset of partition connect-status-4 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,909] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Seeking to EARLIEST offset of partition connect-status-1 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,909] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Seeking to EARLIEST offset of partition connect-status-2 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,909] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Seeking to EARLIEST offset of partition connect-status-3 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,931] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Resetting offset for partition connect-status-1 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,931] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Resetting offset for partition connect-status-2 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,931] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Resetting offset for partition connect-status-0 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,931] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Resetting offset for partition connect-status-3 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,932] INFO [Consumer clientId=consumer-connect-2, groupId=connect] Resetting offset for partition connect-status-4 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:13,932] INFO Finished reading KafkaBasedLog for topic connect-status (org.apache.kafka.connect.util.KafkaBasedLog)
[36mconnect_1             |[0m [2020-08-20 01:08:13,932] INFO Started KafkaBasedLog for topic connect-status (org.apache.kafka.connect.util.KafkaBasedLog)
[36mconnect_1             |[0m [2020-08-20 01:08:13,933] INFO Starting KafkaConfigBackingStore (org.apache.kafka.connect.storage.KafkaConfigBackingStore)
[36mconnect_1             |[0m [2020-08-20 01:08:13,933] INFO Starting KafkaBasedLog with topic connect-config (org.apache.kafka.connect.util.KafkaBasedLog)
[36mconnect_1             |[0m [2020-08-20 01:08:13,934] INFO AdminClientConfig values: 
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = 
[36mconnect_1             |[0m 	connections.max.idle.ms = 300000
[36mconnect_1             |[0m 	default.api.timeout.ms = 60000
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	receive.buffer.bytes = 65536
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 30000
[36mconnect_1             |[0m 	retries = 2147483647
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m  (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,937] WARN The configuration 'config.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,937] WARN The configuration 'rest.advertised.host.name' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,937] WARN The configuration 'status.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,937] WARN The configuration 'group.id' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,937] WARN The configuration 'plugin.path' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,938] WARN The configuration 'internal.key.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,938] WARN The configuration 'config.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,938] WARN The configuration 'rest.port' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,938] WARN The configuration 'internal.key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,938] WARN The configuration 'value.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,939] WARN The configuration 'internal.value.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,939] WARN The configuration 'status.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,939] WARN The configuration 'internal.value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,939] WARN The configuration 'offset.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,939] WARN The configuration 'offset.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,939] WARN The configuration 'value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,940] WARN The configuration 'key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,940] WARN The configuration 'key.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.admin.AdminClientConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:13,940] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,940] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:13,940] INFO Kafka startTimeMs: 1597885693940 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:14,023] INFO Created topic (name=connect-config, numPartitions=1, replicationFactor=1, replicasAssignments=null, configs={cleanup.policy=compact}) on brokers at PLAINTEXT://kafka0:19092 (org.apache.kafka.connect.util.TopicAdmin)
[36mconnect_1             |[0m [2020-08-20 01:08:14,029] INFO ProducerConfig values: 
[36mconnect_1             |[0m 	acks = -1
[36mconnect_1             |[0m 	batch.size = 16384
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	buffer.memory = 33554432
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = producer-3
[36mconnect_1             |[0m 	compression.type = none
[36mconnect_1             |[0m 	connections.max.idle.ms = 540000
[36mconnect_1             |[0m 	delivery.timeout.ms = 2147483647
[36mconnect_1             |[0m 	enable.idempotence = false
[36mconnect_1             |[0m 	interceptor.classes = []
[36mconnect_1             |[0m 	key.serializer = class org.apache.kafka.common.serialization.StringSerializer
[36mconnect_1             |[0m 	linger.ms = 0
[36mconnect_1             |[0m 	max.block.ms = 60000
[36mconnect_1             |[0m 	max.in.flight.requests.per.connection = 1
[36mconnect_1             |[0m 	max.request.size = 1048576
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metadata.max.idle.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	partitioner.class = class org.apache.kafka.clients.producer.internals.DefaultPartitioner
[36mconnect_1             |[0m 	receive.buffer.bytes = 32768
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 30000
[36mconnect_1             |[0m 	retries = 2147483647
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m 	transaction.timeout.ms = 60000
[36mconnect_1             |[0m 	transactional.id = null
[36mconnect_1             |[0m 	value.serializer = class org.apache.kafka.common.serialization.ByteArraySerializer
[36mconnect_1             |[0m  (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,037] WARN The configuration 'group.id' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,038] WARN The configuration 'plugin.path' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,039] WARN The configuration 'internal.key.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,039] WARN The configuration 'status.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,039] WARN The configuration 'offset.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,039] WARN The configuration 'value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,039] WARN The configuration 'key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,039] WARN The configuration 'config.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,039] WARN The configuration 'rest.advertised.host.name' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,039] WARN The configuration 'status.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,040] WARN The configuration 'config.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,040] WARN The configuration 'rest.port' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,040] WARN The configuration 'internal.key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,040] WARN The configuration 'value.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,040] WARN The configuration 'internal.value.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,040] WARN The configuration 'internal.value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,041] WARN The configuration 'offset.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,041] WARN The configuration 'key.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,041] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:14,042] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:14,042] INFO Kafka startTimeMs: 1597885694041 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:14,043] INFO ConsumerConfig values: 
[36mconnect_1             |[0m 	allow.auto.create.topics = true
[36mconnect_1             |[0m 	auto.commit.interval.ms = 5000
[36mconnect_1             |[0m 	auto.offset.reset = earliest
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	check.crcs = true
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = 
[36mconnect_1             |[0m 	client.rack = 
[36mconnect_1             |[0m 	connections.max.idle.ms = 540000
[36mconnect_1             |[0m 	default.api.timeout.ms = 60000
[36mconnect_1             |[0m 	enable.auto.commit = false
[36mconnect_1             |[0m 	exclude.internal.topics = true
[36mconnect_1             |[0m 	fetch.max.bytes = 52428800
[36mconnect_1             |[0m 	fetch.max.wait.ms = 500
[36mconnect_1             |[0m 	fetch.min.bytes = 1
[36mconnect_1             |[0m 	group.id = connect
[36mconnect_1             |[0m 	group.instance.id = null
[36mconnect_1             |[0m 	heartbeat.interval.ms = 3000
[36mconnect_1             |[0m 	interceptor.classes = []
[36mconnect_1             |[0m 	internal.leave.group.on.close = true
[36mconnect_1             |[0m 	isolation.level = read_uncommitted
[36mconnect_1             |[0m 	key.deserializer = class org.apache.kafka.common.serialization.StringDeserializer
[36mconnect_1             |[0m 	max.partition.fetch.bytes = 1048576
[36mconnect_1             |[0m 	max.poll.interval.ms = 300000
[36mconnect_1             |[0m 	max.poll.records = 500
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	partition.assignment.strategy = [class org.apache.kafka.clients.consumer.RangeAssignor]
[36mconnect_1             |[0m 	receive.buffer.bytes = 65536
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 30000
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	session.timeout.ms = 10000
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m 	value.deserializer = class org.apache.kafka.common.serialization.ByteArrayDeserializer
[36mconnect_1             |[0m  (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,053] WARN The configuration 'config.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,053] WARN The configuration 'rest.advertised.host.name' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,053] WARN The configuration 'status.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,054] WARN The configuration 'plugin.path' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,054] WARN The configuration 'internal.key.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,054] WARN The configuration 'config.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,054] WARN The configuration 'rest.port' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,054] INFO [Producer clientId=producer-3] Cluster ID: 40eSduN2R46UaeWXQ6fOrQ (org.apache.kafka.clients.Metadata)
[36mconnect_1             |[0m [2020-08-20 01:08:14,054] WARN The configuration 'internal.key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,066] WARN The configuration 'value.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,066] WARN The configuration 'internal.value.converter.schemas.enable' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,066] WARN The configuration 'status.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,066] WARN The configuration 'internal.value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,066] WARN The configuration 'offset.storage.replication.factor' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,066] WARN The configuration 'offset.storage.topic' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,066] WARN The configuration 'value.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,066] WARN The configuration 'key.converter' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,066] WARN The configuration 'key.converter.schema.registry.url' was supplied but isn't a known config. (org.apache.kafka.clients.consumer.ConsumerConfig)
[36mconnect_1             |[0m [2020-08-20 01:08:14,066] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:14,067] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:14,067] INFO Kafka startTimeMs: 1597885694066 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:08:14,080] INFO [Consumer clientId=consumer-connect-3, groupId=connect] Cluster ID: 40eSduN2R46UaeWXQ6fOrQ (org.apache.kafka.clients.Metadata)
[36mconnect_1             |[0m [2020-08-20 01:08:14,095] INFO [Consumer clientId=consumer-connect-3, groupId=connect] Subscribed to partition(s): connect-config-0 (org.apache.kafka.clients.consumer.KafkaConsumer)
[36mconnect_1             |[0m [2020-08-20 01:08:14,096] INFO [Consumer clientId=consumer-connect-3, groupId=connect] Seeking to EARLIEST offset of partition connect-config-0 (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:14,121] INFO [Consumer clientId=consumer-connect-3, groupId=connect] Resetting offset for partition connect-config-0 to offset 0. (org.apache.kafka.clients.consumer.internals.SubscriptionState)
[36mconnect_1             |[0m [2020-08-20 01:08:14,142] INFO Finished reading KafkaBasedLog for topic connect-config (org.apache.kafka.connect.util.KafkaBasedLog)
[36mconnect_1             |[0m [2020-08-20 01:08:14,142] INFO Started KafkaBasedLog for topic connect-config (org.apache.kafka.connect.util.KafkaBasedLog)
[36mconnect_1             |[0m [2020-08-20 01:08:14,142] INFO Started KafkaConfigBackingStore (org.apache.kafka.connect.storage.KafkaConfigBackingStore)
[36mconnect_1             |[0m [2020-08-20 01:08:14,142] INFO [Worker clientId=connect-1, groupId=connect] Herder started (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:08:14,183] INFO [Worker clientId=connect-1, groupId=connect] Cluster ID: 40eSduN2R46UaeWXQ6fOrQ (org.apache.kafka.clients.Metadata)
[36mconnect_1             |[0m [2020-08-20 01:08:14,185] INFO [Worker clientId=connect-1, groupId=connect] Discovered group coordinator kafka0:19092 (id: 2147483647 rack: null) (org.apache.kafka.clients.consumer.internals.AbstractCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:08:14,187] INFO [Worker clientId=connect-1, groupId=connect] Rebalance started (org.apache.kafka.connect.runtime.distributed.WorkerCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:08:14,190] INFO [Worker clientId=connect-1, groupId=connect] (Re-)joining group (org.apache.kafka.clients.consumer.internals.AbstractCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:08:14,215] INFO [Worker clientId=connect-1, groupId=connect] Join group failed with org.apache.kafka.common.errors.MemberIdRequiredException: The group member needs to have a valid member id before actually entering a consumer group (org.apache.kafka.clients.consumer.internals.AbstractCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:08:14,215] INFO [Worker clientId=connect-1, groupId=connect] (Re-)joining group (org.apache.kafka.clients.consumer.internals.AbstractCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:08:17,291] INFO [Worker clientId=connect-1, groupId=connect] Successfully joined group with generation 1 (org.apache.kafka.clients.consumer.internals.AbstractCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:08:17,292] INFO [Worker clientId=connect-1, groupId=connect] Joined group at generation 1 with protocol version 2 and got assignment: Assignment{error=0, leader='connect-1-5a08990f-63f2-4d31-8199-0e1f16ca3836', leaderUrl='http://connect:8083/', offset=-1, connectorIds=[], taskIds=[], revokedConnectorIds=[], revokedTaskIds=[], delay=0} with rebalance delay: 0 (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:08:17,294] INFO [Worker clientId=connect-1, groupId=connect] Starting connectors and tasks using config offset -1 (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:08:17,294] INFO [Worker clientId=connect-1, groupId=connect] Finished starting connectors and tasks (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:08:17,390] INFO [Worker clientId=connect-1, groupId=connect] Session key updated (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:10:05,260] INFO JVM Runtime does not support Modules (org.eclipse.jetty.util.TypeUtil)
[36mconnect_1             |[0m [2020-08-20 01:12:47,870] INFO AbstractConfig values: 
[36mconnect_1             |[0m 	batch.max.rows = 500
[36mconnect_1             |[0m 	catalog.pattern = null
[36mconnect_1             |[0m 	connection.attempts = 3
[36mconnect_1             |[0m 	connection.backoff.ms = 10000
[36mconnect_1             |[0m 	connection.password = [hidden]
[36mconnect_1             |[0m 	connection.url = jdbc:postgresql://postgres:5432/cta
[36mconnect_1             |[0m 	connection.user = cta_admin
[36mconnect_1             |[0m 	db.timezone = UTC
[36mconnect_1             |[0m 	dialect.name = 
[36mconnect_1             |[0m 	incrementing.column.name = stop_id
[36mconnect_1             |[0m 	mode = incrementing
[36mconnect_1             |[0m 	numeric.mapping = null
[36mconnect_1             |[0m 	numeric.precision.mapping = false
[36mconnect_1             |[0m 	poll.interval.ms = 3600000
[36mconnect_1             |[0m 	query = 
[36mconnect_1             |[0m 	query.suffix = 
[36mconnect_1             |[0m 	quote.sql.identifiers = ALWAYS
[36mconnect_1             |[0m 	schema.pattern = null
[36mconnect_1             |[0m 	table.blacklist = []
[36mconnect_1             |[0m 	table.poll.interval.ms = 60000
[36mconnect_1             |[0m 	table.types = [TABLE]
[36mconnect_1             |[0m 	table.whitelist = [stations]
[36mconnect_1             |[0m 	timestamp.column.name = []
[36mconnect_1             |[0m 	timestamp.delay.interval.ms = 0
[36mconnect_1             |[0m 	timestamp.initial = null
[36mconnect_1             |[0m 	topic.prefix = chicago-transit.connect-
[36mconnect_1             |[0m 	validate.non.null = true
[36mconnect_1             |[0m  (org.apache.kafka.common.config.AbstractConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:48,002] INFO AbstractConfig values: 
[36mconnect_1             |[0m  (org.apache.kafka.common.config.AbstractConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:48,011] INFO [Worker clientId=connect-1, groupId=connect] Connector stations config updated (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:12:48,514] INFO [Worker clientId=connect-1, groupId=connect] Rebalance started (org.apache.kafka.connect.runtime.distributed.WorkerCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:12:48,514] INFO [Worker clientId=connect-1, groupId=connect] (Re-)joining group (org.apache.kafka.clients.consumer.internals.AbstractCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:12:48,542] INFO [Worker clientId=connect-1, groupId=connect] Successfully joined group with generation 2 (org.apache.kafka.clients.consumer.internals.AbstractCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:12:48,543] INFO [Worker clientId=connect-1, groupId=connect] Joined group at generation 2 with protocol version 2 and got assignment: Assignment{error=0, leader='connect-1-5a08990f-63f2-4d31-8199-0e1f16ca3836', leaderUrl='http://connect:8083/', offset=2, connectorIds=[stations], taskIds=[], revokedConnectorIds=[], revokedTaskIds=[], delay=0} with rebalance delay: 0 (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:12:48,546] INFO [Worker clientId=connect-1, groupId=connect] Starting connectors and tasks using config offset 2 (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:12:48,557] INFO [Worker clientId=connect-1, groupId=connect] Starting connector stations (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:12:48,571] INFO ConnectorConfig values: 
[36mconnect_1             |[0m 	config.action.reload = restart
[36mconnect_1             |[0m 	connector.class = io.confluent.connect.jdbc.JdbcSourceConnector
[36mconnect_1             |[0m 	errors.log.enable = false
[36mconnect_1             |[0m 	errors.log.include.messages = false
[36mconnect_1             |[0m 	errors.retry.delay.max.ms = 60000
[36mconnect_1             |[0m 	errors.retry.timeout = 0
[36mconnect_1             |[0m 	errors.tolerance = none
[36mconnect_1             |[0m 	header.converter = null
[36mconnect_1             |[0m 	key.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m 	name = stations
[36mconnect_1             |[0m 	tasks.max = 1
[36mconnect_1             |[0m 	transforms = []
[36mconnect_1             |[0m 	value.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m  (org.apache.kafka.connect.runtime.ConnectorConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:48,572] INFO EnrichedConnectorConfig values: 
[36mconnect_1             |[0m 	config.action.reload = restart
[36mconnect_1             |[0m 	connector.class = io.confluent.connect.jdbc.JdbcSourceConnector
[36mconnect_1             |[0m 	errors.log.enable = false
[36mconnect_1             |[0m 	errors.log.include.messages = false
[36mconnect_1             |[0m 	errors.retry.delay.max.ms = 60000
[36mconnect_1             |[0m 	errors.retry.timeout = 0
[36mconnect_1             |[0m 	errors.tolerance = none
[36mconnect_1             |[0m 	header.converter = null
[36mconnect_1             |[0m 	key.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m 	name = stations
[36mconnect_1             |[0m 	tasks.max = 1
[36mconnect_1             |[0m 	transforms = []
[36mconnect_1             |[0m 	value.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m  (org.apache.kafka.connect.runtime.ConnectorConfig$EnrichedConnectorConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:48,572] INFO Creating connector stations of type io.confluent.connect.jdbc.JdbcSourceConnector (org.apache.kafka.connect.runtime.Worker)
[36mconnect_1             |[0m [2020-08-20 01:12:48,586] INFO Instantiated connector stations with version 5.5.1 of type class io.confluent.connect.jdbc.JdbcSourceConnector (org.apache.kafka.connect.runtime.Worker)
[36mconnect_1             |[0m [2020-08-20 01:12:48,588] INFO Starting JDBC Source Connector (io.confluent.connect.jdbc.JdbcSourceConnector)
[36mconnect_1             |[0m [2020-08-20 01:12:48,590] INFO JdbcSourceConnectorConfig values: 
[36mconnect_1             |[0m 	batch.max.rows = 500
[36mconnect_1             |[0m 	catalog.pattern = null
[36mconnect_1             |[0m 	connection.attempts = 3
[36mconnect_1             |[0m 	connection.backoff.ms = 10000
[36mconnect_1             |[0m 	connection.password = [hidden]
[36mconnect_1             |[0m 	connection.url = jdbc:postgresql://postgres:5432/cta
[36mconnect_1             |[0m 	connection.user = cta_admin
[36mconnect_1             |[0m 	db.timezone = UTC
[36mconnect_1             |[0m 	dialect.name = 
[36mconnect_1             |[0m 	incrementing.column.name = stop_id
[36mconnect_1             |[0m 	mode = incrementing
[36mconnect_1             |[0m 	numeric.mapping = null
[36mconnect_1             |[0m 	numeric.precision.mapping = false
[36mconnect_1             |[0m 	poll.interval.ms = 3600000
[36mconnect_1             |[0m 	query = 
[36mconnect_1             |[0m 	query.suffix = 
[36mconnect_1             |[0m 	quote.sql.identifiers = ALWAYS
[36mconnect_1             |[0m 	schema.pattern = null
[36mconnect_1             |[0m 	table.blacklist = []
[36mconnect_1             |[0m 	table.poll.interval.ms = 60000
[36mconnect_1             |[0m 	table.types = [TABLE]
[36mconnect_1             |[0m 	table.whitelist = [stations]
[36mconnect_1             |[0m 	timestamp.column.name = []
[36mconnect_1             |[0m 	timestamp.delay.interval.ms = 0
[36mconnect_1             |[0m 	timestamp.initial = null
[36mconnect_1             |[0m 	topic.prefix = chicago-transit.connect-
[36mconnect_1             |[0m 	validate.non.null = true
[36mconnect_1             |[0m  (io.confluent.connect.jdbc.source.JdbcSourceConnectorConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:48,592] INFO Attempting to open connection #1 to PostgreSql (io.confluent.connect.jdbc.util.CachedConnectionProvider)
[36mconnect_1             |[0m [2020-08-20 01:12:48,614] INFO Starting thread to monitor tables. (io.confluent.connect.jdbc.source.TableMonitorThread)
[36mconnect_1             |[0m [2020-08-20 01:12:48,652] INFO Finished creating connector stations (org.apache.kafka.connect.runtime.Worker)
[36mconnect_1             |[0m [2020-08-20 01:12:48,657] INFO SourceConnectorConfig values: 
[36mconnect_1             |[0m 	config.action.reload = restart
[36mconnect_1             |[0m 	connector.class = io.confluent.connect.jdbc.JdbcSourceConnector
[36mconnect_1             |[0m 	errors.log.enable = false
[36mconnect_1             |[0m 	errors.log.include.messages = false
[36mconnect_1             |[0m 	errors.retry.delay.max.ms = 60000
[36mconnect_1             |[0m 	errors.retry.timeout = 0
[36mconnect_1             |[0m 	errors.tolerance = none
[36mconnect_1             |[0m 	header.converter = null
[36mconnect_1             |[0m 	key.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m 	name = stations
[36mconnect_1             |[0m 	tasks.max = 1
[36mconnect_1             |[0m 	transforms = []
[36mconnect_1             |[0m 	value.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m  (org.apache.kafka.connect.runtime.SourceConnectorConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:48,666] INFO EnrichedConnectorConfig values: 
[36mconnect_1             |[0m 	config.action.reload = restart
[36mconnect_1             |[0m 	connector.class = io.confluent.connect.jdbc.JdbcSourceConnector
[36mconnect_1             |[0m 	errors.log.enable = false
[36mconnect_1             |[0m 	errors.log.include.messages = false
[36mconnect_1             |[0m 	errors.retry.delay.max.ms = 60000
[36mconnect_1             |[0m 	errors.retry.timeout = 0
[36mconnect_1             |[0m 	errors.tolerance = none
[36mconnect_1             |[0m 	header.converter = null
[36mconnect_1             |[0m 	key.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m 	name = stations
[36mconnect_1             |[0m 	tasks.max = 1
[36mconnect_1             |[0m 	transforms = []
[36mconnect_1             |[0m 	value.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m  (org.apache.kafka.connect.runtime.ConnectorConfig$EnrichedConnectorConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:49,559] INFO [Worker clientId=connect-1, groupId=connect] Tasks [stations-0] configs updated (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:12:49,565] INFO [Worker clientId=connect-1, groupId=connect] Finished starting connectors and tasks (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:12:49,578] INFO [Worker clientId=connect-1, groupId=connect] Handling task config update by restarting tasks [] (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:12:49,582] INFO [Worker clientId=connect-1, groupId=connect] Rebalance started (org.apache.kafka.connect.runtime.distributed.WorkerCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:12:49,582] INFO [Worker clientId=connect-1, groupId=connect] (Re-)joining group (org.apache.kafka.clients.consumer.internals.AbstractCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:12:49,616] INFO [Worker clientId=connect-1, groupId=connect] Successfully joined group with generation 3 (org.apache.kafka.clients.consumer.internals.AbstractCoordinator)
[36mconnect_1             |[0m [2020-08-20 01:12:49,616] INFO [Worker clientId=connect-1, groupId=connect] Joined group at generation 3 with protocol version 2 and got assignment: Assignment{error=0, leader='connect-1-5a08990f-63f2-4d31-8199-0e1f16ca3836', leaderUrl='http://connect:8083/', offset=4, connectorIds=[stations], taskIds=[stations-0], revokedConnectorIds=[], revokedTaskIds=[], delay=0} with rebalance delay: 0 (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:12:49,621] INFO [Worker clientId=connect-1, groupId=connect] Starting connectors and tasks using config offset 4 (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:12:49,630] INFO [Worker clientId=connect-1, groupId=connect] Starting task stations-0 (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:12:49,631] INFO Creating task stations-0 (org.apache.kafka.connect.runtime.Worker)
[36mconnect_1             |[0m [2020-08-20 01:12:49,634] INFO ConnectorConfig values: 
[36mconnect_1             |[0m 	config.action.reload = restart
[36mconnect_1             |[0m 	connector.class = io.confluent.connect.jdbc.JdbcSourceConnector
[36mconnect_1             |[0m 	errors.log.enable = false
[36mconnect_1             |[0m 	errors.log.include.messages = false
[36mconnect_1             |[0m 	errors.retry.delay.max.ms = 60000
[36mconnect_1             |[0m 	errors.retry.timeout = 0
[36mconnect_1             |[0m 	errors.tolerance = none
[36mconnect_1             |[0m 	header.converter = null
[36mconnect_1             |[0m 	key.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m 	name = stations
[36mconnect_1             |[0m 	tasks.max = 1
[36mconnect_1             |[0m 	transforms = []
[36mconnect_1             |[0m 	value.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m  (org.apache.kafka.connect.runtime.ConnectorConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:49,638] INFO EnrichedConnectorConfig values: 
[36mconnect_1             |[0m 	config.action.reload = restart
[36mconnect_1             |[0m 	connector.class = io.confluent.connect.jdbc.JdbcSourceConnector
[36mconnect_1             |[0m 	errors.log.enable = false
[36mconnect_1             |[0m 	errors.log.include.messages = false
[36mconnect_1             |[0m 	errors.retry.delay.max.ms = 60000
[36mconnect_1             |[0m 	errors.retry.timeout = 0
[36mconnect_1             |[0m 	errors.tolerance = none
[36mconnect_1             |[0m 	header.converter = null
[36mconnect_1             |[0m 	key.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m 	name = stations
[36mconnect_1             |[0m 	tasks.max = 1
[36mconnect_1             |[0m 	transforms = []
[36mconnect_1             |[0m 	value.converter = class org.apache.kafka.connect.json.JsonConverter
[36mconnect_1             |[0m  (org.apache.kafka.connect.runtime.ConnectorConfig$EnrichedConnectorConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:49,641] INFO TaskConfig values: 
[36mconnect_1             |[0m 	task.class = class io.confluent.connect.jdbc.source.JdbcSourceTask
[36mconnect_1             |[0m  (org.apache.kafka.connect.runtime.TaskConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:49,644] INFO Instantiated task stations-0 with version 5.5.1 of type io.confluent.connect.jdbc.source.JdbcSourceTask (org.apache.kafka.connect.runtime.Worker)
[36mconnect_1             |[0m [2020-08-20 01:12:49,644] INFO JsonConverterConfig values: 
[36mconnect_1             |[0m 	converter.type = key
[36mconnect_1             |[0m 	decimal.format = BASE64
[36mconnect_1             |[0m 	schemas.cache.size = 1000
[36mconnect_1             |[0m 	schemas.enable = false
[36mconnect_1             |[0m  (org.apache.kafka.connect.json.JsonConverterConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:49,645] INFO JsonConverterConfig values: 
[36mconnect_1             |[0m 	converter.type = value
[36mconnect_1             |[0m 	decimal.format = BASE64
[36mconnect_1             |[0m 	schemas.cache.size = 1000
[36mconnect_1             |[0m 	schemas.enable = false
[36mconnect_1             |[0m  (org.apache.kafka.connect.json.JsonConverterConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:49,646] INFO Set up the key converter class org.apache.kafka.connect.json.JsonConverter for task stations-0 using the connector config (org.apache.kafka.connect.runtime.Worker)
[36mconnect_1             |[0m [2020-08-20 01:12:49,646] INFO Set up the value converter class org.apache.kafka.connect.json.JsonConverter for task stations-0 using the connector config (org.apache.kafka.connect.runtime.Worker)
[36mconnect_1             |[0m [2020-08-20 01:12:49,646] INFO Set up the header converter class org.apache.kafka.connect.storage.SimpleHeaderConverter for task stations-0 using the worker config (org.apache.kafka.connect.runtime.Worker)
[36mconnect_1             |[0m [2020-08-20 01:12:49,657] INFO Initializing: org.apache.kafka.connect.runtime.TransformationChain{} (org.apache.kafka.connect.runtime.Worker)
[36mconnect_1             |[0m [2020-08-20 01:12:49,661] INFO ProducerConfig values: 
[36mconnect_1             |[0m 	acks = -1
[36mconnect_1             |[0m 	batch.size = 16384
[36mconnect_1             |[0m 	bootstrap.servers = [PLAINTEXT://kafka0:19092]
[36mconnect_1             |[0m 	buffer.memory = 33554432
[36mconnect_1             |[0m 	client.dns.lookup = default
[36mconnect_1             |[0m 	client.id = connector-producer-stations-0
[36mconnect_1             |[0m 	compression.type = none
[36mconnect_1             |[0m 	connections.max.idle.ms = 540000
[36mconnect_1             |[0m 	delivery.timeout.ms = 2147483647
[36mconnect_1             |[0m 	enable.idempotence = false
[36mconnect_1             |[0m 	interceptor.classes = []
[36mconnect_1             |[0m 	key.serializer = class org.apache.kafka.common.serialization.ByteArraySerializer
[36mconnect_1             |[0m 	linger.ms = 0
[36mconnect_1             |[0m 	max.block.ms = 9223372036854775807
[36mconnect_1             |[0m 	max.in.flight.requests.per.connection = 1
[36mconnect_1             |[0m 	max.request.size = 1048576
[36mconnect_1             |[0m 	metadata.max.age.ms = 300000
[36mconnect_1             |[0m 	metadata.max.idle.ms = 300000
[36mconnect_1             |[0m 	metric.reporters = []
[36mconnect_1             |[0m 	metrics.num.samples = 2
[36mconnect_1             |[0m 	metrics.recording.level = INFO
[36mconnect_1             |[0m 	metrics.sample.window.ms = 30000
[36mconnect_1             |[0m 	partitioner.class = class org.apache.kafka.clients.producer.internals.DefaultPartitioner
[36mconnect_1             |[0m 	receive.buffer.bytes = 32768
[36mconnect_1             |[0m 	reconnect.backoff.max.ms = 1000
[36mconnect_1             |[0m 	reconnect.backoff.ms = 50
[36mconnect_1             |[0m 	request.timeout.ms = 2147483647
[36mconnect_1             |[0m 	retries = 2147483647
[36mconnect_1             |[0m 	retry.backoff.ms = 100
[36mconnect_1             |[0m 	sasl.client.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.jaas.config = null
[36mconnect_1             |[0m 	sasl.kerberos.kinit.cmd = /usr/bin/kinit
[36mconnect_1             |[0m 	sasl.kerberos.min.time.before.relogin = 60000
[36mconnect_1             |[0m 	sasl.kerberos.service.name = null
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.jitter = 0.05
[36mconnect_1             |[0m 	sasl.kerberos.ticket.renew.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.callback.handler.class = null
[36mconnect_1             |[0m 	sasl.login.class = null
[36mconnect_1             |[0m 	sasl.login.refresh.buffer.seconds = 300
[36mconnect_1             |[0m 	sasl.login.refresh.min.period.seconds = 60
[36mconnect_1             |[0m 	sasl.login.refresh.window.factor = 0.8
[36mconnect_1             |[0m 	sasl.login.refresh.window.jitter = 0.05
[36mconnect_1             |[0m 	sasl.mechanism = GSSAPI
[36mconnect_1             |[0m 	security.protocol = PLAINTEXT
[36mconnect_1             |[0m 	security.providers = null
[36mconnect_1             |[0m 	send.buffer.bytes = 131072
[36mconnect_1             |[0m 	ssl.cipher.suites = null
[36mconnect_1             |[0m 	ssl.enabled.protocols = [TLSv1.2, TLSv1.1, TLSv1]
[36mconnect_1             |[0m 	ssl.endpoint.identification.algorithm = https
[36mconnect_1             |[0m 	ssl.key.password = null
[36mconnect_1             |[0m 	ssl.keymanager.algorithm = SunX509
[36mconnect_1             |[0m 	ssl.keystore.location = null
[36mconnect_1             |[0m 	ssl.keystore.password = null
[36mconnect_1             |[0m 	ssl.keystore.type = JKS
[36mconnect_1             |[0m 	ssl.protocol = TLS
[36mconnect_1             |[0m 	ssl.provider = null
[36mconnect_1             |[0m 	ssl.secure.random.implementation = null
[36mconnect_1             |[0m 	ssl.trustmanager.algorithm = PKIX
[36mconnect_1             |[0m 	ssl.truststore.location = null
[36mconnect_1             |[0m 	ssl.truststore.password = null
[36mconnect_1             |[0m 	ssl.truststore.type = JKS
[36mconnect_1             |[0m 	transaction.timeout.ms = 60000
[36mconnect_1             |[0m 	transactional.id = null
[36mconnect_1             |[0m 	value.serializer = class org.apache.kafka.common.serialization.ByteArraySerializer
[36mconnect_1             |[0m  (org.apache.kafka.clients.producer.ProducerConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:49,699] INFO Kafka version: 5.5.1-ccs (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:12:49,699] INFO Kafka commitId: 3c4783aac9e33249 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:12:49,699] INFO Kafka startTimeMs: 1597885969698 (org.apache.kafka.common.utils.AppInfoParser)
[36mconnect_1             |[0m [2020-08-20 01:12:49,715] INFO [Producer clientId=connector-producer-stations-0] Cluster ID: 40eSduN2R46UaeWXQ6fOrQ (org.apache.kafka.clients.Metadata)
[36mconnect_1             |[0m [2020-08-20 01:12:49,749] INFO [Worker clientId=connect-1, groupId=connect] Finished starting connectors and tasks (org.apache.kafka.connect.runtime.distributed.DistributedHerder)
[36mconnect_1             |[0m [2020-08-20 01:12:49,751] INFO Starting JDBC source task (io.confluent.connect.jdbc.source.JdbcSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:12:49,761] INFO JdbcSourceTaskConfig values: 
[36mconnect_1             |[0m 	batch.max.rows = 500
[36mconnect_1             |[0m 	catalog.pattern = null
[36mconnect_1             |[0m 	connection.attempts = 3
[36mconnect_1             |[0m 	connection.backoff.ms = 10000
[36mconnect_1             |[0m 	connection.password = [hidden]
[36mconnect_1             |[0m 	connection.url = jdbc:postgresql://postgres:5432/cta
[36mconnect_1             |[0m 	connection.user = cta_admin
[36mconnect_1             |[0m 	db.timezone = UTC
[36mconnect_1             |[0m 	dialect.name = 
[36mconnect_1             |[0m 	incrementing.column.name = stop_id
[36mconnect_1             |[0m 	mode = incrementing
[36mconnect_1             |[0m 	numeric.mapping = null
[36mconnect_1             |[0m 	numeric.precision.mapping = false
[36mconnect_1             |[0m 	poll.interval.ms = 3600000
[36mconnect_1             |[0m 	query = 
[36mconnect_1             |[0m 	query.suffix = 
[36mconnect_1             |[0m 	quote.sql.identifiers = ALWAYS
[36mconnect_1             |[0m 	schema.pattern = null
[36mconnect_1             |[0m 	table.blacklist = []
[36mconnect_1             |[0m 	table.poll.interval.ms = 60000
[36mconnect_1             |[0m 	table.types = [TABLE]
[36mconnect_1             |[0m 	table.whitelist = [stations]
[36mconnect_1             |[0m 	tables = ["public"."stations"]
[36mconnect_1             |[0m 	timestamp.column.name = []
[36mconnect_1             |[0m 	timestamp.delay.interval.ms = 0
[36mconnect_1             |[0m 	timestamp.initial = null
[36mconnect_1             |[0m 	topic.prefix = chicago-transit.connect-
[36mconnect_1             |[0m 	validate.non.null = true
[36mconnect_1             |[0m  (io.confluent.connect.jdbc.source.JdbcSourceTaskConfig)
[36mconnect_1             |[0m [2020-08-20 01:12:49,762] INFO Using JDBC dialect PostgreSql (io.confluent.connect.jdbc.source.JdbcSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:12:50,195] INFO Attempting to open connection #1 to PostgreSql (io.confluent.connect.jdbc.util.CachedConnectionProvider)
[36mconnect_1             |[0m [2020-08-20 01:12:50,284] INFO Started JDBC source task (io.confluent.connect.jdbc.source.JdbcSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:12:50,284] INFO WorkerSourceTask{id=stations-0} Source task finished initialization and start (org.apache.kafka.connect.runtime.WorkerSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:12:50,287] INFO Begin using SQL query: SELECT * FROM "public"."stations" WHERE "public"."stations"."stop_id" > ? ORDER BY "public"."stations"."stop_id" ASC (io.confluent.connect.jdbc.source.TableQuerier)
[36mconnect_1             |[0m [2020-08-20 01:12:50,340] WARN [Producer clientId=connector-producer-stations-0] Error while fetching metadata with correlation id 3 : {chicago-transit.connect-stations=LEADER_NOT_AVAILABLE} (org.apache.kafka.clients.NetworkClient)
[36mconnect_1             |[0m [2020-08-20 01:13:49,731] INFO WorkerSourceTask{id=stations-0} Committing offsets (org.apache.kafka.connect.runtime.WorkerSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:13:49,733] INFO WorkerSourceTask{id=stations-0} flushing 0 outstanding messages for offset commit (org.apache.kafka.connect.runtime.WorkerSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:13:49,774] INFO WorkerSourceTask{id=stations-0} Finished commitOffsets successfully in 42 ms (org.apache.kafka.connect.runtime.WorkerSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:14:49,775] INFO WorkerSourceTask{id=stations-0} Committing offsets (org.apache.kafka.connect.runtime.WorkerSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:14:49,776] INFO WorkerSourceTask{id=stations-0} flushing 0 outstanding messages for offset commit (org.apache.kafka.connect.runtime.WorkerSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:15:49,777] INFO WorkerSourceTask{id=stations-0} Committing offsets (org.apache.kafka.connect.runtime.WorkerSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:15:49,777] INFO WorkerSourceTask{id=stations-0} flushing 0 outstanding messages for offset commit (org.apache.kafka.connect.runtime.WorkerSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:16:49,778] INFO WorkerSourceTask{id=stations-0} Committing offsets (org.apache.kafka.connect.runtime.WorkerSourceTask)
[36mconnect_1             |[0m [2020-08-20 01:16:49,778] INFO WorkerSourceTask{id=stations-0} flushing 0 outstanding messages for offset commit (org.apache.kafka.connect.runtime.WorkerSourceTask)
