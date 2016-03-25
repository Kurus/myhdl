from myhdl import *
from myhdl.conversion import analyze

def dff(t,q, d, clk):
    @always(clk.posedge)
    def toggle():
        q.next =not q
    def store():
        q.next= d
    if t==1 :
        return logic
    else return store


from random import randrange

def test_dff():    
    q, d= [[Signal(bool(0)) for i in range(3)] for i in range(2)]
    clk = [Signal(bool(0)) for i in range(3)]  
    counter = [dff(q, d, clk) for i in range(2)]
    @always(delay(10))
    def clkgen():
        clk.next = not clk
    @always(clk.negedge)
    def stimulus():
        d.next = randrange(2)
    return dff_inst, clkgen, stimulus

def simulate(timesteps):
    traceSignals.timescale = "1ps"
    tb = traceSignals(test_dff)
    sim = Simulation(tb)
    sim.run(timesteps)

s=Simulation(test_dff())
s.run(2000)
def convert():
    q, d, clk = [Signal(bool(0)) for i in range(3)]
    toVerilog(dff, q, d, clk)
    analyze(dff, q, d, clk)
 
convert()
    
