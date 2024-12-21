#ifndef CAPTURE_H
#define CAPTURE_H

#include <Arduino.h>

class Capture
{
private:
    bool capState;
    int capPin;

public:
    Capture(int capPin);
    void putUp();
    void putDown();
};

#endif