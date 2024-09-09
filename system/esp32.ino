#include <WiFi.h>
#include <HTTPClient.h>

// Declaracion de los pines
int PinLM35 = 34;
int PinHL69 = 35;

// Variables que se usaran
int SensorLM35;
float TEMPERATURA;
float SensorHL69;
int HUMEDAD;

const char* ssid = "tuki";
const char* password = "00000000";

void setup() {
  delay(10);
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  Serial.print("Conectando");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.print("IP: ");
  Serial.println(WiFi.localIP());

}

void loop() {

// Programacion del LM35
  SensorLM35 = analogRead(PinLM35);
  TEMPERATURA = ((SensorLM35 * 5000.0) / 1023 ) / 10;
  Serial.println(TEMPERATURA);
  delay(2000);

// Programacion del HL-69
  SensorHL69 = analogRead(PinHL69);
  HUMEDAD = map(SensorHL69, 1023, 0, 0, 100);

  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;
    String datosPOST = "Temperatura=" + String(TEMPERATURA, 1) + "&Humedad=" + String(HUMEDAD);

    // http.begin();
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");

    int codigoRepuesta = http.POST(datosPOST);

    if (codigoRepuesta > 0) {

      Serial.println("Codigo HTTP:" + String(codigoRepuesta));
      if (codigoRepuesta == 200) {

        String cuerpoRepuesta = http.getString();
        Serial.println("El servidor respondio:");
        Serial.println(cuerpoRepuesta);

      }

    } else {

      Serial.print("ERROR, codigo:");
      Serial.println(codigoRepuesta);

    }

    http.end()

  } else {

    Serial.println("Error en la conexion WIFI");

  }

  delay(15000);

}