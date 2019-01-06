#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

# 最上位の名前空間を汚さないようにします
# --->> インナークラスにする.


class HouseFactory:

    @classmethod
    def make_wall(Class, color):
        return Class.Wall(color)
    
    @classmethod
    def make_roof(Class, color):
        return Class.Roof(color)
    
    @classmethod
    def make_house(Class, wall, roof):
        return Class.House(wall=wall, roof=roof)


    class House:
        def __init__(self, wall, roof):
            self.wall = wall
            self.roof = roof

        def __str__(self):
            return str(self.wall) + "と" + str(self.roof) + "でできた家"

    class Roof:
        def __init__(self, color):
            self.color = color
        
        def __str__(self):
            return self.color + "い屋根"


    class Wall:
        def __init__(self, color):
            self.color = color
        
        def __str__(self):
            return self.color + "い壁"
    

class JapaneseHouseFactory(HouseFactory):

    class Roof:
        def __init__(self, color):
            self.color = color
        
        def __str__(self):
            return self.color + "い瓦の屋根" 
        
    class Wall:
        def __init__(self, color):
            self.color = color
        
        def __str__(self):
            return self.color + "い草の壁"



class WesternHouseFactory(HouseFactory):

    class Roof:
        def __init__(self, color):
            self.color = color
        
        def __str__(self):
            return self.color + "い洋風の屋根"


    class Wall:
        def __init__(self, color):
            self.color = color
        
        
        def __str__(self):
            return self.color + "い石の壁"
    

def create_house(factory):
    wall = factory.make_wall("白")
    roof = factory.make_roof("赤")
    house = factory.make_house(wall, roof)
    return house


def _main():
    house = create_house(HouseFactory)
    japanese_house = create_house(JapaneseHouseFactory)
    western_house  = create_house(WesternHouseFactory)
    print(house)
    print(japanese_house)
    print(western_house)
    for item in globals():
        print(item)

if __name__ == "__main__":
    _main()