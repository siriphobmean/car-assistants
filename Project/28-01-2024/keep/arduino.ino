#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

SoftwareSerial mySerial(11, 12); // RX, TX
DFRobotDFPlayerMini myDFPlayer;

int sensor_value;

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  myDFPlayer.begin(mySerial);
  myDFPlayer.setTimeOut(500);
  myDFPlayer.play(1); // Start...
  myDFPlayer.volume(18); // 0-30
}

void loop() {
  sensor_value = random(0, 20);
  Serial.println(sensor_value);
  if(sensor_value == 0){
    myDFPlayer.play(2); // Horn!!!
    delay(1500);
    myDFPlayer.play(2); // Horn!!!
    delay(1500);
    myDFPlayer.play(2); // Horn!!!
    delay(1500);
    myDFPlayer.play(2); // Horn!!!
    delay(1500);
    while(sensor_value == 0){
      mySerial.print(sensor_value);
      mySerial.flush();
    }
  }
  delay(1000);
}