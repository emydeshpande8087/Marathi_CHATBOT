import os
import openai
import json

openai.api_key = "INSERT YOUR CREDS HERE"


def sendToOpenAI(input):
  response = openai.Completion.create(
    engine="davinci",
    prompt=input,
    temperature=0.3,
    max_tokens=30,
    top_p=0.3,
    frequency_penalty=0.5,
    presence_penalty=0,
    stop=["\n\n"]
  )
  myresults = response.get('choices')
  output = json.loads(str(myresults[0]))
  print(output["text"])

cnt=0
while(True):
  if(cnt==0):
    read=input("Enter something to Ask \n --> ")
    cnt=cnt+1
  else:
    read=input()

  sendToOpenAI(read)