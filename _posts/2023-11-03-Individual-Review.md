---
title: Individual Review
author: dolphinalt
date: 2023-11-03 11:33:00 +0800
week: 11
categories: [Week11]
tags: week11
type: plans
pin: false
mermaid: false
---

# Individual Review Blog

## Student lessons:

I worked on U6 - Arrays. Detailed review on lessons [here](https://github.com/dolphinalt/APCSA-Pages/issues/3)

| Lesson | Score | Spreadsheet |
| --- | --- | --- |
| U1 | 0.9/1.0 | [Link](https://docs.google.com/spreadsheets/d/1sfd2V18fgzKQJREfusTLqHkfqY54qJfiTN_cHmvfj-k/edit#gid=781778514) |
| U2 | 0.8/1.0 | [Link](https://docs.google.com/spreadsheets/d/1q-zyhdHc9oFvWG7RMvuQVVKMQ8BjdNOyaAEbmjY4xEs/edit#gid=1846745372) |
| U3 | 0.95/1.0 | [Link](https://docs.google.com/spreadsheets/u/2/d/1sfd2V18fgzKQJREfusTLqHkfqY54qJfiTN_cHmvfj-k/edit#gid=781778514) |
| U4 | 1.0/1.0 | [Link](https://docs.google.com/spreadsheets/d/1reH2rO8kZSXO-6_C0YnWGrSvvaeDE18OmsW1VkLYVeI/edit#gid=0) |
| U5 | 0.85 | [Link](https://docs.google.com/spreadsheets/d/1reH2rO8kZSXO-6_C0YnWGrSvvaeDE18OmsW1VkLYVeI/edit#gid=248984290) |
| U6 | N/A | We were teaching this lesson |
| U7 | N/A | We were teaching this lesson |
| U8 | ? | Link |
| **Total** | 4.5/5 | N/A |

## Studying for Exam

I plan to study for the APCSA Exam by doing the following:

1. Reviewing the lessons - Watching back every one of the college board lessons so I know exactly what College Board wants me to know.

2. Doing more Java coding - Working on more of the backend and my own personal projects to familiarize myself for the structure of java and prepare myself for the FRQ section of the exam.

3. Reviewing the practice - Taking and revising my mistakes for tests provided to me on the college board website.

## Iterative progress

Scrum board to manage everything we needed to do. Consistent commits over the past 3 weeks.

## Individual Code

Backend - I helped with debugging of backend, not initial set up. Debugged: JWTs, Request headders, database image storing (I came up with the idea of storing images as strings)

Frontend - Majority of my work. Created functions for resizing page based off of screen size (kind of my own framework), created login system, created leaderboard. Leaderboard was sorted using merge sort, but adapted to be sorting a json database instead of an array. This was hard to do for me, but the solution was much smipler than I thought.

```js
function mergeSort(arr, prop) {
    // Base case
    if (arr.length <= 1) return arr;
    let mid = Math.floor(arr.length / 2);
    // Recursive calls
    let left = mergeSort(arr.slice(0, mid), prop);
    let right = mergeSort(arr.slice(mid), prop);
    return merge(left, right, prop);
}

function merge(left, right, prop) {
    let result = [];
    let leftIndex = 0;
    let rightIndex = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex][prop] > right[rightIndex][prop]) { // Reverse the comparison for greatest to least
            result.push(left[leftIndex]);
            leftIndex++;
        } else {
            result.push(right[rightIndex]);
            rightIndex++;
        }
    }

    return result.concat(left.slice(leftIndex), right.slice(rightIndex));
}
```

Dev-Ops: Devops issues were almost exclusively handled by me. This was debugging the nginx server, fixing domain issues, cors related issues, and more.

Adjunct activity: Created frontend code for login, created backend code for JWT alternatitves but were never used because we ended up not using JWTs/user authentication at all. Also created frontend design for all pages, but only leaderboard was used

## Individual Blog

See rest of blog site for coding and usage of blogs.

College Board Quiz notes: 22/40

I expected to do not great on the first college board quiz, BUT did not expect to do this bad. I have found that this was due to me not being very familiar with the Java questions. I need to work more with Java and experiment with creating my own projects. I also need to review the college board lessons more, and review the lessons created by each of the teams. With that being said, here is the link to the questions I got wrong and explanations for them all: [Link](https://github.com/dolphinalt/APCSA-Pages/issues/4)

Trimester 1 reflection: 