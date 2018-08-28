from test_framework import generic_test

h = {
    0b0000: 0,
    0b0001: 1,
    0b0010: 1,
    0b0011: 0,
    0b0100: 1,
    0b0101: 0,
    0b0110: 0,
    0b0111: 1,
    0b1000: 1,
    0b1001: 0,
    0b1010: 0,
    0b1011: 1,
    0b1100: 0,
    0b1101: 1,
    0b1110: 1,
    0b1111: 0
}


def parity_lookup(num):
    """
    Using a small hash for 4 bits - 16 values - and predetermined parity
    :param num - 4 bits
    :return:
    """
    return h[num]


def parity(x):
    result = 0
    while x:
        result += parity_lookup(x & 0xf)
        x >>= 4
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
