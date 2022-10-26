```python
from PIL import Image
import numpy as np
```

Импортируем библиотеки для работы с изображением


```python
image = Image.open('miku.jpg')
```

Указываем изображением, с которым будем работать


```python
x = np.array(image, dtype = np.float32)
red = x[:,:,0]
green = x[:,:,1]
blue = x[:,:,2]
```

Создаем наш массив для работы с цветовыми каналами RGB


```python
U_red, S_red, V_red = np.linalg.svd(red, full_matrices = False)
U_green, S_green, V_green = np.linalg.svd(green, full_matrices = False)
U_blue, S_blue, V_blue = np.linalg.svd(blue, full_matrices = False)
print(x.shape)
```

    (1261, 2048, 3)
    

И делаем SVD разложение по цветам


```python
for i in range(1,400,40):
    Y_i_red = U_red[:,:i].dot(np.diag(S_red[:i])).dot(V_red[:i,:]) 
    Y_i_red[Y_i_red < 0] = 0
    Y_i_red[Y_i_red > 255] = 255
    Y_i_red = Y_i_red.reshape(1261, 2048, 1)
    Y_i_green = U_green[:,:i].dot(np.diag(S_green[:i])).dot(V_green[:i,:]) 
    Y_i_green[Y_i_green < 0] = 0
    Y_i_green[Y_i_green > 255] = 255
    Y_i_green = Y_i_green.reshape(1261, 2048, 1)
    Y_i_blue = U_blue[:,:i].dot(np.diag(S_blue[:i])).dot(V_blue[:i,:]) 
    Y_i_blue[Y_i_blue < 0] = 0
    Y_i_blue[Y_i_blue > 255] = 255
    Y_i_blue = Y_i_blue.reshape(1261, 2048, 1)
    Y_i = np.concatenate((np.concatenate((Y_i_red, Y_i_green), axis = 2), Y_i_blue), axis = 2)
    Image.fromarray(np.asarray(Y_i, dtype = np.uint8)).save(f'{i}.jpg')
```

И создаем цикл преобразования нашей картинки, путем преобразования наших матриц и сохранения их в отдельные картинки
