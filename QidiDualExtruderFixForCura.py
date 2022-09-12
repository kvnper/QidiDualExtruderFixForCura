# Cura PostProcessingPlugin Script - Qidi Dual Extruder Fix For Cura
# Author:   Kevin Pereira
# Date:     September 13, 2022
# Version: 	1.0

# Description:  Removes the gcode command "T0" that Cura inserts before the start gcode
#		when Cura automatically sets the temperatures (this occurs when the
#		temperatures are not set in the start gcode).
#		It will then add the tool number to the temperature setters that Cura
#		automatically adds before the start gcode.
#	
#		This is needed when using the QIDI I-Fast printer, otherwise the added "T0" gcode
#		will trigger the printer to execute the internal firmware toolchange gcode, 
#		which moves the whole extruder towards the printer sidewall to mechanically 
#		engage the tool. If the extruder position is not correct this will cause 
#		the extruder to continously bang against the sidewall.

from ..Script import Script

class QidiDualExtruderFixForCura(Script):
	"""	Removes the gcode command "T0" that Cura inserts before the start gcode
		when Cura automatically sets the temperatures (this occurs when the
		temperatures are not set in the start gcode).
		It will then add the tool number to the temperature setters that Cura
		automatically adds before the start gcode.
	
		This is needed when using the QIDI I-Fast printer, otherwise the added "T0" gcode
		will trigger the printer to execute the internal firmware toolchange gcode, 
		which moves the whole extruder towards the printer sidewall to mechanically 
		engage the tool. If the extruder position is not correct this will cause 
		the extruder to continously bang against the sidewall.
	"""
	def __init__(self):
		super().__init__()

	def getSettingDataString(self):
		return """{
			"name": "Qidi Dual Extruder Fix For Cura",
			"key": "QidiDualExtruderFixForCura",
			"metadata": {},
			"version": 2,
			"settings":
			{
				"firstLineOfStartGcode":
				{
					"label": "First line of start GCode",
					"description": "Please enter the first line in the Start GCode for this machine. Usually it is G28.",
					"type": "str",
					"default_value": "G28"
				}
			}
		}"""

	def execute(self, data):
		start_gcode_string = self.getSettingValueByKey("firstLineOfStartGcode")
		tool_search_string_t0 = "T0"
		tool_search_string_t1 = "T1"
		tool_index = 0
		
		m104_search_gcode = "M104 S"
		m109_search_gcode = "M109 S"
		
		tool_gcode_found = False
		end_found = False

		for layer in data:
			layer_index = data.index(layer)
			lines = layer.split("\n")
			for line in lines:
				if line.startswith(start_gcode_string):
					end_found = True
					break
				elif not tool_gcode_found:
					if line.startswith(tool_search_string_t0) or line.startswith(tool_search_string_t1):
						line_index = lines.index(line)
						tool_index = lines[line_index][1]
						lines[line_index] = ""
						tool_gcode_found = True
				else:
					if line.startswith(m104_search_gcode) or line.startswith(m109_search_gcode):
						line_index = lines.index(line)
						lines[line_index] = lines[line_index][:5] + "T" + tool_index + " " + lines[line_index][5:]
			final_lines = "\n".join(lines)
			data[layer_index] = final_lines
			if end_found:
				break
		return data
