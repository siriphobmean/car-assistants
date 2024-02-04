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

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  puertoUS100.begin(9600);
  myDFPlayer.begin(mySerial);
  myDFPlayer.setTimeOut(500);
  myDFPlayer.play(1); // Start...
  myDFPlayer.volume(18); // 0-30
}

void loop() {
  puertoUS100.flush();
  puertoUS100.write(0x55);
  delay(500);

  if (puertoUS100.available() >= 2) {
    MSByteDist = puertoUS100.read();
    LSByteDist  = puertoUS100.read();
    cmDist  = (MSByteDist * 256 + LSByteDist) / 10;

    if ((cmDist > 0) && (cmDist < 1000)) {
      Serial.print("Distancia: ");
      Serial.print(cmDist, DEC);
      Serial.println(" cm");
    }
  }

  if (cmDist <= 5) {
    myDFPlayer.play(2); // Horn!!!
    delay(1500);
    myDFPlayer.play(2); // Horn!!!
    delay(1500);
    myDFPlayer.play(2); // Horn!!!
    delay(1500);
    myDFPlayer.play(2); // Horn!!!
    delay(1500);
  }
  delay(1000);
}