import oGUI

oGUI.init()


def button_clicked():
    print('')
    print('button is clicked!')
    print('this massage would only appear once after the button is clicked')


def checkbox_status_changed():
    print('')
    print('checkbox status changed')
    print('now, checkbox is:', 'checked' if checkbox.is_enabled() else 'unchecked')
    print('this massage would only appear once after the checkbox is toggled')


def exit_button_clicked():
    exit(0)


window_x = 100
window_y = 100
window_w = 300
window_h = 500

rect = oGUI.Rect(oGUI.darkgray, window_x, window_y, window_w, window_h)
box = oGUI.Box(oGUI.lightgray, window_x, window_y, window_w, window_h, 5)
checkbox = oGUI.Checkbox(oGUI.gray, oGUI.orange, 125, 150, 20, 20, toggled_callback=checkbox_status_changed,
                         text='checkbox')
button = oGUI.Button(oGUI.gray, oGUI.orange, 120, 200, text='button', clicked_callback=button_clicked)
quit_button = oGUI.Button(oGUI.darkgray, oGUI.lightgray, 368, 103, 30, 35, clicked_callback=exit_button_clicked,
                          text='×')

myText = oGUI.Text(oGUI.orange, window_x + window_w / 2, window_y + 5, 30,
                   "overlayGUI by ethanedits", textAlign=1)

# DVDCJW

credit_text = oGUI.Text(oGUI.orange, window_x + window_w / 2, window_y + window_h / 2 - 20, 30,
                        'major overhaul by DVDCJW', textAlign=1, verticalAlign=1)
credit_text2 = oGUI.Text(oGUI.orange, window_x + window_w / 2, window_y + window_h / 2 + 20, 20, 'including:',
                         textAlign=1, verticalAlign=1)
credit_text3 = oGUI.Text(oGUI.orange, window_x + window_w / 2, window_y + window_h / 2 + 40, 25,
                         'CALLBACK for button and checkbox', textAlign=1, verticalAlign=1)
credit_text4 = oGUI.Text(oGUI.orange, window_x + window_w / 2, window_y + window_h / 2 + 60, 25, 'widgets upgrade',
                         textAlign=1, verticalAlign=1)
credit_text5 = oGUI.Text(oGUI.orange, window_x + window_w / 2, window_y + window_h / 2 + 80, 20,
                         'better checkbox hold logic', textAlign=1, verticalAlign=1)
credit_text6 = oGUI.Text(oGUI.orange, window_x + window_w / 2, window_y + window_h / 2 + 100, 20,
                         'integrated text for callable widgets', textAlign=1, verticalAlign=1)

# feel free to delete my credits if you're not comfortable with it.
# But I really made this project way more practical, efficient and maintainable

while True:
    oGUI.startLoop()  # Start of Draw Loop

    oGUI.update_gui()  # handle update and callback

    # maybe some of your own pygame code if you'd like

    oGUI.endLoop()  # End of Draw Loop

    checkbox.is_hovered(oGUI.lightgray)  # Changes color when checkbox and button(s) is hovered over
    button.is_hovered(oGUI.lightgray)
    quit_button.is_hovered(oGUI.gray)
