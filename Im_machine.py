
class dvigateli:
    def __init__(self,ves,max_speed,potreb):
        self.ves = ves
        self.max_speed = max_speed
        self.potreb = potreb

class bak:
    def __init__(self,ves,V_baka):
        self.ves = ves
        self.V_baka = V_baka

class tormoz:
    def __init__(self,ves,efect_tormoz):
        self.ves = ves
        self.efect_tormoz = efect_tormoz

class kyzov:
    def __init__(self,ves):
        self.ves  = ves

class Machine:
    def __init__(self,name,dvigateli=None,bak=None,tormoz=None,kyzov=None):
        self.name = name
        self.dvigateli = dvigateli
        self.bak = bak
        self.tormoz = tormoz
        self.kyzov = kyzov
        self.ves = 0
        self.Max_xod = 0
        self.tormoz_pyt = 0

    def ves_sun(self):
        self.ves =  self.dvigateli.ves + self.bak.ves + self.tormoz.ves + self.kyzov.ves

    def max_xod_sum(self):
        self.Max_xod = (self.dvigateli.max_speed * self.bak.V_baka) / self.dvigateli.potreb

    def tormoz_pyt_sum(self):
        self.tormoz_pyt = self.ves * self.tormoz.efect_tormoz


class Builder:
    def builder(self,name,dvigateli,bak,tormoz,kyzov):
        machine = Machine(name,dvigateli,bak,tormoz,kyzov)
        machine.ves_sun()
        machine.max_xod_sum()
        machine.tormoz_pyt_sum()
        return machine


Builder = Builder()

dvigateli_ = dvigateli(500,200,10)
bak_  = bak(100,50)
tormoz_ = tormoz(200,0.5)
kyzov_ = kyzov(1000)

machine = Builder.builder("fdsfsdf",dvigateli_,bak_,tormoz_,kyzov_)

print(machine.ves,machine.name,machine.tormoz_pyt)



