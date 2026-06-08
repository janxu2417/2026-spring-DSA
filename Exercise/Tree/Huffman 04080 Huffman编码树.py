import heapq

def main():
    n = int(input())
    w = list(map(int, input().split()))
    heapq.heapify(w)
    total_wpl = 0
    while len(w) > 1:
        left = heapq.heappop(w)
        right = heapq.heappop(w)
        combined = left + right
        total_wpl += combined
        heapq.heappush(w, combined)
    print(total_wpl)

if __name__ == '__main__':
    main()