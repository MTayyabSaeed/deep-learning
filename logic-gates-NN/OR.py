import pandas as pd

# unlike AND, the weights must me either increasesd or bias is decreased
weight1 = 1.5
weight2 = 1.1
bias = 0.0

# Inputs and outputs
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [False, True, True, True]
outputs = []

# Generate and check output
for test_input, correct_output in zip(test_inputs, correct_outputs):
    linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + \
        bias
    # either take the bias negative or don't include 0
    output = int(linear_combination > 0)
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0], test_input[1], linear_combination, output,\
        is_correct_string])


output_frame = pd.DataFrame(outputs, columns=['Input 1', 'Input 2', \
        'Linear Combination', 'Activation', 'Is Correct'])

num_wrong = len([output[4] for output in outputs if output[4] == 'No'])

if not num_wrong:
    print('Nice! You got it all correct')
else:
    print('You got {} wrong.'.format(num_wrong))

print(output_frame.to_string(index=False))
