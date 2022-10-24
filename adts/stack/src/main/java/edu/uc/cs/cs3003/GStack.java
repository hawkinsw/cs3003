package edu.uc.cs.cs3003;

import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;

public class GStack<ElementType> {
    GStack() {
        m_data = new ArrayList<ElementType>();

    }

    public void push(ElementType newelement) {
        m_data.add(newelement);
    }

    public ElementType top() throws EmptyStackException {
        if (m_data.size() == 0) {
            throw new EmptyStackException();
        }
        return m_data.get(m_data.size() - 1);
    }

    public ElementType pop() throws EmptyStackException {
        if (m_data.size() == 0) {
            throw new EmptyStackException();
        }
        ElementType top = top();
        m_data.remove(m_data.size() - 1);
        return top;
    }

    private List<ElementType> m_data;
}
