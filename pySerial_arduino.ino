#include <Joystick.h> // Khai báo thư viện Joystick 

const int button1Pin = 2; // Khai báo chân button 1
const int button2Pin = 3; // Khai báo chân button 2
const int button3Pin = 4; // Khai báo chân button 3
const int button4Pin = 5; // Khai báo chân button 4
const int joystick_button = 6; // Khai báo chân digital của Joystick
const int x_pin = A0; // Khai báo chân analog của Jostick
const int y_pin = A1; // Khai báo chân analog của Joystick
const int led = 13; // Khai báo chân led

bool joystickPressed = false; // Khi chưa ấn nút thì joystick về false
bool buttonPressed = false; // Khi chưa ấn nút thì button về false

void setup() {
  pinMode(led, OUTPUT); // Cài đặt chân led là OUTPUT
  Serial.begin(9600); // Khởi động Serial với baudrate 9600
  pinMode(x_pin, INPUT); // Cài đặt chân x_pin là INPUT
  pinMode(y_pin, INPUT); // Cài đặt chân y_pin là INPUT
  pinMode(button1Pin, INPUT); // Cài đặt chân button1Pin là INPUT
  pinMode(button2Pin, INPUT); // Cài đặt chân button2Pin là INPUT
  pinMode(button3Pin, INPUT); // Cài đặt chân button3Pin là INPUT
  pinMode(button4Pin, INPUT); // Cài đặt chân button4Pin là INPUT
  pinMode(joystick_button, INPUT_PULLUP); // Cài đặt chân joystick_button là INPUT_PULLUP
}

void loop() {
  int button1State = digitalRead(button1Pin); // Đọc trạng thái của button 1
  int button2State = digitalRead(button2Pin); // Đọc trạng thái của button 2
  int button3State = digitalRead(button3Pin); // Đọc trạng thái của button 3
  int button4State = digitalRead(button4Pin); // Đọc trạng thái của button 4
  int x = analogRead(A0); // Đọc giá trị analog từ chân A0
  int y = analogRead(A1); // Đọc giá trị analog từ chân A1
  int joystickState = digitalRead(joystick_button); // Đọc trạng thái của nút joystick

  // Dữ liệu Joystick
  if (Serial.available()) { // Kiểm tra xem có dữ liệu đến từ cổng nối tiếp không
    char ch = Serial.read(); // Đọc tín hiệu từ cổng nối tiếp
    if (ch == '0') { // Nếu tín hiệu là '0'
      digitalWrite(led, LOW); // Tắt đèn LED
    } else if (ch == '1') { // Nếu tín hiệu là '1'
      digitalWrite(led, HIGH); // Bật đèn LED
    }
  }
  
  if (x >= 550) { // Nếu giá trị x lớn hơn hoặc bằng 550
    Serial.println("UP"); // In ra "UP"
  }
  if (x <= 100) { // Nếu giá trị x nhỏ hơn hoặc bằng 100
    Serial.println("DOWN"); // In ra "DOWN"
  }
  if (y >= 550) { // Nếu giá trị y lớn hơn hoặc bằng 550
    Serial.println("RIGHT"); // In ra "RIGHT"
  }
  if (y <= 100) { // Nếu giá trị y nhỏ hơn hoặc bằng 100
    Serial.println("LEFT"); // In ra "LEFT"
  }
  
  // Dữ liệu nút bấm
  Serial.print("Button 1: "); 
  Serial.println(button1State); // In trạng thái của button 1
  Serial.print("Button 2: "); 
  Serial.println(button2State); // In trạng thái của button 2
  Serial.print("Button 3: "); 
  Serial.println(button3State); // In trạng thái của button 3
  Serial.print("Button 4: "); 
  Serial.println(button4State); // In trạng thái của button 4
  
  // Dữ liệu nút Joystick
  Serial.print("JoystickButton:"); 
  Serial.println(joystickState); // In trạng thái của joystick button

  // Đặt lại trạng thái các nút
  if (joystickPressed && buttonPressed) { 
    joystickPressed = false; 
    buttonPressed = false; 
  }

  delay(500); // Chờ 500ms
}
