const int motorPin1 = 8;
const int motorPin2 = 9;
const int motorPin3 = 10;
const int motorPin4 = 11;

const int stepSequence[8][4] = {
  {1, 0, 0, 0},
  {1, 1, 0, 0},
  {0, 1, 0, 0},
  {0, 1, 1, 0},
  {0, 0, 1, 0},
  {0, 0, 1, 1},
  {0, 0, 0, 1},
  {1, 0, 0, 1}
};

const int stepsPerRevolution = 4096;
const int stepsBetweenCaptures = stepsPerRevolution / 100;  // 41 steps

void setup() {
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readString();
    if (command.startsWith("START")) {
      for (int i = 0; i < stepsPerRevolution; i++) {
        takeStep(i % 8);
        delay(100);  // Increased delay to slow down the rotation
        if (i % stepsBetweenCaptures == 0) {
          Serial.println("CAPTURE");
        }
      }
      // Turn off all pins after rotation
      digitalWrite(motorPin1, LOW);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, LOW);
    }
  }
}

void takeStep(int stepIndex) {
  digitalWrite(motorPin1, stepSequence[stepIndex][0]);
  digitalWrite(motorPin2, stepSequence[stepIndex][1]);
  digitalWrite(motorPin3, stepSequence[stepIndex][2]);
  digitalWrite(motorPin4, stepSequence[stepIndex][3]);
}
