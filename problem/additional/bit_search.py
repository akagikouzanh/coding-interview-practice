def additional_bit_search1(n: int, x: int, a: list[int]) -> int:
    """
    https://atcoder.jp/contests/abc014/tasks/abc014_2

    Args:
        n (int): aの数
        x (int): 部分集合
        a (list[int]): 探索されるデータ

    Returns:
        int: 対象の数の合計
    """
    total = 0
    for i in range(n):
        if x & (1 << i):
            total += a[i]

    return total


# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# print(additional_bit_search1(n, x, a))


def additional_bit_search2(n: int, m: int, k: list[list[int]], p: list) -> int:
    """
    https://atcoder.jp/contests/abc128/tasks/abc128_c

    Args:
        n (int): スイッチ数
        m (int): 電球数
        k (list[list[int]]): 繋がれているスイッチのリスト
        p (list[int]): スイッチのOn/Off

    Returns:
        int: 全点灯組み合わせ
    """
    count = 0

    for bit in range(1 << n):
        all_on = True
        for i in range(m):
            on_count = 0
            for switch in k[i]:
                if bit & (1 << (switch - 1)):
                    on_count += 1
            if on_count % 2 != p[i]:
                all_on = False
                break
        if all_on:
            count += 1

    return count


# n, m = map(int, input().split())
# k = [list(map(int, input().split()[1:])) for _ in range(m)]
# p = list(map(int, input().split()))
# print(additional_bit_search2(n, m, k, p))


def additional_bit_search3(n: int, witness: list[tuple[int]]) -> int:
    """
    https://atcoder.jp/contests/abc147/tasks/abc147_c

    Args:
        n (int): 証人者数
        witness list[tuple[int]]: 証言

    Returns:
        int: 正直者の人数

    Remarks:
        パッと会報出なかったので、後回し
    """
    max_honest = 0
    for bit in range(1 << n):
        pass


# n = int(input())
# witness = [[] for _ in range(n)]
# for i in range(n):
#     a = int(input())
#     for _ in range(a):
#         x, y = map(int, input().split())
#         witness[i].append((x - 1, y))
# print(additional_bit_search3(n, witness))


def additional_bit_search4(n: int, l: list[int]) -> str:
    """
    Args:
        n (int): 部分和のターゲット
        l (list[int]): 探索されるデータ

    Returns:
        str: ターゲットにマッチしたかどうか
    """
    for bit in range(1 << len(l)):
        sum_num = 0
        for i in range(len(l)):
            if bit & (1 << i):
                sum_num += l[i]

        if sum_num == n:
            return "Yes"

    return "No"


# _, n = map(int, input().split())
# l = list(map(int, input().split()))
# print(additional_bit_search4(n, l))


def additional_bit_search4(n: int, l: list[int]) -> bool:
    """
    Args:
        n (int): データの個数
        l (list): データのリスト

    Returns:
        bool: 組み合わせ可能な2つの異なる数字があるかどうか
    """
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] & l[j] != 0 and l[i] != l[j]:
                return True

    return False


# n = int(input())
# l = list(map(int, input().split()))
# print(additional_bit_search4(n, l))


def additional_bit_search5(n: int, m: int, l: list[int]) -> bool:
    """
    Args:
        n (int): アイテムの数
        m (int): 判定したい部分集合を表す整数
        l (list): アイテムのリスト

    Returns:
        bool: 部分集合がアイテムリストのいずれかの上位集合があるか
    """
    for i in range(n):
        if (m & l[i]) == l[i]:
            return True

    return False


# n = int(input())
# m = int(input())
# l = list(map(int, input().split()))
# print(additional_bit_search5(n, m, l))


def additional_bit_search6(n: int, m: int, l: list[int]) -> bool:
    """
    Args:
        n (int): 人数
        m (int): 趣味の個数
        l (list[int]): 趣味の組み合わせ

    Returns:
        bool: 同じ趣味を持つ人が2人以上いるか

    note:
        ちょっと考えるのに時間かかるし、難しいなぁと感じる
    """
    for bit in range(1, 1 << n):
        selected = 0
        candidate = (1 << m) - 1
        for i in range(n):
            if (bit >> i) & 1:
                selected += 1
                candidate &= l[i]

        if selected >= 2 and candidate != 0:
            return True

    return False


# n = int(input())
# m = int(input())
# l = list(map(int, input().split()))
# print(additional_bit_search6(n, m, l))
