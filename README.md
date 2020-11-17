# overlayGUI
A simple but powerful GUI python package for overlays.
(Windows only)

**Documentation**
-----------------
**Introduction**

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
Here we are creating a variable called `checkbox` which is equal to the `oGUI.Checkbox()` function.

**Colors**
---------------------

*oGUI* comes with a few **color variables** you can access by using `oGUI.(colorname)`
These are the available colors:

`oGUI.white`
`oGUI.red`
`oGUI.green`
`oGUI.blue`
`oGUI.cyan`
`oGUI.orange`
`oGUI.black`
`oGUI.gray`
`oGUI.purple`
`oGUI.lightgray`
`oGUI.darkgray`

**Functions**
---------------------
Creating *checkboxes*

To create a **checkbox**, we can create a variable and then call the `oGUI.Checkbox()` function.
```py
checkbox1 = oGUI.Checkbox(outsideColor, insideColor, x position, y position, width, height, enabledByDefault)
```
We will continue to use checkbox1 as the checkbox variable for the rest of the documentation.

We can also change the *color* of the box if it is hovered over, using the `is_hovered()` function.
```py
checkbox1.is_hovered(color)
```
The **color** parameter accepts an *RGB value*, for example: `(255, 0, 0)` or it will accept *oGUI colors*. For example, `oGUI.orange`. All the oGUI colors are listed in the **Colors** section, below the Introduction section.
