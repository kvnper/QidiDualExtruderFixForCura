# Cura PostProcessing Plugin: Qidi Dual Extruder Fix For Cura
A Post Processing script for Ultimaker's Cura to fix the issue with QIDI 3D printers with dual extruders


This script removes the gcode command "T0" that Cura inserts before the start gcode when Cura automatically sets the nozzle temperatures (this occurs when the nozzle temperatures are not set in the start gcode). It will then also add the tool number to the nozzle temperature setters that Cura automatically adds before the start gcode.

This is needed when using the QIDI I-Fast printer, otherwise the added "T0" gcode will trigger the printer to execute the internal firmware toolchange gcode, which moves the whole extruder towards the printer sidewall to mechanically engage the tool. If the extruder position is not correct this will cause the extruder to continously bang against the sidewall.

The purge line will need to be removed from the start gcode for the I-Fast as it will cause the printer to try and extrude with disabled extruders. The gcode below removes the extrusion ~~but keeps the movement in order to wipe the nozzles~~. (Currently the wipe line gcode is removed also as it seems to still be extruding)


Usage:
-------------------
1. In Cura, go to the following toolbar menu: Help -> Show Configuration Folder. 
2. A folder should have opened, now open the 'scripts' folder, you'll need this for step 4.
3. Close Cura.
4. Place the file 'QidiDualExtruderFixForCura.py' in the 'script' folder in Cura's configuration folder.
5. Open Cura.
6. Remove the bed and nozzle temperature setters and the purge line gcode in the start gcode or, alternatively, use the start gcode below these steps or in the file 'QIDI I-Fast Start GCode for Cura.txt' (for QIDI I-Fast only). 
7. Copy the first line of the start gcode, you'll need it in step 9.
8. Enable this post processing script from the following toolbar menu: Extensions -> Post Processing -> Modify G-Code -> Add a Script -> Qidi Dual Extruder Fix For Cura .
9. Paste the first line of the start gcode into the field 'First line of start GCode'. The default value for this field is "G28".

Start GCode for the QIDI I-Fast for Cura
-------------------
```
G28
G0 X0 Y0 Z50 F3600
G0 X0 Y6 Z0.3 F3600
G1 X5 E0 F2400
; --- end of start gcode ---
```

GCode Result Examples:
-------------------

First extruder enabled, second extruder disabled, before and after using the postprocessing script


Before:

![image](https://user-images.githubusercontent.com/47488385/189691246-4c852e6f-bf67-4383-a249-a59ac32e4db7.png)


After:

![image](https://user-images.githubusercontent.com/47488385/189691310-b71f05ac-14e5-4c58-8ab9-397431bf02be.png)



First extruder disabled, second extruder enabled, before and after using the postprocessing script


Before:

![image](https://user-images.githubusercontent.com/47488385/189697002-34cd1bb7-e47b-4edd-8c41-3ef57bbd26cf.png)


After:

![image](https://user-images.githubusercontent.com/47488385/189697025-2a338d30-d0cf-4844-ba33-8280e271a612.png)


First extruder enabled, second extruder enabled, before and after using the postprocessing script


Before:

![image](https://user-images.githubusercontent.com/47488385/189691338-f5926a31-dfed-4602-8a36-69d78ce6c085.png)


After:

![image](https://user-images.githubusercontent.com/47488385/189691370-ea5b05e7-a6d7-4ed0-833e-02b4fd2c267a.png)
