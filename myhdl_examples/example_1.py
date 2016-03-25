from myhdl import *


def tff(t,q, d, clk):
    @always(clk.posedge)
    def toggle():
        q.next =not q
    def store():
        q.next= d
    if t==1 :
        return logic
    else:
        return store
