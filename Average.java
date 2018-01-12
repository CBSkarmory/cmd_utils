public class Average {
    public static void main(String[] args) {
        if (args.length == 0) {
            err(-1, "no arguments");
        }
        System.out.printf("%f\n", "-w".equals(args[0])?
                weightedAvg(args): avg(args));
    }

    private static double weightedAvg (String[] args) {
        int count= 0;
        double sum= 0;
        for (int i= 1; i < args.length; ++i) {
            try {
                String[] split= args[i].split(",");
		double num= Double.parseDouble(split[0]), weight= 1.0;
		if (split.length == 2) {   
		    weight= Double.parseDouble(split[1]);
                } else {
		    if (split.length > 2) {
			err(-3, "Invalid formatting");
		    }
		}
		sum += (num * weight);
                count += weight;
            } catch (NumberFormatException e) {
                err(-2, "NumberFormatException");
            }
        }
        return sum/count;
    }

    private static double avg (String[] args) {
        int count= 0;
        double sum= 0;
        for (String s : args) {
            try {
                sum += Double.parseDouble(s);
                ++count;
            } catch (NumberFormatException e) {
                err(-2, "NumberFormatException");
            }
        }
        return sum/count;
    }

    private static void err(int exitCode, String message) {
        System.err.printf("[ERROR] %s\n", message);
        System.exit(exitCode);
    }
}
