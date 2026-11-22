from amaranth import * # pyright: ignore[reportWildcardImportFromLibrary]
from amaranth.lib import enum
from amaranth_boards.de10_lite import DE10LitePlatform

register_size: int = 16

class Blink(Elaboratable):
    def elaborate(self, platform):
        m = Module()
        regs = [Signal(register_size) for x in range(10)]
        pc = Signal(16);

        opArg1 = Signal(register_size)
        opArg1 = Signal(register_size)
        return m




class Alu(Elaboratable):
    def elaborate(self, platform):
        m = Module()



def main():
    platform = DE10LitePlatform()
    platform.build(Blink(), do_program=False)

if __name__ == "__main__":
    main()
