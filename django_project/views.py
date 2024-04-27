import requests
from django.shortcuts import render


def home(request):
  # USING APIS => Example 1
  reponse1 = requests.get('https://dog.ceo/api/breeds/image/random')
  data1 = reponse1.json()
  result1 = data1["message"]

  url = 'https://icanhazdadjoke.com/'
  headers = {'Accept': 'application/json'}

  response2 = requests.get(url, headers=headers)
  data2 = response2.json()
  result2 = data2["joke"]

  return render(request, 'templates/base.html', {
      'result1': result1,
      'result2': result2
  })
