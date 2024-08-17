/* 
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 */

import java.util.ArrayList;
import java.util.List;

public class TextJustification {

    public List<String> fullJustify(String[] words, int maxWidth) {

        List<String> justifiedText = new ArrayList<>();
        List<String> resultText = new ArrayList<>();

        String completeString = "";
        int indexToCompare = 1;
        for (int i = 1; i <= words.length; i++) {
            String newString = "";
            newString = words[indexToCompare - 1] + " ";
            completeString += newString;
            justifiedText.add(completeString);
            completeString = "";
            indexToCompare++;

        }

        completeString = "";

        while (!justifiedText.isEmpty()) {

            while (completeString.length() < maxWidth) {
                for (int i = 0; i < words.length; i++) {

                    completeString += justifiedText.get(i);
                    completeString += " ";

                }
            }
            resultText.add(completeString);
            justifiedText.remove(justifiedText.size() - 1);

        }

        System.out.println(completeString);
        System.out.println(resultText);
        return justifiedText;
    }

    /*Primero derecha a izq, después izq der. loopear. Minus length*/
    public static void main(String[] args) {
        TextJustification instance = new TextJustification();
        String[] words = {"Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"};
        int maxWidth = 20;
        instance.fullJustify(words, maxWidth);

    }

};
