from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import requests

# Automatically called whenever the shadow is updated.
def myShadowUpdateCallback(payload, responseStatus, token):
    print()
    print('UPDATE: $aws/things/' + 'Co2Sensor' + '/shadow/update/#')
    print("payload = " + payload)
    print("responseStatus = " + responseStatus)
    print("token = " + token)
'''
def upload(current_time_str, co2):
    # A random programmatic shadow client ID.
    SHADOW_CLIENT = "myShadowClient"

    # The unique hostname that AWS IoT generated for
    # this device.
    HOST_NAME = "a21y1b44sop8q7-ats.iot.us-west-2.amazonaws.com"

    # The relative path to the correct root CA file for AWS IoT,
    # that you have already saved onto this device.
    ROOT_CA = "../../aws-iot-device-sdk-embedded-C/certs/AmazonRootCA1.pem"

    # The relative path to your private key file that
    # AWS IoT generated for this device, that you
    # have already saved onto this device.
    PRIVATE_KEY = "../../aws-iot-device-sdk-embedded-C/certs/a061163b7b-private.pem.key"

    # The relative path to your certificate file that
    # AWS IoT generated for this device, that you
    # have already saved onto this device.
    CERT_FILE = "../../aws-iot-device-sdk-embedded-C/certs/a061163b7b-certificate.pem.crt"

    # A programmatic shadow handler name prefix.
    SHADOW_HANDLER = "Co2Sensor"
    # Create, configure, and connect a shadow client.
    myShadowClient = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
    myShadowClient.configureEndpoint(HOST_NAME, 8883)
    myShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
    myShadowClient.configureConnectDisconnectTimeout(10)
    myShadowClient.configureMQTTOperationTimeout(5)
    myShadowClient.connect()

    # Create a programmatic representation of the shadow.
    myDeviceShadow = myShadowClient.createShadowHandlerWithName(SHADOW_HANDLER, True)

    data_obj = '{"state": {"reported": {"time": "' + current_time_str + '", "co2": ' + str(co2) + '}}}'
    myDeviceShadow.shadowUpdate(data_obj, myShadowUpdateCallback, 5)
'''

def upload(current_time_str, co2):
    r = requests.post('http://projectcarbon.io/devices/co2/server-side/response_handler.py',
                      data={"command": "insert", "co2": co2, "time": current_time_str})
    print(r.status_code)
    print(r.text)