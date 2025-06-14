import logging
from datetime import datetime
import time
import random

# Configure basic logging to write logs to a file
log_file_path = '/var/log/loki_udemy.log'
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s level=%(levelname)s app=myapp component=%(component)s %(message)s')

def generate_log_entries():
    components = ["database", "backend"]

    for _ in range(10):
        log_level = logging.INFO if _ % 3 == 0 else logging.WARNING if _ % 3 == 1 else logging.ERROR
        component = random.choice(components)

        print(f"Generating log of type {logging.getLevelName(log_level)} with component {component}")

        if log_level == logging.INFO:
            log_message = "Information: Application running normally"
        elif log_level == logging.WARNING:
            log_message = "Warning: Resource usage high"
        else:
            log_message = "Critical error: Database connection lost"

        # Use the extra parameter to dynamically set the 'component' value
        logging.log(log_level, log_message, extra={"component": component})
        time.sleep(1)  # Sleep for 1 second between entries

if __name__ == "__main__":
    generate_log_entries()
    logging.shutdown()

# Ez a Python script egy alapvető naplózási (logging) rendszer működését demonstrálja.
# Konfigurálja a naplózást
# A naplófájl (/var/log/loki_udemy.log) az eseményeket menti.
# A napló formátuma tartalmazza az időbélyeget, a napló szintjét (INFO, WARNING, ERROR), az alkalmazás nevét (myapp), és a komponenst (pl. database, backend).
# Naplóüzeneteket generál
# 10 üzenetet ír be véletlenszerűen kiválasztott komponensekhez.
# Az üzenetek háromféle lehetnek:
# INFO: Normál működés
# WARNING: Magas erőforrás-használat
# ERROR: Kritikus hiba (pl. adatbázis-kapcsolat elveszett)
# Időzített naplóírás
# Minden üzenet írása után 1 másodpercre megáll, így a naplóbejegyzések időbélyegei jól követhetők.
# Leállítja a naplózást
# Amikor a script befejezi a futást, meghívja a logging.shutdown() függvényt.
# Ez a script segít alapvető rendszerinformációkat rögzíteni, amelyek később hibakeresésre vagy teljesítményfigyelésre használhatók.
