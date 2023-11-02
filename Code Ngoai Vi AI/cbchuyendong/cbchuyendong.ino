//define the pins
int Relay = 3;
int PIR = 6;


void setup() {
  //define the Relay pin as output
  pinMode(Relay, OUTPUT);
  //define the sensor pin as input
  pinMode(PIR, INPUT);
  Serial.begin(9600);
}

void loop() {
  //using the digitalRead function we will read the signal of the sensor
  int value = digitalRead(PIR);
  //if its high or if an any object is detected it will activate the Relay Module
  if (value == HIGH){
    digitalWrite(Relay, LOW); //For activating the Relay we will send a LOW as the Relay input pin works inversely.
   Serial.println("co vat");
   delay(1000);
   
  }
  else {
    //digitalWrite(LED, LOW);
    digitalWrite(Relay, HIGH);
     Serial.println("ko co vat");
    delay(1000);
  } 
}
