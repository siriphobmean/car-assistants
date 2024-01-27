int sensor_value;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensor_value = random(10, 20);
  Serial.println(sensor_value);
  delay(1000);
}