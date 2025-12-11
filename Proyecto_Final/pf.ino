#define BLYNK_TEMPLATE_ID "TMPL2hcN1ddQy"
#define BLYNK_TEMPLATE_NAME "CERRADURA"
#define BLYNK_AUTH_TOKEN "HRieeqcj4uz-4okmqpdxun6heqajRfDy"

#include <WiFi.h>
#include <BlynkSimpleEsp32.h>
#include <ESP32Servo.h>
#include "FS.h"
#include "SPIFFS.h"
#include <time.h>

Servo servoMotor;
int servoPin = 4;

const char* correctPassword = "1234";  // CONTRASEÑA
String inputPass = "";


// FUNCION PARA GUARDAR EVENTOS EN CSV
void logEvent(String eventType) {
  if (!SPIFFS.exists("/registro.csv")) {
    File file = SPIFFS.open("/registro.csv", FILE_WRITE);
    file.println("DATE, TIME, EVENT");
    file.close();
  }

  // Obtener fecha y hora del ESP32
  struct tm timeinfo;
  getLocalTime(&timeinfo);

  char dateStr[20], timeStr[20];
  strftime(dateStr, sizeof(dateStr), "%Y-%m-%d", &timeinfo);
  strftime(timeStr, sizeof(timeStr), "%H:%M:%S", &timeinfo);

  // Guardar línea nueva
  File file = SPIFFS.open("/registro.csv", FILE_APPEND);
  file.printf("%s, %s, %s\n", dateStr, timeStr, eventType.c_str());
  file.close();
}

// ABRIR PUERTA (servidor => ESP32)
void abrirPuerta() {
  servoMotor.write(0);
  logEvent("OPEN");
}

// CERRAR PUERTA
void cerrarPuerta() {
  servoMotor.write(90);
  logEvent("CLOSE");
}

// BLYNK TEXT INPUT (contraseña)
BLYNK_WRITE(V0) {
  inputPass = param.asStr();

  if (inputPass == correctPassword) {
    abrirPuerta();
  }
}

// BOTÓN CERRAR
BLYNK_WRITE(V1) {
  int estado = param.asInt();
  if (estado == 1) {
    cerrarPuerta();
  }
}

void setup() {
  Serial.begin(115200);

  // SPIFFS
  SPIFFS.begin(true);

  File file = SPIFFS.open("/registro.csv");
  while (file.available()) {
    Serial.write(file.read());
  }
  file.close();

  // Servo
  servoMotor.attach(servoPin);
  cerrarPuerta(); // inicial

  // Conexión WIFI + Blynk
  Blynk.begin(BLYNK_AUTH_TOKEN, "Toronja", "Girumen2007*");

  // Configurar hora (NTP)
  configTime(-5 * 3600, 0, "pool.ntp.org");
}

void loop() {
  Blynk.run();
}
