class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        res = 1
        if self.prices:
            if price > self.prices[-1][0]:
                res = self.prices[-1][1]
                for i in range(len(self.prices) - self.prices[-1][1], -1, -1):
                    if self.prices[i][0] > price: break
                    res += 1
            elif price == self.prices[-1][0]:
                res = self.prices[-1][1] + 1
        self.prices.append((price,res))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)