#define BLYNK_TEMPLATE_ID "TMPL2qPGUdNIw"
#define BLYNK_TEMPLATE_NAME "MOTOR"
#define BLYNK_AUTH_TOKEN "YiwfWWqu5l5kjCbMNNIQ1g-LRSD5DmLf"

#define BLYNK_PRINT Serial
#include <WiFi.h>
#include <BlynkSimpleEsp32.h>

// Pines de dirección al driver (no al motor)
#define IN1 18   // sentido A
#define IN2 19   // sentido B

char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "Giruminito";
char pass[] = "12345678";

void setup() {
  Serial.begin(115200);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);

  Blynk.begin(auth, ssid, pass);
}

void loop() {
  Blynk.run();
}

// V0 → Giro derecha (CW)
BLYNK_WRITE(V0) {
  int val = param.asInt(); // 1=ON, 0=OFF
  if (val) {
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    Serial.println(" Derecha (CW)");
  } else {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    Serial.println(" Stop");
  }
}

// V1 → Giro izquierda (CCW)
BLYNK_WRITE(V1) {
  int val = param.asInt();
  if (val) {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    Serial.println(" Izquierda (CCW)");
  } else {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    Serial.println(" Stop");
  }
}
