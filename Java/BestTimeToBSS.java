
class BestTimeToBSS {

    public int maxProfit(int[] prices) {
        int i, minPrice = prices[0], maxProfit = 0;

        for (i = 1; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }

            maxProfit = Math.max(maxProfit, prices[i] - minPrice);

        }
        System.out.println(maxProfit);
        return maxProfit;
    }

    public static void main(String[] args) {
        BestTimeToBSS instance = new BestTimeToBSS();
        int[] prices = {7, 1, 5, 3, 6, 4};
        instance.maxProfit(prices);
    }
}
