import RPi.GPIO as GPIO
import time
import json
import urllib.request

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

GPIO.setmode(GPIO.BOARD)

pin_to_circuit = 7

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

def main ():
    while True:
        
        data = Object()
        data.lightElectricalQuantity = rc_time(pin_to_circuit)
        data = urllib.parse.urlencode(data.toJSON()).encode('utf-8')

        req = urllib.request.Request('http://192.168.48.128:5555/api/measurements')
        req.add_header('Content-Type', 'application/json')

        response = urllib.request.urlopen(req, jsodata)
        
        
        print(rc_time(pin_to_circuit))
        time.sleep(1)
#Catch when script is interrupted, cleanup correctly
try:
    main()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

