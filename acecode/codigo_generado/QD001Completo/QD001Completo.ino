// Generado con los generadores de ACECode 2.2.4 y un adaptador sin interfaz.
// Referencia de verificación; el archivo editable es el proyecto .sb3.
#include <ACB_Buzzer.h>
#include <Arduino.h>
#include <ACB_CAR_ARM.h>
#include <ACB_ESP32Servo.h>
#include "esp_task_wdt.h"
#include <ACB_WIFI.h>
#include <ACB_LineTrack.h>
#include <ACB_Servo.h>
#include <ACB_Ultrasonic.h>
#include <ACB_SingleLED.h>
#include <ACB_IR.h>

int str;
int commandTimeout;
int Speeds;
int Speed;
int message;
int Left_Tra_Value;
int Middle_Tra_Value;
int Right_Tra_Value;
int Black_Line;
int leftDistance;
int middleDistance;
int rightDistance;
int ut_distance;
int length0;
int length1;
int length2;
int length3;
int c;
int M;
int action;
int devic;
int Car_mode;
int Car_value;
int Off_Road;
int slider;
int data;
int IR_activo;
int IR_esperar_stop;
int IR_ultima_orden;
ACB_Buzzer buzzer_33(33);
ACB_CAR_ARM arm_car;
String aceCode_armCarCmd;
ACB_WIFI wifi;
ACB_LineTrack rml;
ACB_Servo servo_25;
ACB_Ultrasonic acb_ir_1314(13,14);
ACB_SingleLED led_2(2);
ACB_SingleLED led_12(12);
ACB_IR acb_ir_4(4);

void Music_a() {
buzzer_33.run(33,262,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,262,0.5);
buzzer_33.run(33,392,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,392,0.5);
buzzer_33.run(33,440,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,440,0.5);
buzzer_33.run(33,392,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,349,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,349,0.5);
buzzer_33.run(33,330,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,330,0.5);
buzzer_33.run(33,294,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,294,0.5);
buzzer_33.run(33,262,0.5);
}

void Music_b() {
buzzer_33.run(33,330,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,330,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,330,1);
delay(0.01 * 1000);
buzzer_33.run(33,330,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,330,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,330,1);
delay(0.01 * 1000);
buzzer_33.run(33,330,0.5);
buzzer_33.run(33,392,0.5);
buzzer_33.run(33,262,0.5);
buzzer_33.run(33,294,0.5);
buzzer_33.run(33,330,1);
}

void Music_c() {
buzzer_33.run(33,262,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,262,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,262,0.5);
buzzer_33.run(33,196,0.5);
buzzer_33.run(33,220,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,220,0.5);
buzzer_33.run(33,196,1);
buzzer_33.run(33,330,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,330,0.5);
buzzer_33.run(33,294,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,294,0.5);
buzzer_33.run(33,262,0.5);
}

void Music_d() {
buzzer_33.run(33,523,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,523,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,523,1);
buzzer_33.run(33,392,1);
buzzer_33.run(33,659,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,659,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,659,1);
buzzer_33.run(33,523,1);
delay(0.01 * 1000);
buzzer_33.run(33,523,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,659,0.5);
delay(0.01 * 1000);
buzzer_33.run(33,784,1);
delay(0.01 * 1000);
buzzer_33.run(33,784,1);
buzzer_33.run(33,698,0.5);
buzzer_33.run(33,659,0.5);
buzzer_33.run(33,587,1);
delay(1 * 1000);
}

void armcarMotorV2_callback() {
  CONTROL_IR();
  if ((IR_activo == 1)) {
    if ((((millis()) - IR_ultima_orden) > 100)) {
      arm_car.Vehicle_Move(0,0);
    }
    return;
  }
  if ((IR_esperar_stop == 1)) {
    arm_car.Vehicle_Move(0,0);
    if ((arm_car.val==60)) {
      IR_esperar_stop = 0;
    }
    return;
  }
  if ((arm_car.val==59)) {
    aceCode_8track_callback();
    return;
  }
  if ((arm_car.val==67)) {
    aceCode_roundTrack_callback();
    return;
  }
  if ((arm_car.val==68)) {
    aceCode_follow_callback();
  }
  if ((arm_car.val==69)) {
    aceCode_avoidance_callback();
  }
  aceCode_led_callback();
  aceCode_buzzer_callback();
  aceCode_move_callback();
}

void armCarLoopMotorTask(void *pvParameters) {
        esp_task_wdt_add(NULL);
        for (;;) {
            arm_car.Carloop();
            esp_task_wdt_reset();
            vTaskDelay(pdMS_TO_TICKS(1));
        }
    }
void setup2() {
wifi.initAP("ESP32-CAR","12345678",1);
rml.setpin(39,36,35);
Black_Line = 2000;
Speeds = 255;
leftDistance = 0;
middleDistance = 0;
rightDistance = 0;
Off_Road = 4000;
}

  void aceCode_avoidance_callback () {
servo_25.run((90));
ut_distance = (acb_ir_1314.getData());
middleDistance = (acb_ir_1314.getData());
if ((middleDistance <= 25)) {
  arm_car.Vehicle_Move(0,0);
  delay(0.5 * 1000);
  servo_25.run((45));
  delay(0.5 * 1000);
  rightDistance = (acb_ir_1314.getData());
  servo_25.run((135));
  delay(0.5 * 1000);
  leftDistance = (acb_ir_1314.getData());
  servo_25.run((90));
  if (((leftDistance < 10) && (rightDistance < 10))) {
    arm_car.Vehicle_Move(92,180);
    delay(1 * 1000);
    arm_car.Vehicle_Move(83,220);
    delay(0.5 * 1000);
  }
  else{
    if ((rightDistance < leftDistance)) {
      arm_car.Vehicle_Move(92,180);
      delay(0.5 * 1000);
      arm_car.Vehicle_Move(83,220);
      delay(0.5 * 1000);
    }
    else{
      if ((leftDistance < rightDistance)) {
        arm_car.Vehicle_Move(92,180);
        delay(0.5 * 1000);
        arm_car.Vehicle_Move(172,220);
        delay(0.5 * 1000);
      }
      else{
        arm_car.Vehicle_Move(92,180);
        delay(0.5 * 1000);
        arm_car.Vehicle_Move(172,220);
        delay(0.5 * 1000);
      }
    }
  }
}
else{
  arm_car.Vehicle_Move(163,150);
}
delay(10);
}

  void aceCode_roundTrack_callback () {
Left_Tra_Value = (rml.read('L'));
Right_Tra_Value = (rml.read('R'));
if (((Left_Tra_Value < Black_Line) && (Right_Tra_Value < Black_Line))) {
  arm_car.Vehicle_Move(163,150);
}
else{
  if (((Left_Tra_Value >= Black_Line) && (Right_Tra_Value < Black_Line))) {
    arm_car.Vehicle_Move(83,120);
    return;
  }
  if (((Left_Tra_Value < Black_Line) && (Right_Tra_Value >= Black_Line))) {
    arm_car.Vehicle_Move(172,120);
    return;
  }
  if (((Left_Tra_Value >= Black_Line) && ((Left_Tra_Value < Off_Road) && ((Right_Tra_Value >= Black_Line) && (Right_Tra_Value < Off_Road))))) {
    arm_car.Vehicle_Move(0,0);
    return;
  }
  if (((Left_Tra_Value >= Off_Road) && (Right_Tra_Value >= Off_Road))) {
    arm_car.Vehicle_Move(0,0);
  }
}
delay(10);
}

  void aceCode_led_callback () {
if ((arm_car.val==83)) {
  led_2.closeLED();
  led_12.closeLED();
}
if ((arm_car.val==82)) {
  led_2.openLED();
  led_12.openLED();
}
  if(arm_car.val==83||arm_car.val==82){
      arm_car.val=3;
  }
delay(10);
}

  void aceCode_follow_callback () {
servo_25.run((90));
ut_distance = (acb_ir_1314.getData());
if ((ut_distance < 15)) {
  arm_car.Vehicle_Move(92,200);
}
else{
  if (((15 <= ut_distance) && (ut_distance <= 20))) {
    arm_car.Vehicle_Move(0,0);
  }
  else{
    if (((20 <= ut_distance) && (ut_distance <= 25))) {
      arm_car.Vehicle_Move(163,(Speeds - 70));
    }
    else{
      if (((25 <= ut_distance) && (ut_distance <= 50))) {
        arm_car.Vehicle_Move(163,220);
      }
      else{
        arm_car.Vehicle_Move(0,0);
      }
    }
  }
}
delay(10);
}

  void aceCode_8track_callback () {
servo_25.run((90));
Left_Tra_Value = (rml.read('L'));
Middle_Tra_Value = (rml.read('M'));
Right_Tra_Value = (rml.read('R'));
if (((Left_Tra_Value >= Black_Line) && ((Middle_Tra_Value >= Black_Line) && (Right_Tra_Value < Black_Line)))) {
  arm_car.Vehicle_Move(163,180);
  return;
}
if (((Left_Tra_Value < Black_Line) && ((Middle_Tra_Value >= Black_Line) && (Right_Tra_Value < Black_Line)))) {
  arm_car.Vehicle_Move(163,200);
  return;
}
if (((Left_Tra_Value < Black_Line) && ((Middle_Tra_Value >= Black_Line) && (Right_Tra_Value >= Black_Line)))) {
  arm_car.Vehicle_Move(163,180);
  return;
}
if (((Left_Tra_Value >= Black_Line) && ((Middle_Tra_Value < Black_Line) && (Right_Tra_Value < Black_Line)))) {
  arm_car.Vehicle_Move(83,220);
  return;
}
if (((Left_Tra_Value < Black_Line) && ((Middle_Tra_Value < Black_Line) && (Right_Tra_Value >= Black_Line)))) {
  arm_car.Vehicle_Move(172,220);
  return;
}
if (((Left_Tra_Value >= Off_Road) && ((Middle_Tra_Value >= Off_Road) && (Right_Tra_Value >= Off_Road)))) {
  delay(5);
  arm_car.Vehicle_Move(0,0);
}
delay(10);
}

  void aceCode_move_callback () {
if ((arm_car.val==63)) {
  arm_car.Vehicle_Move(163,Speeds);
}
if ((arm_car.val==65)) {
  arm_car.Vehicle_Move(92,Speeds);
}
if ((arm_car.val==61)) {
  arm_car.Vehicle_Move(106,Speeds);
}
if ((arm_car.val==62)) {
  arm_car.Vehicle_Move(149,Speeds);
}
if ((arm_car.val==64)) {
  arm_car.Vehicle_Move(83,Speeds);
}
if ((arm_car.val==66)) {
  arm_car.Vehicle_Move(172,Speeds);
}
if ((arm_car.val==60)) {
  arm_car.Vehicle_Move(0,0);
}
if ((arm_car.val==58)) {
  if (((arm_car.Car_Speed) == 130)) {
    Speeds = 130;
  }
  if (((arm_car.Car_Speed) == 160)) {
    Speeds = 160;
  }
  if (((arm_car.Car_Speed) == 190)) {
    Speeds = 190;
  }
  if (((arm_car.Car_Speed) == 220)) {
    Speeds = 220;
  }
  if (((arm_car.Car_Speed) == 255)) {
    Speeds = 255;
  }
}
delay(0.01 * 1000);
if ((arm_car.val==74)) {
  arm_car.Vehicle_Move(34,Speeds);
}
if ((arm_car.val==71)) {
  arm_car.Vehicle_Move(72,Speeds);
}
if ((arm_car.val==72)) {
  arm_car.Vehicle_Move(129,Speeds);
}
if ((arm_car.val==73)) {
  arm_car.Vehicle_Move(20,Speeds);
}
delay(10);
}

  void aceCode_buzzer_callback () {
if ((arm_car.val==84)) {
  Music_a();
}
if ((arm_car.val==85)) {
  Music_b();
}
if ((arm_car.val==86)) {
  Music_c();
}
if ((arm_car.val==87)) {
  Music_d();
}
delay(10);
}

void CONTROL_IR() {
if ((acb_ir_4.callback_data(11))) {
  arm_car.Vehicle_Move(0,0);
  IR_activo = 0;
  IR_esperar_stop = 1;
  return;
}
if ((acb_ir_4.callback_data(16))) {
  arm_car.Vehicle_Move(0,0);
  IR_activo = 1;
  IR_ultima_orden = (millis());
  return;
}
if ((acb_ir_4.callback_data(12))) {
  IR_activo = 1;
  IR_ultima_orden = (millis());
  arm_car.Vehicle_Move(163,255);
}
if ((acb_ir_4.callback_data(13))) {
  IR_activo = 1;
  IR_ultima_orden = (millis());
  arm_car.Vehicle_Move(92,255);
}
if ((acb_ir_4.callback_data(14))) {
  IR_activo = 1;
  IR_ultima_orden = (millis());
  arm_car.Vehicle_Move(83,255);
}
if ((acb_ir_4.callback_data(15))) {
  IR_activo = 1;
  IR_ultima_orden = (millis());
  arm_car.Vehicle_Move(172,255);
}
if ((acb_ir_4.callback_data(1))) {
  IR_activo = 1;
  IR_ultima_orden = (millis());
  arm_car.Vehicle_Move(106,255);
}
if ((acb_ir_4.callback_data(3))) {
  IR_activo = 1;
  IR_ultima_orden = (millis());
  arm_car.Vehicle_Move(149,255);
}
if ((acb_ir_4.callback_data(4))) {
  IR_activo = 1;
  IR_ultima_orden = (millis());
  arm_car.Vehicle_Move(34,255);
}
if ((acb_ir_4.callback_data(6))) {
  IR_activo = 1;
  IR_ultima_orden = (millis());
  arm_car.Vehicle_Move(129,255);
}
if ((acb_ir_4.callback_data(7))) {
  IR_activo = 1;
  IR_ultima_orden = (millis());
  arm_car.Vehicle_Move(72,255);
}
if ((acb_ir_4.callback_data(9))) {
  IR_activo = 1;
  IR_ultima_orden = (millis());
  arm_car.Vehicle_Move(20,255);
}
}

void setup() {
arm_car.Car_init(2);
servo_25.allocateTimer(1);
servo_25.setpin(25);
arm_car.Car_init(2);
arm_car.Vehicle_Move(0,0);
IR_activo = 0;
IR_esperar_stop = 0;
IR_ultima_orden = 0;
setup2();
arm_car.startAppServer();
const esp_task_wdt_config_t wdt_config = {10000, 0, true};
esp_task_wdt_reconfigure(&wdt_config);
xTaskCreatePinnedToCore(armCarLoopMotorTask, "MotorTask",20000,NULL,5,NULL,0);
}

void repeat() {
armcarMotorV2_callback();

}
void loop() {repeat();}
