# Chapter 4 Quicksort

### 4.1
See `sum.py`.

### 4.2
See `count.py`.

### 4.3
See `maximum.py`.

### 4.4
The base case is 
```python
if guess == item:
    return mid            
```

The recursive case is
```python
elif guess > item:
    high = mid - 1
else:
    low = mid + 1
```

### 4.5
$O(n)$

### 4.6
$O(n)$

### 4.7
$O(1)$

### 4.8
$O(n^2)$
