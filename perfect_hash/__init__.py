# coding: utf-8


class PerfectHash():
    def __init__(self):
        self.k = 0
        self.blocks = []

    def make(self, elements, p):
        n = len(elements)
        self.k = self._get_k(elements, p, n, 'col1')

        sub_elements = []
        for q in elements:
            sub_elements.append([])

        for q in elements:
            sub_elements[(self.k * q) % p % n].append(q)

        self.blocks = []
        for elements in sub_elements:
            self.blocks.append(self._make_block(elements, p))

        return self

    def membership(self, q, p):
        block = self.blocks[(self.k * q) % p % len(self.blocks)]
        n = len(block['blocks'])
        if (n == 0) or (
            q != block['blocks'][(block['k'] * q) % p % n]
        ):
            return False
        else:
            return True

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
            if (mode == 'col2') and self._check_col2(blocks, n):
                return k
        return p

    def _check_col1(self, blocks, n):
        count = 0
        for block in blocks:
            count += block ** 2
        return True if count < (3 * n) else False

    def _check_col2(self, blocks, n):
        for block in blocks:
            if block > 1:
                return False
        return True
