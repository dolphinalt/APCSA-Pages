---
title: Java Hello
author: Ethan
date: 2023-08-21 11:33:00 +0800
week: 1
categories: ['Week1']
tags: week1
type: hacks
pin: False
mermaid: False
---

## Hello, World!
This article shows the basic language structures and constructs of Java (aka anatomy).  In async order, it is critical to understand these examples and learn vocab for OOP and Creating Objects: 
- [Object Oriented Programming](https://youtu.be/Wok4Xw_5cyY) 
- [Creating Objects](https://youtu.be/C5Ks_u87Ltg)
- [Calling Methods](https://youtu.be/CPE_lYGCw3A)

### Static example
The class HelloStatic contains the classic "Hello, World!" message that is often used as an introduction to a programming language.  The "public static void main(String[] args)", or main method, is the default runtime method in Java and has a very specific and ordered definition (signature). 

The key terms in HelloStatic introduction:
- "class" is a blueprint for code, it is the code definition and must be called to run
- "method" or "static method" in this case, is the code to be run/executed, similar to a procedure
- "method definition" or "signature" are the keywords "public static void" in front of the name "main" and the parameters "String[] args" after the name.
- "method call" is the means in which we run the defined code



```Java
// Define Static Method within a Class
public class HelloStatic {
    // Java standard runtime entry point
    public static void main(String[] args) {    
        System.out.println("Hello World!");
    }
}
// A method call allows us to execute code that is wrapped in Class
HelloStatic.main(null);   // Class prefix allows reference of Static Method
```

    Hello World!


### Dynamic Example
This example starts to use Java in its natural manner, using an object within the main method. This example is a very basic illustration of Object Oriente Programming (OOP). The main method is now used as a driver/tester, by making an instance of the class.  Thus, it creates an Object using the HelloObject() constructor.  Also, this Class contains a getter method called getHello() which returns the value with the "String hello".

The key terms in HelloStatic introduction:
- "Object Oriented Programming" focuses software design around data, or objects.
- "object" contains both methods and data
- "instance of a class" is the process of making an object, unique or instances of variables are created within the object
- "constructor" special method in class, code that is used to initialize the data within the object
- "getter" is a method that is used to extract or reference data from within the object. 


```Java
// Define Class with Constructor returning Object
public class HelloObject {
    private String hello;   // instance attribute or variable
    public HelloObject() {  // constructor
        hello = "Hello, World!";
    }
    public String getHello() {  // getter, returns value from inside the object
        return this.hello;  // return String from object
    }
    public static void main(String[] args) {    
        HelloObject ho = new HelloObject(); // Instance of Class (ho) is an Object via "new HelloObject()"
        System.out.println(ho.getHello()); // Object allows reference to public methods and data
    }
}
// IJava activation
HelloObject.main(null);
```

    Hello, World!


### Dynamic Example with two constructors
This last example adds to the basics of the Java anatomy.  The Class now contains two constructors and a setter to go with the getter.  Also, observe the driver/tester now contains two objects that are initialized differently, 0 and 1 argument constructor.  Look at the usage of the "this" prefix.  The "this" keyword helps in clarification between instance and local variable.

The key terms in HelloDynamic introduction:
- "0 argument constructor" constructor method with no parameter ()
- "1 argument constructor" construct method with a parameter (String hello)
- "this keyword" allows you to clear reference something that is part of the object, data or method
- "local variable" is a variable that is passed to the method in this example, see the 1 argument constructor as it has a local variable "String hello"
- "dynamic" versus "static" is something that has option to change, static never changes.  A class (blueprint) and objects (instance of blueprint) are generally intended to be dynamic.  Constructors and Setters are used to dynamically change the content of an object.
- "Java OOP, Java Classes/Objects, Java Class Attributes, Java Class Methods, Java Constructors" are explained if more complete detail in W3 Schools: https://www.w3schools.com/java/java_oop.asp


```Java


// Define Class
public class HelloDynamic { // name the first letter of class as capitalized, note camel case
    // instance variable have access modifier (private is most common), data type, and name
    private String hello;
    // constructor signature 1, public and zero arguments, constructors do not have return type
    public HelloDynamic() {  // 0 argument constructor
        this.setHello("Hello, World!");  // using setter with static string
    }
    // constructor signature, public and one argument
    public HelloDynamic(String hello) { // 1 argument constructor
        this.setHello(hello);   // using setter with local variable passed into constructor
    }
    // setter/mutator, setter have void return type and a parameter
    public void setHello(String hello) { // setter
        this.hello = hello;     // instance variable on the left, local variable on the right
    }
    // getter/accessor, getter used to return private instance variable (encapsulated), return type is String
    public String getHello() {  // getter
        return this.hello;
    }
    // public static void main(String[] args) is signature for main/drivers/tester method
    // a driver/tester method is singular or called a class method, it is never part of an object
    public static void main(String[] args) {  
        HelloDynamic hd1 = new HelloDynamic(); // no argument constructor
        HelloDynamic hd2 = new HelloDynamic("Hello, Nighthawk Coding Society!"); // one argument constructor
        System.out.println(hd1.getHello()); // accessing getter
        System.out.println(hd2.getHello()); 
    }
}
// IJava activation
HelloDynamic.main(null);
```

    Hello, World!
    Hello, Nighthawk Coding Society!


## Hacks
Build your own Jupyter Notebook meeting these College Board and CTE competencies.  It is critical to understand Static versus Instance Now, this is College Board requirement!!!
- Explain [Anatomy of a Class](https://runestone.academy/ns/books/published/csawesome/Unit5-Writing-Classes/topic-5-1-parts-of-class.html) in comments of program (Diagram key parts of the class).
- Comment in code where there is a definition of a Class and an instance of a Class (ie object)
- Comment in code where there are constructors and highlight the signature difference in the signature
- Call an object method with parameter (ie setters).


Additional requirements (Pick something)
1. Go through code progression of understanding Class usage and generating an Instance of a Class (Object).

    a. Build a purposeful dynamic Class, using an Object, generate multiple instances: 
        - Person: Name and Age
        - Dessert: Type and Cost
        - Location: City, State, Zip

    b. Create a static void main tester method to generate objects of the class.

    c. In tester method, show how setters/mutators can be used to make the data in the Object dynamically change

3. Go through progression of understanding a Static Class.  Build a purposeful static Class, no Objects.

    - Calculate common operations on a Date field, age since date, older of two dates, number of seconds since date
    
    - Calculate stats functions on an array of values: mean, median, mode.


```Java

// import Arraylist
import java.util.ArrayList;
// Define Class
public class DynamicEmployees { // name the first letter of class as capitalized, note camel case
    // instance variable have access modifier (private is most common), data type, and name
    private String name;
    private String id;
    private String email;
    // constructor signature 1, public and zero arguments, constructors do not have return type
    public DynamicEmployees() {  // 0 argument constructor
        this.setName("First Last");  // using setter with static string
        this.setID("$#####");
        this.setEmail("First.Last@fin.com");
    }
    // constructor signature, public and three arguments
    public DynamicEmployees(String name, String id, String email) { // 3 argument constructor
        this.setName(name);   // using setter with local variable passed into constructor
        this.setID(id);
        this.setEmail(email);
    }
    // setter/mutator, setter have void return type and a parameter
    public void setName(String name) { // setter
        this.name = name;     // instance variable on the left, local variable on the right
    }
    public void setID(String id) {
        this.id = id;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    // getter/accessor, getter used to return private instance variable (encapsulated), return type is String
    public ArrayList getEmployee() {  // getter
        ArrayList<String> result = new ArrayList<String>();
        result.add(this.name);
        result.add(this.id);
        result.add(this.email);
        return result;
    }
    // public static void main(String[] args) is signature for main/drivers/tester method
    // a driver/tester method is singular or called a class method, it is never part of an object
    public static void main(String[] args) {
        DynamicEmployees employee1 = new DynamicEmployees(); // no argument constructor
        DynamicEmployees employee2 = new DynamicEmployees("Ethan Zhao", "A00001", "Ethan.Zhao@fin.com"); // three argument constructor
        ArrayList E1=employee1.getEmployee();
        ArrayList E2=employee2.getEmployee();
        System.out.println(E1.get(0) + " - " + E1.get(1) + " - " + E1.get(2)); // accessing getter
        System.out.println(E2.get(0) + " - " + E2.get(1) + " - " + E2.get(2)); 
    }
}
// IJava activation
DynamicEmployees.main(null);
```

    First Last - $##### - First.Last@fin.com
    Ethan Zhao - A00001 - Ethan.Zhao@fin.com



```Java
import java.util.*;

public class Stats {
    public static void main(String[] args) {
        List<Integer> testList = Arrays.asList(1, 3, 5, 7, 9, 20, 5, 3, 15, 13, 12, 11, 2, 4, 6, 8, 10, 14, 16, 18, 19, 17);

        mean(testList);
        std(testList);
        median(testList);
        range(testList);
        min(testList);
        max(testList);
    }

    public static void mean(List<Integer> values) {
        int sum = 0;
        for (int value : values) {
            sum += value;
        }
        System.out.println("Mean: " + ((double) sum / values.size()));
    }

    public static void std(List<Integer> values) {
        int sum = 0;
        for (int value : values) {
            sum += value;
        }
        double mean = (double) sum / values.size();
        double std = 0;
        for (int value : values) {
            std += Math.pow(value - mean, 2);
        }
        System.out.println("Standard Deviation: " + (Math.sqrt(std / values.size())));
    }

    public static void median(List<Integer> values) {
        Collections.sort(values);
        int size = values.size();
        if (size % 2 == 0) {
            int mid1 = values.get(size / 2);
            int mid2 = values.get(size / 2 - 1);
            System.out.println("Median: " + (double) (mid1 + mid2) / 2);
        } else {
            System.out.println("Median: " + ((double) values.get(size / 2)));
        }
    }

    public static void range(List<Integer> values) {
        Collections.sort(values);
        int min = values.get(0);
        int max = values.get(values.size() - 1);
        System.out.println("Range: " + (max - min));
    }

    public static void min(List<Integer> values) {
        Collections.sort(values);
        System.out.println("Min: " + (values.get(0)));
    }

    public static void max(List<Integer> values) {
        Collections.sort(values);
        System.out.println("Max: " + (values.get(values.size() - 1)));
    }
}
Stats.main(null);

```

    Mean: 9.909090909090908
    Standard Deviation: 5.814629597435412
    Median: 9.5
    Range: 19
    Min: 1
    Max: 20

