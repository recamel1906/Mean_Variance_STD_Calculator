import numpy as np


def calculate(input_list):
    if len(input_list) < 9:
        raise ValueError("List must contain nine numbers.")

    # Split list into 3 lists with 3 elements
    list_split1 = [input_list[0], input_list[1], input_list[2]]
    list_split2 = [input_list[3], input_list[4], input_list[5]]
    list_split3 = [input_list[6], input_list[7], input_list[8]]
    list_split = [list_split1, list_split2, list_split3]

    # Convert list of 9 digits into 3x3 Numpy array
    matrix = np.array(list_split)

    calculations = {
        'mean': [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)),
                 list(matrix.mean().flatten(order='C'))[0]],

        'variance': [list(matrix.var(axis=0)), list(matrix.var(axis=1)),
                     list(matrix.var().flatten(order='C'))[0]],

        'standard deviation': [list(matrix.std(axis=0)), list(matrix.std(axis=1)),
                               list(matrix.std().flatten(order='C'))[0]],

        'max': [list(matrix.max(axis=0)), list(matrix.max(axis=1)),
                list(matrix.max().flatten(order='C'))[0]],

        'min': [list(matrix.min(axis=0)), list(matrix.min(axis=1)),
                list(matrix.min().flatten(order='C'))[0]],

        'sum': [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)),
                list(matrix.sum().flatten(order='C'))[0]]
    }
    return calculations
