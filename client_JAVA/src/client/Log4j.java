package client;

import org.apache.log4j.*;

public class Log4j {

	static final Logger logger = Logger.getLogger(Log4j.class);
	
	public static void main(String[] args) {
		
		ConsoleAppender console = new ConsoleAppender();
		console.setLayout(new PatternLayout("%d [%p|%c|%C{1}] %m%n"));
		console.setThreshold(Level.DEBUG);
		console.activateOptions();
		Logger.getRootLogger().addAppender(console);
		
		logger.info("This in an info message");
		logger.warn("cacaaaaaaaaaa");
	}
}
