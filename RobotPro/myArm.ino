#include "pindef.h"
#include "command.h"
#include <AccelStepper.h>
#include <Arduino.h>
#include "util.h"
#include "capture.h"
#include "queue.h"
Queue<struct Cmd> queue(15); // 存储 15 个命令，方便处理多个运动指令
Command command;      // 表示当前正在处理的命令
// 创建Z轴AccelStepper对象，设置电机类型为全步模式（可根据实际电机情况修改）
AccelStepper base_stepper(AccelStepper::DRIVER, BASE_STEP_PIN, BASE_DIR_PIN);

// 创建Y轴AccelStepper对象，设置电机类型为全步模式（可根据实际电机情况修改）
AccelStepper big_arm_stepper(AccelStepper::DRIVER, BIGARM_STEP_PIN, BIGARM_DIR_PIN);

// 创建X轴AccelStepper对象，设置电机类型为全步模式（可根据实际电机情况修改）
AccelStepper small_arm_stepper(AccelStepper::DRIVER, SMALLARM_STEP_PIN, SMALLARM_DIR_PIN);

Capture capture(CAPTURER_PIN);

bool prossingTask;

float currentX=0.0f,currentY=32.6f,currentZ=23.0f;

void setup()
{
    Serial.begin(9600);
    prossingTask=false;
    base_stepper.setAcceleration(10000);
    base_stepper.setMaxSpeed(10000);
    base_stepper.setSpeed(10000);
    big_arm_stepper.setAcceleration(10000);
    big_arm_stepper.setMaxSpeed(10000);
    big_arm_stepper.setSpeed(10000);
    small_arm_stepper.setAcceleration(10000);
    small_arm_stepper.setMaxSpeed(10000);
    small_arm_stepper.setSpeed(10000);

    Serial.println("系统启动");
    
}

void loop()
{
    if (!queue.isFull()) //目前queue不起作用，没有多线程，运动也没拆分为多段
    {
        if (command.handleGcode())
        {
            queue.push(command.getCmd());
            printOk();
        }
    }
    if ((!queue.isEmpty())&&!prossingTask)
    {
        executeCommand(queue.pop());
    }
}

void handleAsErr(struct Cmd&cmd)
{
    printComment("Unknown Cmd " + String(cmd.id) + String(cmd.num) + " (queued)");
}

void moveTo(struct Cmd&cmd){
    
    float basePulse,bigArmPulse,smallArmPulse;
    pointToPulse(cmd.valueX,cmd.valueY,cmd.valueZ,basePulse,bigArmPulse,smallArmPulse,CURCLE_PULSE/360);
    
    base_stepper.moveTo(round(basePulse));
    big_arm_stepper.moveTo(round(bigArmPulse));
    small_arm_stepper.moveTo(round(smallArmPulse));
    while ((base_stepper.distanceToGo()!= 0 || big_arm_stepper.distanceToGo()!= 0 || small_arm_stepper.distanceToGo()!= 0)) {
        base_stepper.run();
        big_arm_stepper.run();
        small_arm_stepper.run();
    }
    currentX=cmd.valueX;
    
    currentY=cmd.valueY;
    currentZ=cmd.valueZ;

}
void moveTo(float x,float y,float z){
    Serial.println("移动到：");Serial.println(x);Serial.println(y);Serial.println(z);
    float basePulse,bigArmPulse,smallArmPulse;
    pointToPulse(x,y,z,basePulse,bigArmPulse,smallArmPulse,CURCLE_PULSE/360);
    
    base_stepper.moveTo(round(basePulse));
    big_arm_stepper.moveTo(round(bigArmPulse));
    small_arm_stepper.moveTo(round(smallArmPulse));
    while ((base_stepper.distanceToGo()!= 0 || big_arm_stepper.distanceToGo()!= 0 || small_arm_stepper.distanceToGo()!= 0)) {
       small_arm_stepper.run();
        base_stepper.run();
        big_arm_stepper.run();
        
    }
    currentX=x;
    currentY=y;
    currentZ=z;
    

}
void moveToCatch(struct Cmd&cmd){

    float basePulse,bigArmPulse,smallArmPulse;
    pointToPulse(cmd.valueX,cmd.valueY,cmd.valueZ,basePulse,bigArmPulse,smallArmPulse,CURCLE_PULSE/360);
    
    base_stepper.moveTo(round(basePulse));
    big_arm_stepper.moveTo(round(bigArmPulse));
    small_arm_stepper.moveTo(round(smallArmPulse));
    while ((base_stepper.distanceToGo()!= 0 || big_arm_stepper.distanceToGo()!= 0 || small_arm_stepper.distanceToGo()!= 0)) {
        base_stepper.run();
        big_arm_stepper.run();
        small_arm_stepper.run();
        
    }
    currentX=cmd.valueX;
    currentY=cmd.valueY;
    currentZ=cmd.valueZ;
    capture.putUp();
}
void moveBackDown(struct Cmd&cmd){

    float basePulse,bigArmPulse,smallArmPulse;
    pointToPulse(cmd.valueC,cmd.valueD,cmd.valueE,basePulse,bigArmPulse,smallArmPulse,CURCLE_PULSE/360);
    base_stepper.moveTo(round(basePulse));
    big_arm_stepper.moveTo(round(bigArmPulse));
    small_arm_stepper.moveTo(round(smallArmPulse));
    while ((base_stepper.distanceToGo()!= 0 || big_arm_stepper.distanceToGo()!= 0 || small_arm_stepper.distanceToGo()!= 0)) {
        base_stepper.run();
        big_arm_stepper.run();
        small_arm_stepper.run();
         
    }
    currentX=cmd.valueC;
    currentY=cmd.valueD;
    currentZ=cmd.valueE;
    capture.putDown();
}
void catchAndPut(struct Cmd&cmd){
    //当前位置高于目标位置，先转 ； 当前位置低于目标位置，后转

    if(!(currentZ>cmd.valueZ))moveTo(currentX,currentY,cmd.valueZ+5.0f); //当前位置小于等于目标位置
    else moveTo(cmd.valueX,cmd.valueY,currentZ);
    
    moveToCatch(cmd);
    delay(200);
    
    if(!(currentZ>cmd.valueE))moveTo(currentX,currentY,cmd.valueE+5.0f); //当前位置小于等于目标位置
    else moveTo(cmd.valueC,cmd.valueD,currentZ); //
    

    moveBackDown(cmd);

}
void executeCommand(struct Cmd cmd){
    if (cmd.id == 'G')
    {
        switch (cmd.num)
        {
        case 0: 
            break;
        case 1:
            break;
        case 2:
            break;
        
        default:
            handleAsErr(cmd);
        }
    }
    else if (cmd.id == 'M')
    {
        switch (cmd.num)
        {
        case 0: //复位所有电机
             // 先复位Y轴电机
            Serial.println("复位开始");
            reset(BIGARM_DIR_PIN,BIGARM_STEP_PIN,BIGARM_LIMIT_PIN,1);
            runAngel(BIGARM_DIR_PIN,BIGARM_STEP_PIN,0,7);

            reset(SMALLARM_DIR_PIN,SMALLARM_STEP_PIN,SMALLARM_LIMIT,0);
            runAngel(SMALLARM_DIR_PIN,SMALLARM_STEP_PIN,1,34);
            currentX=0.0f;
            currentY=33.0f;
            currentZ=23.0f;
            base_stepper.setCurrentPosition(0);
            small_arm_stepper.setCurrentPosition(0);

            big_arm_stepper.setCurrentPosition(0);

            // reset(BASE_DIR_PIN,BASE_STEP_PIN,BASE_LIMIT_PIN,1);
            Serial.println("复位结束");
            break;
        case 1:
            // moveBase(cmd);
            break;
        case 2:
            // moveBigArm(cmd);
            break;
        case 3:
            
            break;
        case 4:
            moveTo(cmd);
            break;
        case 5:
            capture.putUp();
            break;
        case 6:
            capture.putDown();
            break;
        case 7:
            moveToCatch(cmd);
            break;
        case 8:
            moveBackDown(cmd);
            break;
        case 9:
            catchAndPut(cmd);
            break;
        default:
            handleAsErr(cmd);
        }
    }
    else
    {
        handleAsErr(cmd);
    }

}