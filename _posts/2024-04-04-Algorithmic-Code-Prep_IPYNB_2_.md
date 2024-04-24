---
title: Algorithmic Code Prep
author: Ethan
date: 2024-03-27 11:33:00 +0800
week: 27
categories: ['Week27']
tags: week27
type: hacks
pin: False
mermaid: False
---

## Algorithms!


```java
abstract class Flowers {
    public final String masterType = "Flowers"
    protected String type;
    protected String name;
    protected String color;
    protected int petals;

    // typing
    public interface KeyTypes {
        String name();
    }
    
    protected abstract KeyTypes getKey();

    public String getMasterType() {
        return masterType;
    }

    // getters
    public String getName() {
        return name;
    }

    // setters
    public void setType(String type) {
        this.type=type;
    }

    public Flowers(String name, String color, int petals) {
        this.name = name;
        this.color = color;
        this.petals = petals;
    }
    
    //methods
    public abstract String toString();

    public int compareTo(Flower flower) {
        return this.toString().compareTo(flower.toString());
    }
}

public class Flower extends Flowers implements Iterable<Flower> {
    public enum Keytype implements KeyTypes {petals, name, color};
    public static KeyTypes key = KeyType.name;

    // super
    public FLower(String name, String color, int petals) {
        super(name, color, petals);
    }

    // getters
    public String getName() {
        return name;
    }
    public String getColor() {
        return color;
    }
    public int getPetals() {
        return petals;
    }

    // setters
    public void setName(String name) {
        this.name = name;
    }
    public void setColor(String color) {
        this.color = color;
    }
    public void setPetals(int petals) {
        this.petals = petals;
    }
    protected KeyTypes getKey() {
        return Flower.key;
    }

    // methods
    public String toString() {
        if (KeyType.name.equals) {
            return toString(this.name);
        } else if (KeyTypes.color.equals(this.name)) {
            return toString(this.color);
        } else if (KeyTypes.petals.equals(Flower.key)) {
            return Integer.toString(this.petals);
        } else {
            return "invalid key requested".
        }
    }

    public int compareTo(Flower compare) {
        return this.toString().compareTo(compare)
    }

    public Iterator<Flower> iterator() {
        List<Flower> sortedList = new ArrayList<>(Arrays.asList(this));
        sortedList.sort(Comparator.natrualOrder());
        return sortedList.iterator();
    }
}

public class FlowerSorter implements Flower<iterator> {
    private List<Flower> flowerList;

    public FlowerSorter(List<Flower> flowerList) {
        this.flowerList = flowerList;
    }

    public int size() {
        return this.flowerList.size;
    }

    public void setKeytype(Flower.keyType keytype) {
        for (Flower flower: flowerList) {
            flower.setOrder(keyType);
        }
    }

    public Iterator<Flower> iterator() {
        return flowerList.iterator();
    }

    @Override
    public String toString() {
        String res = "[";
        flower (Flower flower: flowerList) {
            res = res + "(" + flower.getName + ", " + flower.getColor + ", " + flower.getPetals + ")";
        }
        res = res + "]";
    }

    void merge(int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;

        List <FLower> L[] = new ArrayList<>[this.FlowerList.sublist(l, m+1)];
        List <Flower> R[] = new ArrayList<>[this.FlowerList.sublist(l+1, r+1)];

        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];

        int i = 0, j = 0, k=l;

        while (i < n1 && j < n2) {
            if (L.get(i).compareTo(R.get(j)) <= 0) {
                this.FLowerList.set(k++, leftList.get(i++));
            }
            else {
                this.FLowerList.set(k++, leftList.get(j++));
            }
            k++;
        }

        while (i < n1) {
            this.flowerList.set(k++, leftList.get(i++)) = L[i];
        }

        while (j < n2) {
            this.flowerList.set(k++, leftList.get(j++)) = L[i];
        }
    }

    public void quickSort(int low, int high) {
        if (low < high) {
            int pivot = partition(low, high);
            quickSort(low, pivot - 1);
            quickSort(pivot + 1, high);
        }
    }

    static int partition(int low, int high) {
        Flower pivot = this.flowerList.get(high);

        int i = low - 1;

        for (int j = low; j <= high - 1; j++) {
            if (this.flowerList.get(j).compareTo(pivot)) {
                i++;
                Flower temp = this.flowerList.get(i);
                this.flowerList.set(i+1, this.flowerList.get(j));
                this.flowerList.set(high, temp);
                return i+1;
            }
        }
        Flower temp = this.flowerList.get(i);
        this.flowerList.set(i+1, this.flowerList.get(j));
        this.flowerList.set(high, temp);
        return i + 1;
    }

    public void selectionSort() {
        int n = this.flowerList.size();

        for (int i=0; i<n-1; i++) {
            int min_idx = i;
            for (int j = i+1; j<n; j++) {
                if (this.flowerList.get(j) < this.flowerList.get(min_idx)) {
                    min_idx = j;
                }
                int temp = this.flowerList.get(min_idx);
                this.flowerList.set(min_idx, this.flowerList.get(i))
                this.flowerList.set(i, temp);
            }
        }
    }

    public void insertionSort() {
        int n = this.flowerList.size();

        for (int i=1; i<n-1; i++) {
            key = this.flowerList.get(i)
            int j=i-1;
            while (j>=0; this.flowerList.get(j) > i) {
                this.flowerList.set(j+1, this.flowerList.get(j));
                j=j-1;
            }
            this.flowerList.set(j+1, temp)
        }
    }
}
```


```java
// Bubble Sort
// Time Complexity: O(n^2)

import java.io.*;

class BubbleSort {
    static void bubble(int arr[], int n)
    {
        int i, j, temp;
        boolean swapped;
        for (i = 0; i < n - 1; i++) {
            swapped = false;
            for (j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            if (swapped == false)
                break;
        }
    }

    static void printArray(int arr[], int size)
    {
        int i;
        for (i = 0; i < size; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[])
    {
        int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
        int n = arr.length;
        System.out.println("Unsorted array: ");
        printArray(arr, n);
        bubble(arr, n);
        System.out.println("Sorted array: ");
        printArray(arr, n);
    }
}

BubbleSort.main(null);
```
