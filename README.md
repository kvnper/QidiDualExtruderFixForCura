# Cura PostProcessing Plugin: Qidi Dual Extruder Fix For Cura
A Post Processing script for Ultimaker's Cura to fix the issue with QIDI 3D printers with dual extruders


This script inserts a home gcode command (G28) into the gcode. It is inserted before the Cura automatic temperature setters.

Without this home command, the I-Fast will activate the extruder and, if not in the correct position, the extruder will bang against the printer wall.


Usage:
-------------------
1. In Cura, go to the following toolbar menu: Help -> Show Configuration Folder. 
2. A folder should have opened, now open the 'scripts' folder, you'll need this for step 4.
3. Close Cura.
4. Place the file 'QidiDualExtruderFixForCuraV2.py' in the 'script' folder in Cura's configuration folder.
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
