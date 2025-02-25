/*

  Simple Apple Detect AI System

*/


void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);
}

void loop() {
  // read the sensor:
  if (Serial.available() > 0) {
    int inByte = Serial.read();
    Serial.write(inByte);

    switch (inByte) {
      case '1':
        digitalWrite(13, HIGH);
        break;

      case '0':
        digitalWrite(13, LOW);
        break;
    }
  }
}
