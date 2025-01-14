def closestSquaredDistance(x, y):
    # Helper function to calculate squared distance
    def squared_distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    # Helper function for the divide-and-conquer algorithm
    def closest_pair_recursive(points_sorted_by_x, points_sorted_by_y):
        n = len(points_sorted_by_x)
        if n <= 3:
            # Brute force for small sets
            min_dist = float('inf')
            for i in range(n):
                for j in range(i + 1, n):
                    min_dist = min(min_dist, squared_distance(points_sorted_by_x[i], points_sorted_by_x[j]))
            return min_dist

        # Divide points into two halves
        mid = n // 2
        mid_x = points_sorted_by_x[mid][0]

        left_half = points_sorted_by_x[:mid]
        right_half = points_sorted_by_x[mid:]

        # Maintain points_sorted_by_y for each half
        left_half_y = [p for p in points_sorted_by_y if p[0] <= mid_x]
        right_half_y = [p for p in points_sorted_by_y if p[0] > mid_x]

        # Recursively find the closest pair in each half
        min_dist_left = closest_pair_recursive(left_half, left_half_y)
        min_dist_right = closest_pair_recursive(right_half, right_half_y)
        min_dist = min(min_dist_left, min_dist_right)

        # Check for points near the dividing line
        strip = [p for p in points_sorted_by_y if abs(p[0] - mid_x) ** 2 < min_dist]

        # Check points in the strip for closer pairs
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if (strip[j][1] - strip[i][1]) ** 2 >= min_dist:
                    break
                min_dist = min(min_dist, squared_distance(strip[i], strip[j]))

        return min_dist

    # Combine x and y coordinates into points
    points = list(zip(x, y))

    # Sort points by x and y coordinates
    points_sorted_by_x = sorted(points, key=lambda p: p[0])
    points_sorted_by_y = sorted(points, key=lambda p: p[1])

    # Start the recursive divide-and-conquer algorithm
    return closest_pair_recursive(points_sorted_by_x, points_sorted_by_y)

# Example usage
x = [0, 1, 2]
y = [0, 1, 4]
print("Squared shortest distance:", closestSquaredDistance(x, y))  # Output: 2
