#!/usr/bin/python

import sys

def buildConnectionString(params):
    """    Build a connection string from a dictionary of parameters.
    Returns string. """
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    
    print sys.path
    sys.path.append("C:\Users\pmohanasundaram\Documents\Trashit\eclipse-java-juno-SR1-win32-x86_64\eclipse")
    print sys.path
    print
    
    myParams = {"server":"mpilgrim", \
                "database":"master", \
                "uid":"sa", \
                "pwd":"secret" \
                }
    print buildConnectionString(myParams)
    print buildConnectionString.__doc__