import random
import itertools 
  
water = "💦💧🌊🤖"
plants = "🌱🌵🌿☘🌳🌲🎋🌴"
happy = "😊😃😄🤗😤🤨🥰😌"

def get_chars(l, min_chars, max_chars):
    if max_chars > len(l)+1:
        raise(ValueError("no"))
        
    return "".join(random.choice(list(itertools.combinations(l, random.randint(min_chars, max_chars)))))

def get_message_content():
    return "".join([get_chars(water, 1, 2),
                    get_chars(plants, 2, 5),
                    get_chars(happy, 1, 2)])