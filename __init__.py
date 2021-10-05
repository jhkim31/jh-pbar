import sys
import math

class jh_pbar:
    def __init__(self, steps, size=20, prefix='', postfix='', color=0):
        self.size = size
        self.steps = steps
        self.update_step = self.steps / self.size
        self.count = 0
        self.progress_bar_origin = '-' * size
        self.progress_bar = self.progress_bar_origin
        self.progress = 1
        self.prefix = prefix
        self.postfix = postfix
        self.result = self.prefix + ' ' + self.progress_bar + ' ' + self.postfix

        self.font_color_end = '\033[0m'
        self.font_color = ''
        if color == 0:
            self.font_color = ''
        elif color == 1:  # red
            self.font_color = '\033[31m'
        elif color == 2:  # green
            self.font_color = '\033[32m'
        elif color == 3:  # blue
            self.font_color = '\033[34m'

    def update(self, count=1, prefix='', postfix=''):
        self.count += count
        if prefix != '':
            self.prefix = prefix
        if postfix != '':
            self.postfix = postfix

        self.progress = math.ceil(self.count / self.update_step)

        self.progress_bar = self.progress_bar_origin.replace('-', '▉', self.progress)

        self.result = f'{self.font_color}{self.prefix} {self.progress_bar} {self.postfix}{self.font_color_end}'
        sys.stdout.write('\r' + self.result)
        sys.stdout.flush()
        if self.count == self.steps:
            print()

    def reset(self, progress=1, prefix='', postfix=''):
        self.progress = progress
        self.progress_bar = '-' * self.size

        if prefix != '':
            self.prefix = prefix
        if postfix != '':
            self.postfix = postfix

        self.result = self.prefix + ' ' + self.progress_bar + ' ' + self.postfix
