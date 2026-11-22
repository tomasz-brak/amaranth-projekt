from amaranth.sim import Simulator, Period, SimulatorContext

from hello_amaranth.alu import ALU
from hello_amaranth.isa import Operation 

dut = ALU()
async def bench(ctx: SimulatorContext):
    ctx.set(dut.opSelect, Operation.ADD)
    ctx.set(dut.a, 10)
    ctx.set(dut.b, 5)
    ctx.set(dut.ldf, 1)

    await ctx.tick().repeat(1)
    ctx.set(dut.ldf, 0)
    await ctx.tick().repeat(1)

    ctx.set(dut.a, 10)
    ctx.set(dut.b, 11)
    await ctx.tick().repeat(1)

    ctx.set(dut.ldf, 1)

    await ctx.tick().repeat(1)

if __name__ == "__main__":
    sim = Simulator(dut)
    sim.add_clock(Period(MHz=1))
    sim.add_testbench(bench)
    with sim.write_vcd("alu.vcd"):
        sim.run()
