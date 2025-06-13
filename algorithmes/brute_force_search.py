"""
Title: 全探索(1) brute force search / exhaustive search
Link: -
Remarks:
"""

import random
import sys


def linear_search(n: list[int], v: int) -> bool:
    """linear searchは1つ1つの値を精査する

    Args:
        n (list[int]): 探索されるデータ
        v (int): 探索データ

    Returns:
        bool: 探索判定結果

    Problem:
        Nこの整数(a1, a2...aN-1)と整数値vが与えられます。
        ai=vとなるデータが存在するか判定する。

    TimeOrder: O(N)
    SpaceOrder: O(1)

    Remarks:
        現在の実装は線形探索（O(N)）である。※データがソートされている場合は二分探索（O(log N)）に変更することで高速化可能。
        ループ内で使用される一時変数（i）の数は固定であり、入力サイズに依存して増加しないため、使用するメモリ量はO(1)になる。
    """
    for i in n:
        if i == v:
            return True

    return False


def linear_search_index(n: list[int], v: int) -> int:
    """
    Args:
        n (list[int]): 探索されるデータ
        v (int): 探索データ

    Returns:
        int: 探索判定結果(インデックス or -1)

    Problem:
        Nこの整数(a1, a2...aN-1)と整数値vが与えられます。
        ai=vとなるデータが存在するか判定し、そのインデックスを返す。ない場合は-1を返す。

    TimeOrder: O(N)
    SpaceOrder: O(1)

    Remarks:
        現在の実装は線形探索（O(N)）である。※データがソートされている場合は二分探索（O(log N)）に変更することで高速化可能。
        ループ内で使用される一時変数（i）の数は固定であり、入力サイズに依存して増加しないため、使用するメモリ量はO(1)になる。
    """
    for i in range(len(n)):
        if n[i] == v:
            return i

    return -1


def linear_search_find_min(n: list[int]) -> int:
    """
    Args:
        n (list[int]): 探索されるデータ

    Returns:
        int: 最小値

    Problem:
        Nこの整数(a1, a2...aN-1)が与えられます。
        最小となる値返しす。

    TimeOrder: O(N)
    SpaceOrder: O(1)

    Remarks:
        現在の実装は線形探索（O(N)）である。※データがソートされている場合は二分探索（O(log N)）に変更することで高速化可能。
        ループ内で使用される一時変数（min_num, i）の数は固定であり、入力サイズに依存して増加しないため、使用するメモリ量はO(1)になる。

    """

    min_num = sys.maxsize
    for i in n:
        if i < min_num:
            min_num = i

    return min_num


def linear_search_pair_find_min(k: int, n: list[int], m: list[int]) -> int:
    """
    Args:
        k (int): ターゲットとなる最小値
        n (list[int]): 探索されるデータ1
        m (list[int]): 探索されるデータ2

    Returns:
        int: 最小値

    Problem:
        N個の整数のn0,n1...nN-1とN個の整数のm0,m1...mN-1が与えられる。
        2組の整数列からぞれぞれ1つずつの整数を選んで和を取る。その和として考えられるうち、整数k以上の範囲内で最小値を求める。
        ただし、ni + mj >= Kを満たすような(i, j)の組みが1つ以上存在するものとする

    TimeOrder: O(N^2)
    SpaceOrder: O(1)

    Remarks:
        ネストのfor文でi, jにアクセスしているためO(N^2)で実装されている状態。
        ループ内で使用される一時変数（min_num, sum_num, i, j）の数は固定であり、入力サイズに依存して増加しないため、使用するメモリ量はO(1)になる。

        continueにした方が処理の明確化やCPUの分岐予測が向上するようなので、そこは改めて調査理解する
        ToDo:分岐予測について
        https://ja.wikipedia.org/wiki/%E5%88%86%E5%B2%90%E4%BA%88%E6%B8%AC
    """
    min_num = sys.maxsize
    for i in range(len(n)):
        for j in range(len(m)):
            sum_num = n[i] + m[j]
            # if sum_num < k:
            #     continue
            if sum_num >= k and sum_num < min_num:
                min_num = sum_num

    return min_num


def linear_search_find_toral_match(w: int, n: list[int]) -> bool:
    """
    Args:
        w (int): 探索対象の総和
        n (list[int]): 探索されるデータ

    Returns:
        bool: 総和になり得る部分集合があるか

    Problem:
        N個の正の整数a0, a1,...an-1と正の整数Wが与えられます。
        a0, a1,...an-1の中から何個かの整数を選んで総和をWとすることができるか判定する。

    TimeOrder: O(N*2^N)
    SpaceOrder: O(1)

    Remarks:
        bit演算で対象の有無を判断しているため、パターンは2通り(2^N)。そこから入力数分かかるためO(N*2^N)となる。
        ループ内で使用される一時変数（bit, sum_num, i）の数は固定であり、入力サイズに依存して増加しないため、使用するメモリ量はO(1)になる。
    """
    for bit in range(1 << len(n)):
        sum_num = 0
        for i in range(len(n)):
            if bit & (1 << i):
                sum_num += n[i]

        if sum_num == w:
            return True

    return False


# ==============================実装お試し=================================
RAND_START = 1
RAND_END = 10


def generate_random(target_range: tuple = (RAND_START, RAND_END)):
    return random.randint(*target_range)


d = generate_random()
n = [generate_random() for _ in range(d)]
v = generate_random()

# 線形探索(ランダムな値)
print(f"入力: {n=}, {v=}")
print(f"{linear_search(n, v)=}")
print(f"{linear_search_index(n, v)=}")
print(f"{linear_search_find_min(n)=}")

# 線形探索(固定した入力)
# print("linear_search_pair_find_minで使用するN, Kを入力してください")
# N, K = map(int, input().split())
# print("aを入力してください")
# a = [int(input()) for _ in range(N)]
# print("bを入力してください")
# b = [int(input()) for _ in range(N)]
# print(f"{linear_search_pair_find_min(K, a, b)=}")

print("linear_search_find_toral_matchで使用するN, Wを入力してください")
N, W = map(int, input().split())
print("aを入力してください")
a = [int(input()) for _ in range(N)]
print(f"{linear_search_find_toral_match(W, a)=}")
