import time, random, framebuf
import ssd1306
from machine import Pin, SoftI2C
time.sleep(0.1) # Wait for USB to become ready

print("Coin Flipper by Vivaan")

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)

def show(oled, msg, scale=1):
    oled.fill(0)
    w = len(msg) * 8 * scale
    big_text(oled, msg, (128 - w) // 2, (64 - 8 * scale) // 2, scale)
    oled.show()

def big_text(oled, msg, x, y, scale):
    w = len(msg) * 8
    fb = framebuf.FrameBuffer(bytearray(w), w, 8, framebuf.MONO_VLSB)
    fb.text(msg, 0, 0, 1)
    for cx in range(w):
        for cy in range(8):
            if fb.pixel(cx, cy):
                oled.framebuf.fill_rect(x + cx * scale, y + cy * scale, scale, scale, 1)

def flip(oled):
  print("flipping coin...")
  random.seed(time.ticks_us())
  show(oled, ' ')
  for i in range(10):                  # quick "spinning" animation
      show(oled, "HEADS" if i % 2 else "TAILS", 2)
      time.sleep(0.025 + i * 0.03)
      show(oled, "-----", 2)
      time.sleep(0.025 + i * 0.03)
  chosen = 'HEADS' if random.randint(0, 1) == 0 else 'TAILS'


  show(oled, chosen, 3)

show(oled, "Flip a Coin", 1)

while True:
  if button.value() == 1:
    flip(oled)
    while button.value() == 1:
      time.sleep(0.01)
    time.sleep(0.01)


