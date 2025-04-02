package com.example.calculator;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    @Test
    void testAdd() {
        assertEquals(5, Calculator.add(2, 3));
    }

    @Test
    void testSubtract() {
        assertEquals(2, Calculator.subtract(5, 3));
    }

    @Test
    void testMultiply() {
        assertEquals(15, Calculator.multiply(5, 3));
    }

    @Test
    void testDivide() {
        assertEquals(2, Calculator.divide(6, 3));
    }

    @Test
    void testDivideByZero() {
        assertThrows(IllegalArgumentException.class, () -> Calculator.divide(1, 0));
    }
}
