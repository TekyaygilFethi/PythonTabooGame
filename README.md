# Python Taboo Game
Python Taboo game is a classical Taboo game contains Turkish words. If you want to english version of this game, you have to change this code:

```python
for k,v in loaded_dict.items():
    k = translator.translate(k, dest="tr").text
    v = [translator.translate(v_single, dest="tr").text for v_single in v if v_single != '']
    alldata[k] = v
```
into this:
```python
for k,v in loaded_dict.items():
    alldata[k] = v
```
in ```preparejson.py``` file. This project converts English words to Turkish words with the help of Google's Translator module.

# Run on computer
1. Clone the repository to your computer

```bash
  git clone https://github.com/TekyaygilFethi/PythonTabooGame.git
```

2. Go to cloned folder via cd.
```cd {cloned folder}```

3. Install necessary google translate module via pip:
```bash
  pip install googletrans
```

4. If you want to create your own version of Taboo (it differs with language) you can either do it on English (which shown in above) or use your own language via changing the ```dest="tr"``` to ```dest="{your desired language code}"```. You can check all the supported languages with executing this line: ```print(googletrans.LANGUAGES)```. Once you changed this part, you need to uncomment the ```preparejson.prepare_json()``` line and run this command from terminal:
```bash
  python main.py
```
5. This execution may be take a while, please wait patiently!
6. Then start main.py file via running this command on the terminal:
```bash
  python main.py
```
7. The game asks you for the limit. Set the limit. If one of the teams approach this score, the game will be over and this team will be the winner.
8. If you want to quit while game is on, press q and then Enter, otherwise press only Enter (you can type anything except q if you want it won't affect the result)
9. So the first team will start and you are good to go!
