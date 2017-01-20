
#include "DHT.h"
#include <XBee.h>
#include <ArduinoJson.h>

#define DHTPIN 13     // what digital pin we're connected to

// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11
//#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht(DHTPIN, DHTTYPE);

XBee xbee = XBee();


// 16-bit addressing: Enter address of remote XBee, typically the coordinator
//Tx16Request tx = Tx16Request(0, payload, sizeof(payload));
//64-bit addressing: This is the SH + SL address of remote XBee
XBeeAddress64 addr64 = XBeeAddress64(0x0013a200, 0x40C348A9);
// unless you have MY on the receiving radio set to FFFF, this will be received as a RX16 packet

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
  Serial.begin(9600);
  //Serial.println("DHTxx test!");
  inputString.reserve(200);

  xbee.setSerial(Serial);

  dht.begin();
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

    Serial.print("Humidity: ");
    Serial.print(h);
    Serial.print(" %\t");
    Serial.print("Temperature: ");
    Serial.print(t);
    Serial.print(" *C ");
    Serial.print(f);
    Serial.print(" *F\t");
    Serial.print("Heat index: ");
    Serial.print(hic);
    Serial.print(" *C ");
    Serial.print(hif);
    Serial.println(" *F");


StaticJsonBuffer<200> jsonBuffer;

JsonObject& root = jsonBuffer.createObject();
root["sensor"] = "Temperatur";
root["unit"] = "Celsius";

JsonArray& data = root.createNestedArray("data");
data.add(t);  // 6 is the number of decimals to print
//data.add(f);   // if not specified, 2 digits are printed
//data.add(h);   // if not specified, 2 digits are printed

char buffer[(root.measureLength() +1)];
root.printTo(buffer, sizeof(buffer));

String temp = String(buffer);

//maximum payload size = 100
byte payload[(temp.length()+1)];

temp.getBytes(payload, sizeof(payload));

Tx64Request tx = Tx64Request(addr64, payload, sizeof(payload));

  xbee.send(tx);

}


