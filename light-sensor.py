# create a program that reads the light level form the sensor and human presence from the PIR sensor to automate the LED light 
# to turn on, dimm or turn off based on the light level and human presence.

# it must be written in Python to run on Arduino devices 

# PIR sensor is used to detect motion and light sensor is used to detect light level

# the program allows the user to set the light level and time for the LED light to turn on and off

# the program allows the user to set the time for the LED light to dim by the set percentage and the time for 
# the LED light to turn off in the absence of motion or light level higher than the set value.

# the LED light will turn on when the light sensor detect litgh level lowered under the set value, for longer than the set time.
# if the light sensor detects light, the LED light will turn off
# if the light sensor does not detect light, the LED light will turn on
# the PIR sensor will detect motion and turn on the LED light
# the LED light 'on' and 'off' State Transitioning conditions
# 1. if the light sensor detects light, the LED light will turn off/remain off
# 2. if the light sensor detects light, the PIR sensor ignored
# 3. if the light sensor does not detect light, the LED light will turn on/remain on, the PIR sensor ignored, the Timer will start countdown set by the user, the PIR sensor will be activated.
# 4. if the PIR sensor detects NO motion for the set time, the LED light will dim by 50% until the PIR sensor detects motion then the LED light will get brighter.
# 5. the LED light will stay on until the light sensor detects light, then the LED light will turn off and the PIR sensor will be ignored until the light sensor detects no light.
# 3. if the PIR sensor detects motion, the LED light will turn on
# 4. if the PIR sensor does not detect motion, the LED light will turn off
# 5. if the light sensor detects light and the PIR sensor detects motion, the LED light will turn off
# 6. if the light sensor does not detect light and the PIR sensor does not detect motion, the LED light will turn on
# 7. if the light sensor does not detect light and the PIR sensor detects motion, the LED light will turn on
# 8. if the light sensor detects light and the PIR sensor does not detect motion, the LED light will turn offcho