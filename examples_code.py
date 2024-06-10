"""
Examples git directory
Created on Tue Jun  4 15:33:54 2024
@author: mlabuss
"""
print('Hello SICSS summer school')



import random 
# Not recommended
def roll_dice():
    return random.randint(0, 4)  
            # what is 4 supposed to represent?

# Recommended
DICE_SIDES = 4

def roll_dice():
    return random.randint(0, DICE_SIDES)

def custom_function(x):
    if x<=0:
        raise ValueError("Value x should be strictly positive")
    else:
        return np.log(x)+1/np.exp(x)
        

def update_df(df: pd.DataFrame, 
              clf: str, 
              acc: float,
              split:float = 0.5,
              remarks: List[str] = []
              ) -> pd.DataFrame:
    
    
    
    