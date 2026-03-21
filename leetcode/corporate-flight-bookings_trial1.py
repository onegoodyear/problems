class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * (n+1)
        for bk in bookings:
            flights[bk[0]-1] += bk[2]
            flights[bk[1]] -= bk[2]
        for i in range(1, n):
            flights[i] += flights[i-1]
        return flights[0:n]