from AutoHotPy import AutoHotPy
from InterceptionWrapper import *
import win32gui
import time

# CONFIGURATION
HEALING_POT_KEY = 0  # Change accordingly
MANA_POT_KEY = 9  # Change accordingly
HEAL_PARTY_MEMBER_KEY = 2  # Change accordingly
start_time=0

# Available pages -> F1, F2, F3, F4, F5, F6, F7
ACTIVE_SKILL_PAGES = {
    #'F4': [1,2,3,4,5]  # Change accordingly
    'F1':[2]
}

# Be careful not to overlap any skills with your HEAL/MANA pot keys

# One skill page with F4 example is below
# ACTIVE_SKILL_PAGES = {
#     'F4': [3, 4, 5, 6]
# }

ENABLE_R_HITS = True  # Change it to True for basic attacks

# Do not change anything below this line
SELF_HP_X = 195
SELF_HP_Y = 46

SELF_MP_X = 180
SELF_MP_Y = 66

MONSTER_HP_X=960-30
MONSTER_HP_y=46

FIRST_PARTY_MEMBER_X = 1799
FIRST_PARTY_MEMBER_Y = 258
CURRENT_PARTY = []
PARTY_VALID_R = 159
PARTY_VALID_G = 57
PARTY_VALID_B = 39
PARTY_MEMBER_OFFSET_Y = 145

repeat_always = False
is_r_used=False

SELECTED_RUNTIME_CONFIGURATION = 0  # None
TIME_DELAY_BETWEEN_SKILLS = 0.1  # in seconds

HP_R = 0
HP_G = 0
HP_B = 0
MP_R = 0
MP_G = 0
MP_B = 0

# END CONFIGURATION


### AutoHotPy Configuration Part ###
def exitAutoHotKey(autohotpy, event):
    """
    exit the program when you press ESC
    """
    autohotpy.stop()


def alwaysLoopMacro(autohotpy, event):
    global repeat_always
    """
        WHERE EVERYTHING STARTS AT
    """
    #    1: Archer 2: Asas 3: Warrior 4: Mage 5: Priest Heal 6: Only auto hp/mp
    # useAttackConfiguration(autohotpy)
    global TIME_DELAY_BETWEEN_SKILLS
    if SELECTED_RUNTIME_CONFIGURATION == 1:
        # Archer
        TIME_DELAY_BETWEEN_SKILLS = 0.7
        useAttackConfiguration(autohotpy)
    elif SELECTED_RUNTIME_CONFIGURATION == 2:
        # Asas
        TIME_DELAY_BETWEEN_SKILLS = 0.4
        useAttackConfiguration(autohotpy)
    elif SELECTED_RUNTIME_CONFIGURATION == 3:
        # Warrior
        TIME_DELAY_BETWEEN_SKILLS = 0.1
        useAttackConfiguration(autohotpy)
    elif SELECTED_RUNTIME_CONFIGURATION == 4:
        # Mage
        TIME_DELAY_BETWEEN_SKILLS = 0.1
        useAttackConfiguration(autohotpy)
    elif SELECTED_RUNTIME_CONFIGURATION == 5:
        # Priest Heal
        TIME_DELAY_BETWEEN_SKILLS = 1.4
        priestHeal(autohotpy)
    elif SELECTED_RUNTIME_CONFIGURATION == 6:
        checkHealth(autohotpy)
        checkMana(autohotpy)

    else:
        useAttackConfiguration(autohotpy)

    # now that we are finished, let's check if we should loop
    # If repeat_always= true, then we tell autohotpy to run loopMacro again
    if repeat_always:
        autohotpy.run(alwaysLoopMacro, event)


def enableDisableLoopMacro(autohotpy, event):
    global start_time
    global repeat_always
    global is_r_used
    global HP_R, HP_G, HP_B, MP_R, MP_G, MP_B
    HP_R, HP_G, HP_B = readPixel(SELF_HP_X, SELF_HP_Y)
    MP_R, MP_G, MP_B = readPixel(SELF_MP_X, SELF_MP_Y)
    print("Recorded HP values -> RGB: {}, {}, {}".format(HP_R, HP_G, HP_B))
    print("Recorded MP values -> RGB: {}, {}, {}".format(MP_R, MP_G, MP_B))
    
    repeat_always =not(repeat_always)
    is_r_used=False

        # let's enable it, and then we call it for the first time, so it starts running as soon as possible
    if repeat_always:
        alwaysLoopMacro(autohotpy, event)


### END AutoHotPy Configuration Part ###

# Preset Configurations for all classes

def priestHeal(autohotpy):
    # Discover how many people in the party atm
    CURRENT_PARTY.clear()
    for i in range(0, 8):  # There can be maximum 8 people in a party
        currentY = FIRST_PARTY_MEMBER_Y + (PARTY_MEMBER_OFFSET_Y * i)
        r, g, b = readPixel(FIRST_PARTY_MEMBER_X, currentY)
        if r == PARTY_VALID_R and g == PARTY_VALID_G and b == PARTY_VALID_G:
            # We have detected a member
            CURRENT_PARTY.append((FIRST_PARTY_MEMBER_X, currentY))

    print("Detected {} party members".format(len(CURRENT_PARTY)))

    # Detect low hps and heal them
    for i in range(0, len(CURRENT_PARTY)):
        checkPartyMemberHealth(
            autohotpy, CURRENT_PARTY[i][0], CURRENT_PARTY[i][1])
        time.sleep(0.4)
        # Recover yourselfz
        checkHealth(autohotpy)
        checkMana(autohotpy)


def useAttackConfiguration(autohotpy):
    global TIME_DELAY_BETWEEN_SKILLS
    global start_time
    global is_r_used

    checkHealth(autohotpy)
    checkMana(autohotpy)
    for skillPage, skillArray in ACTIVE_SKILL_PAGES.items():
        useSkill(autohotpy, skillPage)
        for i in range(0, len(skillArray)):
            
            useSkill(autohotpy, 'z')
            useSkill(autohotpy, skillArray[i])
            if ENABLE_R_HITS:
                isMonsterHpLow=checkMonsterHealtLow()
            
                if (not isMonsterHpLow and not is_r_used):
                    is_r_used=True
                    time.sleep(0.1)
                    useSkill(autohotpy, 'r')

                if(isMonsterHpLow):
                    is_r_used=False
                    
            time.sleep(TIME_DELAY_BETWEEN_SKILLS)
            print(time.time()-start_time);
            




# END Preset Configurations for all classes

# In-Game Helper functionssz


def getPressByKey(autohotpy, key):
    KEY_MAP = {
        0: autohotpy.N0,
        1: autohotpy.N1,
        2: autohotpy.N2,
        3: autohotpy.N3,
        4: autohotpy.N4,
        5: autohotpy.N5,
        6: autohotpy.N6,
        7: autohotpy.N7,
        8: autohotpy.N8,
        9: autohotpy.N9,
        'a': autohotpy.A,
        's': autohotpy.S,
        'd': autohotpy.D,
        'w': autohotpy.W,
        'z': autohotpy.Z,
        'x': autohotpy.X,
        'u': autohotpy.U,
        'r': autohotpy.R,
        'e': autohotpy.E,
        'F1': autohotpy.F1,
        'F2': autohotpy.F2,
        'F3': autohotpy.F3,
        'F4': autohotpy.F4,
        'F5': autohotpy.F5,
        'F6': autohotpy.F6,
        'F7': autohotpy.F7
    }
    return KEY_MAP[key]


def click(autohotpy, x, y):
    autohotpy.moveMouseToPosition(x, y)
    # I highly suggest you to open InterceptionWrapper to read which attributes this class has
    stroke = InterceptionMouseStroke()

    # To simulate a mouse click we manually have to press down, and release the buttons we want.
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN
    autohotpy.sendToDefaultMouse(stroke)
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_LEFT_BUTTON_UP
    autohotpy.sendToDefaultMouse(stroke)


def useSkill(autohotpy, key):
    keyToPress = getPressByKey(autohotpy, key)
    keyToPress.press()


def readPixel(x, y):
    if x >= 1920:
        x = 1919
    if y >= 1080:
        y = 1079
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    r, g, b = rgbint2rgbtuple(color)
    return r, g, b

def checkMonsterHealtLow():
    global HP_R
    x, y = MONSTER_HP_X, MONSTER_HP_y
    r, g, b = readPixel(x, y)
    if(r+10<HP_R):
        return True
    else:
        return False

def checkMana(autohotpy):
    global MP_R, MP_G, MP_B
    x, y = SELF_MP_X, SELF_MP_Y
    r, g, b = readPixel(x, y)
    # print("Checking mana with RGB: {}, {}, {} against {}, {}, {}".format(r, g, b, MP_R, MP_G, MP_B))
    if r == MP_R and g == MP_G and b == MP_B:
         print("\n")
     #   print("MP is above 35%")
    else:
    #    print("Using MP with KEY {}".format(MANA_POT_KEY))
        useSkill(autohotpy, MANA_POT_KEY)


def checkHealth(autohotpy):
    global HP_R, HP_G, HP_B
    x, y = SELF_HP_X, SELF_HP_Y
    r, g, b = readPixel(x, y)
    #print("Checking health with RGB: {}, {}, {} against {}, {}, {}".format( r, g, b, HP_R, HP_G, HP_B))
    if r == HP_R and g == HP_G and b == HP_B:
         print("\n")
       # print("HP is above 40%")
    else:
      #  print("Using HP with KEY {}".format(HEALING_POT_KEY))
        useSkill(autohotpy, HEALING_POT_KEY)


def checkPartyMemberHealth(autohotpy, x, y):
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    r, g, b = rgbint2rgbtuple(color)
    if r < 75:
        print("Party member [{},{}] is at RGB: {}, {}, {}".format(
            x, y, r, g, b))
        click(autohotpy, x, y)
        keyToPress = getPressByKey(autohotpy, HEAL_PARTY_MEMBER_KEY)
        keyToPress.press()


def rgbint2rgbtuple(RGBint):
    red = RGBint & 255
    green = (RGBint >> 8) & 255
    blue = (RGBint >> 16) & 255
    return (red, green, blue)


# END In-Game Helper functions

# Pre-configuration
def displayOptions():
    global start_time
    start_time=time.time()
    return int(input("1: Archer\n2: Asas\n3: Warrior\n4: Mage\n5: Priest Heal\n6: Only auto hp/mp"))


# END Pre-configuration

if __name__ == "__main__":
    auto = AutoHotPy()
    auto.registerExit(auto.F12,
                      exitAutoHotKey)  # Registering an end key is mandatory to be able tos top the program gracefully

    # Registry an entry point for our macro
    SELECTED_RUNTIME_CONFIGURATION = displayOptions()
    auto.registerForKeyDown(auto.F10, enableDisableLoopMacro)

    auto.start()
