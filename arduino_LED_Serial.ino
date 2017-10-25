#define portaLed 13
#define portaLed2 8

void setup() {
  Serial.begin(9600);
  pinMode(portaLed,OUTPUT);
  pinMode(portaLed2,OUTPUT);
}

void loop() {
  char valor_recebido ='0';

  while(Serial.available() > 0 ){ 
    valor_recebido = Serial.read();

    if(valor_recebido == '1'){
      digitalWrite(portaLed,HIGH);
    }
    else if(valor_recebido == '2'){
      digitalWrite(portaLed,LOW);
    }
    else if(valor_recebido == '3'){
      digitalWrite(portaLed2,HIGH);
    }
    else if(valor_recebido == '4'){
      digitalWrite(portaLed2,LOW);
    }

    else if(valor_recebido == '5'){
      digitalWrite(portaLed,HIGH);
      digitalWrite(portaLed2,HIGH);
    }
    else if(valor_recebido == '6'){
      digitalWrite(portaLed,LOW);
      digitalWrite(portaLed2,LOW);
    }
    
  }
}
