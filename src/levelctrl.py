
class LevelCtrl:
    DRUM = 0
    TRACK = 1
    def __init__(self):
        self.mode = LevelCtrl.DRUM
        self.levels = [50,100]
    def increase(self) :
        self.levels[self.mode] = self.levels[self.mode] + 1
        if self.levels[self.mode] >= 100:
            self.levels[self.mode] = 100
        return self.levels[self.mode]
    def decrease(self):
        self.levels[self.mode] = self.levels[self.mode] - 1
        if self.levels[self.mode] <= 1:
            self.levels[self.mode] = 1
        return self.levels[self.mode]
    def toggle_mode(self):
        if self.mode is self.DRUM:
            self.mode = self.TRACK
        else :
            self.mode = self.DRUM
    def curr_mode(self):
        return self.mode
    def curr_level(self):
        return self.levels[self.mode]
    
