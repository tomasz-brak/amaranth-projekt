from amaranth import * # pyright: ignore[reportWildcardImportFromLibrary]
from .isa import Operation

class Register(Elaboratable):
    def __init__(self) -> None:
        self.data_memory = Signal(16)
        self.bb = Signal(16)
        self.bc = Signal(16)
        self.addr = Signal(32)
        self.dest_selector = Signal(16)
        self.program_counter = Signal(32)
        self.stack_pointer = Signal(32)
        self.sid = Signal(3) # Increment/Decrement Control
        self.addr_plexer_selctor = Signal(2)
        self.write_enable = Signal()
