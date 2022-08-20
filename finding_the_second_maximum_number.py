if __name__ == '__main__':
    """Given the participants score sheet for your University Sports Day,
     you are required to find the runner-up score. You are given  scores.
    Store them in a list and find the score of the runner-up."""
    n = int(input())
    arr = list(map(int, input().split()))
    receptor = []
    for x in arr:
        if x not in receptor:
            receptor.append(x)
    maior = max(receptor)
    receptor.remove(maior)
    print(max(receptor))
