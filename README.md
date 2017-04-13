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


## Automated Docker image Build

The Dockerfile in the roor of the github directory is used to automatically build Docker images for pipeline-kafka on Dockerhub here: <https://hub.docker.com/r/akshshar/pipeline-kafka/>

This docker image can be pulled by issuing:

```
docker pull akshshar/pipeline-kafka

```

To run the docker image and supply your own pipeline.conf file for pipeline, mount the custom config file at /data/pipeline.conf :

```
docker run -itd --name pipeline-kafka -v /home/cisco/custom_pipeline.conf:/data/pipeline.conf -p 5432:5432 -p 5958:5958 -p 9092:9092 -p 2181:2181 pipeline-kafka
```   

The ports opened and shared with the host are:

  *   5432:  TCP port opened by default pipeline.conf file. Can be changed by the user based on their pipeline.conf file
  *   5958: UDP port opened by default pipeline.conf file. Can be changed by the user based on their pipeline.conf file 
  *   9092:  port opened by the standalone Kafka instance.
  *   2181:  port opened by the Zookeeper instance.  
  
  
  
## Building and running a pipeline-kafka docker image on IOS-XR

Check out this hands-on tutorial that explains how to bring up this docker image on IOS-XR while being cognizant of the vrf in XR that we run the container in:  <https://xrdocs.github.io/application-hosting/tutorials/2017-04-12-on-box-telemetry-running-pipeline-and-kafka-on-ios-xr/>
