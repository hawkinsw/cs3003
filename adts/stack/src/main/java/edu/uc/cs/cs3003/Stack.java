package edu.uc.cs.cs3003;

import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;

public class Stack {
    Stack() {
        m_data = new ArrayList<Integer>();

    }

    public void push(Integer newelement) {
        m_data.add(newelement);
    }

    public Integer top() throws EmptyStackException {
        if (m_data.size() == 0) {
            throw new EmptyStackException();
        }
        return m_data.get(m_data.size() - 1);
    }

    public Integer pop() throws EmptyStackException {
        if (m_data.size() == 0) {
            throw new EmptyStackException();
        }
        Integer top = top();
        m_data.remove(m_data.size() - 1);
        return top;
    }

    private List<Integer> m_data;
}
