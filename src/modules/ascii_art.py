"""Class to store and display ASCII art with colors."""

from src.modules.colors_and_formats import RESET, GREEN, BLUE

class Ascii_Art:

    def __init__(self):
        self.RESET = RESET
        self.GREEN = GREEN
        self.BLUE = BLUE

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
        hecate_ascii= f"""
        /\\./\\
      = ({GREEN}o{RESET}.{GREEN}o{RESET}) =
        >^~^< 
        (| |)?
    """
        print(hecate_ascii)

    def ragnar(self):
        ragnar_ascii=f"""
         /\\_,,_/\\
        ( = {BLUE}O{RESET}.{BLUE}O{RESET} )=
        /  ||  ||\\
       /   V   V  \\Ⳋ
    """
        print(ragnar_ascii)

    def characters_info(self):
        # Display ASCII art for Hécate and character qualities
        print("Hecate:")
        self.hecate()

        # Print formatted table for Hécate
        print(f"| {'Hecate':<20} | {'Description':<50} |")
        print("-" * 75)
        print(f"| {'Age':<20} | {'3 years old':<50} |")
        print("-" * 75)
        print(f"| {'Size':<20} | {'Has dwarfism, 3kg':<50} |")
        print("-" * 75)
        print(f"| {'Character':<20} | {'Sociable, curious, and energetic':<50} |")
        print("-" * 75)
        print(f"| {'Activity':<20} | {'Nocturnal':<50} |")
        print("-" * 75)
        print(f"| {'Affection':<20} | {'Loving, headbutts when hungry':<50} |")
        print("-" * 75)
        print(f"| {'Appetite Level':<20} | {'Constant':<50} |")
        print("-" * 75)
        print(f"| {'Favorite Game':<20} | {'Catching hair ties':<50} |")
        print("-" * 75)
        print(f"| {'Favorite Snack':<20} | {'Churu':<50} |")
        print("-" * 75)

        # Display ASCII art for Ragnar
        print("Ragnar:")
        self.ragnar()

        # Print formatted table for Ragnar
        print(f"| {'Ragnar':<20} | {'Description':<50} |")
        print("-" * 75)
        print(f"| {'Age':<20} | {'6 years old':<50} |")
        print("-" * 75)
        print(f"| {'Size':<20} | {'Stocky, 5kg':<50} |")
        print("-" * 75)
        print(f"| {'Character':<20} | {'Fearful but protective':<50} |")
        print("-" * 75)
        print(f"| {'Activity':<20} | {'Diurnal':<50} |")
        print("-" * 75)
        print(f"| {'Affection':<20} | {'Loving but from a distance':<50} |")
        print("-" * 75)
        print(f"| {'Appetite Level':<20} | {'Low, drinks broths for kidneys':<50} |")
        print("-" * 75)
        print(f"| {'Favorite Game':<20} | {'Kicking paper balls':<50} |")
        print("-" * 75)
        print(f"| {'Favorite Snack':<20} | {'Malt':<50} |")
        print("-" * 75)


