class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [[0 for _ in coins] for _ in range(amount + 1)]

        for i in range(amount + 1):
            for j, k in enumerate(coins):
                if i - k > 0:
                    dp[i][j] += sum(dp[i-k][:j+1])
                elif i == k:
                    dp[i][j] += 1
        for i in range(amount + 1):
            print(dp[i])
        return sum(dp[-1])