
class STDP:
    def __init__(self, lr=0.01, w_min=0.0, w_max=2.0):
        self.lr = lr
        self.w_min = w_min
        self.w_max = w_max

    def update(self, w, pre_spike, post_spike):
        if pre_spike and post_spike:
            w += self.lr
        elif pre_spike and not post_spike:
            w -= self.lr * 0.5
        return min(max(w, self.w_min), self.w_max)
