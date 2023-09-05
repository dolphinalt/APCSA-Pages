---
title: Java Console Games
author: Ethan
date: 2023-08-23 11:33:00 +0800
week: 1
categories: ['Week1']
tags: week1
type: hacks
pin: False
mermaid: False
---

## Java Kernel for Jupyter Notebooks.
> [Install Java kernel readme}(https://github.com/SpencerPark/IJava).  Java will require an independent kernel in Jupyter Notebooks.  The instruction performed by the Teacher follows, but look to readme if you have troubles.

```bash
(base) id:~$ wget https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip  # download IJava kernel as zip
(base) id:~$ unzip ijava-1.3.0.zip # unzip downloaded IJava kernel
(base) id:~$ python install.py --user # install IJava kernel
(base) id:~$ jupyter kernelspec list # list kernels
Available kernels:
  java          /home/shay/.local/share/jupyter/kernels/java
  python3       /home/shay/.local/share/jupyter/kernels/python3
```

### Console Game Menu
> College Boards Units #1, #3, and #4 and Free Response Methods and Control Structures are built into these labs.  Of course, these games are very popular in beginning programming.  They are here for reference, as they were shared by a student.


```java
import java.util.Scanner; //library for user input
import java.lang.Math; //library for random numbers

public class ConsoleGame {
    public final String DEFAULT = "\u001B[0m";  // Default Terminal Color
    
    public ConsoleGame() {
        Scanner sc = new Scanner(System.in);  // using Java Scanner Object
        
        boolean quit = false;
        while (!quit) {
            this.menuString();  // print Menu
            try {
                int choice = sc.nextInt();  // using method from Java Scanner Object
                System.out.print("" + choice + ": ");
                quit = this.action(choice);  // take action
            } catch (Exception e) {
                sc.nextLine(); // error: clear buffer
                System.out.println(e + ": Not a number, try again.");
            }
            
        }
        sc.close();
    }

    public void menuString(){
        String menuText = ""
                + "\u001B[35m___________________________\n"  
                + "|~~~~~~~~~~~~~~~~~~~~~~~~~|\n"
                + "|\u001B[0m          Menu!          \u001B[35m|\n"
                + "|~~~~~~~~~~~~~~~~~~~~~~~~~|\n"
                + "| 0 - Exit                |\n"    
                + "| 1 - Rock Paper Scissors |\n"
                + "| 2 - Higher or Lower     |\n"
                + "| 3 - Tic Tac Toe         |\n"
                + "|_________________________|   \u001B[0m\n"
                + "\n"
                + "Choose an option.\n"
                ;
        System.out.println(menuText);
    }

    private boolean action(int selection) {
        boolean quit = false;
        switch (selection) {  // Switch or Switch/Case is Control Flow statement and is used to evaluate the user selection
            case 0:
                System.out.print("Goodbye, World!"); 
                quit = true; 
                break;
            case 1:
                rps();
                break;
            case 2:
                horl();
                break;
            case 3:
                ticTacToe();
                break;
                    
            default:
                //Prints error message from console
                System.out.print("Unexpected choice, try again.");
        }
        System.out.println(DEFAULT);  // make sure to reset color and provide new line
        return quit;
    }

    public void horl(){
        System.out.println("Higher or Lower");
        System.out.println("You have three guesses to guess the number I am thinking of between 1-8.");
        System.out.println("If you guess the number correctly, you win!");
        Scanner scHL = new Scanner(System.in);
        int randomG = (int) (Math.random() * 8) + 1;
        int guess = scHL.nextInt();
        for(int i = 3; i > 0; i--){
            if(guess == randomG){
                System.out.println("You win!");
                break;
            }
            else if(guess > randomG){
                System.out.println("The number is lower");
            }
            else if(guess < randomG){
                System.out.println("The number is higher");
            }
            guess = scHL.nextInt();
        }
        System.out.println("Game over.");
        scHL.close();
    }
                                                     
    public void rps(){
        System.out.println("Rock Paper Scissors");
        System.out.println("Type r for rock, p for paper, or s for scissors");
        Scanner scRPS = new Scanner(System.in);
        String userChoice = scRPS.nextLine().toLowerCase();
        Boolean quit = false;
        int random = (int) (Math.random() * 3);
        while(quit == false){
            if(userChoice.equals("r")){
                if(random == 1){
                    System.out.println("You chose rock \nThe computer chose paper \nYou lose!");
                }
                else if(random == 2){
                    System.out.println("You chose rock \nThe computer chose scissors \nYou win!");
                }
                else{
                    System.out.println("You chose rock \nThe computer chose rock \nIt's a tie!");
                }
                quit = true;
            }
            else if(userChoice.equals("p")){
                if(random == 1){
                    System.out.println("You chose paper \nThe computer chose paper \nIt's a tie!");
                }
                else if(random == 2){
                    System.out.println("You chose paper \nThe computer chose scissors \nYou lose!");
                }
                else{
                    System.out.println("You chose paper \nThe computer chose rock \nYou win!");
                }
                quit = true;

            }
            else if(userChoice.equals("s")){
                if(random == 1){
                    System.out.println("You chose scissors \nThe computer chose paper \nYou win!");
                }
                else if(random == 2){
                    System.out.println("You chose scissors \nThe computer chose scissors \nIt's a tie!");
                }
                else{
                    System.out.println("You chose scissors \nThe computer chose rock \nYou lose!");
                }
                quit = true;

            }
            else{
                System.out.println("Invalid input, try again");
                userChoice = scRPS.nextLine();
            }            
        }
        scRPS.close();
    }
    
    public void ticTacToe(){
        System.out.println("Tic Tac Toe");
        Scanner scTTT = new Scanner(System.in);
        String[] board = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
        String player = "X";
        String player2 = "O";
        int turn = 0;
        Boolean quit = false;
        System.out.println("Do you want to play against a friend or the computer?");
        System.out.println("Type 1 for friend, 2 for computer");
        int choice = scTTT.nextInt();
        //make tic tac toe using player1 and player2
        if(choice == 1){                
            System.out.println("Type the number of the square you want to place your piece in");
            while(quit == false){
                System.out.println("Player 1's turn (X)");
                System.out.println(board[0] + " | " + board[1] + " | " + board[2]);
                System.out.println(board[3] + " | " + board[4] + " | " + board[5]);
                System.out.println(board[6] + " | " + board[7] + " | " + board[8]);
                int move = scTTT.nextInt();
                if(board[move - 1].equals("X") || board[move - 1].equals("O")){
                    System.out.println("That square is already taken, try again");
                }
                else{
                    board[move - 1] = player;
                    turn++;
                    if(board[0].equals("X") && board[1].equals("X") && board[2].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[3].equals("X") && board[4].equals("X") && board[5].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[6].equals("X") && board[7].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[0].equals("X") && board[3].equals("X") && board[6].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[1].equals("X") && board[4].equals("X") && board[7].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[2].equals("X") && board[5].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[0].equals("X") && board[4].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[2].equals("X") && board[4].equals("X") && board[6].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(turn == 9){
                        System.out.println("It's a tie!");
                        quit = true;
                    }
                    else{
                        System.out.println("Player 2's turn (O)");
                        System.out.println(board[0] + " | " + board[1] + " | " + board[2]);
                        System.out.println(board[3] + " | " + board[4] + " | " + board[5]);
                        System.out.println(board[6] + " | " + board[7] + " | " + board[8]);
                        int move2 = scTTT.nextInt();
                        if(board[move2 - 1].equals("X") || board[move2 - 1].equals("O")){
                            System.out.println("That square is already taken, try again");
                        }
                        else{
                            board[move2 - 1] = player2;
                            turn++;
                            if(board[0].equals("O") && board[1].equals("O") && board[2].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                            else if(board[3].equals("O") && board[4].equals("O") && board[5].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                            else if(board[6].equals("O") && board[7].equals("O") && board[8].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                            else if(board[0].equals("O") && board[3].equals("O") && board[6].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                            else if(board[1].equals("O") && board[4].equals("O") && board[7].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                            else if(board[2].equals("O") && board[5].equals("O") && board[8].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                        }
                    }
                }
            }
        }
        if(choice == 2){
            String computer = "O";
            System.out.println("Type the number of the square you want to place your piece in");
            while(quit == false){
                System.out.println("Player 1's turn (X)");
                System.out.println(board[0] + " | " + board[1] + " | " + board[2]);
                System.out.println(board[3] + " | " + board[4] + " | " + board[5]);
                System.out.println(board[6] + " | " + board[7] + " | " + board[8]);
                int move = scTTT.nextInt();
                if(board[move - 1].equals("X") || board[move - 1].equals("O")){
                    System.out.println("That square is already taken, try again");
                }
                else{
                    board[move - 1] = player;
                    turn++;
                    if(board[0].equals("X") && board[1].equals("X") && board[2].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[3].equals("X") && board[4].equals("X") && board[5].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[6].equals("X") && board[7].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[0].equals("X") && board[3].equals("X") && board[6].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[1].equals("X") && board[4].equals("X") && board[7].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[2].equals("X") && board[5].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[0].equals("X") && board[4].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[2].equals("X") && board[4].equals("X") && board[6].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(turn == 9){
                        System.out.println("It's a tie!");
                        quit = true;
                    }
                    else{
                        System.out.println("Computer's turn (O)");
                        System.out.println(board[0] + " | " + board[1] + " | " + board[2]);
                        System.out.println(board[3] + " | " + board[4] + " | " + board[5]);
                        System.out.println(board[6] + " | " + board[7] + " | " + board[8]);
                        int move2 = (int)(Math.random() * 9) + 1;
                        if(board[move2 - 1].equals("X") || board[move2 - 1].equals("O")){
                            System.out.println("That square is already taken, try again");
                        }
                        else{
                            board[move2 - 1] = computer;
                            turn++;
                            if(board[0].equals("O") && board[1].equals("O") && board[2].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                            else if(board[3].equals("O") && board[4].equals("O") && board[5].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                            else if(board[6].equals("O") && board[7].equals("O") && board[8].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                            else if(board[0].equals("O") && board[3].equals("O") && board[6].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                            else if(board[1].equals("O") && board[4].equals("O") && board[7].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                            else if(board[2].equals("O") && board[5].equals("O") && board[8].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                        }
                    }
                }
            }
          
    }
        scTTT.close();
    }

    static public void main(String[] args)  {  
        new ConsoleGame(); // starting Menu object
    }


}
ConsoleGame.main(null);


```

    [35m___________________________
    |~~~~~~~~~~~~~~~~~~~~~~~~~|
    |[0m          Menu!          [35m|
    |~~~~~~~~~~~~~~~~~~~~~~~~~|
    | 0 - Exit                |
    | 1 - Rock Paper Scissors |
    | 2 - Higher or Lower     |
    | 3 - Tic Tac Toe         |
    |_________________________|   [0m
    
    Choose an option.
    
    0: Goodbye, World![0m


## Hacks
> To start the year, I want you to consider a simple Java console game or improve on the organization and presentation of the games listed.
- Make RPS, Tic-Tack-Toe, and Higher Lower into different cells and objects.  Document each cell in Jupyter Notebooks.  
- Simplify logic, particularly T-T-T.  What could you do to make this more simple? Java has HashMap (like Python Dictionary), Arrays (fixed size), ArraLists (Dynamic Size). 
- Run the menu using recursion versus while loop.  Try to color differently.
- Look over 10 units for College Board AP Computer Science A.  In your reorganized code blocks and comments identify the Units of Code Used. 
- Answer why you think this reorganization and AP indetification is important?   



```java
import java.util.Random;

public class Dice {
    public static int main(String[] args) {
        Random random = new Random();
        int diceValue = random.nextInt(6) + 1; // Generates a random number between 1 and 6
        return diceValue;
    }
}
public class Game {
    public static void main(String[] args) {
        System.out.println("|----------------------------|");
        System.out.println("| Welcome to Ethan's Games!  |");
        System.out.println("|----------------------------|");
        System.out.println("| 1. Higher Lower            |");
        System.out.println("| 2. Dice Betting            |");
        System.out.println("| 3. Fighters                |");
        System.out.println("|----------------------------|");
        
        Scanner myObj = new Scanner(System.in);
        String input = myObj.nextLine();
        int game = Integer.parseInt(input);

        if (game == 1) {
            Game.HiLo(null);
        }
        else if (game == 2) {
            Game.DiceBetting(null);
        }
        else if (game == 3) {
            Game.Fight(null);
        }
        else {
            System.out.println("Invalid input, please try again");
            Game.main(null);
        }
    }
    public static void Fight(String[] args) {
        int p1hp = 100;
        int p2hp = 75;
        int p1def = 0;
        int p2def = 0;
        int p1atk = 1;
        int p2atk = 1;
        while (true) {
            System.out.println("|----------------------------|");
            System.out.println("| P1 pick your move:         |");
            System.out.println("| hp: " + p1hp + "                    |");
            System.out.println("| defense: " + p1def + "                |");
            System.out.println("| attack: " + p1atk + "                 |");
            System.out.println("|----------------------------|");
            System.out.println("| 1. UPGRADE defense         |");
            System.out.println("| 2. UPGRADE attack          |");
            System.out.println("| 3. HEAL                    |");
            System.out.println("| 4. ATTACK                  |");
            System.out.println("|----------------------------|");
            Scanner myObj1 = new Scanner(System.in);
            String input1 = myObj1.nextLine();
            int move1 = Integer.parseInt(input1);
            if (move1 == 1) {
                if (p1def == 15) {
                    System.out.println("[ARENA] - You can't upgrade your defense anymore! Move wasted.");
                } else {
                    p1def += Dice.main(null);
                    if (p1def >= 15) {
                        p1def = 15;
                        System.out.println("[ARENA] - Defense maxed!");
                    }
                }
            } else if (move1 == 2) {
                if (p1atk == 5) {
                    System.out.println("[ARENA] - You can't upgrade your attack anymore! Move wasted.");
                } else {
                    p1atk += 1;
                    if (p1atk == 5) {
                        System.out.println("[ARENA] - Attack maxed!");
                    }
                }
            } else if (move1 == 3) {
                if (p1hp == 100) {
                    System.out.println("[ARENA] - You are already at full health! Move wasted.");
                } else {
                    p1hp += Dice.main(null);
                    if (p1hp >= 100) {
                        System.out.println("[ARENA] - Health maxed!");
                    }
                }
            } else if (move1 == 4) {
                int dmg1=(Dice.main(null)*p1atk)-p2def;
                p2hp -= dmg1;
                System.out.println("[ARENA] - " + dmg1 + " damage delt!");
                if (p2hp <= 0) {
                    System.out.println("[ARENA] - p1 wins!!");
                    return;
                }
            }


            System.out.println("|----------------------------|");
            System.out.println("| P2 pick your move:         |");
            System.out.println("| hp: " + p2hp + "                    |");
            System.out.println("| defense: " + p2def + "                |");
            System.out.println("| attack: " + p2atk + "                 |");
            System.out.println("|----------------------------|");
            System.out.println("| 1. UPGRADE defense         |");
            System.out.println("| 2. UPGRADE attack          |");
            System.out.println("| 3. HEAL                    |");
            System.out.println("| 4. ATTACK                  |");
            System.out.println("|----------------------------|");
            Scanner myObj2 = new Scanner(System.in);
            String input2 = myObj2.nextLine();
            int move2 = Integer.parseInt(input2);
            if (move2 == 1) {
                if (p2def == 15) {
                    System.out.println("[ARENA] - You can't upgrade your defense anymore! Move wasted.");
                } else {
                    p2def += Dice.main(null);
                    if (p2def >= 15) {
                        p2def = 15;
                        System.out.println("[ARENA] - Defense maxed!");
                    }
                }
            } else if (move2 == 2) {
                if (p2atk == 5) {
                    System.out.println("[ARENA] - You can't upgrade your attack anymore! Move wasted.");
                } else {
                    p2atk += 1;
                    if (p2atk == 5) {
                        System.out.println("[ARENA] - Attack maxed!");
                    }
                }
            } else if (move2 == 3) {
                if (p2hp == 100) {
                    System.out.println("[ARENA] - You are already at full health! Move wasted.");
                } else {
                    p2hp += Dice.main(null);
                    if (p2hp >= 100) {
                        System.out.println("[ARENA] - Health maxed!");
                    }
                }
            } else if (move2 == 4) {
                int dmg2=(Dice.main(null)*p2atk)-p1def;
                p1hp -= dmg2;
                System.out.println("[ARENA] - " + dmg2 + " damage delt!");
                if (p1hp <= 0) {
                    System.out.println("[ARENA] - p2 wins!!");
                    return;
                }
            }
        }
    }
    public static void DiceBetting(String[] args) {
        System.out.println("|----------------------------|");
        System.out.println("| Enter your bet:            |");
        System.out.println("|----------------------------|");
        Scanner myObj = new Scanner(System.in);
        String input = myObj.nextLine();
        double bet = Integer.parseInt(input);
        double earnings = 0;
        int wins = 0;
        for (int i=0; i<3; i++) {
            int playerd1 = Dice.main(null);
            int dealerd1 = Dice.main(null);
            if (playerd1 > dealerd1) {
                wins += 1;
            }
            else if (playerd1 < dealerd1) {
                wins -= 1;
            }
            if (wins == -3) {
                earnings = (bet*-3);
            }
            else if (wins == -2) {
                earnings = (bet*-2);
            }
            else if (wins == -1) {
                earnings = -bet;
            }
            else if (wins == 0) {
                earnings = 0;
            }
            else if (wins == 1) {
                earnings = (bet/10);
            }
            else if (wins == 2) {
                earnings = (bet/4);
            }
            else if (wins == 3) {
                earnings = bet;
            }
            if (i != 2) {
                System.out.println("|----------------------------|");
                System.out.println("| your dice: " + playerd1 + "               |");
                System.out.println("| dealer dice: " + dealerd1 + "             |");
                System.out.println("| net earnings: " + earnings + "          |");
                System.out.println("|----------------------------|");
                System.out.println("| Roll again? (" + (i+1) + "/3)          |");
                System.out.println("| 1. Yes                     |");
                System.out.println("| 2. No                      |");
                System.out.println("|----------------------------|");
            } else if (i==2) {
                System.out.println("|----------------------------|");
                System.out.println("| your dice: " + playerd1 + "               |");
                System.out.println("| dealer dice: " + dealerd1 + "             |");
                System.out.println("| net earnings: " + earnings + "          |");
                System.out.println("|----------------------------|");
                return;
            }
            Scanner myObj2 = new Scanner(System.in);
            String input2 = myObj2.nextLine();
            int cont = Integer.parseInt(input2);
            if (cont == 0) {
                return;
            }
        }
    }
    public static void HiLo(String[] args) {
        int d1 = Dice.main(null);
        System.out.println("|----------------------------|");
        System.out.println("| First dice: " + d1 + "              |");
        System.out.println("|----------------------------|");
        System.out.println("| Higher or lower than " + (d1+3) + "?    |");
        System.out.println("| 1. Higher                  |");
        System.out.println("| 2. Lower                   |");
        System.out.println("| 3. Equal                   |");
        System.out.println("|----------------------------|");
        Scanner myObj = new Scanner(System.in);
        String input = myObj.nextLine();
        int hl = Integer.parseInt(input);
        int d2 = Dice.main(null);
        int total = d1+d2;
        if (total == d1+3 && hl == 3) {
            System.out.println("|----------------------------|");
            System.out.println("| Second dice: " + d2 + "             |");
            System.out.println("| Total: " + (d2+d1) + "                   |");
            System.out.println("|----------------------------|");
            System.out.println("| You win!                   |");
            System.out.println("|----------------------------|");
        } else if (total > d1+3 && hl == 1) {
            System.out.println("|----------------------------|");
            System.out.println("| Second dice: " + d2 + "             |");
            System.out.println("| Total: " + (d2+d1) + "                   |");
            System.out.println("|----------------------------|");
            System.out.println("| You win!                   |");
            System.out.println("|----------------------------|");
        } else if (total < d1+3 && hl == 2) {
            System.out.println("|----------------------------|");
            System.out.println("| Second dice: " + d2 + "             |");
            System.out.println("| Total: " + (d2+d1) + "                   |");
            System.out.println("|----------------------------|");
            System.out.println("| You win!                   |");
            System.out.println("|----------------------------|");

        } else {
            System.out.println("|----------------------------|");
            System.out.println("| Second dice: " + d2 + "             |");
            System.out.println("| Total: " + (d2+d1) + "                   |");
            System.out.println("|----------------------------|");
            System.out.println("| You lose!                  |");
            System.out.println("|----------------------------|");
        }
    }
}
Game.main(null);

```

    |----------------------------|
    | Welcome to Ethan's Games!  |
    |----------------------------|
    | 1. Higher Lower            |
    | 2. Dice Betting            |
    | 3. Fighters                |
    |----------------------------|
    |----------------------------|
    | Enter your bet:            |
    |----------------------------|
    |----------------------------|
    | your dice: 6               |
    | dealer dice: 1             |
    | net earnings: 10.0          |
    |----------------------------|
    | Roll again? (1/3)          |
    | 1. Yes                     |
    | 2. No                      |
    |----------------------------|
    |----------------------------|
    | your dice: 2               |
    | dealer dice: 3             |
    | net earnings: 0.0          |
    |----------------------------|
    | Roll again? (2/3)          |
    | 1. Yes                     |
    | 2. No                      |
    |----------------------------|
    |----------------------------|
    | your dice: 3               |
    | dealer dice: 1             |
    | net earnings: 10.0          |
    |----------------------------|


**An example of a very long game...**
```
|----------------------------|
| Welcome to Ethan's Games!  |
|----------------------------|
| 1. Higher Lower            |
| 2. Dice Betting            |
| 3. Fighters                |
|----------------------------|
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 0                |
| attack: 1                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P2 pick your move:         |
| hp: 75                    |
| defense: 0                |
| attack: 1                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 6                |
| attack: 1                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P2 pick your move:         |
| hp: 75                    |
| defense: 6                |
| attack: 1                 |
...
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 10                |
| attack: 1                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P2 pick your move:         |
| hp: 75                    |
| defense: 10                |
| attack: 1                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 12                |
| attack: 1                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - Defense maxed!
|----------------------------|
| P2 pick your move:         |
| hp: 75                    |
| defense: 12                |
| attack: 1                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - Defense maxed!
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 15                |
| attack: 1                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P2 pick your move:         |
| hp: 75                    |
| defense: 15                |
| attack: 1                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 15                |
| attack: 2                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P2 pick your move:         |
| hp: 75                    |
| defense: 15                |
| attack: 2                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 15                |
| attack: 3                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P2 pick your move:         |
| hp: 75                    |
| defense: 15                |
| attack: 3                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 15                |
| attack: 4                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - Attack maxed!
|----------------------------|
| P2 pick your move:         |
| hp: 75                    |
| defense: 15                |
| attack: 4                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - Attack maxed!
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -10 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 85                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 95                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 90                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 95                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 85                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 75                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 95                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 15 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 85                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 95                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P1 pick your move:         |
| hp: 95                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 70                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 75                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 100                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 75                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 95                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 65                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 90                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 65                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 80                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 55                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 85                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 90                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 15 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 75                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 15 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 55                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 55                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 65                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 15 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 40                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 75                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 45                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 15 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 50                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 50                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 50                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 55                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 50                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 65                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 45                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 55                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 40                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 60                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 30                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 15 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 45                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 20                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 35                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 10                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P1 pick your move:         |
| hp: 35                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 14                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P1 pick your move:         |
| hp: 35                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 22                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P1 pick your move:         |
| hp: 35                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 27                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
|----------------------------|
| P1 pick your move:         |
| hp: 35                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 32                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 30                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 27                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 35                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 32                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 45                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 27                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 45                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -10 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 37                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 35                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 32                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 25                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 37                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 15 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 10                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 42                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 10                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 42                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 15                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 37                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 20                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 32                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 30                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 0 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 32                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 15 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 15                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 27                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 5                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -10 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 37                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 10                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 15 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 22                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -10 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 20                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -5 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 27                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 15 damage delt!
|----------------------------|
| P1 pick your move:         |
| hp: 5                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - -10 damage delt!
|----------------------------|
| P2 pick your move:         |
| hp: 37                    |
| defense: 15                |
| attack: 5                 |
|----------------------------|
| 1. UPGRADE defense         |
| 2. UPGRADE attack          |
| 3. HEAL                    |
| 4. ATTACK                  |
|----------------------------|
[ARENA] - 5 damage delt!
[ARENA] - p2 wins!!
```
