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

# Imports
import webiopi
from webiopi.utils.types import str2bool

BLINKPERIOD = 0.5
BLINKING = False

# ----- Enable debug output -----
webiopi.setDebug() #optional, can be omitted

# ----- WebIOPi predefined functions -----

# Called by WebIOPi at script loading
def setup():
    webiopi.debug("Looptest script - Setup") #optional, can be omitted
    
# Looped by WebIOPi
def loop():
    webiopi.debug("Looptest script - Loop") #optional, can be omitted
    if BLINKING:
        print("B-L-I-N-K") 
        webiopi.sleep(BLINKPERIOD)        
        print("---------") 
    webiopi.sleep(BLINKPERIOD)        

# Called by WebIOPi at server shutdown
def destroy():
    webiopi.debug("Looptest script - Destroy") #optional, can be omitted
    stopBlinking()

# Macros to start and stop blinking
@webiopi.macro
def startBlinking():
    global BLINKING
    BLINKING = True

@webiopi.macro
def stopBlinking():
    global BLINKING
    BLINKING = False

# Additional convenience macros to enable blinking and set/get the blinking period
@webiopi.macro
def enableBlinking(blinking="yes"):
    global BLINKING
    BLINKING = str2bool(blinking)

@webiopi.macro
def setBlinkPeriod(period=0.5):
    global BLINKPERIOD
    BLINKPERIOD = float(period)
    return "Blinking period set to %f seconds." % BLINKPERIOD #optional, can be omitted

@webiopi.macro
def getBlinkPeriod():
    global BLINKPERIOD
    return "%f" % BLINKPERIOD


