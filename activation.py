#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: activation.py

import numpy as np


def sigmoid(z):
#"""The sigmoid function."""
    sigm = 1. / (1. + np.exp(-z))
    return sigm

def sigmoid_prime(z):
#    """Derivative of the sigmoid function."""
    sigm = 1. / (1. + np.exp(-z))
    sigm_prime = sigm * (1. - sigm)
    return (sigm_prime)

