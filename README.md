# overlayGUI
A simple but powerful GUI python package for overlays.

This package will create a transparent, clickable window that you can draw things such as menus on. You can still interact with the window behind the overlay window.
(Windows only)

**Documentation**
-----------------
**Introduction**

To *initialize* oGUI, you need to call
```py
oGUI.init()
```
Once you have called this, you can create an **infinite loop** and call two functions, **startLoop()** and **endLoop()**.
```py
while True:
  oGUI.startLoop()
  
  oGUI.endLoop()
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

*oGUI* comes with a few **color variables** you can access by using `oGUI.colorname`
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
`oGUI.yellow`
`oGUI.lightgray`
`oGUI.darkgray`

**Functions**
---------------------
Creating *checkboxes*

To create a **checkbox**, we can create a variable and then call the `oGUI.Checkbox()` function. Usage:
```py
checkbox1 = oGUI.Checkbox(outsideColor, insideColor, x position, y position, width, height, enabledByDefault)
```
enabledByDefault is optional, and if you leave it blank (dont specify it), it will be false.

We will continue to use *checkbox1* as the *checkbox variable* for the rest of the documentation, and the *rest of these functions* should be called in an **infinite loop.**

To *render* the actual checkbox, we must call its `.draw()` function. Usage:
```py
checkbox1.draw()
```
We need to put this function inbetween of our `startLoop()` and `endLoop()`.

We can also change the *color* of the box if it is hovered over, using the `.is_hovered()` function. Usage:
```py
checkbox1.is_hovered(color)
```
The **color** parameter accepts an *RGB value*, for example: `(255, 0, 0)` or it will accept *oGUI colors*. For example, `oGUI.orange`. All the oGUI colors are listed in the **Colors** section, below the Introduction section.

We can use `.printMousePos()` to print the mouse's position in the GUI window to the console. Usage:
```py
checkbox1.printMousePos()
```

We can also *detect* when the checkbox **is enabled** by doing `.is_enabled()`, this will *return a boolean value* (True/False). Usage:
```py
checkbox1.is_enabled()
```

Creating *buttons*

Creating a button is the same as creating a checkbox with all the same functions, but for the button we call `oGUI.Button()`.

Creating *text*

To create **text**, we can create a variable and then call the `oGUI.Text()` function. Usage:
```py
myText = oGUI.Text(color, x, y, fontSize, "TextToDisplay")
```

To *render* the text, we must call its `.draw()` function. Usage:
```py
myText.draw()
```

We can also display a dropshadow for the text by calling the `.dropShadow()` function. Usage:
```py
myText.dropShadow(color, pixelOffset)
```

Additionally, we can change the font of the text by calling `.font()` Usage:
```py
myText.font('Roboto')
```
