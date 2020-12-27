inputs = [1.0, 2.0, 3.0, 2.5]
weights1 = [0.2, 0.8, -0.5, 1]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
weights = [weights1, weights2, weights3]
bias1 = 2
bias2 = 3
bias3 = 0.5
biases = [bias1, bias2, bias3]

def calculate_outputs():
    layer_outputs = [ [weightArr, bias] for weightArr,bias in zip(weights,biases) ]
    return layer_outputs

print(calculate_outputs())

