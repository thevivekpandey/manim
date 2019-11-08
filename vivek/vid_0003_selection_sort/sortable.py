from manimlib.imports import *
import numpy as np

class Sortable():
    def update_seq(self, target, pos):
        saved = self.seq[target]
        for i in range(target, pos, -1):
            self.seq[i] = self.seq[i - 1]
        self.seq[pos] = saved

    def target_move_up_and_left(self, target, pos):
        target_stick = self.items[self.seq[target]]

        target_stick.generate_target()
        target_stick.target.next_to(target_stick, 2 * UP)
        self.play(MoveToTarget(target_stick))

        shift = (target - pos) * self.multiple + self.delta
        target_stick.generate_target()
        target_stick.target.shift(shift * LEFT)
        self.play(MoveToTarget(target_stick))

    def target_move_down(self, target):
        target_stick = self.items[self.seq[target]]
        target_stick.generate_target()
        target_stick.target.next_to(target_stick, 2 * DOWN)
        self.play(MoveToTarget(target_stick))

    def intermediate_move(self, target, pos):
        # Intermediate elements to move to right
        for i in range(target - 1, pos - 1, -1):
            item = self.items[self.seq[i]]
            item.generate_target()
            item.target.shift(self.multiple * RIGHT)
            self.play(MoveToTarget(item))

    def target_move_right(self, target):
        target_stick = self.items[self.seq[target]]
        target_stick.generate_target()
        target_stick.target.shift(self.delta * RIGHT)
        self.play(MoveToTarget(target_stick))

    def move(self, target, pos):
        if self.adjust:
           self.target_move_up_and_left(target, pos)
           self.target_move_down(target)
           self.target_move_right(target)
           self.intermediate_move(target, pos)
        else:
           self.target_move_up_and_left(target, pos)
           self.intermediate_move(target, pos)
           self.target_move_down(target)
          
        self.update_seq(target, pos)


