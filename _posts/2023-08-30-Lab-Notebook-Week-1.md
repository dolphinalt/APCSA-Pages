---
title: Lab Notebook Week 1
author: Ethan
date: 2023-08-30 11:33:00 +0800
week: 1
categories: ['Week1']
tags: ['week1']
pin: True
mermaid: False
---

# Time to get serious
After this first week in APCSA, things have really started to get interesting. We have to learn Java, a programming language that I've never used before. It will be a great learning experience and I'm excited to see what I can do with it! From what I've seen though, it seems like a pretty easy language to learn, as it is very similar to C++.

## Java Hello
This took a bit of time for me to understand how to do, especially because I was learning the Java syntax as I went along. In the end though, I was able to create a dynamic object called `DynamicEmployees` to store a possible employee set of the following: Name, company ID, and company email. I also created a static class called `Stats` to run some common stats functions on a list of numbers.

## Java Console Games
This one took A LOT of time to create, test, and debug. I created a static class `Games` to store all of my games, and created a static class `Dice` to roll a dice, as a dice is used in every one of my games.

### Higher or Lower
The first game I had was a simple higher or lower game. This game is played by showing the player the value of the first dice. They are now asked to estimate if the next dice will be higher, lower, or equal to the first dice plus 3. I picked this value in order to provide a 50/50 for higher or lower and a 1/6 chance of it being equal, which will give a higher reward.

### Dice betting
The 2nd game I made was a dice betting game. You get 3 games where you roll a dice and compare which is higher, yours or the dealer's. You can bet on each game, and the winnings for wins or losses are as follows:

| Net W/L | Winnings |
|---------|----------|
| -3 | -300% |
| -2 | -200% |
| -1 | -100% |
| 0 | 0% |
| 1 | 10% |
| 2 | 20% |
| 3 | 100% |

### Fight Game
The 3rd game I made was a fight game. Player 1 has 100 health, while Player 2 has 75 health. Player 2 receives less health because they move second. Each turn, the player can choose to upgrade defense, upgrade attack, heal, or attack. The below table breaks all the moves down.

| Move | Explanation |
|---------|----------|
| UPGRADE defense | Rolls a dice, adds it to defense stat. Maxes at 15. Reduces incoming attack by defense amount. NEGATIVE DAMAGE IS INTENTIONAL |
| UPGRADE attack | Adds 1 to attack each time used. Maxes at 5. Multiplies each attack roll by attack stat |
| HEAL | Rolls a dice, adds that amount back to total health |
| ATTACK | Rolls a dice and multiplies the value by attack. |