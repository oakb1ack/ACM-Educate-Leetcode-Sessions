def trap(height: List[int]) -> int:
    n = len(height)

    l, r = 0, n - 1 
    leftMax, rightMax = height[l], height[r]
    ans = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            ans += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            ans += rightMax - height[r]
    return ans
print(trap([0,2,0,3,1,0,1,3,2,1]))
