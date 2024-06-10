import os
disclaimer = "The info used here will not be saved by the program\n"
text = "Enter here your OPENAI api key: "
key = input(disclaimer + text)
from embedchain import App

def main():
    os.environ["OPENAI_API_KEY"] = key

    print("Configuring llm provider")
    # app = App.from_config(config=config)
    app = App()
    print("Done!")
    print()

    print("Adding contextual info...")
    source = "https://www.pg.unicamp.br/norma/31594/0"
    app.add(source, data_type="web_page")
    print("Done!")
    print()

    print("Enter 'exit' to exit the chat")
    print()
    while True:
        prompt = input("[You]: ")
        if prompt == 'exit':
            print("exiting...")
            break
        else:
            print("[Bot]: ", end = '')
            response = app.query(prompt)
            # response = response.partition("Answer:\n")[2]
            print()


    os.environ["OPENAI_API_KEY"] = '' # clears the key

if __name__ == "__main__":
    main()
