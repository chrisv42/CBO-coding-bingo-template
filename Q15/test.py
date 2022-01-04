from colorama import Fore
from Q15_INSERTTEAMNUMBER import two_sum

TEST_INPUT = [
    [[2, 7, 11, 15], 9],
    [[3, 2, 4], 6],
    [[3, 3], 6],
    [[1, 0, 0, 1, 0, 1, 1, 1, 0], 1],
    [[7, 8, 9, 10, 11], 21],
    [[9, 3, 6], 9],
]
TEST_OUTPUT = [
    [[2, 7], [7, 2]],
    [[2, 4], [4, 2]],
    [[3, 3]],
    [[1, 0], [0, 1]],
    [[10, 11], [11, 10]],
    [[3, 6], [6, 3]],
]


def test_function():
    for inp, out in zip(TEST_INPUT, TEST_OUTPUT):
        res = two_sum(inp)
        error_message = ("Expected {} from input value {}, but got {}.").format(
            out, inp, res
        )
        assert res == out, Fore.RED + error_message
    print(Fore.GREEN + "All tests passed!")


def main():
    test_function()


if __name__ == "__main__":
    main()
