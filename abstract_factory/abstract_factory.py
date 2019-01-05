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

class Sushi:
    def __init__(self, neta, topping):
        self.neta = neta
        self.topping = topping
    


class SushiFactory:
    



def _main():
    salmon = create_sushi(SalmonSushiFactory())
    tamago = create_sushi(TamagoSushiFactory())

    print(salmon)
    print(tamago)
    
if __name__ == "__main__":
    _main()
    