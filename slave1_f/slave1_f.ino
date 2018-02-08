String buffer;
long timing;
long startTime;
float yaw,roll,pitch;

void setup() {
  
  startTime = millis();
  Serial.begin(115200);
  
}

String formatPrefixZero(String* number, int width);

void loop() { // run over and over
  
  yaw = 180.00;
  roll = -100.05;
  pitch = 30.02;
  timing = millis() - startTime;
  buffer = "#1" + formatPrefixZero(&String(timing,HEX), 6) + formatPrefixZero(&String((int)(yaw*100)+18000,HEX), 4) + 
          formatPrefixZero(&String((int)(roll*100)+18000,HEX), 4) + formatPrefixZero(&String((int)(pitch*100)+18000,HEX), 4) + "$";
  Serial.println(buffer);
  
}

String formatPrefixZero(String* number, int width) {
  number->toUpperCase();
  int i= width-number->length();
  if(i>0){
    while(i>0){
      *number="0"+*number;
      i--;
    }
  }
  return *number;
  
}
