from manimlib.imports import *

class Coin(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.coin = Circle()
        self.coin.set_width(0.7)
        self.face = TextMobject("H")
        self.face.move_to((self.coin.get_x(), self.coin.get_y(), 0))
        self.add(self.coin, self.face)

    def set_face(self, v):
        t = TextMobject(v)
        t.move_to((self.coin.get_x(), self.coin.get_y(), 0))
        return Transform(self.face, t)

class Tosser():
    def __init__(self):
        self.elems = ['H', 'T', 'T', 'H', 'H', 'H']

    def get_next(self):
        for e in self.elems:
            yield e

class CoinToss(Scene):
    def toss_coin(self, coin, face):
       seq = ["T", "H"] * 3
       if face == "T":
           seq.append(face)

       for e in seq:
           self.play(coin.set_face(e), run_time=0.1)

    def construct(self):
       coin = Coin() 
       coin.to_edge(TOP + LEFT)
       self.play(Write(coin))

       tosser = Tosser()
       prev = None
       for face in tosser.get_next():
           self.toss_coin(coin, face)
           new = TextMobject(face).scale(2)
           if prev:
               new.next_to(prev, RIGHT)
           else:
               new.to_edge(LEFT)
           prev = new
           self.play(Write(new))
