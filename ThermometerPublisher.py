import rticonnextdds_connector as rti
import time as time
from os import path as os_path
from random import randint

file_path = os_path.dirname(os_path.realpath(__file__))

with rti.open_connector(
        config_name="Temperature_Participant_Library::Temperature_Participant",
        url=file_path + "\\TemperatureType_Participant_Config.xml") as connector:
    output = connector.get_output("TemperaturePublisher::TemperatureType_DW")
    output.instance.set_number("sensorId", 1)
    while True:
        output.instance.set_number("temperature", randint(0, 100))
        output.write()

        time.sleep(0.5)  # Write at a rate of one sample every 0.5 seconds, for ex.
