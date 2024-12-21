#ifndef UTIL_H_
#define UTIL_H_

void reset(const int dirPin,const int stepPin,const int limitPin,int dirTolimit);

void pointToPulse(float x, float y, float z, float &basePulse, float &bigArmPulse, float &smallArmPulse,float pulsePerAngel );
void runAngel(const int dirPin, const int stepPin, int shunOrni,int angel);
#endif