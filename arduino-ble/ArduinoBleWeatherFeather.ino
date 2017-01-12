#include <DHT.h>
#include <Arduino.h>
#include <SPI.h>
#include "Adafruit_BLE.h"
#include "Adafruit_BluefruitLE_SPI.h"
#include "Adafruit_BluefruitLE_UART.h"
#include "BluefruitConfig.h"
#define DHTPIN A0
#define DHTTYPE DHT11  

Adafruit_BluefruitLE_SPI ble(BLUEFRUIT_SPI_CS, BLUEFRUIT_SPI_IRQ, BLUEFRUIT_SPI_RST);

// A small helper
void error(const __FlashStringHelper*err) {
  Serial.println(err);
  while (1);
}
DHT dht(DHTPIN, DHTTYPE);
float average_humidity;
float average_temperature;
int samplesize = 25;
int32_t thermopServiceId;
int32_t temperatureCharId;
int32_t humidityCharId;
int32_t heatIndexCharId;

void setup(void)
{
  delay(500);
  boolean success;

  Serial.begin(115200);
  Serial.println(F("Nucleus Example"));
  Serial.println(F("---------------------------------------------------"));

  randomSeed(micros());
  Serial.print(F("Initialising the Bluefruit LE module: "));
  if ( !ble.begin(VERBOSE_MODE) )
  {
    error(F("Couldn't find Bluefruit, make sure it's in CoMmanD mode & check wiring?"));
  }
  Serial.println( F("OK!") );

  /* Perform a factory reset to make sure everything is in a known state */
  Serial.println(F("Performing a factory reset: "));
  if (! ble.factoryReset() ){
       error(F("Couldn't factory reset"));
  }

  /* Disable command echo from Bluefruit */
  ble.echo(false);

  Serial.println("Requesting Bluefruit info:");
  /* Print Bluefruit information */
  ble.info();

  // this line is particularly required for Flora, but is a good idea
  // anyways for the super long lines ahead!
  // ble.setInterCharWriteDelay(5); // 5 ms

  /* Change the device name to make it easier to find */
  Serial.println(F("Setting device name"));

  if (! ble.sendCommandCheckOK(F("AT+GAPDEVNAME=Nucleus")) ) {
    error(F("Could not set device name?"));
  }

  /* Add the Heart Rate Service definition */
  /* Service ID should be 1 */
  Serial.println(F("Adding the Service (UUID = 0x181A): "));
  success = ble.sendCommandWithIntReply( F("AT+GATTADDSERVICE=UUID=0x181A"), &thermopServiceId);
  if (! success) {
    error(F("Could not add service"));
  }
  Serial.println(F("Adding the Temperature characteristic (UUID:0x2A1E): "));
  success = ble.sendCommandWithIntReply( F("AT+GATTADDCHAR=UUID=0x2A6e, PROPERTIES=0x12, MIN_LEN=1, MAX_LEN=5, VALUE=19.0, DESCRIPTION=https://en.wikipedia.org/wiki/Temperature, PRESENTATION=14-00-2F-27-01-00-00"), &temperatureCharId);
    if (! success) {
    error(F("Could not add Temperature characteristic"));
  }

  Serial.println(F("Adding the Humidity characteristic (UUID:0x22A6F): "));
  success = ble.sendCommandWithIntReply( F("AT+GATTADDCHAR=UUID=0x2A6F, PROPERTIES=0x12, MIN_LEN=1, MAX_LEN=5, VALUE=0 DESCRIPTION=Humidty, PRESENTATION=14-00-AD-27-01-00-00"), &humidityCharId);
    if (! success) {
    error(F("Could not add Humidity characteristic"));
  }

    Serial.println(F("Adding the Heat Index characteristic (UUID:0x2A7A): "));
  success = ble.sendCommandWithIntReply( F("AT+GATTADDCHAR=UUID=0x2A7A, PROPERTIES=0x12, MIN_LEN=1, MAX_LEN=5, VALUE=0 DESCRIPTION=Heat Index, PRESENTATION=14-00-2F-27-01-00-00"), &heatIndexCharId);
    if (! success) {
    error(F("Could not add Humidity characteristic"));
  }

 
  
  Serial.print(F("Adding Weather UUID to the advertising payload: "));
  ble.sendCommandCheckOK( F("AT+GAPSETADVDATA=05-02-3A-12-0A-18") );
  /* Reset the device for the new service setting changes to take effect */
  Serial.print(F("Performing a SW reset (service changes require a reset): "));
  dht.begin();

  ble.reset();
  Serial.println("begining DHT");
}

/** Send randomized heart rate data continuously **/
void loop(void)
{
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  float hic = dht.computeHeatIndex(t, h, false);
  Serial.print(F("Updating value TEMP to "));
  Serial.println(t);
  /* Command is sent when \n (\r) or println is called */
  /* AT+GATTCHAR=CharacteristicID,value */
  ble.print( F("AT+GATTCHAR=") );
  ble.print( temperatureCharId );
  ble.print(F(","));
  ble.println((int)(t*100));
  /* Check if command executed OK */
  if ( !ble.waitForOK() )
  {
    Serial.println(F("Failed to get response!"));
  }
  Serial.print(F("Updating HUM value to "));
  Serial.println(h);
  /* Command is sent when \n (\r) or println is called */
  /* AT+GATTCHAR=CharacteristicID,value */
  ble.print( F("AT+GATTCHAR=") );
  ble.print( humidityCharId );
  ble.print( F(",") );
  ble.println((int)(h*100));
  Serial.println((int)(h*100));

  /* Check if command executed OK */
  if ( !ble.waitForOK() )
  {
    Serial.println(F("Failed to get response!"));
  }

  Serial.print(F("Updating HIN value to "));
  Serial.println(hic);
  /* Command is sent when \n (\r) or println is called */
  /* AT+GATTCHAR=CharacteristicID,value */
  ble.print( F("AT+GATTCHAR=") );
  ble.print( heatIndexCharId );
  ble.print( F(",") );
  ble.println((int)(hic));

  /* Check if command executed OK */
  if ( !ble.waitForOK() )
  {
    Serial.println(F("Failed to get response!"));
  }
  int val = analogRead(A2);
  Serial.println(map(val, 0, 1023, 0,100));
  /* Delay before next measurement update */
  delay(1000);
}
