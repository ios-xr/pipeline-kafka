from kafka import KafkaConsumer
import json

if __name__ == "__main__":

    consumer = KafkaConsumer('telemetry', bootstrap_servers=["1.1.1.1:9092"])

    for msg in consumer:
        telemetry_msg =  msg.value
        telemetry_msg_json = json.loads(telemetry_msg)

        print "\nTelemetry data Received:\n "

        print json.dumps(telemetry_msg_json, indent=4, sort_keys=True)

        if "Rows" in telemetry_msg_json:
            content_rows = telemetry_msg_json["Rows"]
            for row in content_rows:
                if row["Keys"]["interface-name"] == 'MgmtEth0/RSP1/CPU0/0':
                    pkt_rcvd = row["Content"]["packets-received"]               
                    input_drops = row["Content"]["input-drops"]

                    print("\nParsed fields for interface  MgmtEth0/RSP1/CPU0/0:\
                            \n  Packets Received = %s,\
                            \n  Input Drops = %s" %(pkt_rcvd, input_drops)) 

