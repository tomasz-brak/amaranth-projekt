from amaranth import *
from amaranth_boards.de10_lite import DE10LitePlatform

class Blink(Elaboratable):
    def elaborate(self, platform):
        m = Module()
        
        # Request built-in LEDR0 (Pin A8)
        led = platform.request("led", 0)
        timer = Signal(24)
        
        m.d.comb += led.o.eq(timer[22])
        m.d.sync += timer.eq(timer + 1)
        
        return m

def main():
    platform = DE10LitePlatform()
    platform.build(Blink(), do_program=False)

if __name__ == "__main__":
    main()
