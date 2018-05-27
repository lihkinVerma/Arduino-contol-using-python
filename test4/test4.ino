int led1=11;
int led2=10;
int led3=9;
int led4=8;
char mydata=0;

void setup() {
  // put your setup code here, to run once:
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
  pinMode(led4,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  mydata=int(Serial.read());
  
  if(mydata=='1')
    digitalWrite(led1,HIGH);
    if(mydata=='2')
     digitalWrite(led2,HIGH);
     if(mydata=='3')
      digitalWrite(led3,HIGH);
      if(mydata=='4')
      digitalWrite(led4,HIGH);
      if(mydata=='0'){
        digitalWrite(led1,LOW);
        digitalWrite(led2,LOW);
        digitalWrite(led3,LOW);
        digitalWrite(led4,LOW);}
    }
