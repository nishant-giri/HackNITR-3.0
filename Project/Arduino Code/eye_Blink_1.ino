int pin1 = 2;
int pin2 = 3;
int dt = 500;

void setup()
{
  
pinMode(pin1, INPUT);
pinMode(pin2, INPUT);
Serial.begin(9600);

}
void loop()
{
  
  int ir_data_1 = digitalRead(pin1);
  int ir_data_2 = digitalRead(pin2);

  
  if(ir_data_1 == 0){
     Serial.println(5);
  }
  if(ir_data_2 == 0){
     Serial.println(4);
  }
  
  delay(dt);
  
}
