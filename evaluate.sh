../kafka_2.12-2.2.0/bin/kafka-topics.sh --zookeeper localhost:2181 --alter --topic hero --config retention.ms=1000
../kafka_2.12-2.2.0/bin/kafka-topics.sh --zookeeper localhost:2181 --alter --topic combatlog --config retention.ms=1000
../kafka_2.12-2.2.0/bin/kafka-topics.sh --zookeeper localhost:2181 --alter --topic output --config retention.ms=1000
sleep 5
../kafka_2.12-2.2.0/bin/kafka-topics.sh --zookeeper localhost:2181 --alter --topic hero --config retention.ms=3600000
../kafka_2.12-2.2.0/bin/kafka-topics.sh --zookeeper localhost:2181 --alter --topic combatlog --config retention.ms=3600000
../kafka_2.12-2.2.0/bin/kafka-topics.sh --zookeeper localhost:2181 --alter --topic output --config retention.ms=3600000
echo "Deleting Outstanding Messages..."
mvn exec:java -Dexec.args="replay.dem $1" -f ../replay-parser/pom.xml
