---
title: U10 Recursion P1 Student
author: David, Derrick
date: 2023-10-30 11:33:00 +0800
week: 11
categories: ['Week11']
tags: week11
type: plans
pin: False
mermaid: False
---

## 10.1 Recursion
> A method calling itself to repeat a certain number of times. 

**Popcorn Hack:** What is recursion?

### Vocabulary
- Base Case - this sets the expected case for when the recursion will stop
- Formal Parameters - method within the method (local variables)

### Method Calling Itself

We will first be looking at how a method can call itself.


```Java
/* 
DO NOT RUN THIS
if you do run this accidentally press `ctrl + c` twice
*/

public class Recursion1 {
  public static void recursionCount(int n) { // original method definition
    System.out.println(n);
    recursionCount(n - 1); // calling the method again
  }

  public static void main(String[] args) {
    recursionCount(3); // original call of the method
  }
}

Recursion1.main(null);
```

In this example, you will receive an overflow error because the method is calling itself infinitely. To avoid this you would create a break point.

A base case usually uses an `if-then` statement to turn the loop off after a certain condition is met.


```Java
public class Recursion2 {
  public static void recursionCount(int n) {
    if (n <= 0) { // added base case, telling the program to stop when n is less than or equal to 0
      System.out.println("done");
    } else {
      System.out.println(n);
      recursionCount(n - 1); // method recursion
    }
  }

  public static void main(String[] args) {
    recursionCount(3); // calling original function
  }
}

Recursion2.main(null);
```

    3
    2
    1
    done


**Popcorn Hack:** Create your own quick recursive program.


```Java
// Add code here
public class RecursionPHack {
    public static void woah(int n) {
      if (n > 8) { // added base case, telling the program to stop when n is less than or equal to 0
        System.out.println("M's in my bank acount");
      } else {
        System.out.println(n);
        woah(n + 1); // method recursion
      }
    }
  
    public static void main(String[] args) {
      woah(1); // calling original function
    }
}
  
System.out.println("I got");
  RecursionPHack.main(null);
```

    I got
    1
    2
    3
    4
    5
    6
    7
    8
    M's in my bank acount


### Calling With Different Parameters

You can also call the method with multiple different local parameters, also known as local variables.

In this example we call an integer and string.


```Java
public class Recursion3 {
  public static void recursionPrint(int n, String a) { // formal parameters are within this method
    if (n <= 0) { // base case
      System.out.println("done");
      return;
    }

    System.out.println("n = " + n + " a = " + a); // printing each var with each call of the method

    String addChar = a + "!"; // mutating string with each recursion
    int addN = n - 1; // mutating integer with each recursion

    recursionPrint(addN, addChar); // recursive function
  }

  public static void main(String[] args) {
    recursionPrint(5, "test"); // initial call
  }
}
Recursion3.main(null);
```

    n = 5 a = test
    n = 4 a = test!
    n = 3 a = test!!
    n = 2 a = test!!!
    n = 1 a = test!!!!
    done


Here we just capture each string and subtract one from every previous number.

### Capturing Progression Through Recursion

You can also capture the progression through recursion. This is useful for doing specific tasks in specific steps through recursion.


```Java
public class Recursion4 {
  public static void recursionCount(int n, int progress) {
    if (n <= 0) {
      System.out.println("done");
    } else {
      if (n == progress) {
        System.out.println("Reached halfway through the array."); // special action done only when the program has reached a certain point
      }
      System.out.println(n);
      recursionCount(n - 1, progress); // recursive call
    }
  }

  public static void main(String[] args) {
    int n = 6;
    int progress = n / 2; // progress is set to half of the array length
    recursionCount(n, progress); // initial call
  }
}

Recursion4.main(null);
```

    6
    5
    4
    Reached halfway through the array.
    3
    2
    1
    done


**Popcorn Hack:** What other situations could we use capturing progression for?

Games, moving a piece around would need capturing progression. It would have to save the game state of the whole board while updating the singular pieces position.

### Converting Recursion to Iteration

Any recursive process can be made iterative, however this is not needed for the AP test. It is, however, still useful.

#### Recursive Version


```Java
public class Recursion5 {
  public static void recursionCount(int n) {
    if (n <= 0){
      System.out.println("done");
    } else {
      System.out.println(n);
      recursionCount(n - 1); // recursive function
    }
  }

  public static void main(String[] args) {
    recursionCount(3); // initial call
  }
}

Recursion5.main(null);
```

    3
    2
    1
    done


#### Iterative Version


```Java
public class Iteration {
  public static void iterationCount(int n) {
    for (int i = n; i >= 1; i--) { // using a for loop to iterate, notice we go only so i is greater than 1 and not 0
      System.out.println(i);
    }
    System.out.println("done");
  }
  
  public static void main(String[] args) {
    iterationCount(3); // same initial call
  }
}

Iteration.main(null);
```

    3
    2
    1
    done


**Popcorn Hacks:** We we go only so i is greater than or equal to 1 and not 0. Why?

If it was set to greater than or equal to 0, the loop would break at 0, not 1


### Traversing With Recursion

You can traverse many things with recursion. Here I will show traversal through a string, array, and an `ArrayList` object.

#### String Traversal

You can traverse through a string, finding a specific character in the string.


```Java
public class FindChar {
    public static boolean findChar(String s, char target, int index) {
        if (index >= s.length()) { // checks for if the index we are looking for is greater than the word length
            return false;
        }

        if (s.charAt(index) == target) { // checks for if there is a character the index we are searching
            return true;
        }

        return findChar(s, target, index + 1); // recalls method, recursion
    }

    public static void main(String[] args) {
        String sampleString = "words"; // example string
        char targetChar = 's'; // character we are looking for

        System.out.println("Sample String: " + sampleString);

        boolean isCharFound = findChar(sampleString, targetChar, 0); // checks if the character we are looking for is found, based on boolean

        if (isCharFound) {
            System.out.println("Character '" + targetChar + "' is found."); // if it is found, show this
        } else {
            System.out.println("Character '" + targetChar + "' is not found."); // if not show this
        }
    }
}

FindChar.main(null);
```

    Sample String: words
    Character 's' is found.


You can also find and print a certain range of characters from the string.


```Java
public class PrintRange {
    public static void printRange(String s, int startIndex, int endIndex) {
        if (startIndex < 0 || endIndex > s.length() || startIndex >= endIndex) { // checks for invalid declaration or end (negative index, index larger than string length, index start has reached the end)
            return;
        }

        System.out.print(s.charAt(startIndex)); // print the characters in the range
        printRange(s, startIndex + 1, endIndex); // recursive calling
    }

    public static void main(String[] args) {
        String sampleString = "example"; // string
        int startIndex = 0;
        int endIndex = 5;
        
        System.out.println("Word: " + sampleString);
        System.out.println("Start: " + startIndex + ", End: " + endIndex);

        System.out.print("Characters in the specified range: ");
        printRange(sampleString, startIndex, endIndex); // initial call
    }
}

PrintRange.main(null);
```

**Popcorn Hack:** Make it so that we can find two different ranges and print them.


```Java
// Enter code here
import java.util.Scanner;

public class PrintRange {
    public static void printRange(String s, int startIndex, int endIndex) {
        if (startIndex < 0 || endIndex > s.length() || startIndex >= endIndex) { // checks for invalid declaration or end (negative index, index larger than string length, index start has reached the end)
            return;
        }

        System.out.print(s.charAt(startIndex)); // print the characters in the range
        printRange(s, startIndex + 1, endIndex); // recursive calling
    }

    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in); // Create a Scanner object
        System.out.println("Enter a string");
        String sampleString = myObj.nextLine();

        System.out.println("Enter a number A");
        int startIndex = myObj.nextInt();

        System.out.println("Enter a number B");
        int endIndex = myObj.nextInt();
        
        System.out.println("Word: " + sampleString);
        System.out.println("Start: " + startIndex + ", End: " + endIndex);

        System.out.print("Characters in the specified range: ");
        printRange(sampleString, startIndex, endIndex); // initial call
    }
}

PrintRange.main(null);
```

    Enter a string
    Enter a number A
    Enter a number B
    Word: whaoaoahoaoaoaoa
    Start: 3, End: 8
    Characters in the specified range: oaoah

#### Array Traversal

You can also traverse arrays using recursion.


```Java
public class ArrayTraversal {
  public static int findIndex(int[] arr, int targetIndex, int currentIndex) {
    if (currentIndex < 0 || currentIndex >= arr.length) { // checks for invalid (index less than 0, index greater than array length)
      return -1; // returns invalid
    }

    if (currentIndex == targetIndex) { // if the index is found
      return currentIndex;
    }

    return findIndex(arr, targetIndex, currentIndex + 1); // recursion
  }

  public static void main(String[] args) {
    int[] sampleArray = {1, 4, 6, 8, 4, 9, 12};
    int targetIndex = 2; // target

    int foundIndex = findIndex(sampleArray, targetIndex, 0);

    if (foundIndex != -1) { // checks what has been outputted
      int value = sampleArray[foundIndex]; // found index value
      System.out.println("Index " + targetIndex + " is found in the array at position " + foundIndex + " with a value of " + value); // found
    } else {
      System.out.println("Index " + targetIndex + " is not found in the array."); // not found
    }
  }
}

ArrayTraversal.main(null);
```

    Index 2 is found in the array at position 2 with a value of 6


### ArrayList Object Traversal

We can also traverse the `ArrayList` object.


```Java
import java.util.ArrayList;

public class ArrayListTraversal {
    public static int findIndex(ArrayList<Integer> list, int targetIndex, int currentIndex) {
        if (currentIndex < 0 || currentIndex >= list.size()) { // checks for invalid
            return -1;
        }

        if (currentIndex == targetIndex) { // finds index
            return currentIndex;
        }

        return findIndex(list, targetIndex, currentIndex + 1); // recusion
    }

    public static void main(String[] args) {
        ArrayList<Integer> sampleList = new ArrayList<>(); // created ArrayList object
        sampleList.add(1);
        sampleList.add(4);
        sampleList.add(6);
        sampleList.add(8);
        sampleList.add(4);
        sampleList.add(9);
        sampleList.add(12);

        int targetIndex = 2; // target

        int foundIndex = findIndex(sampleList, targetIndex, 0);

        if (foundIndex != -1) { // checks for if found or not
            int value = sampleList.get(foundIndex); // gets found index from ArrayList object
            System.out.println("Index " + targetIndex + " is found in the ArrayList at position " + foundIndex + " with a value of " + value);
        } else {
            System.out.println("Index " + targetIndex + " is not found in the ArrayList.");
        }
    }
}

ArrayListTraversal.main(null);
```

    Index 2 is found in the ArrayList at position 2 with a value of 6


### Conclusion

Must Knows:
- How to create recursive code (recalling a method within itself, with parameters that change)
- Record progression through recursion (completing certain tasks through the progression)
- Traversal of strings, arrays, and the `ArrayList` object

Overall, recursion is useful as an alternative to iteration. Recursion is usually chosen for problems that can naturally be divided into parts, like sorting which will be talked about in the next part.

## 10.2 Binary Search

### Binary Search vs Linear Search

target number - 24

intArray - 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40

#### Popcorn hack:
How many times iterated through for Linear Search? 

Answer: 13

### Example of Binary Search with Recursion


```Java
public class BinarySearch {
    public static void main(String[] args) {
        int[] intArray = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40}; // Example array
        int target = 24; // Example target value
        int result = recBinarySearch(intArray, 0, intArray.length - 1, target);

        if (result == -1) {
            System.out.println("Target not found in the array.");
        } else {
            System.out.println("Target found at index: " + result);
        }
    }

    public static int recBinarySearch(int[] intArray, int lowPosition, int highPosition, int target) { //method
        if (lowPosition > highPosition) {
            return -1; // Element not found in the array
        } else {
            int midPosition = (lowPosition + highPosition) / 2;
            if (intArray[midPosition] < target) {
                return recBinarySearch(intArray, midPosition + 1, highPosition, target);
            } else if (intArray[midPosition] > target) {
                return recBinarySearch(intArray, lowPosition, midPosition - 1, target);
            } else {
                return midPosition; // Element found at midPosition
            }
        }
    }
}

BinarySearch.main(null);
```

    Target found at index: 12


#### Call 1
Index = 0 - 20, midPosition = 10, midPosition value = 20

Since 24 > 20, 

then... 

lowPosition = midPosition + 1 = 11
highPosition = highPosition = 20

#### Call 2
Index = 11-20, midPosition index = 15, midPosition value = 30

Since 24 < 30,

then...

lowPosition = lowPosition = 11
high position = midPosition - 1 = 14


#### Call 3
Index = 11-14, midPosition index = 12, midPosition value = 24

Since 24 = 24,

then...

return midPosition;

In total, our recursive calls to the method 3 times.

### Recursive Logic behind Merge Sort

What is Merge Sort?
Merge sort is a recursive sorting algorithm that can be used to sort elements in an array or ArrayList

- Follows a divide and conquer approach

![Link](https://media.discordapp.net/attachments/829194398364729365/1168722443377057872/QUaMvjx.png?ex=6552cc98&is=65405798&hm=6f4a3f3612f2f1ccf4ccbe3741e9dfdc328453c10a27b83338a723ec1e68327b&=&width=337&height=325)

### Notes:
```
List: [38,27,43,3,9,82,10] 

sudocode version:
mergeSort(List) {
    mergeSort(left)
    mergeSort(right)
    merge(left & right)

} 
```

- Must finish call above it in order to finish the call

Call 1: 
1. Splitting List into half 
2. Left side: [38, 27, 43, 3]
3. Must finish call 1 in order to do the right side and do the merge
4. Recursively calls mergesort and splits the list in half again

Call 2:
1. New Left side List: [38, 27]
2. Method calls are stacking on top of each other

![image](https://media.discordapp.net/attachments/829194398364729365/1168730076439908374/image.png?ex=6552d3b4&is=65405eb4&hm=ec96b560869e656d80c5cd64322f7ddeb94f183e19340813edfbef754c8c2445&=&width=762&height=425)

#### Notes:
1. Element 5 can't be split into the left or the right, nor can it be merged with itself
2. Consider the left call complete!

![image](https://media.discordapp.net/attachments/829194398364729365/1168731071916036166/image.png?ex=6552d4a1&is=65405fa1&hm=9014369cfbc0598eff54e91c567bb2281c07f4fa069e416cb6a1e846be283aeb&=&width=772&height=425)

#### Notes:
1. Same thing applies with the right, element 25 can't be split to the left or the right, nor can it merge with itself. 
2.  Now we will merge them back in order: [5, 25]

#### Important concepts: 
1. When making new recursive call, we are NOT making a new list, array, or a new set of elements. 
2. Basically updating all the way back to the original list

![img](https://media.discordapp.net/attachments/829194398364729365/1168731966858862733/image.png?ex=6552d576&is=65406076&hm=07b9e892835812449ea03f9e58a920611e0cb3f800bdface3f25078d64b2e4ba&=&width=725&height=425)

#### Notes:
1. When merging back together, it will merge back from least to greatest. 

![img](https://media.discordapp.net/attachments/829194398364729365/1168732306685558844/image.png?ex=6552d5c7&is=654060c7&hm=6df03d3ea8adbcc67d5cc3a82cc617a96c56d0250ad26e51723b57850358e054&=&width=880&height=425)

#### Popcorn Hack: What will the final list be?

Answer: 3, 9, 10, 27, 38, 43, 82

### The mergeSort Method

```
//sudocode
mergeSort(myArray, low, high) {
    if (low < high) {
        middle = (low + high)/2; //find middle
        mergeSort(myArray, low, middle); //make a recursive call from low to middle (look at left hand side)
        mergeSort(myArray, middle + 1, high); //once low is no longer less than high, make a new recursive call (look at right hand side)
        merge (myArray, low, middle, high); //merge back together
    }
}
```

```
int [] myArray = {3, 4, 6, 8, 1, 2, 5, 7};
```

#### Steps:

1. Split the Array in half
2. Left side: {3, 4, 6, 8}; Right side {1, 2, 5, 7};

![img](https://media.discordapp.net/attachments/829194398364729365/1168735841624006726/image.png?ex=6552d912&is=65406412&hm=7a20be09ae6e63eb0a0f998e5515c4ea6d02a7bb43ca0a8d4725c90cbb2d3727&=&width=662&height=139)

3. Compare the first indexes in each individual array (which would be index 0 and index 4)

![img](https://media.discordapp.net/attachments/829194398364729365/1168736588147212318/image.png?ex=6552d9c4&is=654064c4&hm=3d911c3eb088e3ae6b86ec96c96372f9b0314f86bbb8318a79d7719fa2d24fb3&=&width=587&height=130)

![img](https://media.discordapp.net/attachments/829194398364729365/1168736615351459901/image.png?ex=6552d9cb&is=654064cb&hm=8fb527126ca542b16242b2c5b18e319c2703c863d25caafc657db9a61d3564ef&=&width=824&height=169)

4. Since 1<3, our new index 0 value would be 1 when we merge the array back together

![img](https://media.discordapp.net/attachments/829194398364729365/1168737089744023645/image.png?ex=6552da3c&is=6540653c&hm=d6f2ad0d1586f38a0fba7a3915fea07d22540a1106e461d012305eeae33697b6&=&width=578&height=121)

![img](https://media.discordapp.net/attachments/829194398364729365/1168737204764422144/image.png?ex=6552da57&is=65406557&hm=ba40fc527b3ad870931fd9228940ff66c3540385057d435bbb9d704b0906b054&=&width=837&height=159)

5. Since 5>3, our new index 2 value would be 3 when we merge the array back together

#### Popcorn Hack: What will the final array return?

Answer: {1, 2, 3, 4, 5, 6, 7, 8}

#### Wait, but there's an issue...

![img](https://media.discordapp.net/attachments/829194398364729365/1168738307308519504/image.png?ex=6552db5e&is=6540665e&hm=a4b49b1f7cc3c76823db034dc491fc625b80b0e8f5c2dbfae73f5e9e27c0d39a&=&width=586&height=128)

![img](https://media.discordapp.net/attachments/829194398364729365/1168738330993758318/image.png?ex=6552db64&is=65406664&hm=31a3de717babc4970f8234b1ed17170f092ab42b72fdcc737bba1a55f30b12ab&=&width=722&height=157)

- After comparing index 3 and index 7, we then need to compare index 3 and index, but there is no index 8...
- Will recieve an index out of bounds exception.

No worries! Since we are done with the sort, we can just move the rest of the elements to the end of the array because we are already done sorting. 

Index 3 will now become index 7.

## Hacks

- Create a 2D array either with just a regular array variable that you can recursively traverse through.
- Each value in this 2D array must be a string that you can individually traverse through.
- You must output a result of all string values that have a user inputted letter.


```Java
import java.util.Scanner;

public class String2DArrayTraversal {
    public static void main(String[] args) {
        String[][] array = new String[3][3];
        array[0][0] = "apple";
        array[0][1] = "banana";
        array[0][2] = "cherry";
        array[1][0] = "date";
        array[1][1] = "elderberry";
        array[1][2] = "fig";
        array[2][0] = "grape";
        array[2][1] = "honeydew";
        array[2][2] = "idk";

        System.out.println("Look for A:");
        traverseString2DArray(array, 'a');
        System.out.println();
        System.out.println("Look for B:");
        traverseString2DArray(array, 'b');
        System.out.println();
        System.out.println("Look for C:");
        traverseString2DArray(array, 'w');
    }

    public static void traverseString2DArray(String[][] array, char letter) {
        for (int i=0; i<3; i++) {
            for (int j=0; j<3; j++) {
                String string = array[i][j];
                for (int k=0; k<string.length(); k++) {
                    if (string.charAt(k) == letter) {
                        System.out.println(array[i][j]);
                        break;
                    }
                }
            }
        }
    }
}

String2DArrayTraversal.main(null);
```

    Look for A:
    apple
    banana
    date
    grape
    
    Look for B:
    banana
    elderberry
    
    Look for C:
    honeydew


Create your own merge chart (like the first image in this 10.2 lesson) with your own values from a list, array, or arraylist (doesn't matter). Explain how recursion works in the merge chat.

`[1, 2, 3, 4, 5, 6, 7, 8]`

Lets scramble this array

`[8, 4, 3, 7, 1, 2, 6, 5]`

Merge sort it...

`[8, 4, 3, 7] [1, 2, 6, 5]` Split 1: Split into 2 smaller arrays of 4, but we can keep going

`[8, 4] [3, 7] [1, 2] [6, 5]` Split 2: Split into 4 smaller arrays of 4. Lets sort!

`[4, 8] [3, 7] [1, 2] [5, 6]` Sort 1: 4 is less than 8, so swap the positions. Same thing for 6 and 5

`[4, 8, 3, 7] [1, 2, 5, 6]` Merge 1: Merge the two lists!

`[3, 4, 7, 8] [1, 2, 5, 6]` Sort 2: 4 and 8 are in order, so lets go straight to 3. 3 is less than 8 and 4, so move it past both of those. Next we get to 7, which is less than 8, so move it past 8.

`[3, 4, 7, 8, 1, 2, 5, 6]` Merge 2: Merge the two lists!

`[1, 2, 3, 4, 5, 6, 7, 8]` Sort 3: 3, 4, 7, 8 are in order. 1 is less than 3, 4, 7, and 8, so move it past all of these. 2 is less than 3, 4, 7, and 8, so move it past all of these. 5 is less than 7 and 8, so move it past these. 6 is less than 7 and 8, so move it past these.

We are sorted!
