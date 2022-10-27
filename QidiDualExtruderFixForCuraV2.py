# Cura PostProcessingPlugin Script - Qidi Dual Extruder Fix For Cura
# Author:   Kevin Pereira
# Date:     October 27, 2022
# Version: 	2.0.0

# Description:
#		Adds a home "G28" command in the gcode before the automatically inserted nozzle and bed temperature 
#		setting gcode by Cura (this occurs when the temperatures are not set in the start gcode) which are
#		before the start gcode.
#	
#		This is needed when using the QIDI I-Fast printer, otherwise the added "T0" gcode
#		will trigger the printer to execute the internal firmware toolchange gcode, 
#		which moves the whole extruder towards the printer sidewall to mechanically 
#		engage the tool. If the extruder position is not correct (in home position) this 
#		will cause 	the extruder to continously bang against the sidewall.
#
 

from ..Script import Script

class QidiDualExtruderFixForCuraV2(Script):
	def __init__(self):
		super().__init__()

	def getSettingDataString(self):
		return """{
			"name": "Qidi Dual Extruder Fix For Cura V2",
			"key": "QidiDualExtruderFixForCuraV2",
			"metadata": {},
			"version": 2,
			"settings":
			{
				"isScriptEnabled":
				{
					"label": "Enable Script?",
					"description": "Would you like to enable this script?",
					"type": "bool",
					"default_value": "True"
				},
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
		script_enabled = self.getSettingValueByKey("isScriptEnabled")
		if not script_enabled:
			return data
	
		start_gcode_string = self.getSettingValueByKey("firstLineOfStartGcode")
		tool_search_string_t0 = "T0"
		tool_search_string_t1 = "T1"
		insert_gcode = "G28"
		
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
						lines.insert(lines.index(line),insert_gcode)
						tool_gcode_found = True
			final_lines = "\n".join(lines)
			data[layer_index] = final_lines
			if end_found:
				break
		return data
