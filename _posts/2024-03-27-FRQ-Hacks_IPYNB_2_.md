---
title: FRQ Hacks
author: Ethan
date: 2024-03-27 11:33:00 +0800
week: 27
categories: ['Week27']
tags: week27
type: hacks
pin: False
mermaid: False
---

## ## Question 1: Primitive Types vs Reference Types (Unit 1)

Situation: You are developing a banking application where you need to represent customer information. You have decided to use both primitive types and reference types for this purpose.

(a) Define primitive types and reference types in Java. Provide examples of each.

(b) Explain the differences between primitive types and reference types in terms of memory allocation and usage in Java programs.

(c) Code:

You have a method calculateInterest that takes a primitive double type representing the principal amount and a reference type Customer representing the customer information. Write the method signature and the method implementation. Include comments to explain your code.

## My Solution


```Java
// A:

// primitivie types are the basic types defined by the language
int num =1;
double decimal = 1.1;
boolean bool = true;
char character = 'A';

// reference types are classes
String str = "Hello";
Class class = new Class();
ArrayList<Integer> list = new ArrayList<>();

// B:
// primitives are stored directly in stack memory, while reference types are stored in heap memory. Primitives hold a var's true value while references are a references to a memory location
```


```Java
// C:
class Customer { // define customer class
    private double interestRate; // define the var interestRate

    public Customer(double interestRate) {
        this.interestRate = interestRate;
    }

    public double getInterestRate() {
        return interestRate; // return the interest rate of the customer
    }
}

public class Bank {
    public double calculateInterest(double principal, Customer customer) {
        double interestRate = customer.getInterestRate(); // get interest rate from customer
        double interest = principal*interestRate; // calculate interest rate by doing principle multiplied by the rate
        return interest;
    }

    public static void main(String[] args) { // main tester method
        Customer customer = new Customer(0.1);
        double principal = 1000.0;
        Bank bank = new Bank();
        double interest = bank.calculateInterest(principal, customer);
        System.out.println("Interest: " + interest);
    }
}

Bank.main(null);
```

    Interest: 100.0


## Question 2: Iteration over 2D arrays (Unit 4)
Situation: You are developing a game where you need to track player scores on a 2D grid representing levels and attempts.

(a) Explain the concept of iteration over a 2D array in Java. Provide an example scenario where iterating over a 2D array is useful in a programming task.

(b) Code:

You need to implement a method calculateTotalScore that takes a 2D array scores of integers representing player scores and returns the sum of all the elements in the array. Write the method signature and the method implementation. Include comments to explain your code.

## My Solution


```Java
// A:
// Iteration over a 2D array is when you go through every element in a 2D array. This can be done by an i j loop. A 2D array can be useful when analyzing cartesian graphical values

// B:
public class Game {
    public static int calculateTotalScore(int[][] scores) { // method to calculate total score
        int total = 0;
        for (int i = 0; i < scores.length; i++) {
            for (int j = 0; j < scores[i].length; j++) { // i j loop to iterate through 2D array
                total += scores[i][j];
            }
        }
        return total;

    }

    public static void main(String[] args) { // main tester method
        int[][] scores = {
            {1, 22, 3},
            {11, 22, 33},
            {111, 222, 333}
        };

        Game game = new Game(); // create new game instance

        int totalScore = game.calculateTotalScore(scores); // calculating the score
        System.out.println("Total Score: " + totalScore);
    }
}

Game.main(null);
```

    Total Score: 758


## Question 5: If, While, Else (Unit 3-4)

Situation: You are developing a simple grading system where you need to determine if a given score is passing or failing.

(a) Explain the roles and usage of the if statement, while loop, and else statement in Java programming. Provide examples illustrating each.

(b) Code:

You need to implement a method printGradeStatus that takes an integer score as input and prints “Pass” if the score is greater than or equal to 60, and “Fail” otherwise. Write the method signature and the method implementation. Include comments to explain your code.

## My Solution


```Java
// A:
// If statements are used as a conditional when we need to decide between one thing or another depending on the value of a variable
// While loops are used when we want to loop a block of code until a condition is met
// Else statements are used at the end of an if conditional block and is used as a "catch all"

int age = 0;

while (age < 20) {
    System.out.println("Age: " + age);
    if (age > 18) {
        System.out.println("Adult!");
    } else {
        System.out.println("Child!");
    }
    age++;
}

// B:
System.out.println("================");

public class Grade {
    public void getStatus(int score) {
        if (score >= 60) { // checks if score is greater than or equal to 60
            System.out.println("Pass! " + score + "%"); // passes if condition is met
        } else {
            System.out.println("Fail! " + score + "%"); // fails if condition is not met
        }
    }

    public static void main(String[] args) {
        Grade g = new Grade();

        g.getStatus(75);
        g.getStatus(40);
    }
}

Grade.main(null);
```

    Age: 0
    Child!
    Age: 1
    Child!
    Age: 2
    Child!
    Age: 3
    Child!
    Age: 4
    Child!
    Age: 5
    Child!
    Age: 6
    Child!
    Age: 7
    Child!
    Age: 8
    Child!
    Age: 9
    Child!
    Age: 10
    Child!
    Age: 11
    Child!
    Age: 12
    Child!
    Age: 13
    Child!
    Age: 14
    Child!
    Age: 15
    Child!
    Age: 16
    Child!
    Age: 17
    Child!
    Age: 18
    Child!
    Age: 19
    Adult!
    ================
    Pass! 75%
    Fail! 40%

