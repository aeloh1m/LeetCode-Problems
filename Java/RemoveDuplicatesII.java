
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class RemoveDuplicatesII {

    public int removeDuplicates(int[] nums) {
        Map<Integer, Integer> mostFrecuent = new HashMap<>();
        int highestCount = 0, response = 0, flag = 0, sum = 0, uniqueIndex = 1, count = 1;
        System.out.println(Arrays.toString(nums) + " og");

        for (int i : nums) {
            mostFrecuent.put(i, 1 + mostFrecuent.getOrDefault(i, 0)); //Add the current num and the key +1, if repeated 1+i

            if (mostFrecuent.get(i) > highestCount) {
                response = i;
                highestCount = mostFrecuent.get(i);
            }
        }

        if (nums.length == 0) {
            return 0;
        }

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                count++;

            } else {
                count = 1;
            }

            // Only place the element if count <= 2
            if (count <= 2) {
                nums[uniqueIndex] = nums[i];
                uniqueIndex++;
            }
        }
        System.out.println(Arrays.toString(nums) + " before");

        Collection<Integer> values = mostFrecuent.values();

        // Iterate over values and sum them
        for (Integer value : values) {
            if (value >= 2) {
                sum += 2;

            }
            else if (value <=2)
            {
                sum += value;

            }
        }
        response = sum;

        System.out.println(sum + " sum");
        System.out.println(Arrays.toString(nums) + " new");
        System.out.println(highestCount + " highest");
        System.out.println(response + " res");
        System.out.println(mostFrecuent);

        return response; // The length of the array with unique elements
    }

    public static void main(String[] args) {
        RemoveDuplicatesII instance = new RemoveDuplicatesII();
        int[] nums = {1, 1, 1, 2, 2, 2, 3, 3};
        instance.removeDuplicates(nums);

    }
}
