
import java.util.Arrays;

class MajorityElement {

    public void rotate(int[] nums, int k) {
        System.out.println(Arrays.toString(nums) + " og");

        int i, j, lastIndex;

        for (i = 0; i < k; i++) {
            lastIndex = nums[nums.length - 1];
            // Shift elements from the end to the beginning
            for (j = nums.length - 1; j > 0; j--) {
                nums[j] = nums[j - 1];
            }

            // Place the last element in the first position
            nums[0] = lastIndex;
        }
        System.out.println(Arrays.toString(nums) + " new");

    }

    public void rotateII(int[] nums, int k) {
        System.out.println(Arrays.toString(nums) + " og");
        int numbersLength, positionerForLastRow, i, j;

        numbersLength = nums.length;
        // Handle cases where k is greater than the array length
        k = k % numbersLength;

        if (k == 0 || numbersLength <= 1) {
            return; // No need to rotate if k is 0 or array has 1 or fewer elements
        }

        int[] firstRow, lastRow;

        firstRow = Arrays.copyOfRange(nums, 0, numbersLength - k);
        lastRow = Arrays.copyOfRange(nums, numbersLength - k, numbersLength);
        positionerForLastRow = lastRow.length;

        System.out.println(Arrays.toString(firstRow) + " first");
        System.out.println(Arrays.toString(lastRow) + " last");

        for (i = 0; i < lastRow.length; i++) {
            nums[i] = lastRow[i];

        }

        for (j = 0; j < firstRow.length; j++) {
            nums[positionerForLastRow] = firstRow[j];
            positionerForLastRow++;
        }

        System.out.println(Arrays.toString(nums) + " new");

    }

    /*
    Grab the current index, move to the right +1 */
    public static void main(String[] args) {
        MajorityElement instance = new MajorityElement();
        int[] nums = {-1, -100, 3, 99};
        int k = 2;
        instance.rotateII(nums, k);

    }
}
