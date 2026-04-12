#error handling
#Alex Nairobi kenya

import logging

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
def load_data(data):
    try:
        avarage = sum(data)/len(data)
        return avarage
    except ZeroDivisionError:
     logging.error("Error: Cannot calculate average of empty data")
     
    except TypeError:
      logging.error("Error: Data must be numbers not text")
     


print(load_data([10, 20, 30]))
print(load_data([]))
print(load_data(["nairobi", "kenya"]))

