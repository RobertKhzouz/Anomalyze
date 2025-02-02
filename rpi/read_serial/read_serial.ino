// NOTE:
// You must upload this sketch to the Ardunino in order for python scripts to work.

#include<Wire.h>
#include "Seeed_BMP280.h"

BMP280 bmp;

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);
  if (!bmp.init()) {
    Serial.println("Could not find a valid BME280 sensor");
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  float temperature = bmp.getTemperature();
  float pressure = bmp.getPressure() / 100.0F;
  
  Serial.print(temperature);
  Serial.print(',');
  Serial.println(pressure);

  delay(1000);
}
