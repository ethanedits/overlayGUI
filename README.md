# overlayGUI
A simple but powerful GUI python package for overlays.
(Windows only)

**Documentation:**

To *initialize* oGUI, you need to call
```py
oGui.init()
```
Once you have called this, you can create an **infinite loop** and call two functions, **startLoop()** and **endLoop()**.
```py
while True:
  oGui.startLoop()
  
  oGui.endLoop()
```

*Inbetween* the `start` and `end` loop, you can call the drawing functions.

*Here is an example:*
```py
checkbox = oGUI.Checkbox(oGUI.gray, oGUI.orange, 125, 150, 20, 20)

while True:
    oGUI.startLoop()
    
    checkbox.draw()

    oGUI.endLoop()
```
Here we are creating a variable called `checkbox` which is equal to the 
```py
oGUI.Checkbox()
``` function.
