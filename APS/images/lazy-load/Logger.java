public class Logger {
    private static Logger loggerInstance = null;

    private Logger() {
        /* ... constructor ... */
    }

    public static Logger getLogger() {
        if (loggerInstance == null)
            loggerInstance = new Logger();
        return loggerInstance;
    }
}