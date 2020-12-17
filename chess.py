# -*- coding: utf-8 -*-

def compare_colors(k, l, m, n): #функция распознания цвета
    if (k+l) % 2 == (m+n) % 2:
        print('1) Поля одного цвета')
    else:
        print('1) Поля разных цветов')

def check_queen(k, l, m, n): #функция нахождения ферзя
    print('2) На поле (к, I) расположен ферзь. Угрожает ли он полю (m, n)?')
    if (k == m) or (l == n) or abs(k - m) == abs(l - n):
        print("   ДА")
    else:
        print("   НЕТ")


def check_knight(k, l, m, n): #функция нахождения коня
    print('3)  На поле (к, I) расположен конь. Угрожает ли он полю (m, n)?')
    if ((abs(abs(k - m) - 2) == 0) and (abs(abs(l - n) - 1) == 0) or (abs(abs(k - m) - 1) == 0) and (abs(abs(l - n) - 2) == 0)):
        print('   ДА')
    else:
        print("   НЕТ")


def check_rook_move(k, l, m, n): #функция проверки хода ладьи
    print("4) Можно ли с поля (k, I) одним ходом ладьи попасть на поле (m, n)?")
    if k == m or l == n:
        print("   ДА, возможно")
    else:
        print(f"    НЕТ, сначала вам нужно переместиться на ({k}, {n})")


def check_queen_move(k, l, m, n): #функия проверки хода ферзя
    print("5) Можно ли с поля (k, I) одним ходом ферзя попасть на поле (m, n)?")
    if (k == m) or (l == n) or abs(k - m) == abs(l - n):
        print("   ДА, возможно")
    elif (k + l) % 2 == (m + n) % 2:
        x = (k + l + m - n) // 2
        y = (k + l - m + n) // 2
        if x > 8 or x < 1 or y > 8 or y < 1:
            x = (m + n + k - l) // 2
            y = (m + n - k + l) // 2
        print(f'    НЕТ, сначала вам нужно переместиться на ({x}, {y})')
    else:
        print(f"    НЕТ, сначала вам нужно переместиться на ({k}, {n})")


def check_bishop_move(k, l, m, n): #функция проверки хода слона
    print("6)  Можно ли с поля (k, I) одним ходом слона попасть на поле (m, n)?")
    if (k + l) % 2 == (m + n) % 2:
        if abs(k - m) == abs(l - n):
            print("   ДА, возможно")
        else:
            x = (k + l + m - n) // 2
            y = (k + l - m + n) // 2
            if x > 8 or x < 1 or y > 8 or y < 1:
                x = (m + n + k - l) // 2
                y = (m + n - k + l) // 2
            print(f'   НЕТ, сначала вам нужно переместиться на ({x}, {y})')
    else:
        print("   НЕТ, поля разных цветов")


