
class isPalindrome {

    public boolean isPalindrome(String s) {
        String result = "", reverse = "";
        result = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        reverse = new StringBuilder(result).reverse().toString();

        if(result.equals(reverse))
        {
            return true;
        }
        else {
            return false;
        }
    }

    public static void main(String[] args) {
        isPalindrome instance = new isPalindrome();
        String s = "A man, a plan, a canal: Panama";
        instance.isPalindrome(s);
    }
}
