#byvinson
import base64 #line:1
import sys #line:2
from io import BytesIO #line:3
import numpy as np #line:5
from PIL import Image ,ImageTk #line:6
from tkinter .filedialog import askopenfilename #line:7
import cv2 #line:8
import tkinter as tk #line:9
import tkinter .messagebox #line:10
import PIL #line:11
import dlib #line:12
from flask import request ,Flask ,jsonify #line:13
app =Flask (__name__ )#line:15
detector =dlib .get_frontal_face_detector ()#line:16
predictor =dlib .shape_predictor ('./shape_predictor_68_face_landmarks.dat')#line:17
font =cv2 .FONT_HERSHEY_SIMPLEX #line:18
mask =Image .open ('pic/Mask3.png')#line:19
class AddMask (object ):#line:22
    def __init__ (O00O0000OOOOOOOO0 ):#line:23
        O00O0000OOOOOOOO0 .root =tk .Tk ()#line:24
        O00O0000OOOOOOOO0 .root .title ('一起来带口罩啊')#line:25
        O00O0000OOOOOOOO0 .root .geometry ('1200x700')#line:26
        O00O0000OOOOOOOO0 .path1_ =None #line:28
        O00O0000OOOOOOOO0 .path2_ =None #line:29
        O00O0000OOOOOOOO0 .seg_img_path =None #line:30
        O00O0000OOOOOOOO0 .mask =None #line:31
        O00O0000OOOOOOOO0 .im =None #line:32
        O00O0000OOOOOOOO0 .label_Img_seg =None #line:33
        O0O0O0O0OOOOOO00O =tk .Label ()#line:35
        O0O0O0O0OOOOOO00O .place (x =0 ,y =0 )#line:36
        tk .Button (O00O0000OOOOOOOO0 .root ,text ="输入人脸",command =O00O0000OOOOOOOO0 .show_original1_pic ).place (x =270 ,y =40 )#line:39
        tk .Button (O00O0000OOOOOOOO0 .root ,text ="保存输出",command =O00O0000OOOOOOOO0 .save_mask_face ).place (x =920 ,y =40 )#line:40
        tk .Label (O00O0000OOOOOOOO0 .root ,text ="人脸",font =10 ).place (x =280 ,y =120 )#line:42
        O00O0000OOOOOOOO0 .cv_orinial1 =tk .Canvas (O00O0000OOOOOOOO0 .root ,bg ='white',width =270 ,height =270 )#line:43
        O00O0000OOOOOOOO0 .cv_orinial1 .create_rectangle (8 ,8 ,260 ,260 ,width =1 ,outline ='red')#line:44
        O00O0000OOOOOOOO0 .cv_orinial1 .place (x =180 ,y =150 )#line:45
        O00O0000OOOOOOOO0 .label_Img_original1 =tk .Label (O00O0000OOOOOOOO0 .root )#line:46
        O00O0000OOOOOOOO0 .label_Img_original1 .place (x =180 ,y =150 )#line:47
        tk .Label (O00O0000OOOOOOOO0 .root ,text ="选择口罩",font =10 ).place (x =600 ,y =120 )#line:49
        O000OO000OO000OOO =Image .open ("./pic/Mask.png")#line:51
        O000OO000OO000OOO =O000OO000OO000OOO .resize ((60 ,60 ),Image .ANTIALIAS )#line:52
        O000OO000OO000OOO =ImageTk .PhotoImage (O000OO000OO000OOO )#line:53
        O00O0000OOOOOOOO0 .first =tk .Label (O00O0000OOOOOOOO0 .root ,image =O000OO000OO000OOO )#line:54
        O00O0000OOOOOOOO0 .first .place (x =600 ,y =160 ,width =60 ,height =60 )#line:55
        O00O0000OOOOOOOO0 .first .bind ("<Button-1>",O00O0000OOOOOOOO0 .mask0 )#line:56
        OO0OO00OOOOO0OOOO =Image .open ("./pic/Mask1.png")#line:58
        OO0OO00OOOOO0OOOO =OO0OO00OOOOO0OOOO .resize ((60 ,60 ),Image .ANTIALIAS )#line:59
        OO0OO00OOOOO0OOOO =ImageTk .PhotoImage (OO0OO00OOOOO0OOOO )#line:60
        O00O0000OOOOOOOO0 .second_pic =tk .Label (O00O0000OOOOOOOO0 .root ,image =OO0OO00OOOOO0OOOO )#line:61
        O00O0000OOOOOOOO0 .second_pic .place (x =600 ,y =230 ,width =60 ,height =60 )#line:62
        O00O0000OOOOOOOO0 .second_pic .bind ("<Button-1>",O00O0000OOOOOOOO0 .mask1 )#line:63
        O0000OO0O0O00000O =Image .open ("./pic/Mask3.png")#line:65
        O0000OO0O0O00000O =O0000OO0O0O00000O .resize ((60 ,60 ),Image .ANTIALIAS )#line:66
        O0000OO0O0O00000O =ImageTk .PhotoImage (O0000OO0O0O00000O )#line:67
        O00O0000OOOOOOOO0 .third_pic =tk .Label (O00O0000OOOOOOOO0 .root ,image =O0000OO0O0O00000O )#line:68
        O00O0000OOOOOOOO0 .third_pic .place (x =600 ,y =300 ,width =60 ,height =60 )#line:69
        O00O0000OOOOOOOO0 .third_pic .bind ("<Button-1>",O00O0000OOOOOOOO0 .mask3 )#line:70
        OO00OOO0000O00OO0 =Image .open ("./pic/Mask4.png")#line:72
        OO00OOO0000O00OO0 =OO00OOO0000O00OO0 .resize ((60 ,60 ),Image .ANTIALIAS )#line:73
        OO00OOO0000O00OO0 =ImageTk .PhotoImage (OO00OOO0000O00OO0 )#line:74
        O00O0000OOOOOOOO0 .forth_pic =tk .Label (O00O0000OOOOOOOO0 .root ,image =OO00OOO0000O00OO0 )#line:75
        O00O0000OOOOOOOO0 .forth_pic .place (x =600 ,y =370 ,width =60 ,height =60 )#line:76
        O00O0000OOOOOOOO0 .forth_pic .bind ("<Button-1>",O00O0000OOOOOOOO0 .mask4 )#line:77
        OO0OO0O000OOOO00O =Image .open ("./pic/Mask2.png")#line:79
        OO0OO0O000OOOO00O =OO0OO0O000OOOO00O .resize ((60 ,60 ),Image .ANTIALIAS )#line:80
        OO0OO0O000OOOO00O =ImageTk .PhotoImage (OO0OO0O000OOOO00O )#line:81
        O00O0000OOOOOOOO0 .fifth_pic =tk .Label (O00O0000OOOOOOOO0 .root ,image =OO0OO0O000OOOO00O )#line:82
        O00O0000OOOOOOOO0 .fifth_pic .place (x =600 ,y =440 ,width =60 ,height =60 )#line:83
        O00O0000OOOOOOOO0 .fifth_pic .bind ("<Button-1>",O00O0000OOOOOOOO0 .mask2 )#line:84
        tk .Label (O00O0000OOOOOOOO0 .root ,text ="佩戴效果",font =10 ).place (x =920 ,y =120 )#line:86
        O00O0000OOOOOOOO0 .cv_seg =tk .Canvas (O00O0000OOOOOOOO0 .root ,bg ='white',width =270 ,height =270 )#line:87
        O00O0000OOOOOOOO0 .cv_seg .create_rectangle (8 ,8 ,260 ,260 ,width =1 ,outline ='red')#line:88
        O00O0000OOOOOOOO0 .cv_seg .place (x =820 ,y =150 )#line:89
        O00O0000OOOOOOOO0 .label_Img_seg =tk .Label (O00O0000OOOOOOOO0 .root )#line:90
        O00O0000OOOOOOOO0 .label_Img_seg .place (x =820 ,y =150 )#line:91
        O00O0000OOOOOOOO0 .root .mainloop ()#line:93
    def show_original1_pic (O0OOO0OO0000000OO ):#line:96
        O0OOO0OO0000000OO .path1_ =askopenfilename (title ='选择文件')#line:97
        print (O0OOO0OO0000000OO .path1_ )#line:98
        O0OOO0OO0000000OO .Img =PIL .Image .open (r'{}'.format (O0OOO0OO0000000OO .path1_ ))#line:99
        O0O000OOOOOOO0000 =O0OOO0OO0000000OO .Img .resize ((270 ,270 ),PIL .Image .ANTIALIAS )#line:100
        OOOO00OOO0O0O000O =ImageTk .PhotoImage (O0O000OOOOOOO0000 )#line:101
        O0OOO0OO0000000OO .label_Img_original1 .config (image =OOOO00OOO0O0O000O )#line:102
        O0OOO0OO0000000OO .label_Img_original1 .image =OOOO00OOO0O0O000O #line:103
        O0OOO0OO0000000OO .cv_orinial1 .create_image (5 ,5 ,anchor ='nw',image =OOOO00OOO0O0O000O )#line:104
    def show_morpher_pic (O0O0O0OOOO00O00O0 ):#line:107
        OOOOOOO000O00O00O =cv2 .imread (O0O0O0OOOO00O00O0 .path1_ )#line:108
        OO00OO00OOOO0OO0O ,O0O000000OO0O0O0O ,O0O0OOOOO00O0OOOO ,OOOOOO00O00OO000O ,O0000000O00O0OOO0 =O0O0O0OOOO00O00O0 .get_mouth (OOOOOOO000O00O00O )#line:109
        OOO0OO000O0OOO000 =O0O0O0OOOO00O00O0 .mask .resize (O0000000O00O0OOO0 )#line:110
        O00OO000OOO0O0OOO =Image .fromarray (OOOOOOO000O00O00O [:,:,::-1 ])#line:111
        O00OO000OOO0O0OOO .paste (OOO0OO000O0OOO000 ,(int (OO00OO00OOOO0OO0O ),int (O0O0OOOOO00O0OOOO )),OOO0OO000O0OOO000 )#line:113
        O0O0O0OOOO00O00O0 .im =O00OO000OOO0O0OOO #line:117
        OOOO0O0O00OO000OO =O00OO000OOO0O0OOO .resize ((270 ,270 ),PIL .Image .ANTIALIAS )#line:118
        OO0000OO0000O0O0O =ImageTk .PhotoImage (OOOO0O0O00OO000OO )#line:119
        O0O0O0OOOO00O00O0 .label_Img_seg .config (image =OO0000OO0000O0O0O )#line:120
        O0O0O0OOOO00O00O0 .label_Img_seg .image =OO0000OO0000O0O0O #line:121
    def save_mask_face (O0000OO0OOO0OOO0O ):#line:124
        O0O0OOO0OO0000000 =O0000OO0OOO0OOO0O .path1_ .split ('.')[0 ]+'_result.jpg'#line:125
        O0000OO0OOO0OOO0O .im .save (O0O0OOO0OO0000000 )#line:126
        tk .messagebox .showinfo ('提示','保存成功')#line:127
    def mask0 (O00O00OO0OO0OOOO0 ,OOOOO0OO00000OOOO ):#line:129
        O00O00OO0OO0OOOO0 .mask =Image .open ('pic/mask.png')#line:130
        O00O00OO0OO0OOOO0 .show_morpher_pic ()#line:131
    def mask1 (OOO0OOO00OOOO0O0O ,OOO0O0OOOOO000O00 ):#line:133
        OOO0OOO00OOOO0O0O .mask =Image .open ('pic/mask1.png')#line:134
        OOO0OOO00OOOO0O0O .show_morpher_pic ()#line:135
    def mask2 (O00000OO0OOO0OOO0 ,O0OOO0OOOO00O00OO ):#line:137
        O00000OO0OOO0OOO0 .mask =Image .open ('pic/mask2.png')#line:138
        O00000OO0OOO0OOO0 .show_morpher_pic ()#line:139
    def mask3 (OO000O000OO0OOO00 ,O000O0OO0OOO00000 ):#line:141
        OO000O000OO0OOO00 .mask =Image .open ('pic/mask3.png')#line:142
        OO000O000OO0OOO00 .show_morpher_pic ()#line:143
    def mask4 (OOO00OO0000O00O0O ,O0OO0OOOO00OOO00O ):#line:145
        OOO00OO0000O00O0O .mask =Image .open ('pic/mask4.png')#line:146
        OOO00OO0000O00O0O .show_morpher_pic ()#line:147
    def get_mouth (OO00O000O0OOOO0OO ,OO000O000000OOOO0 ):#line:149
        OOOO0O0000OO0O000 =cv2 .cvtColor (OO000O000000OOOO0 ,cv2 .COLOR_BGR2GRAY )#line:150
        OOO000OO00OO0O0OO =dlib .get_frontal_face_detector ()#line:151
        OOOOO0OO0000O000O =dlib .shape_predictor ('./shape_predictor_68_face_landmarks.dat')#line:152
        OO00O0O0000OO0000 =OOO000OO00OO0O0OO (OOOO0O0000OO0O000 ,0 )#line:153
        for O0000O00000O000O0 ,OOO0O000O0O00OO00 in enumerate (OO00O0O0000OO0000 ):#line:154
            O0OOO0O0OOO000OOO =[]#line:155
            OOO00OOO0OO0O00OO =[]#line:156
            OO000O0O0O0O0OOOO =OOO0O000O0O00OO00 .bottom ()-OOO0O000O0O00OO00 .top ()#line:158
            O0OOOOOOOOOOOOOO0 =OOO0O000O0O00OO00 .right ()-OOO0O000O0O00OO00 .left ()#line:160
            O00OOOOOO0O00OOO0 =OOOOO0OO0000O000O (OOOO0O0000OO0O000 ,OOO0O000O0O00OO00 )#line:161
            for OO000OO0OO000000O in range (48 ,68 ):#line:163
                O0OOO0O0OOO000OOO .append (O00OOOOOO0O00OOO0 .part (OO000OO0OO000000O ).x )#line:164
                OOO00OOO0OO0O00OO .append (O00OOOOOO0O00OOO0 .part (OO000OO0OO000000O ).y )#line:165
            O0OO0OOOOOOO00O00 =int (max (OOO00OOO0OO0O00OO )+OO000O0O0O0O0OOOO /3 )#line:167
            O0OOOOOO0OO000O0O =int (min (OOO00OOO0OO0O00OO )-OO000O0O0O0O0OOOO /3 )#line:168
            OOO000OOO000O0OOO =int (max (O0OOO0O0OOO000OOO )+O0OOOOOOOOOOOOOO0 /3 )#line:169
            OO00OO0OO0OOO0000 =int (min (O0OOO0O0OOO000OOO )-O0OOOOOOOOOOOOOO0 /3 )#line:170
            OO0O0O00000O0000O =((OOO000OOO000O0OOO -OO00OO0OO0OOO0000 ),(O0OO0OOOOOOO00O00 -O0OOOOOO0OO000O0O ))#line:171
            return OO00OO0OO0OOO0000 ,OOO000OOO000O0OOO ,O0OOOOOO0OO000O0O ,O0OO0OOOOOOO00O00 ,OO0O0O00000O0000O #line:172
    def quit (O0O0O0O0O0000O0O0 ):#line:174
        O0O0O0O0O0000O0O0 .root .destroy ()#line:175
def drawDot (OOO0O0OO00O0OOO0O ,O00OO0O0OO00OOOO0 ):#line:178
    if len (O00OO0O0OO00OOOO0 )!=0 :#line:180
        for OOO0000OO0O000000 in range (len (O00OO0O0OO00OOOO0 )):#line:182
            OO0O00OO0O0OOO0O0 =np .matrix ([[O0O00OO0000OO0O0O .x ,O0O00OO0000OO0O0O .y ]for O0O00OO0000OO0O0O in predictor (OOO0O0OO00O0OOO0O ,O00OO0O0OO00OOOO0 [OOO0000OO0O000000 ]).parts ()])#line:184
            for O0000O0O0OOO0O000 ,O0O000OO0OO0000O0 in enumerate (OO0O00OO0O0OOO0O0 ):#line:185
                OOOOOO00OOO0OO00O =(O0O000OO0OO0000O0 [0 ,0 ],O0O000OO0OO0000O0 [0 ,1 ])#line:187
                cv2 .circle (OOO0O0OO00O0OOO0O ,OOOOOO00OOO0OO00O ,2 ,color =(139 ,0 ,0 ))#line:190
                cv2 .putText (OOO0O0OO00O0OOO0O ,str (O0000O0O0OOO0O000 +1 ),OOOOOO00OOO0OO00O ,font ,0.2 ,(187 ,255 ,255 ),1 ,cv2 .LINE_AA )#line:192
        cv2 .putText (OOO0O0OO00O0OOO0O ,"faces: "+str (len (O00OO0O0OO00OOOO0 )),(20 ,50 ),font ,1 ,(0 ,0 ,0 ),1 ,cv2 .LINE_AA )#line:194
    else :#line:195
        cv2 .putText (OOO0O0OO00O0OOO0O ,"no face",(20 ,50 ),font ,1 ,(0 ,0 ,0 ),1 ,cv2 .LINE_AA )#line:197
    return OOO0O0OO00O0OOO0O #line:198
@app .route ('/shape',methods =["POST"])#line:201
def shape ():#line:202
    OOO0O0O0O0OOO0OOO =request .files .get ('face')#line:203
    if OOO0O0O0O0OOO0OOO :#line:204
        O000000000000000O =OOO0O0O0O0OOO0OOO .read ()#line:205
        O0O000OOO0OO000O0 =cv2 .imdecode (np .frombuffer (O000000000000000O ,np .uint8 ),cv2 .IMREAD_COLOR )#line:206
        O0O000OOO000000OO =cv2 .cvtColor (O0O000OOO0OO000O0 ,cv2 .COLOR_BGR2GRAY )#line:207
        OO0O0O0000OOOO0OO =detector (O0O000OOO000000OO ,0 )#line:208
        O0OOOO0OOOO0O000O =drawDot (O0O000OOO0OO000O0 ,OO0O0O0000OOOO0OO )#line:209
        O0OOOO0O00000O0O0 =Image .fromarray (O0OOOO0OOOO0O000O [:,:,::-1 ])#line:210
        OOO0O0O0OOO0OOO00 =BytesIO ()#line:211
        O0OOOO0O00000O0O0 .save (OOO0O0O0OOO0OOO00 ,format ='PNG')#line:212
        O0O000000OOO00OOO =base64 .b64encode (OOO0O0O0OOO0OOO00 .getvalue ())#line:213
        OO00OO0O0OOOOO0O0 =O0O000000OOO00OOO .decode ()#line:214
        return jsonify (OO00OO0O0OOOOO0O0 )#line:215
    return "hello"#line:216
@app .route ('/make',methods =["POST"])#line:219
def make ():#line:220
    OO0000O0O0OOOO00O =request .files .get ('face')#line:221
    if OO0000O0O0OOOO00O :#line:222
        try :#line:223
            O000OOO0000000000 =OO0000O0O0OOOO00O .read ()#line:224
            OOO0OO0000O0OO0O0 =cv2 .imdecode (np .frombuffer (O000OOO0000000000 ,np .uint8 ),cv2 .IMREAD_COLOR )#line:225
            OO00O00O000OOOOOO =cv2 .cvtColor (OOO0OO0000O0OO0O0 ,cv2 .COLOR_BGR2GRAY )#line:226
            O0000O00O0O0OO00O =detector (OO00O00O000OOOOOO ,0 )#line:227
            for OOOO0OO0O00O00OOO ,OOO0O0OOO0OO00O0O in enumerate (O0000O00O0O0OO00O ):#line:228
                O000OO00OO0O0OOO0 =[]#line:229
                O00OO0O0O00O0O00O =[]#line:230
                OOO0O000OOO00O0OO =OOO0O0OOO0OO00O0O .bottom ()-OOO0O0OOO0OO00O0O .top ()#line:232
                OO0O0OO00OOOO0000 =OOO0O0OOO0OO00O0O .right ()-OOO0O0OOO0OO00O0O .left ()#line:234
                O0O00O0OO00O00OO0 =predictor (OO00O00O000OOOOOO ,OOO0O0OOO0OO00O0O )#line:235
                for OO0O00O00O0O0O0OO in range (48 ,68 ):#line:237
                    O000OO00OO0O0OOO0 .append (O0O00O0OO00O00OO0 .part (OO0O00O00O0O0O0OO ).x )#line:238
                    O00OO0O0O00O0O00O .append (O0O00O0OO00O00OO0 .part (OO0O00O00O0O0O0OO ).y )#line:239
                O00000OO00OO0OOOO =int (max (O00OO0O0O00O0O00O )+OOO0O000OOO00O0OO /3 )#line:241
                OOO0OOOOOO00OO0OO =int (min (O00OO0O0O00O0O00O )-OOO0O000OOO00O0OO /3 )#line:242
                O0O00OOO00O00000O =int (max (O000OO00OO0O0OOO0 )+OO0O0OO00OOOO0000 /3 )#line:243
                O000O000O000O0OOO =int (min (O000OO00OO0O0OOO0 )-OO0O0OO00OOOO0000 /3 )#line:244
                O0O0O00O00OO000OO =((O0O00OOO00O00000O -O000O000O000O0OOO ),(O00000OO00OO0OOOO -OOO0OOOOOO00OO0OO ))#line:245
                OO0OO0000OOO0O000 =mask .resize (O0O0O00O00OO000OO )#line:246
                O00OO0OOOOOOO00OO =Image .fromarray (OOO0OO0000O0OO0O0 [:,:,::-1 ])#line:247
                O00OO0OOOOOOO00OO .paste (OO0OO0000OOO0O000 ,(int (O000O000O000O0OOO ),int (OOO0OOOOOO00OO0OO )),OO0OO0000OOO0O000 )#line:249
                O00000O0O0O000OOO =BytesIO ()#line:250
                O00OO0OOOOOOO00OO .save (O00000O0O0O000OOO ,format ='PNG')#line:251
                OOOOOO0O0OO0OOOOO =base64 .b64encode (O00000O0O0O000OOO .getvalue ())#line:252
                OO000OOOO00O00OO0 =OOOOOO0O0OO0OOOOO .decode ()#line:253
                return jsonify ({"code":200 ,"format":"PNG","data":OO000OOOO00O00OO0 })#line:254
        except ():#line:255
            return jsonify ({"code":500 })#line:256
    return "hello"#line:257
if __name__ =='__main__':#line:260
    port =1234 #line:261
    argv =sys .argv #line:262
    if len (argv )>1 :#line:263
        port =int (argv [1 ])#line:264
    app .run (host ='0.0.0.0',port =port )#line:266
