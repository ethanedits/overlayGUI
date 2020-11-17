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
