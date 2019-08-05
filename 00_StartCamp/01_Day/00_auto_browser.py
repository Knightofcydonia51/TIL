import webbrowser
import requests

# webbrowser.open_new('https://google.com')
# webbrowser.open_new_tab('https://naver.com')

# idol=["슬기", "예리", "아이린", "조이"]

# for i in idol:
#     webbrowser.open_new('https://search.naver.com/search.naver?query={}'.format(i))

requests.get("http://naver.com").status_code