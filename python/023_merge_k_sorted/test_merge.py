from dataclasses import dataclass

from merge import Solution, make_list, collect_list


@dataclass
class Case:
    input: list[list[int]]
    expected: list[int]


cases = [
    Case(
        input=[
            [1, 4, 5],
            [1, 3, 4],
            [2, 6],
        ],
        expected=[1, 1, 2, 3, 4, 4, 5, 6],
    ),
    Case(input=[], expected=[]),
    Case(input=[[]], expected=[]),
]

solution = Solution()


def test_merge():
    for case in cases:
        input = [make_list(arr) for arr in case.input]
        output = solution.mergeKLists(input)
        assert collect_list(output) == case.expected


def test_merge2():
    for case in cases:
        input = [make_list(arr) for arr in case.input]
        output = solution.mergeKListsV2(input)
        assert collect_list(output) == case.expected


def test_merge3():
    for case in cases:
        input = [make_list(arr) for arr in case.input]
        output = solution.mergeKListsV3(input)
        assert collect_list(output) == case.expected


def test_merge_cheat():
    for case in cases:
        input = [make_list(arr) for arr in case.input]
        output = solution.mergeKListsVCheat(input)
        assert collect_list(output) == case.expected


bench_input = [make_list(list(range(0, 100))) for _ in range(100)]


def test_merge_benchmark(benchmark):
    _ = benchmark(Solution().mergeKLists, bench_input)


def test_merge_benchmark2(benchmark):
    _ = benchmark(Solution().mergeKListsV2, bench_input)


def test_merge_benchmark3(benchmark):
    _ = benchmark(Solution().mergeKListsV3, bench_input)


def test_merge_benchmark_cheat(benchmark):
    _ = benchmark(Solution().mergeKListsVCheat, bench_input)
