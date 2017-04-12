from kafka import KafkaConsumer
import json, re
import pdb

FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
WHITESPACE = re.compile(r'[ \t\n\r]*', FLAGS)

class ConcatJSONDecoder(json.JSONDecoder):
    def decode(self, s, _w=WHITESPACE.match):
        s_len = len(s)

        objs = []
        end = 0
        while end != s_len:
            obj, end = self.raw_decode(s, idx=_w(s, end).end())
            end = _w(s, end).end()
            objs.append(obj)
        return objs


if __name__ == "__main__":

    consumer = KafkaConsumer('telemetry', bootstrap_servers=["localhost:9092"])

    for msg in consumer:
        telemetry_msg =  msg.value
        telemetry_msg_json = json.loads(telemetry_msg)

        if "Rows" in telemetry_msg_json:
            content_rows = json.loads(telemetry_msg)["Rows"]
            for row in content_rows:
                if row["Keys"]["interface-name"] == 'MgmtEth0/RSP1/CPU0/0':
                    pkt_rcvd = row["Content"]["packets-received"]               
                    input_drops = row["Content"]["input-drops"]

                    print("Packets Received = %s, \n Input Drops = %s" %(pkt_rcvd, input_drops)) 

