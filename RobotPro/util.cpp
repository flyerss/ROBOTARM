#include "util.h"
#include <AccelStepper.h>
#include <Arduino.h>
#include "pindef.h"
void reset(const int dirPin, const int stepPin, const int limitPin, int dirTolimit)
{

    pinMode(BASE_DIR_PIN, OUTPUT);
    pinMode(BIGARM_DIR_PIN, OUTPUT);
    pinMode(SMALLARM_DIR_PIN, OUTPUT);

    pinMode(SMALLARM_LIMIT, INPUT);
    pinMode(BIGARM_LIMIT_PIN, INPUT);
    pinMode(BASE_LIMIT_PIN, INPUT);
    digitalWrite(dirPin, dirTolimit == 1 ? HIGH : LOW);

    while (1)
    {
        

        digitalWrite(stepPin, HIGH);
        delayMicroseconds(2);
        digitalWrite(stepPin, LOW);
        delay(2);
        if (digitalRead(limitPin) == HIGH)
            break;
    }
}
const float bigArmLength = 21.9f;
const float smallArmLength = 21.0f;
const float armCompensation = 6.0f;
const float baseCompensation = 5.6f;
const float baseHeight = 7.2f;
const float heightCompensation = 6.1f;
const float putUpCompensation = 0.2f;

// 函数定义，实现计算角度的逻辑，对应Python中的computeAngel函数
void pointToPulse(float x, float y, float z, float &basePulse, float &bigArmPulse, float &smallArmPulse, float pulsePerAngel)
{
    z += heightCompensation;
    // z = z + y * 0.1;
    // x = x * (1.16 - y * 0.01);
    float baseAngle, bigArmAngle, smallArmAngle;
    baseAngle = (y != 0) ? (atan(x / y)+atan(putUpCompensation / sqrt(x * x + y * y))) * (180.0f / 3.14159265358979323846f) : 90.0f;

    float verticalProjection = sqrt(x * x + y * y) - armCompensation - baseCompensation;
    float shortSide = fabs(baseHeight - z);
    float hypotenuse = sqrt(shortSide * shortSide + verticalProjection * verticalProjection);

    float bigArmAngle1 = acos((bigArmLength * bigArmLength + hypotenuse * hypotenuse - smallArmLength * smallArmLength) / (2 * bigArmLength * hypotenuse));
    float bigArmAngle2; 
    if (baseHeight == z)
    {
        bigArmAngle2 = 0.0f;
    }
    else if (baseHeight > z)
    {
        bigArmAngle2 = atan(verticalProjection / shortSide) - 1.57079632679489661923f;
    }
    else
    {
        bigArmAngle2 = atan(shortSide / verticalProjection);
    }
    bigArmAngle = (bigArmAngle1 + bigArmAngle2);
    smallArmAngle = (acos((bigArmLength * bigArmLength + smallArmLength * smallArmLength - hypotenuse * hypotenuse) / (2 * bigArmLength * smallArmLength)) + bigArmAngle - 1.57079632679489661923f);
    baseAngle = baseAngle;
    bigArmAngle = 90.0f - bigArmAngle * (180.0f / 3.14159265358979323846f);
    smallArmAngle = 90.0f - smallArmAngle * (180.0f / 3.14159265358979323846f);

    // 小臂向上计算出的角度是负数 ， 向上是反转负脉冲，可直接转换为脉冲数
    smallArmPulse = pulsePerAngel * smallArmAngle;
    // 大臂向前计算出的角度是正数，但是向前是反转负脉冲，所以需要求想反数
    bigArmPulse = -(bigArmAngle * pulsePerAngel);
    // 同理底座向右计算出的角度是正数，为反转负脉冲，同样需要求相反数
    basePulse = -(baseAngle * pulsePerAngel);
}

void runAngel(const int dirPin, const int stepPin, int shunOrni,int angel) {
    long numPulses=(CURCLE_PULSE/360)*angel;
    digitalWrite(dirPin, shunOrni == 1? HIGH : LOW);  //0为逆时针，1为顺时针
    for (int i = 0; i < numPulses; i++) {
       

        digitalWrite(stepPin, HIGH);
        delayMicroseconds(5);
        digitalWrite(stepPin, LOW);
        delay(5);
    }
}