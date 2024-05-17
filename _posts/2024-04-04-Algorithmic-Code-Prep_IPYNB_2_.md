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

For this event, our large group across periods 1 and 2 organized a performance along with some student volunteers from AP CSP to demonstrate how our sorting algorithms function. Notably, we recorded down the performances for at least 3 out of 5 of our practices and have also uploaded them to instagram, where we have garnered widespread internet attention.

![Instagram](https://raw.githubusercontent.com/YLu-1258/YLU_blog/0e4c1d7f7bd3d54916d26925109b4392255f4df8/assets/img/flower_mergers.png)

For the practices, I found it very hard to coordinate a time where everyone was able to show up on time for practice. We had around 17 people in our group, so most practices consisted of only a majority of people to practice our roles. Nonetheless, the entire project was about understanding how a sort worked, so as we reviewed the concept of mergesort, we found the overall algorithm to be very easy to understand, and subsequently, our performance also became easier to manage.

In addition to scheduling, we also did a partition of work for who should work on the project. Most of us were flowers and we assigned me to be the conductor as he had the loudest voice. Additionally, I helped to design what the flowers for our event should look like, and the idea was subsequently passed onto our other performers to create flowers for the whole team. I also partook in the initial ideation of the project, coming up with the idea of sorting the flowers by the number of petals.

Overall, I found the event very fun as I was able to see what other creative methods other groups found to show off their algorithms. Notably, I really liked that one group who demonstrated both quicksort and bogo sort. Although they received criticism for being slightly confusing to the audience, I thought that their premise and idea was very unique and funny to show off an otherwise confusing algorithm to implement.

## Algorithms!


```Java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public abstract class FlowerCollectable implements Comparable<FlowerCollectable> {
    public final String masterType = "FlowerCollectable";
	private String type;
    protected int numberPetals;
    protected String name;
    protected String color;

    // Are we selling or buying the Flower?
    // @NotEmpty
    // private String operation;

    public interface KeyTypes {
		String name();
	}
	protected abstract KeyTypes getKey();

    public String getMasterType() {
		return masterType;
	}

	// getter
	public String getType() {
		return type;
	}

	// setter
	public void setType(String type) {
		this.type = type;
    }

    // this method is used to establish key order
	public abstract String toString();

	// this method is used to compare toString of objects
	public int compareTo(FlowerCollectable obj) {
		return this.toString().compareTo(obj.toString());
	}

    // Essentially, we record who buys the Flower (id), what Flower they bought (name), cost of the share (cost), amount of the shares (shares), time of the transaction (time), and whether it was bought or sold (operation)
    public FlowerCollectable(String name, String color, Integer numberPetals) {
        this.name = name;
        this.color = color;
        this.numberPetals = numberPetals;
    }
}

public class Flower extends FlowerCollectable implements Iterable<Flower> {
    public enum KeyType implements KeyTypes {petals, name, color}
    public static KeyTypes key = KeyType.name;
	public void setOrder(KeyTypes key) {Flower.key = key;}

    public Flower(int p, String n, String c) {
        super(n,c,p);
    }

    // Getters
    public int getNumberPetals() {
        return numberPetals;
    }

    public String getName() {
        return name;
    }

    public String getColor() {
        return color;
    }

    // Setters
    public void setNumberPetals(int numberPetals) {
        this.numberPetals = numberPetals;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String toString() {
        if (KeyType.petals.equals(Flower.key)) {
            return "(" + Integer.toString(this.numberPetals) + ")";
        } else if (KeyType.name.equals(Flower.key)) {
            return "(" + this.name + ")";
        } else if (KeyType.color.equals(Flower.key)) {
            return "(" + this.color + ")";
        } else {
            return "Invalid Key";
        }
    }

    public int compareTo(Flower otherFlower) {
        return this.toString().compareTo(otherFlower.toString());
    }

	protected KeyTypes getKey() { return Flower.key; }

    public Iterator<Flower> iterator() {
        List<Flower> sortedList = new ArrayList<>(Arrays.asList(this));
        sortedList.sort(Comparator.naturalOrder());
        return sortedList.iterator();
    }
}

public class FlowerIterator implements Iterable<Flower> {
    private List<Flower> FlowerList;

    public FlowerIterator(List<Flower> FlowerList) {
        this.FlowerList = FlowerList;
    }

    public Integer size() {
        return this.FlowerList.size();
    }

    public void setKeyType(Flower.KeyType keyType) {
        // Update keyType for all Flowers in the iterator
        for (Flower Flower : FlowerList) {
            Flower.setOrder(keyType);
        }
    }

    public Iterator<Flower> iterator() {
        return FlowerList.iterator();
    }

    @Override
    public String toString() {
        String res = "[";
        for (Flower flower : FlowerList) {
            res = res + "(" + flower.getName() + ", " + flower.getColor() + ", petals: " + flower.getNumberPetals() + "), ";
        }
        return res.substring(0,res.length()-2) + "]";
    }

    public void mergeSort(int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSort(left, mid);
            mergeSort(mid + 1, right);
            merge(left, mid, right);
        }
    }

    private void merge(int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        List<Flower> leftList = new ArrayList<>(this.FlowerList.subList(left, mid + 1));
        List<Flower> rightList = new ArrayList<>(this.FlowerList.subList(mid + 1, right + 1));

        int i = 0, j = 0, k = left;

        while (i < n1 && j < n2) {
            if (leftList.get(i).compareTo(rightList.get(j)) <= 0) {
                this.FlowerList.set(k++, leftList.get(i++));
            } else {
                this.FlowerList.set(k++, rightList.get(j++));
            }
        }

        while (i < n1) {
            this.FlowerList.set(k++, leftList.get(i++));
        }

        while (j < n2) {
            this.FlowerList.set(k++, rightList.get(j++));
        }
    }

    public void quickSort(int low, int high) {
        if (low < high) {
            int pi = partition(low, high);
            quickSort(low, pi - 1);
            quickSort(pi + 1, high);
        }
    }
    
    private int partition(int low, int high) {
        Flower pivot = this.FlowerList.get(high);
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (this.FlowerList.get(j).compareTo(pivot) < 0) {
                i++;
                Flower temp = this.FlowerList.get(i);
                this.FlowerList.set(i, this.FlowerList.get(j));
                this.FlowerList.set(j, temp);
            }
        }
        Flower temp = this.FlowerList.get(i + 1);
        this.FlowerList.set(i + 1, this.FlowerList.get(high));
        this.FlowerList.set(high, temp);
        return i + 1;
    }

    public void selectionSort() {
        int n = this.FlowerList.size();
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (this.FlowerList.get(j).compareTo(this.FlowerList.get(minIndex)) < 0) {
                    minIndex = j;
                }
            }
            // Swap the found minimum element with the first element
            Flower temp = this.FlowerList.get(minIndex);
            this.FlowerList.set(minIndex, this.FlowerList.get(i));
            this.FlowerList.set(i, temp);
        }
    }

    public void insertionSort() {
        for (int i = 1; i < this.FlowerList.size(); i++) {
            Flower key = this.FlowerList.get(i);
            int j = i - 1;
    
            // Iteratively move all elements greater than the current key to ahead of the key.
            while (j >= 0 && this.FlowerList.get(j).compareTo(key) > 0) {
                this.FlowerList.set(j + 1, this.FlowerList.get(j));
                j--;
            }
            this.FlowerList.set(j + 1, key);
        }
    }

    public void bubbleSort() {
        int n = this.FlowerList.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (this.FlowerList.get(j).compareTo(this.FlowerList.get(j + 1)) > 0) {
                    // Swap list[j] with list[j+1]
                    Flower temp = this.FlowerList.get(j);
                    this.FlowerList.set(j, this.FlowerList.get(j + 1));
                    this.FlowerList.set(j + 1, temp);
                }
            }
        }
    }
}

public class GenerateNecklace {
    public static FlowerIterator generate() {
        // Create an ArrayList to store Flower objects
        ArrayList<Flower> flowerNecklace = new ArrayList<>();

        // Add Flower objects to the ArrayList
        flowerNecklace.add(new Flower(5, "Rose", "Red"));
        flowerNecklace.add(new Flower(6, "Lily", "White"));
        flowerNecklace.add(new Flower(4, "Tulip", "Yellow"));
        flowerNecklace.add(new Flower(8, "Daisy", "Pink"));
        flowerNecklace.add(new Flower(3, "Sunflower", "Yellow"));
        flowerNecklace.add(new Flower(5, "Carnation", "Pink"));
        flowerNecklace.add(new Flower(7, "Orchid", "Purple"));
        flowerNecklace.add(new Flower(4, "Daffodil", "Yellow"));
        flowerNecklace.add(new Flower(6, "Peony", "Pink"));
        flowerNecklace.add(new Flower(5, "Hibiscus", "Red"));
        FlowerIterator iterator = new FlowerIterator(flowerNecklace);
        return iterator;
    }
}
FlowerIterator FlowerNecklace = GenerateNecklace.generate();
```


```Java
// BUBBLE SORT


System.out.println("=====================");
System.out.println("==== BUBBLE SORT ====");
System.out.println("=====================");
FlowerIterator FlowerNecklace = GenerateNecklace.generate(); 
System.out.println("KEY: Name");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("name"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.bubbleSort();
System.out.println("Flower Necklace after sort: " + FlowerNecklace);
System.out.println("KEY: color");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("color"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.bubbleSort();
System.out.println("Flower Necklace after sort: " + FlowerNecklace);
System.out.println("KEY: petals");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("petals"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.bubbleSort();
System.out.println("Flower Necklace after sort: " + FlowerNecklace);

// INSERTION SORT

System.out.println("");
System.out.println("========================");
System.out.println("==== INSERTION SORT ====");
System.out.println("========================");
FlowerIterator FlowerNecklace = GenerateNecklace.generate(); 
System.out.println("KEY: Name");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("name"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.insertionSort();
System.out.println("Flower Necklace after sort: " + FlowerNecklace);
System.out.println("KEY: color");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("color"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.insertionSort();
System.out.println("Flower Necklace after sort: " + FlowerNecklace);
System.out.println("KEY: petals");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("petals"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.insertionSort();
System.out.println("Flower Necklace after sort: " + FlowerNecklace);

// SELECTION SORT

System.out.println("");
System.out.println("========================");
System.out.println("==== SELECTION SORT ====");
System.out.println("========================");
FlowerIterator FlowerNecklace = GenerateNecklace.generate(); 
System.out.println("KEY: Name");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("name"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.selectionSort();
System.out.println("Flower Necklace after sort: " + FlowerNecklace);
System.out.println("KEY: color");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("color"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.selectionSort();
System.out.println("Flower Necklace after sort: " + FlowerNecklace);
System.out.println("KEY: petals");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("petals"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.selectionSort();
System.out.println("Flower Necklace after sort: " + FlowerNecklace);

// QUICK SORT

System.out.println("");
System.out.println("====================");
System.out.println("==== QUICK SORT ====");
System.out.println("====================");
FlowerIterator FlowerNecklace = GenerateNecklace.generate(); 
System.out.println("KEY: Name");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("name"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.quickSort(0, FlowerNecklace.size()-1);
System.out.println("Flower Necklace after sort: " + FlowerNecklace);
System.out.println("KEY: color");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("color"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.quickSort(0, FlowerNecklace.size()-1);
System.out.println("Flower Necklace after sort: " + FlowerNecklace);
System.out.println("KEY: petals");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("petals"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.quickSort(0, FlowerNecklace.size()-1);
System.out.println("Flower Necklace after sort: " + FlowerNecklace);

// MERGE SORT

System.out.println("");
System.out.println("====================");
System.out.println("==== MERGE SORT ====");
System.out.println("====================");
FlowerIterator FlowerNecklace = GenerateNecklace.generate(); 
System.out.println("KEY: Name");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("name"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.mergeSort(0, FlowerNecklace.size()-1);
System.out.println("Flower Necklace after sort: " + FlowerNecklace);
System.out.println("KEY: color");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("color"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.mergeSort(0, FlowerNecklace.size()-1);
System.out.println("Flower Necklace after sort: " + FlowerNecklace);
System.out.println("KEY: petals");
System.out.println("============================");
FlowerNecklace.setKeyType(Flower.KeyType.valueOf("petals"));
System.out.println("Flower Necklace before sort: " + FlowerNecklace);
FlowerNecklace.mergeSort(0, FlowerNecklace.size()-1);
System.out.println("Flower Necklace after sort: " + FlowerNecklace);
```

    =====================
    ==== BUBBLE SORT ====
    =====================
    KEY: Name
    ============================
    Flower Necklace before sort: [(Rose, Red, petals: 5), (Lily, White, petals: 6), (Tulip, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Sunflower, Yellow, petals: 3), (Carnation, Pink, petals: 5), (Orchid, Purple, petals: 7), (Daffodil, Yellow, petals: 4), (Peony, Pink, petals: 6), (Hibiscus, Red, petals: 5)]
    Flower Necklace after sort: [(Carnation, Pink, petals: 5), (Daffodil, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Peony, Pink, petals: 6), (Rose, Red, petals: 5), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    KEY: color
    ============================
    Flower Necklace before sort: [(Carnation, Pink, petals: 5), (Daffodil, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Peony, Pink, petals: 6), (Rose, Red, petals: 5), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    Flower Necklace after sort: [(Carnation, Pink, petals: 5), (Daisy, Pink, petals: 8), (Peony, Pink, petals: 6), (Orchid, Purple, petals: 7), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Lily, White, petals: 6), (Daffodil, Yellow, petals: 4), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    KEY: petals
    ============================
    Flower Necklace before sort: [(Carnation, Pink, petals: 5), (Daisy, Pink, petals: 8), (Peony, Pink, petals: 6), (Orchid, Purple, petals: 7), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Lily, White, petals: 6), (Daffodil, Yellow, petals: 4), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    Flower Necklace after sort: [(Sunflower, Yellow, petals: 3), (Daffodil, Yellow, petals: 4), (Tulip, Yellow, petals: 4), (Carnation, Pink, petals: 5), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Peony, Pink, petals: 6), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Daisy, Pink, petals: 8)]
    
    ========================
    ==== INSERTION SORT ====
    ========================
    KEY: Name
    ============================
    Flower Necklace before sort: [(Rose, Red, petals: 5), (Lily, White, petals: 6), (Tulip, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Sunflower, Yellow, petals: 3), (Carnation, Pink, petals: 5), (Orchid, Purple, petals: 7), (Daffodil, Yellow, petals: 4), (Peony, Pink, petals: 6), (Hibiscus, Red, petals: 5)]
    Flower Necklace after sort: [(Carnation, Pink, petals: 5), (Daffodil, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Peony, Pink, petals: 6), (Rose, Red, petals: 5), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    KEY: color
    ============================
    Flower Necklace before sort: [(Carnation, Pink, petals: 5), (Daffodil, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Peony, Pink, petals: 6), (Rose, Red, petals: 5), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    Flower Necklace after sort: [(Carnation, Pink, petals: 5), (Daisy, Pink, petals: 8), (Peony, Pink, petals: 6), (Orchid, Purple, petals: 7), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Lily, White, petals: 6), (Daffodil, Yellow, petals: 4), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    KEY: petals
    ============================
    Flower Necklace before sort: [(Carnation, Pink, petals: 5), (Daisy, Pink, petals: 8), (Peony, Pink, petals: 6), (Orchid, Purple, petals: 7), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Lily, White, petals: 6), (Daffodil, Yellow, petals: 4), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    Flower Necklace after sort: [(Sunflower, Yellow, petals: 3), (Daffodil, Yellow, petals: 4), (Tulip, Yellow, petals: 4), (Carnation, Pink, petals: 5), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Peony, Pink, petals: 6), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Daisy, Pink, petals: 8)]
    
    ========================
    ==== SELECTION SORT ====
    ========================
    KEY: Name
    ============================
    Flower Necklace before sort: [(Rose, Red, petals: 5), (Lily, White, petals: 6), (Tulip, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Sunflower, Yellow, petals: 3), (Carnation, Pink, petals: 5), (Orchid, Purple, petals: 7), (Daffodil, Yellow, petals: 4), (Peony, Pink, petals: 6), (Hibiscus, Red, petals: 5)]
    Flower Necklace after sort: [(Carnation, Pink, petals: 5), (Daffodil, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Peony, Pink, petals: 6), (Rose, Red, petals: 5), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    KEY: color
    ============================
    Flower Necklace before sort: [(Carnation, Pink, petals: 5), (Daffodil, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Peony, Pink, petals: 6), (Rose, Red, petals: 5), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    Flower Necklace after sort: [(Carnation, Pink, petals: 5), (Daisy, Pink, petals: 8), (Peony, Pink, petals: 6), (Orchid, Purple, petals: 7), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Lily, White, petals: 6), (Daffodil, Yellow, petals: 4), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    KEY: petals
    ============================
    Flower Necklace before sort: [(Carnation, Pink, petals: 5), (Daisy, Pink, petals: 8), (Peony, Pink, petals: 6), (Orchid, Purple, petals: 7), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Lily, White, petals: 6), (Daffodil, Yellow, petals: 4), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    Flower Necklace after sort: [(Sunflower, Yellow, petals: 3), (Daffodil, Yellow, petals: 4), (Tulip, Yellow, petals: 4), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Carnation, Pink, petals: 5), (Lily, White, petals: 6), (Peony, Pink, petals: 6), (Orchid, Purple, petals: 7), (Daisy, Pink, petals: 8)]
    
    ====================
    ==== QUICK SORT ====
    ====================
    KEY: Name
    ============================
    Flower Necklace before sort: [(Rose, Red, petals: 5), (Lily, White, petals: 6), (Tulip, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Sunflower, Yellow, petals: 3), (Carnation, Pink, petals: 5), (Orchid, Purple, petals: 7), (Daffodil, Yellow, petals: 4), (Peony, Pink, petals: 6), (Hibiscus, Red, petals: 5)]
    Flower Necklace after sort: [(Carnation, Pink, petals: 5), (Daffodil, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Peony, Pink, petals: 6), (Rose, Red, petals: 5), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    KEY: color
    ============================
    Flower Necklace before sort: [(Carnation, Pink, petals: 5), (Daffodil, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Peony, Pink, petals: 6), (Rose, Red, petals: 5), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    Flower Necklace after sort: [(Peony, Pink, petals: 6), (Carnation, Pink, petals: 5), (Daisy, Pink, petals: 8), (Orchid, Purple, petals: 7), (Rose, Red, petals: 5), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Tulip, Yellow, petals: 4), (Daffodil, Yellow, petals: 4), (Sunflower, Yellow, petals: 3)]
    KEY: petals
    ============================
    Flower Necklace before sort: [(Peony, Pink, petals: 6), (Carnation, Pink, petals: 5), (Daisy, Pink, petals: 8), (Orchid, Purple, petals: 7), (Rose, Red, petals: 5), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Tulip, Yellow, petals: 4), (Daffodil, Yellow, petals: 4), (Sunflower, Yellow, petals: 3)]
    Flower Necklace after sort: [(Sunflower, Yellow, petals: 3), (Daffodil, Yellow, petals: 4), (Tulip, Yellow, petals: 4), (Carnation, Pink, petals: 5), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Peony, Pink, petals: 6), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Daisy, Pink, petals: 8)]
    
    ====================
    ==== MERGE SORT ====
    ====================
    KEY: Name
    ============================
    Flower Necklace before sort: [(Rose, Red, petals: 5), (Lily, White, petals: 6), (Tulip, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Sunflower, Yellow, petals: 3), (Carnation, Pink, petals: 5), (Orchid, Purple, petals: 7), (Daffodil, Yellow, petals: 4), (Peony, Pink, petals: 6), (Hibiscus, Red, petals: 5)]
    Flower Necklace after sort: [(Carnation, Pink, petals: 5), (Daffodil, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Peony, Pink, petals: 6), (Rose, Red, petals: 5), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    KEY: color
    ============================
    Flower Necklace before sort: [(Carnation, Pink, petals: 5), (Daffodil, Yellow, petals: 4), (Daisy, Pink, petals: 8), (Hibiscus, Red, petals: 5), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Peony, Pink, petals: 6), (Rose, Red, petals: 5), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    Flower Necklace after sort: [(Carnation, Pink, petals: 5), (Daisy, Pink, petals: 8), (Peony, Pink, petals: 6), (Orchid, Purple, petals: 7), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Lily, White, petals: 6), (Daffodil, Yellow, petals: 4), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    KEY: petals
    ============================
    Flower Necklace before sort: [(Carnation, Pink, petals: 5), (Daisy, Pink, petals: 8), (Peony, Pink, petals: 6), (Orchid, Purple, petals: 7), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Lily, White, petals: 6), (Daffodil, Yellow, petals: 4), (Sunflower, Yellow, petals: 3), (Tulip, Yellow, petals: 4)]
    Flower Necklace after sort: [(Sunflower, Yellow, petals: 3), (Daffodil, Yellow, petals: 4), (Tulip, Yellow, petals: 4), (Carnation, Pink, petals: 5), (Hibiscus, Red, petals: 5), (Rose, Red, petals: 5), (Peony, Pink, petals: 6), (Lily, White, petals: 6), (Orchid, Purple, petals: 7), (Daisy, Pink, petals: 8)]

