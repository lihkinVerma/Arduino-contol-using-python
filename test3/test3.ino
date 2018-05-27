int led1=13;
int led2=11;
int led3=9;
char mydata=0;

void setup() {
  // put your setup code here, to run once:
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
   pinMode(led3,OUTPUT);
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

  if(mydata=='0')
    digitalWrite(led1,LOW);
}
