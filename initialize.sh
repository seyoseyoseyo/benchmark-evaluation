  ../kafka_2.12-2.2.0/bin/kafka-server-stop.sh
  ../kafka_2.12-2.2.0/bin/zookeeper-server-stop.sh
sleep 5
{ ../kafka_2.12-2.2.0/bin/zookeeper-server-start.sh ../kafka_2.12-2.2.0/config/zookeeper.properties; } &
{ sleep 5 && ../kafka_2.12-2.2.0/bin/kafka-server-start.sh ../kafka_2.12-2.2.0/config/server.properties; } &
