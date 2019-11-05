from manimlib.imports import *
import numpy as np

class Sortable():
    def __init__(self, seq, items):
        self.seq = seq
        self.items = items

    def update_seq(self, target, pos):
        saved = self.seq[target]
        for i in range(target, pos, -1):
            self.seq[i] = self.seq[i - 1]
        self.seq[pos] = saved

    def move(self, target, pos):
        target_stick = self.items[self.seq[target]]
        pos_stick = self.items[self.seq[pos]]

        target_stick.generate_target()
        target_stick.target.next_to(target_stick, 2 * UP)
        self.play(MoveToTarget(target_stick))

        target_stick.generate_target()
        target_stick.target.next_to(pos_stick, 0.8* LEFT + 2 * UP)
        self.play(MoveToTarget(target_stick))

        target_stick.generate_target()
        target_stick.target.next_to(pos_stick, 0.8* LEFT)
        self.play(MoveToTarget(target_stick))

        self.items[self.seq[target - 1]].generate_target()
        self.items[self.seq[target - 1]].target.next_to(self.items[self.seq[target - 1]], RIGHT, buff=0.6*LARGE_BUFF )
        self.play(MoveToTarget(self.items[self.seq[target - 1]]))

        for i in range(target - 2, pos - 1, -1):
            self.items[self.seq[i]].generate_target()
            self.items[self.seq[i]].target.next_to(self.items[self.seq[i + 1]], LEFT, buff=0.6*LARGE_BUFF )
            self.play(MoveToTarget(self.items[self.seq[i]]))
         
        target_stick.generate_target()
        target_stick.target.next_to(pos_stick, LEFT, buff=0.6*LARGE_BUFF )
        self.play(MoveToTarget(target_stick))
        self.update_seq(target, pos)
