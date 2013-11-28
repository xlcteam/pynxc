#define ULTRASONIC 1
#define EYES 1
#define LIGHT 2
#define SOUND 3
#define MIC 3
#define TOUCH 4
#define COMPASS 5

#define None 0


int SensorTypes[]={0,0,0,0};

inline int SensorVal(int s_) {

    s_=s_-1;
    int t_ = SensorTypes[s_];

    if (t_==None) {
        return -1;
    } else if (t_==ULTRASONIC) {
        Wait(100);
        return SensorUS(s_);
    } else if (t_ == COMPASS) {
        return SensorHTCompass(s_);
    } else {
        return Sensor(s_);
    }

}

void DefineSensors(int s1,int s2,int s3,int s4) {

    int sa[];
    int i;

    ArrayInit(sa,0,4);
    sa[0]=s1;
    sa[1]=s2;
    sa[2]=s3;
    sa[3]=s4;

    for (i=0; i<4; i++) {

        if (sa[i]==None) {
            SensorTypes[i]=None;
        } else if (sa[i]==ULTRASONIC) {
            SetSensorLowspeed(i);
            SensorTypes[i]=ULTRASONIC;
        } else if (sa[i]==LIGHT) {
            SetSensorLight(i);
            SensorTypes[i]=LIGHT;
        } else if (sa[i]==SOUND) {
            SetSensorSound(i);
            SensorTypes[i]=SOUND;
        } else if (sa[i]==TOUCH) {
            SetSensor(i,SENSOR_TOUCH);
            SensorTypes[i]=TOUCH;
        } else if (sa[i] == COMPASS) {
            SetSensorLowspeed(i);
            SensorTypes[i] = COMPASS;
        }
    }
}

void set_sensor(int port, int type)
{
    SensorTypes[port] = type;
    DefineSensors(SensorTypes[0], SensorTypes[1], SensorTypes[2], SensorTypes[3]);
}

#define set_sensors(s1, s2, s3, s4) DefineSensors(s1, s2, s3, s4)
#define sensor(port) SensorVal(port)

#define lcd_clear ClearScreen
#define lcd_reset ResetScreen

#define on_fwd OnFwd
#define on_rev OnRev
#define rotate_motor RotateMotor

#define random Random

#define wait Wait

// The value '6' means OUT_ABC which was not used for performance reasons.
inline int off(int port = 6)
{
    return Off(port);
}


int _cur_lcd_line = 1;
int _line_position = 0;
void lcd_print(string text)
{
    string character;
    int char_pos = 0;

    for(int i = 0; i < StrLen(text); i++){
        character = SubStr(text, i, 1);

        if (SubStr(text, i, 1) == "\n"){
            _cur_lcd_line++;
            char_pos = 0;
            continue;
        }

        if(_cur_lcd_line == 8){
            ClearScreen();
            _cur_lcd_line = 1;
        }

        _line_position = 64 - _cur_lcd_line * 8;
        TextOut(char_pos*8, _line_position, character);       
        char_pos++;

        if (i == StrLen(text)){
            _cur_lcd_line = 1;
        }
    }
}


