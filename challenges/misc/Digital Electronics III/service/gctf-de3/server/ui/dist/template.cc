#include<Arduino.h>
int srClock1 = 12;
int rClock1 = 13;
int data1 = 2;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  pinMode(srClock1, OUTPUT);
  pinMode(rClock1, OUTPUT);
  pinMode(data1, OUTPUT);

  digitalWrite(rClock1, LOW);      // (11) ST_CP [RCK] on 74HC595
  digitalWrite(srClock1, LOW);      // (9) SH_CP [SCK] on 74HC595
  digitalWrite(data1, LOW);

  pinMode(10, OUTPUT); // Reset Pin

    // Reset the Flip Flops.
  digitalWrite(10, 1);
  digitalWrite(10, 0);



  Serial.println("Setup complete.");
}

void loop() {
  // put your main code here, to run repeatedly:
  // only use this function if absolutely needed.
  // your code should not need to loop and will have a timeout.
 
}
