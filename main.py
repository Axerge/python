# - * - кодировка: utf-8 - * -
import requests
import vk_api
import vk
'вместо * указать данные
message_text = 'Проверка' #здесь указать текст для поста

token = '0a0fc....5f5' 'токен
group_id = '***' #ид группы
session = vk.AuthSession(scope='wall,message,groups', app_id= '***', user_login= '***', user_password= '***') #логинимся
vk.api.access_token= token
api = vk.API(vk.Session(access_token=token), v=5.92)

foto = 'image/1.jpg' #расположение фото
upload_url = api.photos.getWallUploadServer(group_id=group_id)['upload_url'] 
resp = requests.post(upload_url, files = {'file': open(foto, 'rb')}).json()
s = api.photos.saveWallPhoto(group_id=group_id, server = resp['server'], photo= resp['photo'], hash = resp['hash']) #записывает в память фото и получаем данные на него

ss = api.wall.post(owner_id='-' + group_id, from_group='1', attachments=f"photo{s[0]['owner_id']}_{s[0]['id']}", message= message_text, v= '5.7') #постим запись

originalUrl = 'https://vk.com/club'+ group_id +'?w=wall-' + group_id + '_' + str(ss['post_id']) + '%2Fall' #получение ссылки
print('Запись успешно добавлена')
print('Ссылка: ' + originalUrl)
