import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "rxdn0x",
        "typeId": "Soujanya",
        "deviceId":"12345"
    },
    "auth": {
        "token": "123456789"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
