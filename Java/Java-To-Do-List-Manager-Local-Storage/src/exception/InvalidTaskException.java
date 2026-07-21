package exception;


public class InvalidTaskException extends Exception {

    public InvalidTaskException() {
        super();
    }

    public InvalidTaskException(String message) {
        super(message);
    }

    public InvalidTaskException(String message, Throwable cause) {
        super(message, cause);
    }
}