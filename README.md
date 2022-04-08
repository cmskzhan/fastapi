# fastapi
pip install fastapi uvicorn python-multipart; <br>
cd fastapi; <br>
uvicorn main:app --reload

<p>
http://127.0.0.1:8000/
  <br>
http://127.0.0.1:8000/my/page/items/?page=3&limit=2&skip=2
<br>
curl -X POST "http://127.0.0.1:8000/purchase/item/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":\"sample item\",\"info\":\"This is info for the item\",\"price\":40,\"qty\":2}"
<br>Or

```python
import requests

url = 'http://localhost:8000/purchase/item/'
headers = {"accept": "application/json", "Content-Type": "application/json"}
data = {'name': 'item1', 'info':'item1_info', 'price': 40.5, 'qty':2}

x = requests.post(url, json = data, headers = headers)
```

Username/Password Form Post: 
<br>
curl -X 'POST' \
  'http://localhost:8000/accounts/login/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=aa&password=bb'
 
```python
import requests
headers = {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}
data = {
    'username': 'aa',
    'password': 'bb',
}
response = requests.post('http://localhost:8000/accounts/login/', headers=headers, data=data) 
```
  
## Doc
  http://localhost:8000/docs
