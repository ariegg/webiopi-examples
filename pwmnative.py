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

# This script shows the solution for native GPIO ports.

# Imports
import webiopi

# Enable debug output
webiopi.setDebug()

# Retrieve GPIO lib
GPIO = webiopi.GPIO
PWMPORT = 21 # assuming you want to control Pin 21, otherwise change number

# Called by WebIOPi at script loading
def setup():
    webiopi.debug("PWM script - Setup")
    # Setup GPIOs
    GPIO.setFunction(PWMPORT, GPIO.PWM)  
    GPIO.pwmWrite(PWMPORT, 0.0)      # set to 0% ratio

# Called by WebIOPi at server shutdown
def destroy():
    webiopi.debug("PWM script - Destroy")
    # Reset GPIO functions
    GPIO.setFunction(PWMPORT, GPIO.IN)

@webiopi.macro
def setBrightnessTo20Percent():
    GPIO.pwmWrite(PWMPORT, 0.2) 

@webiopi.macro
def setBrightnessTo50Percent():
    GPIO.pwmWrite(PWMPORT, 0.5) 

@webiopi.macro
def setBrightnessTo80Percent():
    GPIO.pwmWrite(PWMPORT, 0.8)

@webiopi.macro
def setBrightnessToXPercent(x):
    value = float(x) / 100
    GPIO.pwmWrite(PWMPORT, value)

@webiopi.macro
def setAngleTo45Degrees():
    GPIO.pwmWriteAngle(PWMPORT, 45.0)

@webiopi.macro
def setAngleToMinus45Degrees():
    GPIO.pwmWriteAngle(PWMPORT, -45.0)

    
