import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="server.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)