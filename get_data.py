import os
import requests

url = r'http://guba.eastmoney.com/interface/GetData.aspx'


def get_question_answer_pairs(code):
    if not os.path.exists('./output'):
        os.makedirs('./output')

    with open(f'./output/{code}.txt', mode='w') as f:
        f.write('')
    for i in range(1, 20):
        data = dict(param=f'code={code}&ps=15&p={i}&qatype=1', path='question/api/Info/Search', env=2)

        header = {'Referer': f'http://guba.eastmoney.com/qa/qa_search.aspx?company={code}&keyword=&questioner=&qatype=1',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40)'}

        response = requests.post(url=url, headers=header, data=data)

        response_json = response.json()
        with open(f'./output/{code}.txt', mode='a') as f:
            for record in response_json['re']:
                try:
                    f.write('发表时间(publish time): ' + record['post_publish_time'] + '\t' + '展示时间(display time): ' + record['post_display_time'] + '\n')
                    f.write(record['user_nickname'] + ': ' + record['ask_question'] + '\n')
                    f.write(record['ask_answer'] + '\n'*2)
                except IndexError:
                    pass


if __name__ == '__main__':
    code = 600519
    get_question_answer_pairs(code=code)