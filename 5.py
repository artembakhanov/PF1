def prime_numbers(N):
    """
    Sieve of Eratosthenes approach is used here.
    Check https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    flags = [True] * N
    primes = []
    for i in range(1, N):
        if flags[i]:
            primes.append(i + 1)
        for j in range(i, N, i + 1):
            flags[j] = False
    return primes


print(*prime_numbers(13))
