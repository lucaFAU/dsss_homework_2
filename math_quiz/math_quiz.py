import random

def get_random_int(min, max):
    """
    Get a Random integer
    Parameters
    ----------
    min: float
        minimum value of the intervall to choose the random number
    max: float
        maximum value of the intervall to choose the random number
    Returns
    ---------
    int
        random number in the intervall (min, max)
    """
    try:
        rand_num = random.randint(min, max)
    except:
        max = int(max)
        min = int(min)
        rand_num = random.randint(min, max)
    return rand_num

def get_random_operator():
    """
    Randomly chooses a operator from [+, -, *]
    Returns
    ---------
    string
        randomly choosen charater
    """
    return random.choice(['+', '-', '*'])


def perform_operation(n1, n2, o):
    """
     Perform the operation

    Parameters
    ----------
    n1, n2: float
        two numbers to perform the operation on
    o: string
        operation that should be performed
    Returns
    ---------
    p: string
        combines the operation as string
    a: float
        result of the operation
    """
    # create string of the function to calculate
    p = f"{n1} {o} {n2}"
    #perform the operation
    if o == '-': a = n1 - n2
    elif o == '+': a = n1 + n2
    else: a = n1 * n2
    return p, a


def math_quiz():
    s = 0
    t_q = 3#3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = get_random_int(1, 10); n2 = get_random_int(1, 5.5); o = get_random_operator()
        PROBLEM, ANSWER = perform_operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
