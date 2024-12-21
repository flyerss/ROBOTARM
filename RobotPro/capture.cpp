#include "capture.h"

// 构造函数的实现
Capture::Capture(int capPin)
{
    this->capPin = capPin;
    pinMode(capPin, OUTPUT);
    capState = false;
}

// 抬起操作函数的实现
void Capture::putUp()
{
    digitalWrite(capPin, HIGH);
    capState = true;
}

// 放下操作函数的实现
void Capture::putDown()
{
    digitalWrite(capPin, LOW);
    capState = false;
}