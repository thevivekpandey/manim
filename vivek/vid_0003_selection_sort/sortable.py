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
        target_stick.target.next_to(target_stick, 3 * UP)
        self.play(MoveToTarget(target_stick))

        shift = (target - pos) * self.multiple + self.delta
        target_stick.generate_target()
        target_stick.target.shift(shift * LEFT)
        self.play(MoveToTarget(target_stick))

    def target_move_down_and_right(self, target, pos):
        target_stick = self.items[self.seq[target]]

        target_stick.generate_target()
        target_stick.target.next_to(target_stick, 3 * DOWN)
        self.play(MoveToTarget(target_stick))

        shift = (pos - target) * self.multiple + self.delta
        target_stick.generate_target()
        target_stick.target.shift(shift * RIGHT)
        self.play(MoveToTarget(target_stick))

    def target_move_down(self, target):
        target_stick = self.items[self.seq[target]]
        target_stick.generate_target()
        target_stick.target.next_to(target_stick, 3 * DOWN)
        self.play(MoveToTarget(target_stick))

    def target_move_up_down(self, up, down):
        up_stick = self.items[self.seq[up]]
        up_stick.generate_target()
        up_stick.target.next_to(up_stick, 3 * UP)

        down_stick = self.items[self.seq[down]]
        down_stick.generate_target()
        down_stick.target.next_to(down_stick, 3 * DOWN)
        self.play(MoveToTarget(up_stick), MoveToTarget(down_stick))

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

    def move(self, target, pos, partial=False):
        if self.adjust:
           self.target_move_up_and_left(target, pos)
           self.target_move_down(target)
           self.intermediate_move(target, pos)
           self.target_move_right(target)
        else:
           self.target_move_up_and_left(target, pos)
           self.intermediate_move(target, pos)
           if not partial:
               self.target_move_down(target)
          
        if not partial:
            self.update_seq(target, pos)

    def move_left(self, start, num):
        for i in range(start, start + num):
            item = self.items[self.seq[i]]
            item.generate_target()
            item.target.shift(self.multiple * LEFT)
        arr = [MoveToTarget(self.items[self.seq[i]]) for i in range(start, start + num)]
        arr.extend([FadeOut(self.tot), FadeOut(self.b1), FadeOut(self.cross)])
        self.play(*arr)

    def swap(self, later, former):
        later_stick = self.items[self.seq[later]]
        former_stick = self.items[self.seq[former]]

        later_stick.generate_target()
        later_stick.target.next_to(later_stick, 3 * UP)
        former_stick.generate_target()
        former_stick.target.next_to(former_stick, 3 * DOWN)
        self.play(MoveToTarget(later_stick), MoveToTarget(former_stick))

        shift = (later - former) * self.multiple + self.delta

        later_stick.generate_target()
        later_stick.target.shift(shift * LEFT)
        former_stick.generate_target()
        former_stick.target.shift(shift * RIGHT)
        self.play(MoveToTarget(later_stick), MoveToTarget(former_stick))

        later_stick.generate_target()
        later_stick.target.next_to(later_stick, 3 * DOWN)
        former_stick.generate_target()
        former_stick.target.next_to(former_stick, 3 * UP)
        self.play(MoveToTarget(later_stick), MoveToTarget(former_stick))
        
        self.seq[later], self.seq[former] = self.seq[former], self.seq[later]
