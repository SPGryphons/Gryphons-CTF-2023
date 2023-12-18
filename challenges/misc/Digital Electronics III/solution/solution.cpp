#include<Arduino.h>

int srClock1 = 12;
int rClock1 = 13;
int data1 = 2;

void updateShiftRegister(unsigned int value)
{
   digitalWrite(rClock1, LOW);
   digitalWrite(srClock1, LOW);
   Serial.println("write val" + String(value));
   shiftOut(data1, srClock1, LSBFIRST, value);
   digitalWrite(rClock1, HIGH);
}


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
  // 0b10 -> 1
  // 0b00 -> 0
  // PGT. So we switch to 0 first.
  // 10011101

  digitalWrite(10, 1);
    digitalWrite(10, 0);



  for (uint16_t i=0; i<=0b011110110101; i++) {
    updateShiftRegister(0b00);

    updateShiftRegister(0b10);
    Serial.println(i,BIN);
  }

  Serial.println("Setup complete.");
}

void loop() {
}

