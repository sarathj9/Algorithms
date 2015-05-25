Min Hops in Snake and Ladders
------------------------------
------------------------------
####Problem: 
Find out the minimum number of Hops required from start point to end point in Snake and Ladders, Given the following information
- [x] No of Tiles in the Snake and Ladders board. 
- [x] Snakes and their corresponding end points. 
- [x] Ladders and their corresponding end points.  
- [x] A dice ranging from 1 to 6. Whenever you throw a dice you would get the desired number.  
 
    
####Solution:

Since, we want the minimum no. of hops, and we have the opportunity to get desired option(as number), we can never be bitten by
Snake bites. So the problem will default to finding the ladder that take us to the end point with minimum number of paths. 

A formula like below will help us find minimum no. of hops from start to end point using a particular ladder

```math 
No. of Hops Required for the given ladder = Total number of minimum hops required to reach the ladder +   --->a
                                            (Total number of tiles deducted because of ladder) / 6    +   --->b
                      Total number of minimum hops required from given ladder end point to the end point  --->c
```
                    
a is minimum distance(implies using any possible ladder) from the start point to ladder start point (should be found)

b is the difference of ladder end points/6 (given)

c is the total no. of tiles (should be found)

Steps followed to satisfy above equation

1. find min hops for all the ladders.

2. find min distance from the start point to all ladder start points.

3. find min distance from all ladder end points to the end point. 

4. find distance from start to end point in all possible paths and know which path is minimum path

| ladder Name| start point|end point|
| -----------|:----------:| -------:|
|l1          |1           |5        |
|l2          |5           |13       |
|l3          |13          |19       |
|l4          |7           |13       |
|l5          |1           |8        |

    
  ![Alt text](http://g.gravizo.com/g?
    digraph G {
      aize ="4,4";
      1 [shape=box,style=filled,color=".7 .3 1.0"];
      21 [shape=box,style=filled,color=".7 .3 1.0"];
      19 [shape=box];
      5 [shape=box];
      19 ->21 [style=dotted,label="1"];
      13 -> 19 [weight=5,label="1"];
      8 ->13 [style=dotted,label="1"]; 
      5 ->7 [style=dotted,label="1"];
      5 -> 13 [weight=5,label="1"];
      1 -> 5 [style=dotted,label="1"];
      7 -> 13 [weight=5,label="1"];
      1 ->8 [weight=5,label="1"];
    }
  )
  

The lines in dotted are the minimum paths from ladder start point to start point. 

It is computed by:
 - Identifying the ladder end point that is closest to the current ladder point. 
 - Identifying ladder start point closest to current ladder end point.
 - Connecting largest ladder end point to the end point. 
 - Connecting smallest ladder start point to the start point.

Json representing the above graph:
```json
{"1": [[8, 1], [5, 1]], "5": [[13, 1], [7, 1]], "7": [[13, 1]], "8": [[13, 1]], "13": [[19, 1]], "19": [[21, 1]]}
```
Min distance path(s) are : [1, 5, 13, 19, 21], [1, 8, 13, 19, 21]],  with distance, 4

####Examples:
Json: 
```json
{"1": [[2, 1]], "2": [[7, 1], [5, 1]], "5": [[12, 1], [6, 1]], "6": [[12, 1]], "7": [[12, 1], [8, 1]], "8": [[21, 1], [9, 1]], 
"9": [[15, 1]], "12": [[18, 1], [17, 1]], "15": [[18, 1]], "17": [[21, 1]], "18": [[21, 1]]}')
```
Min distance path(s) are : [[1, 12, 17, 21], [1, 12, 18, 21], [1, 7, 8, 21], [1, 12, 17, 21], [1, 12, 18, 21]], with distance 3

Json:
```json
{"8": [[19, 1]], "1": [[5, 1]], "19": [[21, 1]], "5": [[13, 1], [8, 1]], "13": [[19, 1]]}
```
Min distance path(s) are : [[1, 5, 8, 19, 21], [1, 5, 13, 19, 21]],  with distance, 4