FROM akshshar/pipeline-kafka:latest

Maintainer akshshar

# Specify the "vrf" you want to run daemons in during build time
# By default, it is global-vrf

ARG vrf=global-vrf

# Set up the ARG for use by Entrypoint or CMD scripts
ENV vrf_exec "ip netns exec $vrf"

# Add a sample kafka_consumer.py script. User can provide their own
ADD kafka_consumer.py /kafka_consumer.py


CMD $vrf_exec echo "127.0.0.1 localhost" >> /etc/hosts && $vrf_exec supervisord -n
