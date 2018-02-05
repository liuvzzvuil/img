#!/usr/bin/env python
# -*- coding: utf-8 -*-

from train import get_guess
guess_obj = get_guess()
xx = guess_obj.predict([[1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 2]*20])
print(xx)
