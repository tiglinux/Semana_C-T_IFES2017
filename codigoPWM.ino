#define led 9
int brilho = 0;
int x;

void setup() {
  pinMode(led,OUTPUT);
}

void loop() {
  for(int i = 0; i <= 255; i++){
    analogWrite(led,i);
    delay(50);  //Espera 50 ms para a proxima tensão aplicada...0V....1V...2V (cresce gradativamente.)
  }
  
 
  
  for(x = 255;x >= 0; x--){
    analogWrite(led,x);
    delay(50);
  }
  
}
