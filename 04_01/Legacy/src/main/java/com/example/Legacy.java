package com.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class Legacy {

    public static void main(String[] args) {
        List<String> items = new ArrayList<>();
        items.add("Apple");
        items.add("Banana");
        items.add("Cherry");

        // Using forEach with a lambda expression
        items.forEach(item -> System.out.println(item));

        // Optional usage with ifPresent
        Optional<String> optionalItem = findItem(items, "Banana");
        if (optionalItem.isPresent()) {
            System.out.println("Found item: " + optionalItem.get());
        } else {
            System.out.println("Item not found");
        }

        // Traditional for loop for processing
        for (String item : items) {
            System.out.println(item.toUpperCase());
        }
        
    }

    private static Optional<String> findItem(List<String> items, String searchItem) {
        for (String item : items) {
            if (item.equalsIgnoreCase(searchItem)) {
                return Optional.of(item);
            }
        }
        return Optional.empty();
    }
}
