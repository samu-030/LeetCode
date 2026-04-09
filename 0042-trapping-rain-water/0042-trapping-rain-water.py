class Solution(object):
    def trap(self, height):

        l = 0
        r = len(height) - 1

        lm, rm = 0, 0

        water = 0

        while (l < r):

            if height[l] < height[r]:
                if lm <= height[l]:
                    lm = height[l]
                else:
                    water += lm - height[l]
                l += 1

            else:
                if rm <= height[r]:
                    rm = height[r]
                else:
                    water += rm - height[r]
                r -= 1

        return water

        '''
        n = len(height)
        water = 0

        for i in range(n):

            lmax = max(height[:i+1])
            rmax = max(height[i:])

            water += min(lmax, rmax) - height[i]

        return water
        '''