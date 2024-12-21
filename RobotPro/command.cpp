#include "command.h"

Command::Command()
{
    // initialize Command to a zero-move value;
    command.valueX = NAN;
    command.valueY = NAN;
    command.valueZ = NAN;
    command.valueC = 0;
    command.valueD = 0;
    command.valueE = 0;

    message = "";
}

bool Command::handleGcode()
{
    if (Serial.available())
    {
        char c = Serial.read();
        Serial.print(c);
        if (c == '\n')
        {
            return false;
        }
        if (c == '\r')
        { // 处理字符串，一条完整的命令已经接收完毕，去处理接收完毕的message
            bool b = processMessage(message);
            message = "";
            return b;
        }
        else
        {
            message += c; // 一个一个读取字符直到换行符
        }
    }
    return false;
}
// msg = "G1 X10.0 Y20.0"
bool Command::processMessage(String &msg)
{
    msg += ' '; // 最后一位加空格，以便pos找到总长度
    msg.toUpperCase();
    command.id = msg[0];
    // exit if not GCode
    if ((command.id != 'G') && (command.id != 'M'))
    {
        printErr();
        return false;
    }
    // parse number
    int first = 1;
    int last = pos(msg, ' ', 1);
    if (last < 0) // 没找到空格
    {
        printErr();
        return false;
    }
    String s = msg.substring(first, last);
    command.num = s.toInt();
    // Serial.println(cmd.num);

    // parse up to 5 Values
    command.valueX = NAN;
    command.valueY = NAN;
    command.valueZ = NAN;
    command.valueC = 0;
    command.valueD = 0;
    command.valueE = 0;
    int parsePosition = last + 1; //开始解析X,Y,Z,C位置 第一个命令种类和第二个命令编码已经解析完毕了，后面可以出错
    int i = 0;
    while (i < 6)
    {
        char id = msg[parsePosition++]; // id是命令编号
        if (id != ' ')
        { // test if a command here
            int first = parsePosition;
            int last = pos(msg, ' ', parsePosition);
            if (last < first)
            { 
                i = 6;
            }
            else
            {
                String floatString = msg.substring(first, last);
                float value = floatString.toFloat();
                switch (id)
                {
                case 'X':
                    command.valueX = value;
                    break;
                case 'Y':
                    command.valueY = value;
                    break;
                case 'Z':
                    command.valueZ = value;
                    break;
                case 'C':
                    // command.valueC = static_cast<int>(value);
                    command.valueC=value;
                    break;
                case 'D':
                    command.valueD = value;
                    break;
                case 'E':
                    command.valueE = value;
                    break;
                default:
                    i = 6; // 遇到不支持格式字符
                }
                parsePosition = last + 1; //去下一个
            }
        }
        else
        {
            i = 6; // 结束
        }
        i++;
    }

    return true;
}

int Command::pos(String &s, char c, int start)
{
    int len = s.length();
    for (int i = start; i < len; i++)
    {
        if (c == s[i])
        {
            return i;
        }
    }
    return -1;
}

Cmd Command::getCmd() const
{
    return command;
}

void printErr()
{
    Serial.println("commanderror"); //'resend'
}



void printComment(char *c)
{
    Serial.print("// ");
    Serial.println(c);
}

void printComment(String &s)
{
    Serial.print("// ");
    Serial.println(s);
}

void printOk()
{
    Serial.println("ok");
}
