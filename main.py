# byvinson
import base64
import math
import sys
from io import BytesIO

import numpy as np
from PIL import Image
import cv2
import dlib
from flask import request, Flask, jsonify

app = Flask(__name__)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')
font = cv2.FONT_HERSHEY_SIMPLEX
mask = Image.open('pic/Mask5.png')

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


# 计算两点角度
def calc_angle(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    z = math.sqrt(x * x + y * y)
    angle = round(math.asin(y / z) / math.pi * 180)
    return angle


# 旋转图片
def rotate_bound(image, angle):
    # 获取图像的尺寸
    # 旋转中心
    (h, w) = image.shape[:2]
    (cx, cy) = (w / 2, h / 2)

    # 设置旋转矩阵
    M = cv2.getRotationMatrix2D((cx, cy), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # 计算图像旋转后的新边界
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # 调整旋转矩阵的移动距离（t_{x}, t_{y}）
    M[0, 2] += (nW / 2) - cx
    M[1, 2] += (nH / 2) - cy

    return cv2.warpAffine(image, M, (nW, nH))


def make_mask(im1, cols, rows):
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
        # 左至k5，右至k13，上至k31，下至k9
        y_max = int(max(y) + height / 3)
        y_min = int(min(y) - height / 3)
        x_max = int(max(x) + width / 3)
        x_min = int(min(x) - width / 3)
        size = ((x_max - x_min), (y_max - y_min))
        adding = mask.resize(size)
        angle = calc_angle(shape.part(48).x, shape.part(48).y, shape.part(54).x, shape.part(54).y)
        # y1大为逆时针，否则为顺时针
        if 0 != angle:
            if shape.part(48).y < shape.part(54).y:
                angle = -angle
            adding = adding.rotate(angle)

        # 创建全白的mask
        # m = cv2.cvtColor(np.asarray(adding), cv2.COLOR_RGB2BGR)
        # mm = 255 * np.ones(m.shape, m.dtype)
        # gg = cv2.seamlessClone(m, im1, mm, (int(x_min), int(y_min)), cv2.NORMAL_CLONE)

        im = Image.fromarray(im1[:, :, ::-1])  # 切换RGB格式
        # 在合适位置添加图层
        im.paste(adding, (x_min, y_min), adding)
        output_buffer = BytesIO()
        im.save(output_buffer, format='PNG')
        base64_data = base64.b64encode(output_buffer.getvalue())
        s = base64_data.decode()
        return jsonify({"code": 200, "format": "PNG", "data": s})
    return None


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
    return jsonify({"code": 400})


@app.route('/make', methods=["POST"])
def make():
    file_pic = request.files.get('face')
    result = None
    if file_pic:
        try:
            face = file_pic.read()
            arr = np.frombuffer(face, np.uint8)
            im1 = cv2.imdecode(arr, cv2.IMREAD_COLOR)
            # 原图的高、宽 以及通道数
            rows, cols, channel = im1.shape
            result = make_mask(im1, cols, rows)
            if None is result:
                for i in range(1, 4):
                    # 绕图像的中心旋转
                    # 参数：旋转中心 旋转度数 scale
                    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), i * -90, 1)
                    # 参数：原始图像 旋转参数 元素图像宽高
                    rotated = cv2.warpAffine(im1, M, (cols, rows))
                    result = make_mask(rotated, cols, rows)
                    if None is not result:
                        break
        except():
            return jsonify({"code": 500})
    if None is not result:
        return result
    else:
        return jsonify({"code": 400})


if __name__ == '__main__':
    port = 1234
    argv = sys.argv
    if len(argv) > 1:
        port = int(argv[1])
    # app.debug = True
    app.run(host='0.0.0.0', port=port)

# if __name__ == '__main__':
#     AddMask()
