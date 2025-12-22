
class LIFNeuron:
    def __init__(self, threshold=1.0, decay=0.95, reset=0.0, refractory=0):
        self.v = 0.0
        self.threshold = threshold
        self.decay = decay
        self.reset = reset
        self.refractory = refractory
        self.ref_count = 0

    def step(self, input_current):
        if self.ref_count > 0:
            self.ref_count -= 1
            return 0, self.v
        self.v = self.decay * self.v + input_current
        if self.v >= self.threshold:
            self.v = self.reset
            self.ref_count = self.refractory
            return 1, self.v
        return 0, self.v


class IFNeuron:
    def __init__(self, threshold=1.0, reset=0.0):
        self.v = 0.0
        self.threshold = threshold
        self.reset = reset

    def step(self, input_current):
        self.v += input_current
        if self.v >= self.threshold:
            self.v = self.reset
            return 1, self.v
        return 0, self.v


class IzhikevichNeuron:
    def __init__(self, a=0.02, b=0.2, c=-65, d=8):
        self.v = -65
        self.u = b * self.v
        self.a, self.b, self.c, self.d = a, b, c, d

    def step(self, I):
        v, u = self.v, self.u
        v += 0.5 * (0.04*v*v + 5*v + 140 - u + I)
        v += 0.5 * (0.04*v*v + 5*v + 140 - u + I)
        u += self.a * (self.b * v - u)
        spike = 0
        if v >= 30:
            self.v = self.c
            self.u = u + self.d
            spike = 1
        else:
            self.v, self.u = v, u
        return spike, self.v
