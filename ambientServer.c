#include <FastLED.h>
#define LED_PIN     9
#define NUM_LEDS    112
#define BRIGHTNESS  21
#define LED_TYPE    WS2812
#define COLOR_ORDER GRB
CRGB leds[NUM_LEDS]; 

char buf1[106];
char buf2[106];
char buf3[64];
char buf4[64];

void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS);
  FastLED.setBrightness(  BRIGHTNESS );

}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    
    int len1 = Serial.readBytesUntil(0xA, buf1, 106);
    int len2 = Serial.readBytesUntil(0xA, buf2, 106);
    int len3 = Serial.readBytesUntil(0xA, buf3, 64);
    int len4 = Serial.readBytesUntil(0xA, buf4, 64);
    int i = 0;
    if(len1 > 0 && len2 > 0 && len3 > 0 && len4 > 0){
     for(int j = 0; j < 105; j++){
      int r = buf1[j++];
      int g = buf1[j++];
      int b = buf1[j++];
      leds[i++] = CRGB(r, g, b);
     }
     for(int j = 0; j < 105; j++){
      int r = buf2[j++];
      int g = buf2[j++];
      int b = buf2[j++];
      leds[i++] = CRGB(r, g, b);
     }
     for(int j = 0; j < 64; j++){
      int r = buf3[j++];
      int g = buf3[j++];
      int b = buf3[j++];
      leds[i++] = CRGB(r, g, b);
     }
     for(int j = 0; j < 64; j++){
      int r = buf4[j++];
      int g = buf4[j++];
      int b = buf4[j++];
      leds[i++] = CRGB(r, g, b);
     }
     FastLED.show();
     delay(40);
       
     
     
    }
                
  }
}
