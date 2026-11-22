from amaranth import * # pyright: ignore[reportWildcardImportFromLibrary]
from .isa import Operation

class ALU(Elaboratable):
    def __init__(self) -> None:
        self.a = Signal(signed(16))
        self.b = Signal(signed(16))
        self.opSelect = Signal(5)
        self.ldf = Signal()
        self.y = Signal(16)
        self.carry = Signal()
        self.zero = Signal()
        self.sign = Signal()
        self.parity = Signal()

    def elaborate(self, platform):
        m = Module()
        res = Signal(17)

        with m.Switch(self.opSelect):
            with m.Case(Operation.ADD): m.d.comb += res.eq(self.a + self.b)
            with m.Case(Operation.SUB): m.d.comb += res.eq(self.a - self.b)
            with m.Case(Operation.NAND): m.d.comb += res.eq(~(self.a & self.b))
            with m.Case(Operation.SHR): m.d.comb += res.eq(self.a >> 1)
            with m.Default(): m.d.comb += res.eq(self.a)

        m.d.comb += self.y.eq(res[0:16])

        # Set flags

        with m.If(self.ldf):
            m.d.sync += [
                self.zero.eq(res[0:16]==0),
                self.sign.eq(res[15]),
                self.carry.eq(res[16]^res[15]),
                self.parity.eq(~res[0:16].xor())
            ]
        return m
