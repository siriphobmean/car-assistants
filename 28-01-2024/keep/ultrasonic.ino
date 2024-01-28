#include <SoftwareSerial.h>

const int US100_TX = 2;
const int US100_RX = 3;

SoftwareSerial puertoUS100(US100_RX, US100_TX);

unsigned int MSByteDist = 0;
unsigned int LSByteDist = 0;
unsigned int cmDist = 0;  // ปรับให้เป็น cm

void setup() {
    Serial.begin(9600);
    puertoUS100.begin(9600);
}

void loop() {
    puertoUS100.flush();
    puertoUS100.write(0x55);
    delay(500);

    if(puertoUS100.available() >= 2) {
        MSByteDist = puertoUS100.read();
        LSByteDist  = puertoUS100.read();
        cmDist  = (MSByteDist * 256 + LSByteDist) / 10;  // แปลงเป็น cm

        if((cmDist > 0) && (cmDist < 1000)) {
            Serial.print("Distancia: ");
            Serial.print(cmDist, DEC);
            Serial.println(" cm");
        }
    }

    delay(500);
}
