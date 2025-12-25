// ESP32 LED Blinking Program

#define LED_PIN 2   // Built-in LED pin for most ESP32 boards

void setup() {
  pinMode(LED_PIN, OUTPUT);   // Set LED pin as output
}

void loop() {
  digitalWrite(LED_PIN, HIGH); // LED ON
  delay(1000);                 // wait 1 second

  digitalWrite(LED_PIN, LOW);  // LED OFF
  delay(1000);                 // wait 1 second
}
