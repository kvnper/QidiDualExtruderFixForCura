WARNING: Currently not final. Does not work when first extruder is disabled and second extruder enabled.

# Cura-PostProcessing-Plugin_QidiDualExtruderFixForCura
A Post Processing script for Ultimaker's Cura to fix the issue with QIDI 3D printers with dual extruders


This script removes the gcode command "T0" that Cura inserts before the start gcode when Cura automatically sets the temperatures (this occurs when the temperatures are not set in the start gcode). It will then also add the tool number to the temperature setters that Cura automatically adds before the start gcode.

This is needed when using the QIDI I-Fast printer, otherwise the added "T0" gcode will trigger the printer to execute the internal firmware toolchange gcode, which moves the whole extruder towards the printer sidewall to mechanically engage the tool. If the extruder position is not correct this will cause the extruder to continously bang against the sidewall.



Examples:
-------------------

First extruder enabled, second extruder disabled, before and after using the postprocessing script


Before:

![image](https://user-images.githubusercontent.com/47488385/189691246-4c852e6f-bf67-4383-a249-a59ac32e4db7.png)


After:

![image](https://user-images.githubusercontent.com/47488385/189691310-b71f05ac-14e5-4c58-8ab9-397431bf02be.png)



First extruder enabled, second extruder enabled, before and after using the postprocessing script


Before:

![image](https://user-images.githubusercontent.com/47488385/189691338-f5926a31-dfed-4602-8a36-69d78ce6c085.png)


After:

![image](https://user-images.githubusercontent.com/47488385/189691370-ea5b05e7-a6d7-4ed0-833e-02b4fd2c267a.png)
