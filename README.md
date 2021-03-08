# Consumer-GUI-etaNET-HSKA
This Respository contains all relevant code to get the Consumer-GUI for the Project etaNet in the GenLab of the Hochschule Karlsruhe - Technik und Wirtschaft running.


1. make sure pandas and pyqt5 are installed
2. The Programm starts by navigating to the path the folder sits and then use:

      python3 main.py


3. for more information check documentation at GenLab (contact: ferhat.aslan@hs-karlsruhe.de)

If your IDE has problems finding all the python files in subfolders add a simple empty __init__.py file in each folder

For running Gui in the Lab:
1. Make sure the Raspberry Pi is connected to the etaNet-Network in order to receive the HeatMeter Data
2. For using the MQTT-Option, make sure the etaNet-Network is able to establish an internet connection (currently (March 2021), the etaNet has no Interent connection)
