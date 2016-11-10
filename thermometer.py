# Imports
import webiopi

# ----- Enable debug output -----
webiopi.setDebug()

# ----- Define global variables -----

# Digital port functions
OUT = 1
IN  = 0

# Digital port values
HIGH = 1
LOW  = 0

# LED port numbers
REDPORT   = 0
GREENPORT = 1
BLUEPORT  = 2

# LED port values
RED     = 0b11111110
GREEN   = 0b11111101
BLUE    = 0b11111011
BLACK   = 0b11111111
YELLOW  = RED & GREEN
MAGENTA = RED & BLUE
CYAN    = GREEN & BLUE
WHITE   = RED & GREEN & BLUE

# Digital port device (MCP23008)
DIO = None

# ----- WebIOPi predefined functions -----

# Called by WebIOPi at script loading
def setup():
    global DIO
    webiopi.debug("Thermometer script - Setup")
    
    # Setup digital IO ports for RGB LED
    DIO = webiopi.deviceInstance("digio")
    DIO.setFunction(REDPORT, OUT)
    DIO.setFunction(GREENPORT, OUT)
    DIO.setFunction(BLUEPORT, OUT)

    # Blink white 5 x
    for i in range(5):
        white()
        webiopi.sleep(0.5)
        black()
        webiopi.sleep(0.5)
    
# Looped by WebIOPi
def loop():

    thermometer = webiopi.deviceInstance("temp")
    
    temperature = thermometer.getCelsius()
    
    if temperature > 27:
        red()
    elif temperature > 26.5:
        yellow()
    elif temperature > 26:
        green()
    elif temperature > 25.5:
        cyan()
    elif temperature > 25:
        blue()
    else:
        magenta()
        
    webiopi.sleep(0.5)        

# Called by WebIOPi at server shutdown
def destroy():
    global DIO
    webiopi.debug("Thermometer script - Destroy")
    
    # Blink white 5 x
    for i in range(5):
        white()
        webiopi.sleep(0.5)
        black()
        webiopi.sleep(0.5)
        
    # Reset functions
    DIO.setFunction(REDPORT, IN)
    DIO.setFunction(GREENPORT, IN)
    DIO.setFunction(BLUEPORT, IN)

# ----- Helper functions -----
#Helper functions
@webiopi.macro
def red():
    global DIO
    DIO.portWrite(RED)

@webiopi.macro
def green():
    global DIO
    DIO.portWrite(GREEN)

@webiopi.macro
def blue():
    global DIO
    DIO.portWrite(BLUE)

@webiopi.macro
def cyan():
    global DIO
    DIO.portWrite(CYAN)

@webiopi.macro
def yellow():
    global DIO
    DIO.portWrite(YELLOW)

@webiopi.macro
def magenta():
    global DIO
    DIO.portWrite(MAGENTA)

@webiopi.macro
def white():
    global DIO
    DIO.portWrite(WHITE)

@webiopi.macro
def black():
    global DIO
    DIO.portWrite(BLACK)

    
