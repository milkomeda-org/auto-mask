import base64 #line:1
import math #line:2
import sys #line:3
from io import BytesIO #line:4
import numpy as np #line:5
from PIL import Image ,ImageTk #line:6
from tkinter .filedialog import askopenfilename #line:7
import cv2 #line:8
import tkinter as tk #line:9
import tkinter .messagebox #line:10
import PIL #line:11
import dlib #line:12
from flask import request ,Flask ,jsonify #line:13
app =Flask (__name__ )#line:14
detector =dlib .get_frontal_face_detector ()#line:15
predictor =dlib .shape_predictor ('./shape_predictor_68_face_landmarks.dat')#line:16
font =cv2 .FONT_HERSHEY_SIMPLEX #line:17
mask =Image .open ('pic/Mask5.png')#line:18
class AddMask (object ):#line:19
    def __init__ (OO0O00OOO0OOO0OOO ):#line:20
        OO0O00OOO0OOO0OOO .root =tk .Tk ()#line:21
        OO0O00OOO0OOO0OOO .root .title ('一起来带口罩啊')#line:22
        OO0O00OOO0OOO0OOO .root .geometry ('1200x700')#line:23
        OO0O00OOO0OOO0OOO .path1_ =None #line:24
        OO0O00OOO0OOO0OOO .path2_ =None #line:25
        OO0O00OOO0OOO0OOO .seg_img_path =None #line:26
        OO0O00OOO0OOO0OOO .mask =None #line:27
        OO0O00OOO0OOO0OOO .im =None #line:28
        OO0O00OOO0OOO0OOO .label_Img_seg =None #line:29
        OO000000O0000O0OO =tk .Label ()#line:30
        OO000000O0000O0OO .place (x =0 ,y =0 )#line:31
        tk .Button (OO0O00OOO0OOO0OOO .root ,text ="输入人脸",command =OO0O00OOO0OOO0OOO .show_original1_pic ).place (x =270 ,y =40 )#line:32
        tk .Button (OO0O00OOO0OOO0OOO .root ,text ="保存输出",command =OO0O00OOO0OOO0OOO .save_mask_face ).place (x =920 ,y =40 )#line:33
        tk .Label (OO0O00OOO0OOO0OOO .root ,text ="人脸",font =10 ).place (x =280 ,y =120 )#line:34
        OO0O00OOO0OOO0OOO .cv_orinial1 =tk .Canvas (OO0O00OOO0OOO0OOO .root ,bg ='white',width =270 ,height =270 )#line:35
        OO0O00OOO0OOO0OOO .cv_orinial1 .create_rectangle (8 ,8 ,260 ,260 ,width =1 ,outline ='red')#line:36
        OO0O00OOO0OOO0OOO .cv_orinial1 .place (x =180 ,y =150 )#line:37
        OO0O00OOO0OOO0OOO .label_Img_original1 =tk .Label (OO0O00OOO0OOO0OOO .root )#line:38
        OO0O00OOO0OOO0OOO .label_Img_original1 .place (x =180 ,y =150 )#line:39
        tk .Label (OO0O00OOO0OOO0OOO .root ,text ="选择口罩",font =10 ).place (x =600 ,y =120 )#line:40
        O0O00OOOO0000O00O =Image .open ("./pic/Mask.png")#line:41
        O0O00OOOO0000O00O =O0O00OOOO0000O00O .resize ((60 ,60 ),Image .ANTIALIAS )#line:42
        O0O00OOOO0000O00O =ImageTk .PhotoImage (O0O00OOOO0000O00O )#line:43
        OO0O00OOO0OOO0OOO .first =tk .Label (OO0O00OOO0OOO0OOO .root ,image =O0O00OOOO0000O00O )#line:44
        OO0O00OOO0OOO0OOO .first .place (x =600 ,y =160 ,width =60 ,height =60 )#line:45
        OO0O00OOO0OOO0OOO .first .bind ("<Button-1>",OO0O00OOO0OOO0OOO .mask0 )#line:46
        OO000OOO0O0O0OOOO =Image .open ("./pic/Mask1.png")#line:47
        OO000OOO0O0O0OOOO =OO000OOO0O0O0OOOO .resize ((60 ,60 ),Image .ANTIALIAS )#line:48
        OO000OOO0O0O0OOOO =ImageTk .PhotoImage (OO000OOO0O0O0OOOO )#line:49
        OO0O00OOO0OOO0OOO .second_pic =tk .Label (OO0O00OOO0OOO0OOO .root ,image =OO000OOO0O0O0OOOO )#line:50
        OO0O00OOO0OOO0OOO .second_pic .place (x =600 ,y =230 ,width =60 ,height =60 )#line:51
        OO0O00OOO0OOO0OOO .second_pic .bind ("<Button-1>",OO0O00OOO0OOO0OOO .mask1 )#line:52
        OOOOOOO00O00O00O0 =Image .open ("./pic/Mask3.png")#line:53
        OOOOOOO00O00O00O0 =OOOOOOO00O00O00O0 .resize ((60 ,60 ),Image .ANTIALIAS )#line:54
        OOOOOOO00O00O00O0 =ImageTk .PhotoImage (OOOOOOO00O00O00O0 )#line:55
        OO0O00OOO0OOO0OOO .third_pic =tk .Label (OO0O00OOO0OOO0OOO .root ,image =OOOOOOO00O00O00O0 )#line:56
        OO0O00OOO0OOO0OOO .third_pic .place (x =600 ,y =300 ,width =60 ,height =60 )#line:57
        OO0O00OOO0OOO0OOO .third_pic .bind ("<Button-1>",OO0O00OOO0OOO0OOO .mask3 )#line:58
        O00O0O00OO0OO0O00 =Image .open ("./pic/Mask4.png")#line:59
        O00O0O00OO0OO0O00 =O00O0O00OO0OO0O00 .resize ((60 ,60 ),Image .ANTIALIAS )#line:60
        O00O0O00OO0OO0O00 =ImageTk .PhotoImage (O00O0O00OO0OO0O00 )#line:61
        OO0O00OOO0OOO0OOO .forth_pic =tk .Label (OO0O00OOO0OOO0OOO .root ,image =O00O0O00OO0OO0O00 )#line:62
        OO0O00OOO0OOO0OOO .forth_pic .place (x =600 ,y =370 ,width =60 ,height =60 )#line:63
        OO0O00OOO0OOO0OOO .forth_pic .bind ("<Button-1>",OO0O00OOO0OOO0OOO .mask4 )#line:64
        O00OOOOO00OOOO000 =Image .open ("./pic/Mask2.png")#line:65
        O00OOOOO00OOOO000 =O00OOOOO00OOOO000 .resize ((60 ,60 ),Image .ANTIALIAS )#line:66
        O00OOOOO00OOOO000 =ImageTk .PhotoImage (O00OOOOO00OOOO000 )#line:67
        OO0O00OOO0OOO0OOO .fifth_pic =tk .Label (OO0O00OOO0OOO0OOO .root ,image =O00OOOOO00OOOO000 )#line:68
        OO0O00OOO0OOO0OOO .fifth_pic .place (x =600 ,y =440 ,width =60 ,height =60 )#line:69
        OO0O00OOO0OOO0OOO .fifth_pic .bind ("<Button-1>",OO0O00OOO0OOO0OOO .mask2 )#line:70
        tk .Label (OO0O00OOO0OOO0OOO .root ,text ="佩戴效果",font =10 ).place (x =920 ,y =120 )#line:71
        OO0O00OOO0OOO0OOO .cv_seg =tk .Canvas (OO0O00OOO0OOO0OOO .root ,bg ='white',width =270 ,height =270 )#line:72
        OO0O00OOO0OOO0OOO .cv_seg .create_rectangle (8 ,8 ,260 ,260 ,width =1 ,outline ='red')#line:73
        OO0O00OOO0OOO0OOO .cv_seg .place (x =820 ,y =150 )#line:74
        OO0O00OOO0OOO0OOO .label_Img_seg =tk .Label (OO0O00OOO0OOO0OOO .root )#line:75
        OO0O00OOO0OOO0OOO .label_Img_seg .place (x =820 ,y =150 )#line:76
        OO0O00OOO0OOO0OOO .root .mainloop ()#line:77
    def show_original1_pic (OO00OOOOOO0O00O0O ):#line:78
        OO00OOOOOO0O00O0O .path1_ =askopenfilename (title ='选择文件')#line:79
        print (OO00OOOOOO0O00O0O .path1_ )#line:80
        OO00OOOOOO0O00O0O .Img =PIL .Image .open (r'{}'.format (OO00OOOOOO0O00O0O .path1_ ))#line:81
        OOO00OOOO0O0O000O =OO00OOOOOO0O00O0O .Img .resize ((270 ,270 ),PIL .Image .ANTIALIAS )#line:82
        OOO0OO0OO000O0O00 =ImageTk .PhotoImage (OOO00OOOO0O0O000O )#line:83
        OO00OOOOOO0O00O0O .label_Img_original1 .config (image =OOO0OO0OO000O0O00 )#line:84
        OO00OOOOOO0O00O0O .label_Img_original1 .image =OOO0OO0OO000O0O00 #line:85
        OO00OOOOOO0O00O0O .cv_orinial1 .create_image (5 ,5 ,anchor ='nw',image =OOO0OO0OO000O0O00 )#line:86
    def show_morpher_pic (O0OOO000OOO00OOOO ):#line:87
        O0O0OOOO0O0O00OOO =cv2 .imread (O0OOO000OOO00OOOO .path1_ )#line:88
        OOO0OOOOO00O0OOO0 ,O0000O000000OOOO0 ,O0000OO0000OOO0OO ,OOOO00OO0O00O0OOO ,O0OO0OO00000O0O00 =O0OOO000OOO00OOOO .get_mouth (O0O0OOOO0O0O00OOO )#line:89
        OOO00OO00OO000OOO =O0OOO000OOO00OOOO .mask .resize (O0OO0OO00000O0O00 )#line:90
        O00O0OO00O00000O0 =Image .fromarray (O0O0OOOO0O0O00OOO [:,:,::-1 ])#line:91
        O00O0OO00O00000O0 .paste (OOO00OO00OO000OOO ,(int (OOO0OOOOO00O0OOO0 ),int (O0000OO0000OOO0OO )),OOO00OO00OO000OOO )#line:92
        O0OOO000OOO00OOOO .im =O00O0OO00O00000O0 #line:93
        O0OOO0O000O000OOO =O00O0OO00O00000O0 .resize ((270 ,270 ),PIL .Image .ANTIALIAS )#line:94
        OO00OO0O0000OO000 =ImageTk .PhotoImage (O0OOO0O000O000OOO )#line:95
        O0OOO000OOO00OOOO .label_Img_seg .config (image =OO00OO0O0000OO000 )#line:96
        O0OOO000OOO00OOOO .label_Img_seg .image =OO00OO0O0000OO000 #line:97
    def save_mask_face (OO0000000O000O000 ):#line:98
        OO00O0000O0OOO00O =OO0000000O000O000 .path1_ .split ('.')[0 ]+'_result.jpg'#line:99
        OO0000000O000O000 .im .save (OO00O0000O0OOO00O )#line:100
        tk .messagebox .showinfo ('提示','保存成功')#line:101
    def mask0 (O0O0O0OO00000OO0O ,O0O00O000000OOOOO ):#line:102
        O0O0O0OO00000OO0O .mask =Image .open ('pic/mask.png')#line:103
        O0O0O0OO00000OO0O .show_morpher_pic ()#line:104
    def mask1 (OO00O0O0OOO0OOO00 ,O0O0OOO000OO00OO0 ):#line:105
        OO00O0O0OOO0OOO00 .mask =Image .open ('pic/mask1.png')#line:106
        OO00O0O0OOO0OOO00 .show_morpher_pic ()#line:107
    def mask2 (OO00OOOOO0OO00OO0 ,O0O0O0O0OO0OO0OO0 ):#line:108
        OO00OOOOO0OO00OO0 .mask =Image .open ('pic/mask2.png')#line:109
        OO00OOOOO0OO00OO0 .show_morpher_pic ()#line:110
    def mask3 (OOOOO0000O00O0O0O ,OO000OO00OO0OOO00 ):#line:111
        OOOOO0000O00O0O0O .mask =Image .open ('pic/mask3.png')#line:112
        OOOOO0000O00O0O0O .show_morpher_pic ()#line:113
    def mask4 (O000O0000OO00O000 ,O0OOO0OO00O000OO0 ):#line:114
        O000O0000OO00O000 .mask =Image .open ('pic/mask4.png')#line:115
        O000O0000OO00O000 .show_morpher_pic ()#line:116
    def get_mouth (O0O000000OOO00O00 ,O000OOOOO0000OOOO ):#line:117
        OOO000OOO0O0O00O0 =cv2 .cvtColor (O000OOOOO0000OOOO ,cv2 .COLOR_BGR2GRAY )#line:118
        O0OO0OO000O000OO0 =dlib .get_frontal_face_detector ()#line:119
        O00O000O0O000OO00 =dlib .shape_predictor ('./shape_predictor_68_face_landmarks.dat')#line:120
        O0000OOO0OOO0OOO0 =O0OO0OO000O000OO0 (OOO000OOO0O0O00O0 ,0 )#line:121
        for O00O000OO0O0O0O00 ,OOOO00000OO0000OO in enumerate (O0000OOO0OOO0OOO0 ):#line:122
            OO0OO00OO0O0O00O0 =[]#line:123
            O0O00OOOOO0OO00O0 =[]#line:124
            O0O00O0O00O0000OO =OOOO00000OO0000OO .bottom ()-OOOO00000OO0000OO .top ()#line:125
            O0O000O0O0OO00000 =OOOO00000OO0000OO .right ()-OOOO00000OO0000OO .left ()#line:126
            OO0OOO00O00O0000O =O00O000O0O000OO00 (OOO000OOO0O0O00O0 ,OOOO00000OO0000OO )#line:127
            for O00OO00OO0OOO00OO in range (48 ,68 ):#line:128
                OO0OO00OO0O0O00O0 .append (OO0OOO00O00O0000O .part (O00OO00OO0OOO00OO ).x )#line:129
                O0O00OOOOO0OO00O0 .append (OO0OOO00O00O0000O .part (O00OO00OO0OOO00OO ).y )#line:130
            O0000OOOOO0OO00O0 =int (max (O0O00OOOOO0OO00O0 )+O0O00O0O00O0000OO /3 )#line:131
            OO000OOO00O000O00 =int (min (O0O00OOOOO0OO00O0 )-O0O00O0O00O0000OO /3 )#line:132
            OOOOO0O000000OO00 =int (max (OO0OO00OO0O0O00O0 )+O0O000O0O0OO00000 /3 )#line:133
            OOOO0OO0OOO0O0O00 =int (min (OO0OO00OO0O0O00O0 )-O0O000O0O0OO00000 /3 )#line:134
            OO0O0OO0O0000OOOO =((OOOOO0O000000OO00 -OOOO0OO0OOO0O0O00 ),(O0000OOOOO0OO00O0 -OO000OOO00O000O00 ))#line:135
            return OOOO0OO0OOO0O0O00 ,OOOOO0O000000OO00 ,OO000OOO00O000O00 ,O0000OOOOO0OO00O0 ,OO0O0OO0O0000OOOO #line:136
    def quit (OOO0O0OOO00OOOOO0 ):#line:137
        OOO0O0OOO00OOOOO0 .root .destroy ()#line:138
def drawDot (O0O0OO00O0O000O0O ,OO0OOOOOO000OO0O0 ):#line:139
    if len (OO0OOOOOO000OO0O0 )!=0 :#line:140
        for O0O0OOOOO0000OOOO in range (len (OO0OOOOOO000OO0O0 )):#line:141
            O000O000OO00OO0O0 =np .matrix ([[O0OOOO0OO0OO00OOO .x ,O0OOOO0OO0OO00OOO .y ]for O0OOOO0OO0OO00OOO in predictor (O0O0OO00O0O000O0O ,OO0OOOOOO000OO0O0 [O0O0OOOOO0000OOOO ]).parts ()])#line:142
            for OO00OOOO00O00OOO0 ,O00O00O000O000O00 in enumerate (O000O000OO00OO0O0 ):#line:143
                O0OOOOOO0O00O00O0 =(O00O00O000O000O00 [0 ,0 ],O00O00O000O000O00 [0 ,1 ])#line:144
                cv2 .circle (O0O0OO00O0O000O0O ,O0OOOOOO0O00O00O0 ,2 ,color =(139 ,0 ,0 ))#line:145
                cv2 .putText (O0O0OO00O0O000O0O ,str (OO00OOOO00O00OOO0 +1 ),O0OOOOOO0O00O00O0 ,font ,0.2 ,(187 ,255 ,255 ),1 ,cv2 .LINE_AA )#line:146
        cv2 .putText (O0O0OO00O0O000O0O ,"faces: "+str (len (OO0OOOOOO000OO0O0 )),(20 ,50 ),font ,1 ,(0 ,0 ,0 ),1 ,cv2 .LINE_AA )#line:147
    else :#line:148
        cv2 .putText (O0O0OO00O0O000O0O ,"no face",(20 ,50 ),font ,1 ,(0 ,0 ,0 ),1 ,cv2 .LINE_AA )#line:149
    return O0O0OO00O0O000O0O #line:150
def calc_angle (OO0OOO0OOO00OOOOO ,OOOO00O00O00OO0OO ,O0O0OOOO00000OOO0 ,OO0O00OO00O0OOO00 ):#line:151
    OO0O0OOOO0O0O00O0 =abs (OO0OOO0OOO00OOOOO -O0O0OOOO00000OOO0 )#line:152
    O00O00000OO00OOO0 =abs (OOOO00O00O00OO0OO -OO0O00OO00O0OOO00 )#line:153
    OO0O0OOO0OO0O0000 =math .sqrt (OO0O0OOOO0O0O00O0 *OO0O0OOOO0O0O00O0 +O00O00000OO00OOO0 *O00O00000OO00OOO0 )#line:154
    O0O00O0O00OOOOO0O =round (math .asin (O00O00000OO00OOO0 /OO0O0OOO0OO0O0000 )/math .pi *180 )#line:155
    return O0O00O0O00OOOOO0O #line:156
def rotate_bound (OO00OOO0O0000O00O ,O00O0O00OO0OOO00O ):#line:157
    (O0000OOOO00O000OO ,O0O0OOO0O0O0000O0 )=OO00OOO0O0000O00O .shape [:2 ]#line:158
    (O0OOO00O000OO0000 ,O0O0O0OOO0O0O0O00 )=(O0O0OOO0O0O0000O0 /2 ,O0000OOOO00O000OO /2 )#line:159
    O0O0OO0OOOO0000OO =cv2 .getRotationMatrix2D ((O0OOO00O000OO0000 ,O0O0O0OOO0O0O0O00 ),-O00O0O00OO0OOO00O ,1.0 )#line:160
    OOOO00O0OOOOOOO0O =np .abs (O0O0OO0OOOO0000OO [0 ,0 ])#line:161
    O00O0O000OO0O0OOO =np .abs (O0O0OO0OOOO0000OO [0 ,1 ])#line:162
    OO0O0O0OOO0O000OO =int ((O0000OOOO00O000OO *O00O0O000OO0O0OOO )+(O0O0OOO0O0O0000O0 *OOOO00O0OOOOOOO0O ))#line:163
    OOOOO0O000O00O000 =int ((O0000OOOO00O000OO *OOOO00O0OOOOOOO0O )+(O0O0OOO0O0O0000O0 *O00O0O000OO0O0OOO ))#line:164
    O0O0OO0OOOO0000OO [0 ,2 ]+=(OO0O0O0OOO0O000OO /2 )-O0OOO00O000OO0000 #line:165
    O0O0OO0OOOO0000OO [1 ,2 ]+=(OOOOO0O000O00O000 /2 )-O0O0O0OOO0O0O0O00 #line:166
    return cv2 .warpAffine (OO00OOO0O0000O00O ,O0O0OO0OOOO0000OO ,(OO0O0O0OOO0O000OO ,OOOOO0O000O00O000 ))#line:167
@app .route ('/shape',methods =["POST"])#line:168
def shape ():#line:169
    OOO0000000OO000O0 =request .files .get ('face')#line:170
    if OOO0000000OO000O0 :#line:171
        OO00000O00OO00O0O =OOO0000000OO000O0 .read ()#line:172
        O00OOOO000000OO00 =cv2 .imdecode (np .frombuffer (OO00000O00OO00O0O ,np .uint8 ),cv2 .IMREAD_COLOR )#line:173
        OOO000OO00OOO0OOO =cv2 .cvtColor (O00OOOO000000OO00 ,cv2 .COLOR_BGR2GRAY )#line:174
        OO0OO0OO0O0O0OOOO =detector (OOO000OO00OOO0OOO ,0 )#line:175
        OO0000000O00O0O00 =drawDot (O00OOOO000000OO00 ,OO0OO0OO0O0O0OOOO )#line:176
        O0OOO0OOO0O0O00O0 =Image .fromarray (OO0000000O00O0O00 [:,:,::-1 ])#line:177
        O000O000000OO0000 =BytesIO ()#line:178
        O0OOO0OOO0O0O00O0 .save (O000O000000OO0000 ,format ='PNG')#line:179
        O00OOO0000000OOOO =base64 .b64encode (O000O000000OO0000 .getvalue ())#line:180
        O000000000O0O000O =O00OOO0000000OOOO .decode ()#line:181
        return jsonify (O000000000O0O000O )#line:182
    return jsonify ({"code":400 })#line:183
@app .route ('/make',methods =["POST"])#line:184
def make ():#line:185
    OOO0O0O0O00O00OO0 =request .files .get ('face')#line:186
    if OOO0O0O0O00O00OO0 :#line:187
        try :#line:188
            O0O0O00OOOO000O00 =OOO0O0O0O00O00OO0 .read ()#line:189
            OO0OO0OO0O00OOOOO =cv2 .imdecode (np .frombuffer (O0O0O00OOOO000O00 ,np .uint8 ),cv2 .IMREAD_COLOR )#line:190
            O0OOO0O00000OO0O0 =cv2 .cvtColor (OO0OO0OO0O00OOOOO ,cv2 .COLOR_BGR2GRAY )#line:191
            O0OO0OOO0000OOOOO =detector (O0OOO0O00000OO0O0 ,0 )#line:192
            for O00OO0OOO0000OO00 ,OOO00O0OOOO0O000O in enumerate (O0OO0OOO0000OOOOO ):#line:193
                O000O00000OOO0000 =[]#line:194
                OO00O00O0OO0OO000 =[]#line:195
                OOO00OOO0OOOOOOO0 =OOO00O0OOOO0O000O .bottom ()-OOO00O0OOOO0O000O .top ()#line:196
                OOOOOOOO0O00O0OOO =OOO00O0OOOO0O000O .right ()-OOO00O0OOOO0O000O .left ()#line:197
                O0000O00O00OO0000 =predictor (O0OOO0O00000OO0O0 ,OOO00O0OOOO0O000O )#line:198
                for O00OO000OO0OOOOOO in range (48 ,68 ):#line:199
                    O000O00000OOO0000 .append (O0000O00O00OO0000 .part (O00OO000OO0OOOOOO ).x )#line:200
                    OO00O00O0OO0OO000 .append (O0000O00O00OO0000 .part (O00OO000OO0OOOOOO ).y )#line:201
                OOOOO000O0O0OOOO0 =int (max (OO00O00O0OO0OO000 )+OOO00OOO0OOOOOOO0 /3 )#line:202
                O00O00OOOO0000000 =int (min (OO00O00O0OO0OO000 )-OOO00OOO0OOOOOOO0 /3 )#line:203
                OOO0O0O0OOOOOO0O0 =int (max (O000O00000OOO0000 )+OOOOOOOO0O00O0OOO /3 )#line:204
                OO0O0O0O000O0O00O =int (min (O000O00000OOO0000 )-OOOOOOOO0O00O0OOO /3 )#line:205
                OOO0OO00OO00O0O00 =((OOO0O0O0OOOOOO0O0 -OO0O0O0O000O0O00O ),(OOOOO000O0O0OOOO0 -O00O00OOOO0000000 ))#line:206
                OOO0000O00OO0OO0O =mask .resize (OOO0OO00OO00O0O00 )#line:207
                O000O0O0000O00OOO =calc_angle (O0000O00O00OO0000 .part (48 ).x ,O0000O00O00OO0000 .part (48 ).y ,O0000O00O00OO0000 .part (54 ).x ,O0000O00O00OO0000 .part (54 ).y )#line:208
                if 0 !=O000O0O0000O00OOO :#line:209
                    if O0000O00O00OO0000 .part (48 ).y <O0000O00O00OO0000 .part (54 ).y :#line:210
                        O000O0O0000O00OOO =-O000O0O0000O00OOO #line:211
                    OOO0000O00OO0OO0O =OOO0000O00OO0OO0O .rotate (O000O0O0000O00OOO )#line:212
                OOOOO0OO000OO00OO =Image .fromarray (OO0OO0OO0O00OOOOO [:,:,::-1 ])#line:213
                OOOOO0OO000OO00OO .paste (OOO0000O00OO0OO0O ,(OO0O0O0O000O0O00O ,O00O00OOOO0000000 ),OOO0000O00OO0OO0O )#line:214
                OOOO000O00OO0O00O =BytesIO ()#line:215
                OOOOO0OO000OO00OO .save (OOOO000O00OO0O00O ,format ='PNG')#line:216
                O0O0000O0O0OOOO00 =base64 .b64encode (OOOO000O00OO0O00O .getvalue ())#line:217
                O0OO0000O000OO0O0 =O0O0000O0O0OOOO00 .decode ()#line:218
                return jsonify ({"code":200 ,"format":"PNG","data":O0OO0000O000OO0O0 })#line:219
        except ():#line:220
            return jsonify ({"code":500 })#line:221
    return jsonify ({"code":400 })#line:222
if __name__ =='__main__':#line:223
    port =1234 #line:224
    argv =sys .argv #line:225
    if len (argv )>1 :#line:226
        port =int (argv [1 ])#line:227
    app .run (host ='0.0.0.0',port =port )#line:228
