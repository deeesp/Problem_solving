# Chapter 5
## Q1 973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key= lambda x: (x[0]**2 + x[1]**2))[:K]
```

## Q5 1.  Two Sum 
https://leetcode.com/problems/two-sum/

```python
class Solution:
    
    """
    1. Brute-Force
    Time: O(N^2)
    Space: O(1)
    """
    def twoSum1(self, nums: List[int], target: int) -> List[int]:    
        for idx in range(len(nums)):
            for i in range(idx+1,len(nums)):
                if nums[idx] + nums[i] == target:
                    return [idx, i]
        return []
    
    
    """
    2. One-Pass Hash Table
    Time: O(N)
    Space: O(N)
    """
    def twoSum2(self, nums, target):
        d = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], idx]
            else:
                d[num] = idx # {key <-> value switch}
        return []
```

## Q6 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        아나그램 집합! input의 문자가 중복이 될수도 있지 않을까?
        # 중요한 아이디어
        # dictionary key에 tuple 이 들어갈 수 있는 것
        # value 에 list가 들어갈 수 있고 append도 가능하다는 것        
        
        Time: O(NMlogM)
        Space: O(NM)
        
        """
        
        answer = {}
        
        for s in strs:
            key = tuple(sorted(s))
            if key not in answer:
                answer[key] = [s]
            else:
                answer[key].append(s)
        return answer.values()
```

## Q7 560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

```python
class Solution:
    '''
    Time: O(N)
    Space: O(N)
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:

        count, cur, res = {0: 1}, 0, 0
        for num in nums:
            cur += num
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res
```
