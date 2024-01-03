# Hash tables

### 5.1
$f(x)$ is consistent, but not admissible. It causes colission for all $x$.

### 5.2
$f(x)$ is inconsistent.

### 5.3
$f(x)$ is inconsistent.

### 5.4
$f(x)$ is consistent.

### 5.5
Given that the $a$ function is not a suitable hash function, and the $b$ function is ruled out due to names with the same length, as well as the exclusion of the $c$ function because of names sharing the same first letter, the most viable option emerges as the $d$ function.

### 5.6
We can't use function $c$ because the battery types are all represented by a single character. If we have more battery types, function $d$ might also collide, so it's best to use function $b$, which only computes hashes with character lengths.

### 5.7
Given that titles share the same length, opting for the $b$ function is not feasible. While both the $c$ and $d$ functions remain viable options, the preference leans towards the $d$ function, especially when factoring in the addition of another book.