#ifndef COMMAND_H_
#define COMMAND_H_

#include <Arduino.h>

struct Cmd
{
    char id;
    int num;
    float valueX;
    float valueY;
    float valueZ;
    float valueC;
    float valueD;
    float valueE;

};
class Command {
  public:
    Command();
    bool handleGcode();
    bool processMessage(String& msg);
    Cmd getCmd() const;
  private: 
    int pos(String& s, char c, int start = 0);
    String message;
    Cmd command;
};

void printErr();
void printComment(char* c);
void printComment(String& s);
void printOk();












#endif