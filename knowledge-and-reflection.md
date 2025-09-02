# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> All of the above functions are hash functions because they all take in a key which the function then returns a hash.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> - The first hash function is simple and easy to set up, however it always produces a hash collision.
> - The second hash has an algorithm to produce unique hashes, however it is still prone to hash collisions.
> - The third is a pearson hash function which is designed to be efficient on 8-bit systems. It is however non-cryptographic, so it's not used in secure situations.
> - The fourth uses pythons built-in hash function, it's simple to set up and can hash more data types than just a string, however it does not work on mutable objects.
> - The last one uses an SHA hash function, it is far more complicated to understand but, it is cryptographic so is much more secure.

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> - Collision Resistance.
> - Sensitivity to input changes.
> - Item Access Speed.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> I would use the second hash function as the required purpose of the assessment is to handle hash collisions. Using this function will often produce both unique and colliding hashes which is useful for testing.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> - The first two lines establishes the pearson_table which includes a random order of numbers within a bytes size.
> - The next line is the function declaration which includes inputs for the key and size.
> - The next line establishes the starting hash value of 0
> - For each character in the key, the hash becomes equal to a value within the pearson_table, the index for the table is set with the XOR operator and compares the bits between the current hash value and the current character to produce an index.
> - The last line returns the final calculated hash modulo with the specified size.

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> ```python
> class PlayerHashMap:
>     SIZE 10
>     hashmap    
> 
>     def get_index(self, key):
>         return hash_function(key) % SIZE
> 
>     def __setitem__(self, key, name):
>         player_list = hashmap[get_index(key)]
>         player = search_function(player_list, key)
>         if player is None:
>             player_list.append(key, name)
>         else:
>             player.name = name
> ```

## Reflection

1. What was the most challenging aspect of this task?

> The most challenging part of this task was developing a function that searches through an indexed PlayerList within a Hashmap.

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> I would have used a standard python list which stores nodes, the list will start with a specified amount of empty nodes. Each node would have a key and a value. When adding an item to a list, i would hash the key to get the index and then store the node at the specified index. to access, remove or modify the item, I would use the key of that item and use the same hash to locate it in the list. I would use modulo to limit the produced hashes to fit within the list size.

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
