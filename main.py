from server import GSIServer
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()
def play_pause(keyboard: Controller):
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)
    
server = GSIServer(("127.0.0.1", 3000), "S8RL9Z6Y22TYQK45JB4V8PHRJJMD9DS9")
server.start_server()
is_playing = True


while True:
    me = server.get_info("player")
    try:
        hp = me["state"]["health"]
        name = me["name"]
    except TypeError:
        continue # Player is not in game yet
    if hp > 0:
        if is_playing:
            play_pause(keyboard)
            is_playing = False
            print(f"Paused music as {name} have {hp} HP")
        else:
            pass
    else:
        if not is_playing:
            play_pause(keyboard)
            is_playing = True
            print(f"Played music as {name} have {hp} HP")
        else:   
            pass
    sleep(0.5)


"""
{
   "name":"AG",
   "activity":"playing",
   "forward":"None",
   "position":"None",
   "observer_slot":1,
   "team":"CT",
   "clan":"None",
   "steamid":"76561198438348309",
   "spectarget":"None",
   "state":{
      "health":100,
      "armor":0,
      "helmet":false,
      "flashed":0,
      "smoked":0,
      "burning":0,
      "money":800,
      "round_kills":0,
      "round_killhs":0,
      "equip_value":200
   }
}
""" # When person is alive

"""
{
   "name":"AG",
   "activity":"textinput",
   "forward":"None",
   "position":"None",
   "observer_slot":1,
   "team":"CT",
   "clan":"None",
   "steamid":"76561198438348309",
   "spectarget":"None",
   "state":{
      "health":0,
      "armor":0,
      "helmet":false,
      "flashed":0,
      "smoked":0,
      "burning":0,
      "money":2700,
      "round_kills":0,
      "round_killhs":0,
      "equip_value":200
   }
}
"""