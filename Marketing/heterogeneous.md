---
date created: Monday, November 7th 2022, 3:07:54 pm
date modified: Tuesday, November 8th 2022, 5:27:06 pm
date_created: Monday, November 7th 2022, 3:07:54 pm
date_modified: Tuesday, November 8th 2022, 5:30:19 pm
---
You may have read somehwere that Python lists (and tuples) are heterogeneous, and maybe like me you wondered what that means and why it matters.

Put simply, it means that they can contain multiple types.
As an example here's a list containing an int, a string and a float. 

multi_list = [2,"phlawless", 10.5]

If you have an expereice with staticaly typed languages this might seem a little strange,
and if you know anything about arrays, you might wonder how is this even possible?

for those of you who don't know much about datastructures, here's a simple overview of why this is intresting.

The first thing to unserstand is python lists are arrays "under the hood"

-- The humble array -- 
"Array" is a word you may have heared outside of computerscience (in terms of missle launchers, solar pannels or flowers even),
if not a google definition search gives us "an impressive display or range of a particular type of thing." and  "an ordered series or arrangement"
In programming, an array refers to essentially the same thing, more than one of something, next to eachother in memory.
More specifically the array variable will contain the memory addresss of the first element and the type of elements it holds (more on this later).

<image of memory>

The reason this matters has to do with how indexing works, say we have an array of integers:

array = [100,200,300]

and we ask for the second element by index 

n = array[1]

This happens in O(1) (constant) time, if you don't know anything about "Big O notation" the simplest way to think of this case would be
no matter which element you access , it will take the same ammount of time.

n = array[0]
n = array[100]
n = array[10000]
n = array[1000000]
#these all take the same ammout of time 

If you remeber our simplified memory diagram

<image of mememory with bold addresses>

notice the mememory addresses are sequential,
Remeber  our array variable knows the adress of the first element and the element type
so let's say for example our array is unsigned (positive only) 8 bit integers (one of many common integer types).

Consider this array 
<image of array in mememory>

and this instruction

n = array[100]

our array is at memory address 250, so the memmory address of array[100] = 250 + (100 * 8)  #1050

You should be able to see now why heterogeneous lists aren't simple, this O(1) (constant) time access is only possible because each elment is the same size.

Take a few minutes to think about how you might solve this problem (don't worry if you can't figure it out).

python's approach to this problem is quite clever (I think) , they acheive this level of performance only ever storing one type in lists, You heard me right.

our example from before 

multi_list = [2,"phlawless", 10.5]

It may look like 3 distinct types in this list (integer, string, float). but the list actually contains only 1 type
"memory address" (in python this is refered to as an object reference) remeber from our memory model

<image of memory>

all memory addresses are just numbers.

