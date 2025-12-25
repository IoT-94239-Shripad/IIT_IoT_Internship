int gasPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int gasValue = analogRead(gasPin);
  Serial.print("Gas Level: ");
  Serial.println(gasValue);

  if (gasValue > 400) {
    Serial.println(" Gas / Smoke Detected");
  }

  delay(1000);
}
