import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)

print("Iniciando modulo abra un bloc de notas")
time.sleep(5)

print("Escribiendo")
kbd.send(Keycode.SHIFT, Keycode.H)
kbd.send(Keycode.O)
kbd.send(Keycode.L)
kbd.send(Keycode.A)

layout = KeyboardLayoutUS(kbd)
layout.write('\nHola mundo desde la raspberry\n')


kbd.release_all()