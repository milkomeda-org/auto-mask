#byvinson
import base64
import sys
from io import BytesIO

import numpy as np
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import cv2
import tkinter as tk
import tkinter.messagebox
import PIL
import dlib
from flask import request, Flask, jsonify

app = Flask(__name__)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')
font = cv2.FONT_HERSHEY_SIMPLEX
mask = Image.open('pic/Mask3.png')


class AddMask(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('一起来带口罩啊')
        self.root.geometry('1200x700')

        self.path1_ = None
        self.path2_ = None
        self.seg_img_path = None
        self.mask = None
        self.im = None
        self.label_Img_seg = None

        img = tk.Label()
        img.place(x=0, y=0)

        # 原图1的展示
        tk.Button(self.root, text="输入人脸", command=self.show_original1_pic).place(x=270, y=40)
        tk.Button(self.root, text="保存输出", command=self.save_mask_face).place(x=920, y=40)

        tk.Label(self.root, text="人脸", font=10).place(x=280, y=120)
        self.cv_orinial1 = tk.Canvas(self.root, bg='white', width=270, height=270)
        self.cv_orinial1.create_rectangle(8, 8, 260, 260, width=1, outline='red')
        self.cv_orinial1.place(x=180, y=150)
        self.label_Img_original1 = tk.Label(self.root)
        self.label_Img_original1.place(x=180, y=150)

        tk.Label(self.root, text="选择口罩", font=10).place(x=600, y=120)

        first_pic = Image.open("./pic/Mask.png")
        first_pic = first_pic.resize((60, 60), Image.ANTIALIAS)
        first_pic = ImageTk.PhotoImage(first_pic)
        self.first = tk.Label(self.root, image=first_pic)
        self.first.place(x=600, y=160, width=60, height=60)
        self.first.bind("<Button-1>", self.mask0)

        second_pic = Image.open("./pic/Mask1.png")
        second_pic = second_pic.resize((60, 60), Image.ANTIALIAS)
        second_pic = ImageTk.PhotoImage(second_pic)
        self.second_pic = tk.Label(self.root, image=second_pic)
        self.second_pic.place(x=600, y=230, width=60, height=60)
        self.second_pic.bind("<Button-1>", self.mask1)

        third_pic = Image.open("./pic/Mask3.png")
        third_pic = third_pic.resize((60, 60), Image.ANTIALIAS)
        third_pic = ImageTk.PhotoImage(third_pic)
        self.third_pic = tk.Label(self.root, image=third_pic)
        self.third_pic.place(x=600, y=300, width=60, height=60)
        self.third_pic.bind("<Button-1>", self.mask3)

        forth_pic = Image.open("./pic/Mask4.png")
        forth_pic = forth_pic.resize((60, 60), Image.ANTIALIAS)
        forth_pic = ImageTk.PhotoImage(forth_pic)
        self.forth_pic = tk.Label(self.root, image=forth_pic)
        self.forth_pic.place(x=600, y=370, width=60, height=60)
        self.forth_pic.bind("<Button-1>", self.mask4)

        fifth_pic = Image.open("./pic/Mask2.png")
        fifth_pic = fifth_pic.resize((60, 60), Image.ANTIALIAS)
        fifth_pic = ImageTk.PhotoImage(fifth_pic)
        self.fifth_pic = tk.Label(self.root, image=fifth_pic)
        self.fifth_pic.place(x=600, y=440, width=60, height=60)
        self.fifth_pic.bind("<Button-1>", self.mask2)

        tk.Label(self.root, text="佩戴效果", font=10).place(x=920, y=120)
        self.cv_seg = tk.Canvas(self.root, bg='white', width=270, height=270)
        self.cv_seg.create_rectangle(8, 8, 260, 260, width=1, outline='red')
        self.cv_seg.place(x=820, y=150)
        self.label_Img_seg = tk.Label(self.root)
        self.label_Img_seg.place(x=820, y=150)

        self.root.mainloop()

    # 原图1展示
    def show_original1_pic(self):
        self.path1_ = askopenfilename(title='选择文件')
        print(self.path1_)
        self.Img = PIL.Image.open(r'{}'.format(self.path1_))
        Img = self.Img.resize((270, 270), PIL.Image.ANTIALIAS)  # 调整图片大小至256x256
        img_png_original = ImageTk.PhotoImage(Img)
        self.label_Img_original1.config(image=img_png_original)
        self.label_Img_original1.image = img_png_original  # keep a reference
        self.cv_orinial1.create_image(5, 5, anchor='nw', image=img_png_original)

    # 人脸戴口罩效果展示
    def show_morpher_pic(self):
        img1 = cv2.imread(self.path1_)
        x_min, x_max, y_min, y_max, size = self.get_mouth(img1)
        adding = self.mask.resize(size)
        im = Image.fromarray(img1[:, :, ::-1])  # 切换RGB格式
        # 在合适位置添加头发图片
        im.paste(adding, (int(x_min), int(y_min)), adding)
        # im.show()
        # save_path = self.path1_.split('.')[0] + '_result.jpg'
        # im.save(save_path)
        self.im = im
        Img = im.resize((270, 270), PIL.Image.ANTIALIAS)  # 调整图片大小至270x270
        img_png_seg = ImageTk.PhotoImage(Img)
        self.label_Img_seg.config(image=img_png_seg)
        self.label_Img_seg.image = img_png_seg  # keep a reference

    # 戴口罩人脸输出保存
    def save_mask_face(self):
        save_path = self.path1_.split('.')[0] + '_result.jpg'
        self.im.save(save_path)
        tk.messagebox.showinfo('提示', '保存成功')

    def mask0(self, event):
        self.mask = Image.open('pic/mask.png')
        self.show_morpher_pic()

    def mask1(self, event):
        self.mask = Image.open('pic/mask1.png')
        self.show_morpher_pic()

    def mask2(self, event):
        self.mask = Image.open('pic/mask2.png')
        self.show_morpher_pic()

    def mask3(self, event):
        self.mask = Image.open('pic/mask3.png')
        self.show_morpher_pic()

    def mask4(self, event):
        self.mask = Image.open('pic/mask4.png')
        self.show_morpher_pic()

    def get_mouth(self, img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')
        faces = detector(img_gray, 0)
        for k, d in enumerate(faces):
            x = []
            y = []
            # 人脸大小的高度
            height = d.bottom() - d.top()
            # 人脸大小的宽度
            width = d.right() - d.left()
            shape = predictor(img_gray, d)
            # 48-67 为嘴唇部分
            for i in range(48, 68):
                x.append(shape.part(i).x)
                y.append(shape.part(i).y)
            # 根据人脸的大小扩大嘴唇对应口罩的区域
            y_max = int(max(y) + height / 3)
            y_min = int(min(y) - height / 3)
            x_max = int(max(x) + width / 3)
            x_min = int(min(x) - width / 3)
            size = ((x_max - x_min), (y_max - y_min))
            return x_min, x_max, y_min, y_max, size

    def quit(self):
        self.root.destroy()


def drawDot(img_rd, faces):
    # 标 68 个点
    if len(faces) != 0:
        # 检测到人脸
        for i in range(len(faces)):
            # 取特征点坐标
            landmarks = np.matrix([[p.x, p.y] for p in predictor(img_rd, faces[i]).parts()])
            for idx, point in enumerate(landmarks):
                # 68 点的坐标
                pos = (point[0, 0], point[0, 1])

                # 利用 cv2.circle 给每个特征点画一个圈，共 68 个
                cv2.circle(img_rd, pos, 2, color=(139, 0, 0))
                # 利用 cv2.putText 写数字 1-68
                cv2.putText(img_rd, str(idx + 1), pos, font, 0.2, (187, 255, 255), 1, cv2.LINE_AA)

        cv2.putText(img_rd, "faces: " + str(len(faces)), (20, 50), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
    else:
        # 没有检测到人脸
        cv2.putText(img_rd, "no face", (20, 50), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
    return img_rd


@app.route('/shape', methods=["POST"])
def shape():
    file_pic = request.files.get('face')
    if file_pic:
        face = file_pic.read()
        im1 = cv2.imdecode(np.frombuffer(face, np.uint8), cv2.IMREAD_COLOR)
        img_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
        faces = detector(img_gray, 0)
        img_rd = drawDot(im1, faces)
        im = Image.fromarray(img_rd[:, :, ::-1])  # 切换RGB格式
        output_buffer = BytesIO()
        im.save(output_buffer, format='PNG')
        base64_data = base64.b64encode(output_buffer.getvalue())
        s = base64_data.decode()
        return jsonify(s)
    return "hello"


@app.route('/make', methods=["POST"])
def make():
    file_pic = request.files.get('face')
    if file_pic:
        try:
            face = file_pic.read()
            im1 = cv2.imdecode(np.frombuffer(face, np.uint8), cv2.IMREAD_COLOR)
            img_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
            faces = detector(img_gray, 0)
            for k, d in enumerate(faces):
                x = []
                y = []
                # 人脸大小的高度
                height = d.bottom() - d.top()
                # 人脸大小的宽度
                width = d.right() - d.left()
                shape = predictor(img_gray, d)
                # 48-67 为嘴唇部分
                for i in range(48, 68):
                    x.append(shape.part(i).x)
                    y.append(shape.part(i).y)
                # 根据人脸的大小扩大嘴唇对应口罩的区域
                y_max = int(max(y) + height / 3)
                y_min = int(min(y) - height / 3)
                x_max = int(max(x) + width / 3)
                x_min = int(min(x) - width / 3)
                size = ((x_max - x_min), (y_max - y_min))
                adding = mask.resize(size)
                im = Image.fromarray(im1[:, :, ::-1])  # 切换RGB格式
                # 在合适位置添加图层
                im.paste(adding, (int(x_min), int(y_min)), adding)
                output_buffer = BytesIO()
                im.save(output_buffer, format='PNG')
                base64_data = base64.b64encode(output_buffer.getvalue())
                s = base64_data.decode()
                return jsonify({"code": 200, "format": "PNG", "data": s})
        except():
            return jsonify({"code": 500})
    return "hello"


if __name__ == '__main__':
    port = 1234
    argv = sys.argv
    if len(argv) > 1:
        port = int(argv[1])
    # app.debug = True
    app.run(host='0.0.0.0', port=port)

# if __name__ == '__main__':
#     AddMask()
