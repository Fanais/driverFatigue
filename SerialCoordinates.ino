const byte buffSize = 40;
char coordBuffer[buffSize];
const char startMarker = '<';
const char endMarker = '>';
byte bytesRecvd = 0;
boolean readInProgress = false;
boolean newDataFromPC = false;

//char messageFromPC[buffSize] = {0};
int state = 0;

//=============

void getSignal() {

    // receive data from PC and save it into coordBuffer
    
  if(Serial.available() > 0) {

    char x = Serial.read();

      // the order of these IF clauses is significant
      
    if (x == endMarker) {
      readInProgress = false;
      newDataFromPC = true;
      coordBuffer[bytesRecvd] = 0;
      parseSignal();
    }
    
    if(readInProgress) {
      coordBuffer[bytesRecvd] = x;
      bytesRecvd ++;
      if (bytesRecvd == buffSize) {
        bytesRecvd = buffSize - 1;
      }
    }

    if (x == startMarker) { 
      bytesRecvd = 0; 
      readInProgress = true;
    }
  }
}

//=============
 
void parseSignal() {

    // split the data into its parts
    
  char * strtokIndx; // this is used by strtok() as an index
  
  //strtokIndx = strtok(coordBuffer,",");      // get the first part - the string
  //strcpy(messageFromPC, strtokIndx); // copy it to messageFromPC
  
  strtokIndx = strtok(coordBuffer, ","); // this continues where the previous call left off
  state = atoi(coordBuffer);     // convert this part to an integer

}

//=============

void replyState() {

  if (newDataFromPC) {
    newDataFromPC = false;
    Serial.print("<");
    Serial.print(state);
    Serial.println(">");
  }
}
