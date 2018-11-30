import pandas as pd

# User input for W and b
weight1 = float(input("weight 1: "))
weight2 = float(input("weight 2: "))
bias = float(input("bias: "))

test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_or_outputs = [False, True, True, True]
correct_and_outputs = [False, False, False, True]
or_outputs = []
and_outputs = []


for test_input, correct_or_output, correct_and_output in zip(test_inputs, \
        correct_or_outputs, correct_and_outputs):
    linear_combination = weight1 * test_input[0] + weight2 * test_input[1] \
        + bias
    output = int(linear_combination > 0)
    is_correct_or_string = 'Yes' if output == correct_or_output else 'No'
    is_correct_and_string = 'Yes' if output == correct_and_output else 'No'
    or_outputs.append([test_input[0], test_input[1], linear_combination,\
        output, is_correct_or_string])
    and_outputs.append([test_input[0], test_input[1], linear_combination,\
        output, is_correct_and_string])


num_or_wrong = len([or_output[4] for or_output in or_outputs \
        if or_output[4] == 'No'])
num_and_wrong = len([and_output[4] for and_output in and_outputs \
        if and_output[4] == 'No'])


output_or_frame = pd.DataFrame(or_outputs, columns=['Input 1', 'Input 2', \
    'Linear Combination', 'Activation Output', 'Is Correct'])
output_and_frame = pd.DataFrame(and_outputs, columns=['Input 1', 'Input 2', \
    'Linear Combination', 'Activation Output', 'Is Correct'])


if not num_or_wrong:
    print("Well done! You got it all correct and its an OR Perceptron")
    print(output_or_frame.to_string(index=False))
elif not num_and_wrong:
    print("Well done! You got it all correct and its an AND Perceptron")
    print(output_and_frame.to_string(index=False))
else:
    if num_or_wrong > num_and_wrong:
        print("You got {} less wrong for OR Perceptron compare to AND \
              Perceptron".format(num_or_wrong - num_and_wrong))
    elif num_or_wrong < num_and_wrong:
        print("You got {} less wrong for AND Perceptron compare to OR \
              Perceptron.".format(num_and_wrong - num_or_wrong))
    else:
        print("You got equal wrongs for both OR and AND Perceptrons")


