import oGUI

oGUI.init()

checkbox = oGUI.Checkbox(oGUI.gray, oGUI.orange, 125, 150, 20, 20)

while True:

    oGUI.startLoop()

    oGUI.drawRect(oGUI.darkgray, 100, 100, 300, 500)
    oGUI.drawBox(oGUI.lightgray, 100, 100, 300, 500, 5)
    checkbox.draw()

    oGUI.endLoop()

    checkbox.is_hovered(oGUI.lightgray)
    if checkbox.is_enabled():
        print('Checkbox is Enabled!')