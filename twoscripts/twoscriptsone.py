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
from twoscriptscommon import VALUES

# Enable debug output
webiopi.setDebug()

# Called by WebIOPi at script loading
def setup():
    VALUES['a'] = 'aaaaa' # Optional, show initialisation
    print(VALUES)
    

# Macros 
@webiopi.macro
def setNamedValueOne(someName, someValue):
    print('Setting in script one:')
    print(someName)
    print(someValue)
    VALUES[someName] = someValue
    print(VALUES)

@webiopi.macro
def getNamedValueOne(someName):
    print('Getting in script one:')
    if someName in VALUES:
        return VALUES[someName]
    else:
        return 'Name %s is n/a.' % someName

@webiopi.macro
def useNamedValueOne(someName):
    print('Using in script one:')
    if someName in VALUES:
        val = VALUES[someName]
        VALUES[someName] = val + val
        print(VALUES)
    else:
        return 'Using name %s is not possible.' % someName
