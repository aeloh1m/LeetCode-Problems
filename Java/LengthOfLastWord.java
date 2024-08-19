
import java.util.HashMap;
import java.util.Map;

class LengthOfLastWord {

    public int lengthOfLastWord(String s) {
        int num = 0;
        boolean flag = false;

        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) != ' ') {
                flag = true; // This means the few first spaces
                num++;

            }
            if (flag == true) {

                if (s.charAt(i) == ' ') {
                    System.err.println(num);
                    return num--;
                }

            }
        }

        return num;

    }

    /*
     * I have the arr which I'm iterating from the end => If it encounter spaces it
     * will skip the num++
     * if it encounters letters, it will start counting
     * then if it encounters a new " " after the letters, returns the num.
     */

    public static void main(String[] args) {
        LengthOfLastWord instance = new LengthOfLastWord();
        String s = "Hello World";
        instance.lengthOfLastWord(s);

    }
}
