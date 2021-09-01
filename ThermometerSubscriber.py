import rticonnextdds_connector as rti
from os import path as os_path

file_path = os_path.dirname(os_path.realpath(__file__))

with rti.open_connector(
        config_name="Temperature_Participant_Library::Temperature_Participant",
        url=file_path + "\\TemperatureType_Participant_Config.xml") as connector:
    temperatureType_input = connector.getInput("TemperatureSubscriber::TemperatureType_DR")

    while True:
        try:
            temperatureType_input.take()
            for sample in temperatureType_input.samples:
                if sample.valid_data:
                    temperature = sample.get_number("temperature")
                    sensorId = sample.get_number("sensorId")
                    print("temperature " + str(temperature) + " received from sensor id " + str(sensorId))
        except Exception as error:
            print(str(error))
