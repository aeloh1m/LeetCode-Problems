
import java.util.HashMap;
import java.util.Map;

class MajorityElement {

    public int majorityElement(int[] nums) {
        Map<Integer, Integer> mostFrecuent = new HashMap<>();
        int highestCount = 0;
        int response = 0;
        for (int i : nums) {
            mostFrecuent.put(i, 1 + mostFrecuent.getOrDefault(i, 0)); //Add the current num and the key +1, if repeated 1+i

            if (mostFrecuent.get(i) > highestCount) {
                response = i;
                highestCount = mostFrecuent.get(i);
            }
        }

        return response;

    }

    public static void main(String[] args) {
        MajorityElement instance = new MajorityElement();
        int[] nums = {3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3};
        instance.majorityElement(nums);

    }
}
