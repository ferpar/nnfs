# basic neuron information
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

def calc_neuron():
    output = ( inputs[0]*weights[0] +
        inputs[1]*weights[1] +
        inputs[2]*weights[2] +
        inputs[3]*weights[3] + bias )
    return output

print(calc_neuron())
