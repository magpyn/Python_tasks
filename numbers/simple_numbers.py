
def calculate_sum_via_list(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def run_example():
    numbers = [2, 3, 45, 6, 81, 22]
    result = calculate_sum_via_list(numbers)
    print(result)

if __name__ == '__main__':
    run_example()