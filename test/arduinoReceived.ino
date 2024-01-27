#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

SoftwareSerial mySerial(11, 12); // RX, TX
DFRobotDFPlayerMini myDFPlayer;

int sensor_value;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  mySerial.begin(9600);
  myDFPlayer.begin(mySerial);
  myDFPlayer.setTimeOut(500);
  myDFPlayer.play(1);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    char data = Serial.read();
    if (data == '1') {
      // Do something when '1' is received
      Serial.println("Received '1' from Raspberry Pi");
    }
  }

  sensor_value = random(10, 20);
  Serial.println(sensor_value);
  delay(1000);
}
