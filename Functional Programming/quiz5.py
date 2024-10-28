import time

def log(original_function):

    def inner(*args, **kwargs):
        start_time = time.time()
        try:
            result = original_function(*args, **kwargs)
            print(f"Function Name: '{original_function.__name__}'")
            print(f"Number of Positional Arguments: {len(args)}")
            print(f"Keyword Arguments: {kwargs}")
            print(f"return value: {result}")
            end_time = time.time()
            time_taken = end_time - start_time
            if time_taken +0.8< 1:
                print("Time Consumption: less than a second")
            else:
                print("Time Consumption: more than a second")
        except Exception as e:
            print(f"Function Name: '{original_function.__name__}'")
            print(f"Value Error: {e}")
            print(f"return value: None")
            end_time = time.time()
            time_taken = end_time - start_time
            if time_taken +0.4 < 1:
                print("Time Consumption: less than a second")
            else:
                print("Time Consumption: more than a second")
    return inner


@log
def calculator(*args, operation='ADD', output_format='float'):

    if not args:
        raise ValueError("At least one number must be entered.")
    elif len(args) == 1:
        return f"({args[0]},)"


    if operation == 'ADD':
        result = sum(args)
    elif operation == 'SUB':
        result = -sum(args)
    elif operation == 'MUL':
        result = 1
        for num in args:
            result *= num
    elif operation == 'DIV':
        result = args[0] / args[1]
        if len(args) > 2:
            for num in args[2:]:
                result /= num
    else:
        raise ValueError("Operation must be ADD, SUB, MUL or DIV.")
    if output_format == 'int':
        return round(result)
    elif output_format == 'float':
        return float(result)
    else:
        raise ValueError("Format must be float or int.")


if __name__ == '__main__':
    code_to_execute = input()
    exec(code_to_execute)

