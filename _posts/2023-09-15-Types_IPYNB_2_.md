---
title: Types
author: Ethan
date: 2023-10-03 11:33:00 +0800
week: 6
categories: ['Week6']
tags: week6
type: hacks
pin: False
mermaid: False
---

Java is used around the world to create applications and is one of the most popular coding languages. The reason Java is so popular is because of it's security and versatility provided by it's Object Oriented nature.

# 1.1 Basics

```
public class Main {
  int x = 5;

  public static void main(String[] args) {
    Main myObj = new Main();
    System.out.println(myObj.x);
  }
}
```

# 1.2 Variables and Data Types

## Variables

A Variable is a name given to a memory location that is holding the specified value. Here are some naming practices:

- Use camel case. likeThis.
- Don't start with a number.
- Spaces are not allowed.
- No reserved characters, like $, @, and &

***Java is a strongly typed language so you always need to declare the type of the variable.*** Variables can also be declared on their own or in the same line as when they are given a value:



```java
int primitive5;
primitive4 = 1;

//Or...
int primitive6 = 1;
```

What are the greatest values integers and doubles can store?
Largest negative DOUBLE value: -1.7976931348623157E+308.
Largest positive DOUBLE value: 1.7976931348623157E+308.
Largest possible INTEGER value: 2147483647
Largest possible INTEGER value: –9223372036854775808

## Primitive Data

Primitive data determines ***the size and type of information***. Primitive types are the most simple type of variable. They are simply store a short amount of raw data, and are not associated with another class.

Here are the different primitive types:
- byte: An 8-bit signed two's complement integer.
- short: A 16-bit signed two's complement integer.
- int: A 32-bit signed two's complement integer.
- long: A 64-bit signed two's complement integer.
- float: A single-precision 32-bit IEEE 754 floating point.
- double: A double-precision 64-bit IEEE 754 floating point.
- boolean: Stores either true or false.
- char: Stores a single character.

For this class you need to know:


```java
boolean primitive3 = true; //Stores a true of false binary value
int primitive1 = 0; //Whole number
double primitive2 = 1.1; //Decimal values. Floating point numbers.
char primitive4 = 'a'; //Single character
```

| Data Type | Size (bits) |
|-----------|-------------|
| boolean   | 8           |
| int       | 32          |
| double    | 64          |
| char      | 16          |


```java
public class GreatestValue {
    public static void main(String[] args) {
        i=Integer.MAX_VALUE;
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE);
        System.out.println(Double.MAX_VALUE);
        System.out.println(Double.MIN_VALUE);
        system.out.println(++i;);
    }
}
GreatestValue.main(null);
```

## Reference Types
Some data types, like String, start with a capital letter. This is because they are not primiative, but are refrence types. They are called this because they refrence an object.
> "A reference type is a code object that is not stored directly where it is created, but that acts as a kind of pointer to a value stored elsewhere."


```java
int integer = 7120; //"int" starts with a lowercase
String string = "abc"; //"String" starts with an uppercase, because it is an object and not a primitive type
```

## All Reference Types Reference Objects: String Example

String is the most common reference type. Here is an example of how a String type is really just referencing an object.


```java
public class WorseString {
    private char[] charArray;

    public WorseString(String inputString) {
        this.charArray = inputString.toCharArray();
    }

    public String getChars() {
        return new String(this.charArray);
    }

    @Override
    public String toString() {
        return getChars();
    }
}
```


```java
WorseString string = new WorseString("Hello, World!");
System.out.println(string);
```

    Hello, World!


Therefore, these two things are the same:


```java
String string = "abc";
String string = new String("abc");
```

## Literal vs String literal

- Literal: Source code representation of a fixed value --- 3
- String Literal: In double quotes, a String --- "3"

# 1.3 Expressions and Assignment Statements

Calculations and evaluating arithmetic statements is important when coding to create algorithms and other code. Make sure you are doing arithmetic statements with int or double values and not String literals

## Operators

| Operator | Example Equation | Output | Use |
|----------|------------------|--------|------------|
| +        | 5 + 3            | 8      | Add numbers together. |
| -        | 5 - 3            | 2      | Subtract one number from another. |
| *        | 5 * 3            | 15     | Multiply numbers together. |
| /        | 5 / 3            | 1 | Divide one number by another. |
| /        | 5 / 3.0            | 1.67 | Divide one number by a double. |
| %        | 5 % 3            | 2      | Find the remainder of a division operation. |


> Tip: In the AP subset, you only have to worry about operations with int values. However, it's good to know how to use arithmetic statements with doubles and other types. 

If you do an operation with two ints or doubles, it returns the respective type. If you mix types, Java returns the one with more bits, a double in this case.

## Modulus

Modulus gets the remainder if you were to divide two numbers. One common use is to find odd/even numbers. 

- 5 % 2 = 1
- 100 % 10 = 0

You try: 

- 8 % 3 = 2
- 4 % 1 = 0

**__*Modulus joins multiplication and division in the order of operations*__**

## Assignment Operator

= is called the assignment operator because it is used to assign a value to a variable. It is the last in the order of operations.

## Casting
Casting is converting one type of variable to another
ex: double to int


```java
public class Casting {
    public static void main(String[] args) {
        double castTest = 3.2;
        System.out.println((int) castTest);
        castTest = 3.7;
        System.out.println((int) castTest);
        System.out.println((int) (castTest+0.5));

        int castTest2 = 3;
        System.out.println(castTest2/2);
        System.out.println(castTest2/2.0);
    }
}
Casting.main(null);
```

    3
    3
    4
    1
    1.5


What will this output?
```java
castTest2 = 7;
System.out.println(castTest2/3);
System.out.println((int) (castTest2+0.5));
```
output:
```
2
7
```

## Wrapper Classes

For many operations in Java, you need to have a class. Some examples are:
- **ArrayLists or HashMaps**
- If you require nullability (meaning the value could be null)
- Generics
- Methods that require objects as input

To accomplish this, we use a wrapper class. A wrapper class is essentially a class which 'wraps' the primitive type and makes it into an object rather than a primitive.

What is a downside of using wrapper classes? Why not always use them?

<spoiler>Increased memory usage</spoiler> 


```java
//This code fails
ArrayList ArrayList = new ArrayList<int>();
```


```java
//This code works
ArrayList ArrayList = new ArrayList<Integer>();
```

![]({{site.baseurl}}/images/download.jfif)


```java
public class Wrappers {
    Integer ageWrapper = 17;
    int age = Integer.parseInt("17");
    String gpaString = "3.9";
    double gpaDouble = Double.parseDouble(gpaString);

    public static void main(String[] args) {
        Wrappers wrapper = new Wrappers();
        System.out.println(wrapper.ageWrapper);
        System.out.println(wrapper.age);
        System.out.println(wrapper.gpaDouble);
    }
}
Wrappers.main(null);
```

    17
    17
    3.9


How do you complete this output so that it outputs an integer
```java
String grade = "95";
int gradeInt = Integer.parseInt(grade);
System.out.println(gradeInt);
```
```
95
```

How do you complete this output so that it outputs a double?
```java
String grade = "95.5";
int gradeDouble = Double.parseDouble(grade);
System.out.println(gradeDouble);
```
```
95.5
```

## Enums
What are they?
<spoiler>Enums are a type of data, which allows a variable to be a predetermined set of values</spoiler>

Uses
* Examples: days of the week

Things you can do with Enums
* ordinal
* switch
* for loops


```java
public class EnumTest { 
    enum Units {
    PRIMITVE_DATA_TYPES,
    CLASSES,
    BOOLEAN,
    ITERATION,
    WRITING_CLASSES,
    ARRAY,
    ARRAY_LIST,
    TWO_DIMENSIONAL_ARRAY,
    INHERITANCE,
    RECURSION;
}
public static void main(String[] args) { 
  System.out.println("What is the third unit in AP CSA? Answer: " + Units.BOOLEAN);
  Units classUnit = Units.CLASSES;
  System.out.println("What is the unit is Classes in AP CSA? Answer: " + (classUnit.ordinal() + 1));
  Units selectedUnit = Units.ARRAY_LIST;

  switch(selectedUnit) {
    case PRIMITVE_DATA_TYPES:
      System.out.println("The selected unit is: primitive data types");
      break;
    case BOOLEAN:
       System.out.println("The selected unit is: boolean");
      break;
    case CLASSES:
      System.out.println("The selected unit is: classes");
      break;
    case ITERATION:
      System.out.println("The selected unit is: iteration");
      break;
    case WRITING_CLASSES:
      System.out.println("The selected unit is: writing classes");
      break;
    case ARRAY:
      System.out.println("The selected unit is: array");
      break;
    case ARRAY_LIST:
      System.out.println("The selected unit is: array list");
      break;
    case TWO_DIMENSIONAL_ARRAY:
      System.out.println("The selected unit is: 2d array");
      break;
    case INHERITANCE:
      System.out.println("The selected unit is: inheritance");
      break;
    case RECURSION:
      System.out.println("The selected unit is: recursion");
      break;
  }
  for (Units allUnits: Units.values()) {
    System.out.println(allUnits);
  }
} 
}
EnumTest.main(null);
```

    What is the third unit in AP CSA? Answer: BOOLEAN
    What is the unit is Classes in AP CSA? Answer: 2
    The selected unit is: array list
    PRIMITVE_DATA_TYPES
    CLASSES
    BOOLEAN
    ITERATION
    WRITING_CLASSES
    ARRAY
    ARRAY_LIST
    TWO_DIMENSIONAL_ARRAY
    INHERITANCE
    RECURSION


# Homework

All of your homework is on this [form](https://forms.gle/M6FgxZwX1AnWdZmL9). (Link is https://forms.gle/M6FgxZwX1AnWdZmL9)

Create a program using enums and a switch statement. The values in the enum are the days of the week. If it is Tuesday, then print, "Today is Tuesday!".


```java
public class Week {
  enum Days {
      Monday,
      Tuesday,
      Wednesday,
      Thursday,
      Friday,
      Saturday,
      Sunday
  }

  public static void main(String[] args) {
      System.out.println("What is the third day of the week? Answer: " + Days.values()[2]);

      Days fourthDay = Days.Thursday;
      System.out.println("What is the unit in Classes in AP CSA? Answer: " + (fourthDay.ordinal() + 1));

      Days selectedDay = Days.Tuesday;
      switch (selectedDay) {
          case Monday:
              System.out.println("The selected day is: Monday");
              break;
          case Tuesday:
              System.out.println("The selected day is: Tuesday");
              break;
          case Wednesday:
              System.out.println("The selected day is: Wednesday");
              break;
          case Thursday:
              System.out.println("The selected day is: Thursday");
              break;
          case Friday:
              System.out.println("The selected day is: Friday");
              break;
          case Saturday:
              System.out.println("The selected day is: Saturday");
              break;
          case Sunday:
              System.out.println("The selected day is: Sunday");
              break;
      }

      for (Days allDays : Days.values()) {
          System.out.println(allDays);
      }
  }
}

```


```java
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
            System.out.println("|============================|");
            System.out.println("|Welcome to the Calculator!  |");
            System.out.println("|============================|");

        while (true) {
            System.out.println("|=======================|");
            System.out.println("| Choose an operation:  |");
            System.out.println("| 1. Addition           |");
            System.out.println("| 2. Subtraction        |");
            System.out.println("| 3. Multiplication     |");
            System.out.println("| 4. Exit               |");
            System.out.println("|=======================|");

            int operationChoice = scanner.nextInt();

            if (operationChoice == 4) {
                System.out.println("|===============================|");
                System.out.println("| Calculator exiting. Goodbye!  |");
                System.out.println("|===============================|");
                break;
            }

            System.out.print("Enter the first number: ");

            double operand1;
            double operand2;
            if (operationChoice == 1 || operationChoice == 2 || operationChoice == 3) {
                operand1 = scanner.nextDouble();
                System.out.println("|===========================|");
                System.out.println("| Enter the second number:  |");
                System.out.println("|===========================|");
                operand2 = scanner.nextDouble();
            } else {
                System.out.println("Invalid choice. Please enter a valid option.");
                continue;
            }

            double result;
            String operationSymbol;

            switch (operationChoice) {
                case 1:
                    result = operand1 + operand2;
                    operationSymbol = "+";
                    break;
                case 2:
                    result = operand1 - operand2;
                    operationSymbol = "-";
                    break;
                case 3:
                    result = operand1 * operand2;
                    operationSymbol = "*";
                    break;
                default:
                    System.out.println("\nInvalid choice. Please enter a valid option.");
                    continue;
            }

            System.out.println("\nResult: " + operand1 + " " + operationSymbol + " " + operand2 + " = " + result);
        }

        scanner.close();
    }
}

```
