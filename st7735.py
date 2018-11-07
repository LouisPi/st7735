from luma_driver import LumaScreen
from luma.lcd.device import st7735

from output.output import OutputDevice

class Screen(LumaScreen, OutputDevice):
  def init_display(self, autoscroll=False, **kwargs):
      self.device = st7735(self.serial, width=128, height=128, bgr=True, h_offset=1, v_offset=2)
