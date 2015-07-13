# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import math


def areaofpolygon(n,s):
    return ((1.0/4)*n*(s**2))/(math.tan(math.pi/n))


print areaofpolygon(7,3)
