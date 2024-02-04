#include <SoftwareSerial.h>

int sensor_value;

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
}

void loop() {
  sensor_value = random(0, 20); // for test
  Serial.println(sensor_value);
  delay(1000);
}