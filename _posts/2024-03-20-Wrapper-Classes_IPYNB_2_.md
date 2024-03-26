---
title: Wrapper Classes
author: Ethan
date: 2024-03-26 11:33:00 +0800
week: 21
categories: ['Week21']
tags: week21
type: hacks
pin: False
mermaid: False
---

# Lesson on Java Wrapper Classes

## Introduction
- Java's primitive data types are efficient but not as flexible as objects.
- Wrapper classes turn primitive data types into objects.
- Part of `java.lang` package, automatically imported.


## What Are Wrapper Classes?
his is crucial in Java because it allows primitives to be used in contexts that require objects, like ArrayLists.
- Each primitive data type in Java has a corresponding wrapper class. 
- Provide object versions of eight primitive types.
- Enable primitives to be used in object-required scenarios, like collections.

### Primitive Types and Their Wrappers
- `byte` → `Byte`
- `short` → `Short`
- `int` → `Integer`
- `long` → `Long`
- `float` → `Float`
- `double` → `Double`
- `char` → `Character`
- `boolean` → `Boolean`

Popcorn Hack: Fill out the above.

# Why Use Wrapper Classes? 
- Collections Framework: The Collections Framework in Java works with objects, not primitive types. To store, for example, integers in an ArrayList, you need to use the Integer wrapper class.

- Utilities: Wrapper classes provide useful methods. For instance, you can convert strings to integers or check the size of an integer or character.

- Null Value Support: Primitive types cannot be null, but their wrapper classes can be. This is useful when you need a way to represent the absence of a value.

## Creating Wrapper Objects
1. **Constructor Method** (Older, less preferred method)
   - `Integer myInt = new Integer(5);`
   - `Double myDouble = new Double(4.5);`
2. **valueOf() Method** (Preferred method)
   - `Integer myInt = Integer.valueOf(5);`
   - `Double myDouble = Double.valueOf(4.5);`

## Autoboxing and Unboxing
- **Autoboxing**: Automatic conversion from primitive to wrapper.
  - `Integer myInt = 5;`
- **Unboxing**: Automatic conversion from wrapper to primitive.
  - `int myPrimitiveInt = myInt;`

## Utility Methods
- **Parsing Strings**: `int num = Integer.parseInt("123");`
- **Converting to Strings**: `String str = myInt.toString();`
- **Comparing Values**: `int comparison = Integer.compare(5, 10);`

## Example Code Snippets
### Autoboxing and Unboxing
```java
Integer autoBoxedInt = 15; // Autoboxing
int unboxedInt = autoBoxedInt; // Unboxing
```

### Using Utility Methods
```java
int parsedInt = Integer.parseInt("20");
String intString = Integer.toString(10);
int comparisonResult = Integer.compare(5, 10);
```

### Practical Example


```Java
public class WrapperDemo {
    public static void main(String[] args) {
        // Creating Wrapper Objects
        Integer myInt = Integer.valueOf(10);
        Double myDouble = Double.valueOf(5.5);

        // Demonstrating Autoboxing
        Integer autoBoxedInt = 15;
        
        // Demonstrating Unboxing
        int unboxedInt = autoBoxedInt;
        
        // Using Utility Methods
        int parsedInt = Integer.parseInt("20");
        String intString = myInt.toString();
        
        // Displaying Results
        System.out.println("Parsed Integer from String: " + parsedInt);
        System.out.println("Integer to String: " + intString);
    }
}

WrapperDemo.main(null);
```

    Parsed Integer from String: 20
    Integer to String: 10


<h1>Example FRQ (2015 FRQ 2 ADAPTED)</h1>

You are given a Java class called HiddenWord, which represents a hidden word puzzle game. Your task is to modify the HiddenWord class to include a method that returns the length of the hidden word as an instance of a wrapper class called WordLength. Provide comments throughout your code to ensure understanding of wrapper classes and their implementation in the HiddenWord class.

**SOLUTION**


```Java
public class HiddenWord {
    private String word;
    private Integer length; // Using Integer wrapper class to store the length

    // Constructor to initialize the hidden word and its length
    public HiddenWord(String hWord) {
        word = hWord;
        length = hWord.length(); // Storing the length using the Integer wrapper class
    }

    // Method to retrieve the length of the word
    public Integer getLength() {
        return length;
    }

}

```

<h1>Common Tips & Tricks for Classes FRQ</h1>

1. Make sure to use all the names for the methods and classes that are given to you on the exam. This is a basic layup point, and not following instructions can cause you to lose easy points. Read the question as carefully as possible!

2. The classes FRQ is always going to have the same structure - class, private instance variables, constructors, and accessing that instance variable. Then, there will be the algorithm that needs to be implemented, which you can likely figure out from the problem and code blobs it provides for you.

3. It is likely that Java wrapper classes are not going to be explicitly tested upon in the FRQs. However, you should remember the common wrapper classes - integer, double, boolean, character, etc. Furthermore, make sure that you don't unnecessarily use autoboxing/unboxing. You want your code to be as efficient and as object-oriented as possible, so make sure you are only autoboxing when you need to.


<h1>HACKS</h1>

(a) Provide a brief summary of what a wrapper class is and provide a small code block showing a basic example of a wrapper class.

Wrapper classes are classes that wrap, or encapsulate, primitive data types in Java.

```java
int myInt = 5; // Primitive
Integer myInt = 5; // Wrapped
```

(b) Create a Java wrapper class called Temperature to represent temperatures in Celsius. Your Temperature class should have the following features:

Fields:

A private double field to store the temperature value in Celsius.


Constructor:

A constructor that takes a double value representing the temperature in Celsius and initializes the field.


Methods:

getTemperature(): A method that returns the temperature value in Celsius.
setTemperature(double value): A method that sets a new temperature value in Celsius.
toFahrenheit(): A method that converts the temperature from Celsius to Fahrenheit and returns the result as a double value. 


```Java
public class Celsius {
    private Double temperature;

    public Celsius(Double temp) {
        temperature = temp;
    }
    public Double getTemperature() {
        return temperature;
    }
    public Double toFahrenheit() {
        return (temperature * 9 / 5) + 32;
    }
}

public class Main {
    public static void main(String[] args) {
        Celsius celsius = new Celsius(25.0);
        System.out.println("Temperature in Celsius: " + celsius.getTemperature());
        System.out.println("Temperature in Fahrenheit: " + celsius.toFahrenheit());
    }
}

Main.main(null);



```

    Temperature in Celsius: 25.0
    Temperature in Fahrenheit: 77.0

