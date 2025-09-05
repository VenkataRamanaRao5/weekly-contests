# Week 5 - Arrays  2 - questions and solutions

Contest link: https://www.hackerrank.com/weekly-contest-third-years-5/


## Maximum rooms booked
- Idea here is to use the concept of `difference array`
- We pre process the intervals and build an array `pre`.
- Then we do a running sum and store the same result.
- Then we find maximum value in `pre`  which gives us the *maximum overlapping interval*  .

```
def hotelReservations(reservation):
    p1 = reservation.split('|')
    q = [list(map(int,num.split(','))) for num in p1]
    
    #print(p1)
    #print(q)
    
    maxi = 0
    for a,b in q:
        maxi = max(maxi,a,b)
    #print(maxi)
    
    #pre-processing
    pre = [0]*(maxi+2)
    for start,end in q:
        pre[start]+=1
        pre[end+1]-=1
    
    #print(pre)
    #process the running sum
    curr = 0
    for i in range(len(pre)):
        curr += pre[i]
        pre[i] = curr
        
    
    #print(pre)
    return max(pre)
    
reservation = "1,3|2,4|3,5"
print(hotelReservations(reservation))
```

## Trek with Bear Grylls

- My thought process here is to simply remove the duplicates to make it simpler problem and proceed with the problem.
  
```
def countIt(nums,n):
        count = 0
        arr = []
        for i in range(len(nums)):
            if arr:
                if arr[-1]!=nums[i]:
                    arr.append(nums[i])
            else:
                arr.append(nums[i])
        #print(arr)
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i]>arr[i+1] or arr[i-1]>arr[i]<arr[i+1]:
                #print(i)
                count += 1
        return count
```

- Another solution is to use two variables - left and flat to keep track of left slope and flat height.
- If current and flat are equal, continue.
- Else, current is the right slope. Compare it with left and flat and calculate if it is a mountain or a valley.
- Only one pass is enough.

```
def countIt(nums, n):
    count = 0
    left = nums[0]
    flat = nums[1]
    for current in nums[2:]:
        if current == flat:
            continue
        if (flat - left) * (flat - current) > 0:
            count += 1
        left = flat
        flat = current     
    return count
```


## IPL Ticket Management

- This problem is a very similar variant of the Josephus problem, but with negative skip and a starting position.
- Incorporate that into Josephus and you have the solution.
- Make sure to verify with the sample how skip works for positive and negative and if offset is the 1-based position or 0-based index.

```
def reorderQueue(length, offset, skip):
    l = length
    arr = [i for i in range(l)]
    current = offset - 1
    reordered = []
    if skip < 0:
        skip -= 1
        current = (current + 1) % l
    while l > 0:
        current = (current + skip) % l
        reordered.append(arr.pop(current))
        current = current % l
        l -= 1

    return reordered
```

## Find Triplets
- This is a binary search problem if you want the most time optimized solution
- From the problem statement we know that there is either 1 or 0 triplet and pairs or triplets both occur consecutively.
- Based on this we see a property, if no triplet has occured before a particular index, then pairs start at the even index implying the triplet is on the right side
- If the pair starts at odd index then triplet has already occured so we search in the left hand side

```
public static int findTriplet(int n, List<Integer> arr) {
        if(n % 2 == 0) {
            return -1; 
        }

        int start = 0, end = n - 1;

        while(start < end) {
            int mid = start + (end - start) / 2;


            if(mid > 0 && mid < n - 1 && 
               arr.get(mid - 1).equals(arr.get(mid)) && 
               arr.get(mid).equals(arr.get(mid + 1))) {
                return arr.get(mid);
            }


            if(mid % 2 == 0) {

                if(mid < n - 1 && arr.get(mid).equals(arr.get(mid + 1))) {

                    start = mid + 2;
                } else {

                    end = mid;
                }
            } else {

                if(mid > 0 && arr.get(mid - 1).equals(arr.get(mid))) {

                    start = mid + 1;
                } else {

                    end = mid;
                }
            }
        }
        if(start%2==0){
            start--;
        }

        if(start > 0 && start < n - 1 &&
           arr.get(start - 1).equals(arr.get(start)) && 
           arr.get(start).equals(arr.get(start + 1))) {
            return arr.get(start);
        }

        return -1;

    }
```

## Organizing Containers of Balls

- The key is to see the fact that the total number of balls in every container remains the same (since we can only swap balls between two containers, the total count does not change).
- Second, we can convert this to subproblem. Suppose the answer is possible.
- We perform swap operations so that the container i has only one kind of balls, say type j. We can do this by swapping out every ball of other types for balls of type j. Now, we can ignore the container i and type j. This converts this into a subproblem with with n - 1 containers and n - 1 types.
- We can recursively do this until all containers hold only one kind of balls.
- Therefore, for solution to be possible, it is enough that the number of balls in a container matches the number of balls of a specific type and it is possible to find matching types for all containers.
- By this logic, we can determine if it is possible or not as follows:
  - Count the total number of balls per each container and sort it.
  - Count the number of balls per each type across containers and sort it.
  - If both sorted arrays are same, then it is possible to organize the balls into one type per container.
  - If not, then it is impossible.

```
def organizingContainers(container):
    n = len(container)
    containers = [0 for i in range(n)]
    types = [0 for i in range(n)]
    for nrow in range(n):
        for ncol in range(n):
            containers[nrow] += container[nrow][ncol]
            types[ncol] += container[nrow][ncol]
    containers.sort()
    types.sort()
    return "Possible" if all([c == t for c, t in zip(containers, types)]) else "Impossible"
```
