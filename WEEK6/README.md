# Week 6 - solutions

Contest link: https://www.hackerrank.com/weekly-contest-third-years-6/

## Array Rotation

- After each rotation, the last element is moved to first.
- After $k$ rotations, the first element ie the min will be at index $k$
- We have to find the index $k$ such that arr[k - 1] > arr[k]
- If arr[mid] > arr[high], then the min is on the right subarray (exclusive)
- Otherwise, it is on the left subarray (inclusive)
- When the subproblem size is 1, return that index.

```
def numberOfRotations(nums, n):
    low = 0
    high = n - 1
    while low < high:
        mid = low + (high - low) // 2; # mid value
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
            
    return low
```

## Maximize Energy

- We have to find the maximum barrier such that the sum of energy after that barrier is greater than or equal to $th$.
- Use binary search to find the optimal barrier.
- The minumum barrier is 0, while the maximum can be max(barrier). This is the search space.
- If mid value gives total energy > $th$, store it as a potential solution. Then search with low = mid + 1 to see if any higher barrier also satisfies the condition.
- If not, then search lower values with high = mid - 1

```
def getMaxBarrier(initialEnergy, th):
    def sum_after_barrier(barrier):
        return sum(max(0, e - barrier) for e in initialEnergy)
    
    low, high = 0, max(initialEnergy)
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if sum_after_barrier(mid) >= th:
            ans = mid      
            low = mid + 1
        else:
            high = mid - 1    
    
    return ans
```

## Perfect Square

- Straight forward binary search
- The lower limit is 1, higher limit is num. (Can be num / 2 if you account for edge cases like num = 1)
- If mid * mid == num, then num is a perfect square, return 1
- To avoid overflow, we can check mid = num / mid. Otherwise for 10^15, mid * mid will overflow beyond long int.
- If mid * mid > num, search for lower values with high = mid.
- If mid * mid < num, search for higher values with low = mid + 1
- If all values are exhausted, return 0

```
def isPerfectSquare(num):
    low = 1
    high = num
    while low < high:
        mid = (low + high) // 2
        if mid * mid == num:
            return 1
        elif mid * mid < num:
            low = mid + 1
        else:
            high = mid
    return 0
```

## Subarray split

- This is again a binary search problem where we have to search for the maximum sum possible
- Searching for the maximum sum is again a greedy choice. We choose a sum as possible sum and we pass it to a helper function
- In this helper function we try to divide the array into some number of parts such that the sum of any subarray is less than the chosen sum.
- If number of parts divided is greater than K , then this sum is too small to be a viable maximum sum and hence we have to choose for a larger sum and retry
- If the number of parts is less than or equal to K, then this sum is a viable sum, but we may have a possibility of finding an even smaller sum so we continue our search in binary search pattern
- If number_of_parts>k then low=mid+1, else high=mid-1 is the condition
- To find the number of parts, greedily add the seen elements to the running sum of subarray until the sum exceeds the limit_sum choosen for the particular trial

```
class Solution {
    boolean isPossible(int[] nums,long allowed,int k){
        int curSplitCount=1;
        long runningTotal=0L;
        for(int a:nums){
            if(a>allowed){
                return false;
            }
            else if(curSplitCount>k){
                return false;
            }
            else if(runningTotal+(long)a>allowed){
                runningTotal=a;
                curSplitCount++;
            }else{
                runningTotal+=a;
            }
        }
        return curSplitCount<=k;
    }
    public int splitArray(int[] nums, int k) {
        long end=0L;
        for(int a:nums){
            end+=(long)a;
        }
        long start=0;
        int ans=0;
        while(start<=end){
            long mid=start+(end-start)/2;
           
            if(isPossible(nums,mid,k)){
                ans=(int)mid;
                end=mid-1;
            }else{
                start=mid+1;
            }
        }
        
        return ans;
    }
}
```
