#include"seeed_line_chart.h" //include the library
#include <math.h>
#include "QuickStats.h"

QuickStats stats;
TFT_eSPI tft;



#define max_size 600 //maximum size of data
//doubles data; //Initilising a doubles type to store data
TFT_eSprite spr = TFT_eSprite(&tft);  // Sprite 
int run = 1;
int count = 0;

const int GSR=A1;
int gsrVal=0;
int gsr_average=0;

int datas[max_size];

void setup() {
  // put your setup code here, to run once:
  pinMode(WIO_MIC, INPUT);
  Serial.begin(9600);
  Serial.println("Starting...");
  tft.begin();
  tft.setRotation(3);
}

void loop() {
  // put your main code here, to run repeatedly:
  spr.fillSprite(TFT_DARKGREY);

  //######## MIC VALUE ########
  int val = (int)analogRead(WIO_MIC);

  //######## ECG VALUE ########
  int ecgvalue = analogRead(A0);
  long gsr_sum = 0;
  for (int x=0; x<10;x++) {
    gsrVal=analogRead(GSR);
    gsr_sum += gsrVal;
    delay(5);
  }

  //############ GSR_AVERAGE ##########
  gsr_average = gsr_sum/10;
  
  if (run == 1) {
    delay(50);
    //Serial.println(1);
    datas[count] = val;
    if (count == max_size) {
      run = 0;
    } else {
      count++;
    }
  }
  else {
    count = 0;
    int peaks = 0;
    int summs = 0;

    float devsum = 0;
    for(int i = 0; i < max_size+1; i++) {
      summs += datas[i];
    }

    int means = summs/max_size;
    for(int i = 0; i < max_size+1; i++) {
      devsum += datas[i] - means;
    }
    float stdv = sqrt(sq(devsum)/(max_size-1));
    for(int i = 0; i < max_size+1; i++) {
      if (datas[i] > (means +(stdv*3))) {
        peaks++;
      }
    }

    //print sound!
    //Serial.print("Number of abnormalities:");
    //Serial.println(peaks);
    int datas[max_size];
    run = 1;
  }
  Serial.print("Microphone:");
  Serial.print(val);
  Serial.print(",GSR:");
  Serial.print(gsr_average);
  Serial.print(",ECG:");
  Serial.println(ecgvalue);
}
