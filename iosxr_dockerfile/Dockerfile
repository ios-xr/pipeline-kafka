FROM pipeline-kafka:latest

Maintainer akshshar

# Specify the "vrf" you want to run daemons in during build time
# By default, it is global-vrf

ARG vrf=global-vrf

CMD ip netns exec global-vrf supervisord -n
