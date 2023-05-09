prompt = "Hello, my name is"
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=50
)

generated_text = response.choices[0].text


if __name__ == "__main__":
   print(generated_text)
