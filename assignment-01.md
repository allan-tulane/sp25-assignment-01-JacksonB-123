

# CMPS 2200 Assignment 1

**Name:**___Jackson Burch______________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.g(n) ≤ c x f(n)

 2^(n+1) ≤ c x 2^n  		For all n>n0
 
  You can rewrite 2^(n+1) as 2 x 2^n
  
	Thus 2 x 2^n ≤ c x 2^n
  
	Divide out 2^n
  
	2 ≤ c
  
	Therefore the  2^(n+1) ∈ O(2^n) is true for any c=2 and n0≥ 0.

	2^n is allowed to be multiplied by a constanst as long as it is 2 or greater to satisfy the conditions of big O

  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  g(n)≤ c x f(n)

 2^(2)^n ≤ c x 2^(n)		 for all n≥n0

  You can rewrite 2^(2)^n as  2^(n)^2

  Thus ( 2^n)^2 ≤ c x 2^n

  Divide both sides by 2^n

  2^n ≤ c

  Therefore  2^(2)^n∈ O(2^n) is not valid.

  The inequality is not true for all n≥n0

  ( 2^n)^2 grows faster than c x 2^n

  No this is not true

  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.   n1.01 ∈ O(log2n) is not true
    
  The polynomial n^1.01 always grows faster than log2n 
  
  A c>0 does not exist where:
  
  n^1.01 ≤ c x log2 n for all n≥0


  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  n^1.01≥ c x log2n

  This is true because n^(1.01) is a polynomial and will always grow faster than log2n when n>0. The       polynomial will always grow faster

  n^1.01 ∈ Ω(log2n) is true

  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  √ n = n^(1/2)  
  A c> 0 and n0≥ 0 do not exist such that:

  n^(1/2) ≤ c x (logn)^3 for all n≥n0
  
  Square root functions always dominate/ grow faster than polylogarithmic functions
  
  Thus it is false
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  √ n = n^(1/2)

  A c> 0 and n0≥ 0  exists such that:
  
   n^(1/2) ≥ c x (logn)^3 for all n≥n0
   
  Square root functions always dominate/ grow faster than plylogarithmic functions
  
  Thus it is true


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

The base case of the function is if the x is less than or equal to 1  the function will return x

Then for every other value of x the foo function calls itself twice calculating the fibonacci number at x-1 and x-2 and then summing the values together for the new fibonacci numberat position x. This is the recursive step


  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  The work is O(n) and the span is O(n)


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  W(n)=O(nlogn) and S(n)=O(logn)



  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  W(n) = O(n log n) and S(n) = O(n)


