# Chapter 2 Selection sort

### 2.1
A list takes $O(1)$ to insert and $O(n)$ to read, so it's a good choice if you have lots of inserts and few reads.

### 2.2
In this situation, reads, inserts, and deletes are all frequent, and the data is always accessed from both ends. Therefore, this app should be implemented using a list.

### 2.3
In this situation, reads are frequent, but inserts and deletes are rare. Also, because of the frequent random access, unsername should be stored in an array.

### 2.4
In order to keep the username sorted in alphabetical order, the array has to push back the data behind the insertion position by one space, which means the insertion will take $O(n)$.

### 2.5
This hybrid data structure shows retrieval speeds that are faster than list and slower than array. For inserts, it shows speeds slower than list and faster than array.