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
  ...
  oGUI.endLoop()
```

*Inbetween* the `start` and `end` loop, you should execute the update_gui() *ONCE*.
Then it will render all the gui and handle the callbacks for you

*Here is an example:*
```py
checkbox = oGUI.Checkbox(oGUI.gray, oGUI.orange, 125, 150, 20, 20)

while True:
    oGUI.startLoop()
    
    oGUI.update_gui()

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

**Creating widgets**
---------------------
e.g. Creating *checkboxes*

To create a **checkbox**, we can create a variable and then call the `oGUI.Checkbox()` function. Usage:
```py
checkbox1 = oGUI.Checkbox(outsideColor, insideColor, x position, y position, width, height, enabledByDefault, callback_function)
```
enabledByDefault is optional, and if you leave it blank (dont specify it), it will be false.

We will continue to use *checkbox1* as the *checkbox variable* for the rest of the documentation, and the *rest of these functions* should be called in an **infinite loop.**

To *render* the actual checkbox, ~~we must call its `.draw()` function~~
Now, you will only have to run the update_gui() **ONCE** and it will draw *ALL* the widgets you've created(as long as they're not hidden) for you.
So idealy, you won't have to call the draw function manually.
Usage:
```py
while True:
    oGUI.startLoop()
    
    oGUI.update_gui()

    oGUI.endLoop()
```
for more widgets creation, goto [example.py](examples/example.py)

**
We need to put this function inbetween of our `startLoop()` and `endLoop()`.

**Callbacks**
---------------------
call back is the core of a gui. This allows a funciton to be called once a widget is interacted in a certain way.
e.g.
```py
import oGUI

oGUI.init()


def button_clicked():
    print('I am clicked')

button = oGUI.Button(oGUI.blue, oGUI.white, 400, 300, 100, 30, text='click me', clicked_callback=button_clicked)

while True:
    oGUI.startLoop()  # Start of Draw Loop

    oGUI.update_gui()  # handle update and callback

    oGUI.endLoop()  # End of Draw Loop
```
The function *button_clicked* will be executed everytime the button is clicked.
However, the function will be run in the main thread defaultly, 
this means the rest of the program and the mainloop would have to wait for the called function to finish.
So if the function takes up a considerable amount of time, the gui will noticibly stop responding. 
To fix this, use multithread libs, so that the callback function and the maintheard can run simultaneously.

Notice that you WON'T want the brackets if you're defining the callback, 
Just like in the example, we used button_clicked NOT button_clicked().
The reason is that if you use *funciton*, the function itself will be passed on to the callback
On the contrary, if you use *function()*, the function itself will be executed and its return will be passed on to the callback.
Normally, we don't want this to happen.

More examples of callback can be found in the [example.py](examples/example.py)

**Malipulating widgets**
---------------------
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
