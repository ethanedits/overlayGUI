import oGUI

oGUI.init()

checkbox = oGUI.Checkbox(oGUI.gray, oGUI.orange, 125, 150, 20, 20)
rect = oGUI.Rect(oGUI.darkgray, 100, 100, 300, 500)
box = oGUI.Box(oGUI.lightgray, 100, 100, 300, 500, 5)

while True:

    oGUI.startLoop()

    rect.draw()
    box.draw()
    checkbox.draw()

    oGUI.endLoop()

    checkbox.is_hovered(oGUI.lightgray)
    if checkbox.is_enabled():
        print('Checkbox is Enabled!')
