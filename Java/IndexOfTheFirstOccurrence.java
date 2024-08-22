

class IndexOfTheFirstOccurrence {

    public int indexOfTheFirstOccurrence(String haystack, String needle) {



        for(int i = 0; i <= haystack.length() - needle.length(); i++)
        {
            String coincidence = haystack.substring(i, i + needle.length());

            if (coincidence.equals(needle)) {
                System.out.println(i);
                System.out.println(coincidence);
                return i;
                
            }
        }

        return -1;

    }

    /*
     * 
     */
    public static void main(String[] args) {
        IndexOfTheFirstOccurrence instance = new IndexOfTheFirstOccurrence();
        String haystack = "sadbutsad", needle = "sad";
        instance.indexOfTheFirstOccurrence(haystack, needle);

    }
}
