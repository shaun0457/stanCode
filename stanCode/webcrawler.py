"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
        response = requests.get(url, headers=header)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # ----- Write your code below this line ----- #
        all_td = soup.find_all('td')
        n = 0 #同個牌評會有兩筆資料 用於判斷男女生         偶:male 奇: female
        boy = 0
        girl = 0
        for element in all_td: #element為 TD裡所有資料
            data = manipulation(element.text) #人數了有小數點要把它去掉
            if len(data) > 3 and len(data) <= 6: #第一個len為去掉排名; 第二個不知道為甚麼沒有設這條件 男生最後會有筆7位數字
                if n % 2 == 0: # 判斷是男生的人數還是女生的
                    boy += int(data)
                    n += 1
                    # print(data)
                else:
                    girl += int(data)
                    n += 1
        print("male: " + str(boy))
        print("female: " + str(girl))

def manipulation(num):
    ans = ''
    for ch in num:
        if ch.isdigit():
            ans += ch
    return ans


if __name__ == '__main__':
    main()
