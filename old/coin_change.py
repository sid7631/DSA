from collections import deque

def coinChange( coins, amount):
    q = deque([(amount, 0)])
    seen = set([amount])
    while q:
        accum_amount, num_coins = q.popleft()
        if accum_amount == 0:
                return num_coins
        for coin in coins:
            if accum_amount - coin >= 0 and accum_amount - coin not in seen:
                q.append((accum_amount - coin, num_coins + 1))
                seen.add(accum_amount - coin)

    return -1

if __name__ == '__main__':
    print(coinChange([1,2,5],11))