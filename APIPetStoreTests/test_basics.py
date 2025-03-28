import requests, json
def test_api():
    url="https://petstore3.swagger.io/api/v3/pet/findByStatus?status=available"
    header={'Content-Type': 'application/json'}
    request =requests.get(url,verify=False, headers=header)
    DATA=request.json()
    assert request.status_code  == 200
    print(json.dumps(DATA,indent= 3))
    assert DATA['name']=='Dogs'
    request.elapsed.total_seconds()