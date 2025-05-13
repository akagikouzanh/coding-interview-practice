import sys


def chapter3_problem1(n: int, v: int, a: list[int]) -> int:
    """
    Args:
        n (int): データの個数
        v (int): ターゲット値
        a (list[int]): 探索されるデータ

    Returns:
        int: ai=vである最大のindex

    TimeOrder: O(N)
    SpaceOrder: O(1)

    Remarks:
        単純なforを一つ使ったパターンの全探索のため、O(N)
        また、使用している変数自体も定数なので、O(1)
    """
    found_id = -1
    for i in range(n):
        if a[i] == v:
            found_id = i

    return found_id


# 5 10
# n, v = map(int, input().split())
# 1 10 8 10 2
# a = list(map(int, input().split()))
# print(f"{chapter3_problem1(n,v,a)=}") # 3


def chapter3_problem2(n: int, v: int, a: list[int]) -> int:
    """
    Args:
        n (int): データの個数
        v (int): ターゲット値
        a (list[int]): 探索されるデータ

    Returns:
        int: vにマッチする個数

    TimeOrder: O(N)
    SpaceOrder: O(1)

    Remarks:
        単純なforを一つ使ったパターンの全探索のため、O(N)
        また、使用している変数自体も定数なので、O(1)
    """
    v_count = 0
    for i in range(n):
        if a[i] == v:
            v_count += 1

    return v_count


# 5 10
# n, v = map(int, input().split())
# 1 10 8 10 2
# a = list(map(int, input().split()))
# print(f"{chapter3_problem2(n, v, a)=}")  # 2


def chapter3_problem3(n: int, a: list[int]) -> int:
    """
    Args:
        n (int): データの個数(n>2)
        a (list[int]): 探索されるデータ

    Returns:
        int: 2番目に小さい値

    TimeOrder: O(N)
    SpaceOrder: O(1)

    Remarks:
        単純なforを一つ使ったパターンの全探索のため、O(N)
        また、使用している変数自体も定数（比較と代入のみのため）、O(1)
    """
    min_num = min_second_num = sys.maxsize

    # 便宜上nを使用する
    for i in range(n):
        if a[i] < min_num:
            min_num, min_second_num = a[i], min_num
        elif a[i] > min_num and a[i] < min_second_num:
            min_second_num = a[i]

    return min_second_num


# 10
# n = int(input())
# 9 11 6 20 30 8 13 19 40 22
# a = list(map(int, input().split()))
# print(f"{chapter3_problem3(n, a)=}")  # 8


def chapter3_problem4(n: int, a: list[int]) -> int:
    """
    Args:
        n (int): データの個数
        a (list[int]): 探索されるデータ

    Returns:
        int: 2つの最大差

    TimeOrder: O(N)
    SpaceOrder: O(1)

    Remarks:
        単純なforを一つ使ったパターンの全探索のため、O(N)
        また、使用している変数自体も定数（比較と代入のみのため）、O(1)
    """
    max_val = -sys.maxsize
    min_val = sys.maxsize
    for i in range(n):
        if a[i] < min_val:
            min_val = a[i]

        if a[i] > max_val:
            max_val = a[i]

    return max_val - min_val


# 10
# n = int(input())
# 14 5 12 7 25 34 20 10 16 18
# a = list(map(int, input().split()))
# print(f"{chapter3_problem4(n, a)=}")  # 29


def chapter3_problem5(n: int, a: list[int]) -> int:
    """
    Args:
        n (int): データの個数
        a (list[int]): 探索されるデータ

    Returns:
        int: 全てが偶数の場合の操作回数

    TimeOrder: O(N log a)
    SpaceOrder: O(1)

    Remarks:
        各要素 a[i] に対して最大 log a[i] 回の割り算処理があるため、O(N log A)
        また、使用している変数自体も定数なので、O(1)
    """
    min_count = sys.maxsize
    for i in range(n):
        local_count = 0
        while a[i] > 0 and a[i] % 2 == 0:
            local_count += 1
            a[i] //= 2

        min_count = min(local_count, min_count)

    return min_count


# 10
# n = int(input())
# 8 6 4 2 1 0 3 7 10 12
# a = list(map(int, input().split()))
# print(f"{chapter3_problem5(n, a)=}")  # 10


def chapter3_problem6(k: int, n: int) -> int:
    """
    https://atcoder.jp/contests/abc051/tasks/abc051_b

    Args:
        k (int): max数値
        n (int): 探索値

    Returns:
        int: 0~kまでの総和にマッチする探索値のパターン数

    TimeOrder: O(N^2)
    SpaceOrder: O(1)

    Remarks:
        パッと浮かんだのがO(n^3)だった。z = n - x - yになることがわかっていれば、O(n^2)にできるなと理解できた。
        ネストのforでx, yへアクセスしているため、O(N^2)となる。
        ループ内で使用される一時変数（base, count, x, y, z）の数は固定であり、入力サイズに依存して増加しないため、使用するメモリ量はO(1)になる。
    """
    base = min(k, n)
    count = 0
    for x in range(base + 1):
        for y in range(base + 1):
            z = n - x - y

            if 0 <= z <= k:
                count += 1

    return count


# 2 2
# k, n = map(int, input().split())
# print(f"{chapter3_problem6(k, n)=}")  # 6


def chapter3_problem7(n: int, s: str) -> int:
    """
    https://atcoder.jp/contests/abc045/tasks/arc061_a
    Args:
        n (int): sの長さ
        s (str): 探索対象文字列

    Returns:
        int: 総和を返す

    TimeOrder: O(N * 2^N)
    SpaceOrder: O(1)

    Remarks:
        パッと解法が出なかった。bitシフトを使用して対象をチェックすることで解決。2^Nした探索とN探索のため、O(N * 2^N)
        内容としては、文字となっている数値の間に+を挟んでいくパターンを全て列挙。その総和を返す。
        また、使用している変数自体も定数なので、O(1)
    """
    res = 0
    for bit in range(1 << (n - 1)):
        tmp = 0
        for i in range(n - 1):
            tmp *= 10
            tmp += int(s[i])
            if bit & (1 << i):
                res += tmp
                tmp = 0

        tmp *= 10
        tmp += int(s[-1])
        res += tmp

    return res


# 125
# s = input()
# print(f"{chapter3_problem7(len(s), s)=}")  # 176
