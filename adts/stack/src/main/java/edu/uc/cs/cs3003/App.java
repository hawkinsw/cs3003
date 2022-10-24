package edu.uc.cs.cs3003;

import java.util.EmptyStackException;

/**
 * Hello world!
 */
public final class App {
    private App() {
    }

    private static void TestStack() {
        Stack stack = new Stack();

        stack.push(5);
        stack.push(10);
        stack.push(15);
        stack.push(20);

        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());

        try {
            System.out.println(stack.pop());
        } catch (EmptyStackException ese) {
            System.out.println("Oops: " + ese.toString());
        }
    }

    /**
     * Says hello to the world.
     * @param args The arguments of the program.
     */
    public static void main(String[] args) {
        TestStack();
    }
}
