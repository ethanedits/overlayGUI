import oGUI

oGUI.init()

checkbox = oGUI.Checkbox(oGUI.gray, oGUI.orange, 125, 150, 20, 20)
rect = oGUI.Rect(oGUI.darkgray, 100, 100, 300, 500)
box = oGUI.Box(oGUI.lightgray, 100, 100, 300, 500, 5)
myText = oGUI.Text(oGUI.orange, 195, 110, 30, "oGUI Demo")
myText2 = oGUI.Text(oGUI.orange, 155, 152, 25, "Checkbox")

while True:

    oGUI.startLoop()

    rect.draw()
    box.draw()
    checkbox.draw()
    myText.font('Roboto')
    myText.draw()
    myText2.font('Roboto')
    myText2.draw()

    oGUI.endLoop()

    checkbox.is_hovered(oGUI.lightgray)

    myText.dropShadow(oGUI.black, 2)
    myText2.dropShadow(oGUI.black, 2)

    if checkbox.is_enabled():
        print('Checkbox is Enabled!')
