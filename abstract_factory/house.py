#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

# https://qiita.com/HagaSpa/items/5f7ce6b666f12c2ea405
# インスタンス生成を専門に行うクラス（Factory）を作成することで、
# 関連性のあるインスタンスを間違いなく生成するためのデザインパターンのこと。
# つまりFactoryクラス毎に生成できるインスタンスが決められている実装のこと。

# http://www.techscore.com/tech/DesignPattern/AbstractFactory.html/
# 第８章では、 AbstractFactory パターンを学びます。
# AbstractFactory を日本語に直訳すると「抽象的な工場」となります。
# いったい抽象的な工場とは、どんな工場なのでしょう。
# AbstractFactory パターンとは、
# インスタンスの生成を専門に行うクラスを用意することで、
# 整合性を必要とされる一連のオブジェクト群を間違いなく生成するための
# パターンです。

# http://www.ie.u-ryukyu.ac.jp/~e085739/java.it.2.html
# Abstract Factory パターン 
# (互いに関連する一連のオブジェクト群を, 
# その具象クラスに依存しないで生成するための
# インタフェースを提供する)
# [Abstract Factory] という単語は, [抽象的工場] を意味する.
# このパターンは, 関連の一連のオブジェクト群をまとめて生成する方法を提供するパターン. 
# このパターンを適用すると, 上記関連オブジェクトグループ単位での入れ替え, 
# 追加が容易に行える.
# よく似たパターンに [Factory Method] パターンがあるが, 
# [Factory Method] パターンは,
# [オブジェクト生成] の抽象化にポイントを置いたパターンであるのに体し, 
# [Abstract Factory] パターンは, 
# [関連するオブジェクト群をまとめて生成するための手順] の抽象化にある.
# ↑この説明が一番しっくり来た.

"""
顧客は屋根と壁の色だけ指定できる.会社によって素材は変わる.
"""






class HouseFactory:
    @classmethod
    def make_wall(Class, color):
        return Wall(color)
    
    @classmethod
    def make_roof(Class, color):
        return Roof(color)
    
    @classmethod
    def make_house(Class, wall, roof):
        return House(wall=wall, roof=roof)
    pass



class JapaneseHouseFactory:

    @classmethod
    def make_wall(Class, color):
        return JapaneseWall(color)
    
    @classmethod
    def make_roof(Class, color):
        return JapaneseRoof(color)
    
    @classmethod
    def make_house(Class, wall, roof):
        return JapaneseHouse(wall=wall, roof=roof)


class WesternHouseFactory:

    @classmethod
    def make_wall(Class, color):
        return WesternWall(color)
    
    @classmethod
    def make_roof(Class, color):
        return WesternRoof(color)
    
    @classmethod
    def make_house(Class, wall, roof):
        return WesternHouse(wall=wall, roof=roof)



class JapaneseHouse:
    def __init__(self, wall, roof):
        self.wall = wall
        self.roof = roof

    def __str__(self):
        return str(self.wall) + "と" + str(self.roof) + "でできた家"


class JapaneseRoof:
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return self.color + "い瓦の屋根" 
    
class JapaneseWall:
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return self.color + "い草の壁"


class WesternHouse:
    def __init__(self, wall, roof):
        self.wall = wall
        self.roof = roof

    def __str__(self):
        return str(self.wall) + "と" + str(self.roof) + "でできた家"

class WesternRoof:
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return self.color + "い洋風の屋根"


class WesternWall:
    def __init__(self, color):
        self.color = color
    
    
    def __str__(self):
        return self.color + "い石の壁"
    

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