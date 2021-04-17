import cv2 as cv



def intToBinary(x):
    answer = ""
    while x>0:
        m = x%2
        answer = str(m) + answer
        x //= 2
    return answer

def asciiToBinary(x):
    x = ord(x)
    answer = intToBinary(x)
    while len(answer) < 8:
        answer = "0" + answer
    return answer

def convertTextToBinary(text):
    b = ""
    for i in text:
        b += asciiToBinary(i)
    return b

def binaryToAscii(b):
    n = 8
    power = (2**(n-1))
    number = 0
    for i in b:
        number += (power * (ord(i)-48))
        power //= 2
    return chr(number)

def embedTextToImage(img,text):
    [n,m,l] = img.shape
    textPointer = 0
    done = 0
    for i in range(0,n,1):
        for j in range(0,m,1):
            for k in range(0,l,1):

                im = 1 if img[i][j][k]&1 else 0

                if text[textPointer] == '0':
                    if im == 1:
                        img[i][j][k] -= 1 
                else:
                    if im == 0:
                        img[i][j][k] += 1

                textPointer += 1

                if textPointer == len(text):
                    done = 1
                    break
            if done :
                break
        if done :
            break
    return img

def extractImage(img):
    [n,m,l] = img.shape
    temp = ""
    text = ""
    done = 0
    for i in range(0,n,1):
        for j in range(0,m,1):
            for k in range(0,l,1):
                im = 1 if img[i][j][k]&1 else 0

                temp += str(im)

                if len(temp) == 8:
                    c = binaryToAscii(temp)
                    if c == '$':
                        done = 1
                        break 
                    text += c
                    temp = ""
            if done :
                break
        if done :
            break

    return text


if __name__ == "__main__":
    img = cv.imread('hope.PNG')
    text = input()
    text = text + "$"
    p = convertTextToBinary(text)
    # print(p)
    embed_img = embedTextToImage(img,p)
    cv.imwrite('encoded.PNG',embed_img)
    message = extractImage(embed_img)
    print(message)
