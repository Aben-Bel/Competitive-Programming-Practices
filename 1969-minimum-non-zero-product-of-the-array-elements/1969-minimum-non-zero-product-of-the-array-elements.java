import java.math.BigInteger;
class Solution {
    public int minNonZeroProduct(int p) {
        BigInteger n = new BigInteger("2");
        n = n.pow(p);
        n = n.subtract(new BigInteger("1"));
        BigInteger m = new BigInteger("1000000007");
        // n = n.mod(m);
        BigInteger n_1 = n.subtract(new BigInteger("1"));
        n = ((n_1).modPow(n.divide(new BigInteger("2")), m)).multiply(n).mod(m);
        return n.intValue();
    }
}