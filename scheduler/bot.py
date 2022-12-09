import requests, json, random, logging

logger = logging.getLogger('my')

def select_id(num):
    bot_info = []
    for _ in range(num):
        bot = {
            'login_id':f"bot{random.randint(1,10)}",
            'password':"1111"
        }
        bot_info.append(bot)
    return bot_info

def get_accessKey(bot_info):
    accessKey = []
    for bot in bot_info:
        response = requests.post('http://127.0.0.1:8000/user/signin/', json=bot)
        json_ = json.loads(response.text)
        accessKey.append(json_['token']['access'])
    return accessKey

def create_post(accessKey):
    post_info_id = []
    for key in accessKey:
        idx = random.randint(1, 101)
        header = {'Authorization':f"Bearer {key}"}
        data = {
            'title':f'Bot {idx}',
            'body':f'아무거나 적어놓는 {idx} 뭔가를 적어놔야하는데 뭘적을까ㅣ요'
        }
        response = requests.post('http://127.0.0.1:8000/blog/create/', json=data, headers=header)
        print(response.text)
        text = json.loads(response.text)
        post_info_id.append(text['id'])    
    return post_info_id

def destroy_post(post_info_id, accessKey):
    for bot, key in zip(post_info_id, accessKey):
        header = {'Authorization':f"Bearer {key}"}
        response = requests.delete(f'http://127.0.0.1:8000/blog/{bot}', headers=header)

def bot_schedule(num):
    bots = select_id(num)
    accesskey = get_accessKey(bots)
    post_info = create_post(accesskey)
    destroy_post(post_info, accesskey)


bot_schedule(2)