"""Class to store and display ASCII art with colors."""

from src.modules.colors_and_formats import RESET, GREEN, BLUE

class Ascii_Art:

    def __init__(self):
        self.RESET = RESET
        self.GREEN = GREEN
        self.BLUE = BLUE
        self.armchair = armchair
        self.tv = tv
        self.bio_pet = bio_pet
        self.hecate = hecate
        self.ragnar = ragnar

    def logo(self):
        """Prints the game logo with ANSI colors."""
        logo_ascii = rf"""{RESET}
                  ____   _         _____        _        
                 |  _ \ (_)       |  __ \      | |       
                 | |_) | _   ___  | |__) | ___ | |_      
                 |  _ < | | / _ \ |  ___/ / _ \| __|     
                 | |_) || || (_) || |    |  __/| |_      
                 |____/ |_| \___/ |_|     \___| \__|     
    
           {BLUE}/\_,,_/\{RESET}                                  {GREEN}/\./\
          {BLUE}( =  0.0 )={RESET}                              {GREEN}= (0.0) =
          {BLUE}/  ||  ||\{RESET}                                 {GREEN}>^~^<
         {BLUE}/   V   V  \?{RESET}                               {GREEN}(| |)?{RESET} 
        """
        print(logo_ascii)


def armchair(self):
    armchair_art= """         '--._
    .---.     '-..
   .---  )     '-..
    )  -.-           `.
  ,.|\\_=/              -._       _.
'.' /   (                  ' ,----'|---.
| |  \\  )\\                  |`-.|     |
|  \\ '_.__`---,.____.       |   |     |
| `.= ..,_'\\.\\..L__//       |   |     |
|         .'._   `--'       |   |     |
\\        .'-._\\_            '`.,|     |
 `       |    -.`.  _,..,--- `'.-----.'
  \\_____,|`-.   \\ \\.            | | 
  | |./| |./ \\  ,-.'            | |
  './  './   '...-'            |__.__|
"""
    print(armchair_art)

def tv(self):
    tv_ascii = """   .----------------------------------------------------.
  |   -----------------------------------------------    |
  | o |||                                          ||| o |
  |   |||                                          |||   |
  |.-.|||   ____   _         _____         _       |||.-.|
  | o |||  |  _ \\ (_)       |  __ \\       | |      ||| o |
  |   |||  | |_) | _   ___  | |__) |  ___ | |_     |||   |
  | o |||  |  _ \\ | | /   \\ |  ___/  / _ || |      ||| o |
  |.-.|||  | |_) || || (_) || |     |  __/| |__    |||.-.|
  | O |||  |____/ |_| \\___/ |_|      \\___| \\__|    ||| O |
  | _ |||                                          ||| _ |
  |(_)|||                                          |||(_)|
  |    -----------------------------------------------   |
   .----------------------------------------------------.'
        _||_                                   _||_
       /____\\                                 /____\\
"""
    print(tv_ascii)

def bio_pet(self):
    bio_pet= """     -----------------
  ___|||||||||||||||||___
     ||    ____     ||
     ||   |  _ \\    ||
     ||   | |_) |   ||
     ||   |  _ \\    ||
     ||   | |_) |   ||
     ||   |____/    ||
  ___||             ||___
     |||||||||||||||||
     -----------------
"""
    print(bio_pet)

def hecate(self):
    hecate_ascii= f"""    /\\./\\
  = ({GREEN}o{RESET}.{GREEN}o{RESET}) =
    >^~^< 
    (| |)?
"""
    print(hecate_ascii)

def ragnar(self):
    ragnar_ascii= f"""     /\\_,,_/\\
    ( = {BLUE}O{RESET}.{BLUE}O{RESET} )=
    /  ||  ||\\
   /   V   V  \\Ⳋ
"""
    print(ragnar_ascii)


