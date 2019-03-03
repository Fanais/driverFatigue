#define VIBE 10

extern int state;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(200);
  Serial.println("<Arduino is ready>");
}

void loop() {
  getSignal();
  replyState();
  if(state == 1){
    analogWrite(VIBE,255);
  } else {
    analogWrite(VIBE,0);
  }
}
