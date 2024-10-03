#include <WiFi.h>
#include <HTTPClient.h>

// Declaracion de los pines
#define PinLM35 35
#define PinHL69 34

// Variables que se usaran

#define VOLTAJE 5000.0
#define BITS 4096.0

int SensorValueLM35;
float miliVolt;
float TEMPERATURA;
int SensorValueHL69;
float HUMEDAD;

const char* ssid = "TeleCentro-75ce";
const char* password = "GNKJMWMWNZQJ";

const char* id = "ML16";

void setup() {
  delay(10);
  Serial.begin(115200);

  pinMode(PinLM35, INPUT);
  pinMode(PinHL69, INPUT);

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
  SensorValueLM35 = analogRead(PinLM35);
  miliVolt = SensorValueLM35 * (VOLTAJE / BITS);
  TEMPERATURA = miliVolt / 10;
  Serial.println(TEMPERATURA, 1);

// Programacion del HL-69
  SensorValueHL69 = analogRead(PinHL69);
  HUMEDAD = map(SensorValueHL69, 4095, 0, 0, 100);
  Serial.println(HUMEDAD, 0);

// Programacion del WiFi
  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;
    String datosPOST = "?idProducto="+ String(id) +"&Temperatura=" + (String(TEMPERATURA, 1) + " C°") + "&Humedad=" + (String(HUMEDAD, 0) + "%");

    http.begin("sql10.freemysqlhosting.net");
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

      Serial.print("ERROR, codigo: ");
      Serial.println(codigoRepuesta);

    }

    http.end();

  } else {

    Serial.println("Error en la conexion WIFI");

  }

  delay(900000);

}