# coding: utf-8


class PerfectHash():
    def __init__(self):
        self.k = 0
        self.blocks = []

    # 自然数の集合 elements と
    # elements がとりうる値よりも大きい素数 p を渡して
    # ハッシュを作ります
    def make(self, elements, p):
        n = len(elements)
        self.k = self._get_k(elements, p, n, 'col1')

        sub_elements = []
        for i in range(n):
            sub_elements.append([])

        for q in elements:
            sub_elements[(self.k * q) % p % n].append(q)

        self.blocks = []
        for elements in sub_elements:
            self.blocks.append(self._make_block(elements, p))

        return self

    # 自然数 q が make() で渡した elements の中に
    # 存在するかどうかの情報を得ます
    def membership(self, q, p):
        block = self.blocks[(self.k * q) % p % len(self.blocks)]
        n = len(block['blocks'])
        if (n == 0) or (
            q != block['blocks'][(block['k'] * q) % p % n]
        ):
            return False
        else:
            return True

    # ハッシュの精度を計算します
    # 1.0 が返ってこない場合, なんらかの不具合があります
    def check(self, elements, p):
        valid_count = 0
        total_count = 0
        for q in range(1, p):
            in_elements = q in elements
            in_blocks = self.membership(q, p)
            if in_elements and in_blocks:
                valid_count += 1
            elif (not in_elements) and (not in_blocks):
                valid_count += 1
            total_count += 1
        return valid_count / total_count

    # ハッシュに必要なブロック数を取得します
    #
    # 普通の自然数の配列の場合, ブロック数が配列長 n で
    # membership() の時間計算量が O(n) になります
    #
    # 完全ハッシュの場合はブロック数が n + o(n) で
    # membership() の時間計算量が O(1) になります
    #
    # ブロック数に関する詳細な情報は README の論文を参照してください
    def size(self):
        count = 1
        for block in self.blocks:
            count += 1
            n = len(block['blocks'])
            if n > 1:
                count += (n + 2)
        return count

    def _make_block(self, elements, p):
        n = len(elements) ** 2
        k = self._get_k(elements, p, n, 'col2')

        blocks = [0] * n
        for q in elements:
            blocks[(k * q) % p % n] = q

        return {
            'k': k,
            'blocks': blocks,
        }

    def _get_k(self, elements, p, n, mode):
        for k in range(1, p):
            blocks = [0] * n
            for q in elements:
                blocks[(k * q) % p % n] += 1
            if (mode == 'col1') and self._check_col1(blocks, n):
                return k
            if (mode == 'col2') and self._check_col2(blocks):
                return k
        return p

    def _check_col1(self, blocks, n):
        count = 0
        for block in blocks:
            count += block ** 2
        return True if count < (3 * n) else False

    def _check_col2(self, blocks):
        for block in blocks:
            if block > 1:
                return False
        return True
