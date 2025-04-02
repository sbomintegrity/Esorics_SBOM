package com.example.calculator;

import java.util.Scanner;

public class CalculatorApp {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Simple Calculator");
        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();

        System.out.print("Choose operation (+, -, *, /): ");
        char op = scanner.next().charAt(0);

        double result;
        switch (op) {
            case '+':
                result = Calculator.add(num1, num2);
                break;
            case '-':
                result = Calculator.subtract(num1, num2);
                break;
            case '*':
                result = Calculator.multiply(num1, num2);
                break;
            case '/':
                try {
                    result = Calculator.divide(num1, num2);
                } catch (IllegalArgumentException e) {
                    System.out.println(e.getMessage());
                    scanner.close();
                    return;
                }
                break;
            default:
                System.out.println("Invalid operation.");
                scanner.close();
                return;
        }

        System.out.println("Result: " + result);
        scanner.close();
    }
}

