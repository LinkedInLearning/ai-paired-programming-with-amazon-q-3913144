package com.example;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.xml.bind.DatatypeConverter;

public class Legacy {

    public static void main(String[] args) {
        // Generating a random number using Math.random()
        double randomValue = Math.random();
        System.out.println("Random value (Math.random()): " + randomValue);

        // Old way of creating an unmodifiable list (returns an unmodifiable view)
        List<String> items = new ArrayList<>();
        items.add("Apple");
        items.add("Banana");
        items.add("Cherry");
        List<String> unmodifiableItems = Collections.unmodifiableList(items);

        System.out.println("Unmodifiable list: " + unmodifiableItems);

        // Converting a byte array to a hex string using DatatypeConverter (deprecated)
        byte[] data = {0x01, 0x02, 0x03, 0x04, 0x05};
        String hexString = DatatypeConverter.printHexBinary(data);
        System.out.println("Hex string: " + hexString);

        // Parsing a hex string back to a byte array using DatatypeConverter (deprecated)
        byte[] parsedData = DatatypeConverter.parseHexBinary(hexString);
        System.out.println("Parsed data: " + parsedData);
    }
}
