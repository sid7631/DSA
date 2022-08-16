import heapq

def kthSmallest(matrix, k) -> int:
    
    # The size of the matrix
    N = len(matrix)
    
    # Preparing our min-heap
    minHeap = []
    for r in range(min(k, N)):
        
        # We add triplets of information for each cell
        minHeap.append((matrix[r][0], r, 0))
    
    # Heapify our list
    heapq.heapify(minHeap)    
    
    # Until we find k elements
    while k:
        
        # Extract-Min
        element, r, c = heapq.heappop(minHeap)
        
        # If we have any new elements in the current row, add them
        if c < N - 1:
            heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
        
        # Decrement k
        k -= 1
    
    return element  

if __name__ == '__main__':
    print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))