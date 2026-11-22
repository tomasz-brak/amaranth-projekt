from amaranth import * # pyright: ignore[reportWildcardImportFromLibrary]
from amaranth.lib import enum

class Operation(enum.IntEnum , shape=8):
    LOAD=0
    STORE=1
    LDI=2
    ADD=3
    SUB=4
    NAND=5
    SHR=6
    JZ=7
    JS=8
    JMP=9
    PUSH=10
    POP=11
    PASS_A=12
    PASS_B=13



