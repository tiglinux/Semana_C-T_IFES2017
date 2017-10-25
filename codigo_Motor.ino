#define motor1A 7
#define motor1B 8

void setup() {
  pinMode(motor1A,OUTPUT);
  pinMode(motor1B,OUTPUT);
}

void loop() {
  
}

void frente(){
  digitalWrite(motor1A,LOW);
  digitalWrite(motor1B,HIGH);
}

void tras(){
  digitalWrite(motor1A,HIGH);
  digitalWrite(motor1B,LOW);
}

void parar(){
  digitalWrite(motor1A,LOW);
  digitalWrite(motor1B,LOW);
}

