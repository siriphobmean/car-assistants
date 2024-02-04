#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

const int US100_TX = 2;
const int US100_RX = 3;
SoftwareSerial puertoUS100(US100_RX, US100_TX);
SoftwareSerial mySerial(11, 12); // RX, TX
DFRobotDFPlayerMini myDFPlayer;

unsigned int MSByteDist = 0;
unsigned int LSByteDist = 0;
unsigned int cmDist = 0;

int sensor_value;
bool hasSentAlert = false;

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  puertoUS100.begin(9600);
  myDFPlayer.begin(mySerial);
  myDFPlayer.setTimeOut(500);
  myDFPlayer.play(1); // Start...
  myDFPlayer.volume(30); // 0-30
}

void loop() {
  puertoUS100.flush();
  puertoUS100.write(0x55);
  delay(1000);

  if (puertoUS100.available() >= 2) {
    MSByteDist = puertoUS100.read();
    LSByteDist  = puertoUS100.read();
    cmDist  = (MSByteDist * 256 + LSByteDist) / 10;

    if ((cmDist > 0) && (cmDist < 1000)) {
      Serial.println(cmDist, DEC);
    }
  }

  if (cmDist <= 6) {
    myDFPlayer.play(2); // Horn!!!
    while (sensor_value <= 6) {
      mySerial.print(sensor_value);
      mySerial.flush();
    }
    hasSentAlert = true;
    delay(1000);
  }
  if (cmDist > 6) {
    hasSentAlert = false;
  }
}