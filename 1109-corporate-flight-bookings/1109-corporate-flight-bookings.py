class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0]*(n+1)
        for i in range(len(bookings)):
            book = bookings[i]
            prefix[book[0]-1] += book[2]
            prefix[book[1]] -= book[2]
        
        for i in range(1,n):
            prefix[i] += prefix[i-1]
        
        return prefix[:-1]