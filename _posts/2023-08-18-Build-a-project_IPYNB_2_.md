---
title: Build A Project
author: Ethan
date: 2023-08-18 11:33:00 +0800
week: 0
categories: ['Week0']
tags: ['week0']
pin: False
mermaid: False
---

# Calculator

Click the buttons to enter their respective functions. An eval is ran on the string in the calculator screen when the equals button is pressed. This gives us the output of the mathematical operation requested.


<html>
    <head>
        <meta charset="utf-8">
        <title>Calculator</title>
        <meta name="description" content="">
        <style>
            .circle {
                position: absolute;
                height: 50px;
                width: 50px;
                border-radius: 50%;
                text-align: center;
                vertical-align: middle;
            }
            .longCircle {
                position: absolute;
                height: 50px;
                width: 125px;
                border-radius: 25px;
                text-align: center;
                vertical-align: middle;
            }
        </style>
    </head>
    <body style="background-color: #000101; color: #F8F8F8; margin-bottom: 1000%">
        <script>
            reset=false;
            result="";
            function calc(val) {
                if (val == "AC") {
                    document.getElementById("calcScreen").innerHTML = 0;
                }else if (val == "=") {
                    evaluate=eval(document.getElementById("calcScreen").innerHTML);
                    document.getElementById("calcScreen").innerHTML=(evaluate);
                } else {
                    if (document.getElementById("calcScreen").innerHTML == 0) {
                        document.getElementById("calcScreen").innerHTML = "";
                        document.getElementById("calcScreen").innerHTML += val;
                    } else if (reset) {
                        console.log("reset")
                        document.getElementById("calcScreen").innerHTML = "";
                        document.getElementById("calcScreen").innerHTML += val;
                    } else {
                        if (document.getElementById("calcScreen").innerHTML == result) {
                            document.getElementById("calcScreen").innerHTML = "";
                        }
                        document.getElementById("calcScreen").innerHTML += val;
                    }
                }
            }
        </script>

        <div style="position: absolute; top: 300px; left: 135px; width: 225px; font-size: 32px;"><p id="calcScreen" ALIGN=RIGHT>0</p></div>

        <div class="circle" style="background-color: #9E9F9E; top: 400px; left: 100px; color: #000101;" onClick="calc('AC')">AC</div>
        <div class="circle" style="background-color: #9E9F9E; top: 400px; left: 175px; color: #000101;" onClick="calc('sign')">+/-</div>
        <div class="circle" style="background-color: #9E9F9E; top: 400px; left: 250px; color: #000101;">%</div>
        <div id = "/" class="circle" style="background-color: #EA9B3E; top: 400px; left: 325px;" onClick="calc('/')">÷</div>

        <div class="circle" style="background-color: #313030; top: 475px; left: 100px;" onClick="calc('7')">7</div>
        <div class="circle" style="background-color: #313030; top: 475px; left: 175px;" onClick="calc('8')">8</div>
        <div class="circle" style="background-color: #313030; top: 475px; left: 250px;" onClick="calc('9')">9</div>
        <div id = "x" class="circle" style="background-color: #EA9B3E; top: 475px; left: 325px;" onClick="calc('*')">x</div>

        <div class="circle" style="background-color: #313030; top: 550px; left: 100px;" onClick="calc('4')">4</div>
        <div class="circle" style="background-color: #313030; top: 550px; left: 175px;" onClick="calc('5')">5</div>
        <div class="circle" style="background-color: #313030; top: 550px; left: 250px;" onClick="calc('6')">6</div>
        <div id = "-" class="circle" style="background-color: #EA9B3E; top: 550px; left: 325px;" onClick="calc('-')">-</div>

        <div class="circle" style="background-color: #313030; top: 625px; left: 100px;" onClick="calc('1')">1</div>
        <div class="circle" style="background-color: #313030; top: 625px; left: 175px;" onClick="calc('2')">2</div>
        <div class="circle" style="background-color: #313030; top: 625px; left: 250px;" onClick="calc('3')">3</div>
        <div id = "+" class="circle" style="background-color: #EA9B3E; top: 625px; left: 325px;" onClick="calc('+')">+</div>

        <div class="longCircle" style="background-color: #313030; top: 700px; left: 100px;" onClick="calc('0')">0</div>
        <div class="circle" style="background-color: #313030; top: 700px; left: 250px;">.</div>
        <div class="circle" style="background-color: #EA9B3E; top: 700px; left: 325px;" onClick="calc('=')">=</div>
    </body>
</html>
