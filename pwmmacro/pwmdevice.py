#   Copyright 2016 Andreas Riegg - t-h-i-n-x.net
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# This script shows the solution for regular PWM devices.

# Imports
import webiopi

# Enable debug output
webiopi.setDebug()

# Retrieve PWM device assuming you want to use device named "mypwm" from config
PWMDEVICE = webiopi.deviceInstance("mypwm")

# assuming you want to control PWM channel 0, otherwise change number
PWMPORT = 0            

# Called by WebIOPi at script loading
def setup():
    global PWMDEVICE
    webiopi.debug("PWM script - Setup")
    PWMDEVICE.pwmWriteFloat(PWMPORT, 0.0) # set to 0% ratio

# Called by WebIOPi at server shutdown
def destroy():
    global PWMDEVICE
    webiopi.debug("PWM script - Destroy")
    PWMDEVICE.pwmWriteFloat(PWMPORT, 0.0) # reset to 0% ratio

@webiopi.macro
def setBrightnessTo20Percent():
    global PWMDEVICE
    PWMDEVICE.pwmWriteFloat(PWMPORT, 0.2) 

@webiopi.macro
def setBrightnessTo50Percent():
    global PWMDEVICE
    PWMDEVICE.pwmWriteFloat(PWMPORT, 0.5) 

@webiopi.macro
def setBrightnessTo80Percent():
    global PWMDEVICE
    PWMDEVICE.pwmWriteFloat(PWMPORT, 0.8)

@webiopi.macro
def setBrightnessToXPercent(x):
    global PWMDEVICE
    value = float(x) / 100
    PWMDEVICE.pwmWriteFloat(PWMPORT, value)

@webiopi.macro
def setAngleTo45Degrees():
    global PWMDEVICE
    PWMDEVICE.pwmWriteAngle(PWMPORT, 45.0)

@webiopi.macro
def setAngleToMinus45Degrees():
    global PWMDEVICE
    PWMDEVICE.pwmWriteAngle(PWMPORT, -45.0)

    
