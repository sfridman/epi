from collections import Counter, OrderedDict

from test_framework import generic_test


# O(Nlog(N)) from sorting
def h_index(citations):
    counter = Counter(citations)  # Dictionary
    ordered = OrderedDict(sorted(counter.items()))
    big_equal = [(c, sum([v for k, v in ordered.items() if k >= c])) for c in ordered.keys()]
    print(big_equal)

    # TODO: No need to iterate over all since it is sorted - can find first
    try:
        result = max(list(map(min, big_equal)))
    except ValueError:
        result = 0
    return result
    # Max(Min(pair))
    # try:
    #     result = next(v-1 for k, v in big_equal if v < k)
    # except StopIteration:
    #     result = 0
    # return result


if __name__ == '__main__':
    print(h_index([]))
    exit(generic_test.generic_test_main("h_index.py", 'h_index.tsv', h_index))
