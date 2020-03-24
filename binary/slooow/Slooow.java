import java.math.BigInteger;
import java.nio.charset.StandardCharsets;

public class Slooow {
    public static final String prefix = "AFNOM{";
    public static final String suffix = "}";

    private StringBuilder flag;

    public static void main(String[] args) {
        Slooow slooow = new Slooow();
        slooow.run();
    }

    public Slooow() {
        flag = new StringBuilder();
    }

    public void run() {
        for (char ch : prefix.toCharArray()) {
            add_to_flag(Character.toString(ch));
        }

        while (flag.length() < 60) {
            byte part = 0;
            BigInteger length = BigInteger.valueOf(flag.length());
            BigInteger count = BigInteger.TWO.pow(flag.length()).subtract(BigInteger.ONE);

            while (count.compareTo(BigInteger.ZERO) >= 0) {
                part ^= flag.charAt(count.mod(length).intValue());
                count = count.subtract(BigInteger.ONE);
            }

            add_to_flag(String.format("%x", part));
        }

        for (char ch : suffix.toCharArray()) {
            add_to_flag(Character.toString(ch));
        }
    }

    private void add_to_flag(String s) {
        flag.append(s);
        System.out.println(flag);
    }
}