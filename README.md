# pipeline-kafka
Pipeline and Kafka docker image creation to host Telemetry receivers on box for IOS-XR

This repository is meant to host Dockerfile for the creation of a Docker image containing the following items:  

*  pipeline: (see <https://github.com/cisco/bigmuddy-network-telemetry-pipeline>) A Multi-function open source telemetry receiver written in Go.
*  kafka, zookeeper: (see <https://github.com/spotify/docker-kafka>) Apache Kafka and Zookeeper ready to be packages together into a single docker image.
*  Kafka-python: (see <https://github.com/dpkp/kafka-python>) Python implementation of Kafka's Consumer and Producer APIs to serve as a way to script clients interacting with the Kafka Bus.  

**We use submodules to keep the dependency on Pipeline and docker-kafka current**
If you clone this repository, make sure you run:  

```shell

git clone --recursive https://github.com/ios-xr/pipeline-kafka

```

to automatically fetch all the submodules. 

