import cv2

img = cv2.imread('screenshot.jpg')
cv2.imshow('img',img)
cv2.waitkey(0)
cv2.destoryAllWindows()

#サイズの変更
#v2.resize(元画像, (幅, 高さ))
img = cv2.imread('block.jpg')
height = img.shape[0]
width = img.shape[1]

#グレースケールにする
cv2.resize(元画像, cv2.COLOR_RGBA2GRAY)

#エッジ検出
cv2.Canny(元画像, パラメータ1, パラメータ2)

#画像の保存
cv2.imwrite(ファイルパス, 画像オブジェクト)

#円の検出
import cv2
import sy2

img = cv2.imread('road_sign.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny_img = cv2.Ganny(Gray_img, 600, 650)

circles = cv2.HoughCircles(canny_img, cv2. #円の検出
HOUGH_GRADIENT, dp=1, minDist=10, param1=700, 
param2=27, minRadius=20, maxRadius=60)

if circles is None: #if nothing detected. finish procesing 
    sys.exit()

for (x,y,r) in circles[0]:
    cv2.circle(img, (inx(x),int(y),int(r),(0,255,0),6))

cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 円の情報を返す　HoughCircles(対象とする画像, cv2.HOUGH_GRADIENT, dp, minDist, param1, param2, minRadius, maxRadius)
# 画像オブジェクトの上に、指定された中心、半径、色、線の太さで、円を描画するcv2.circle(画像オブジェクト, (中心のx座標, 中心のy座標), 半径, 色情報, 線の太さ)


