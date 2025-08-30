# Week 5 - Arrays  2 - questions and solutions




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

## IPL Ticket Management

- This problem is a very similar variant of the Josephus problem, but with negative skip and a starting position.
- Incorporate that into Josephus and you have the solution.
- Make sure to verify with the sample how skip works and if offset is the 1-based position or 0-based index.

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

##Find Triplets
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
