'''
Your First Task:
Try to manually calculate what happens when:

Input: [2, 3]
Weights: [0.5, -0.3]
Bias: 0.1
Activation: Sigmoid

Calculate: sigmoid(0.5*2 + (-0.3)*3 + 0.1) '''

import math

def sigmoid(x):
    res = 1 / (1 + math.e**(-x))
    return res

Inp = [2,3]
W = [0.5, -0.3]
B = 0.1

def n1(Input, Weights, Bias):
    x = sum(i*w for i,w in zip(Input,Weights)) + Bias
    return(sigmoid(x))

print(n1(Inp, W, B))