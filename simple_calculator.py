#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:51:39 2020

@author: apple
"""

import sys
class Matrix():
    def start():
        while True:
            print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
            choice = int(input('Your choice:'))
            if choice == 1:
                Matrix.add()
            elif choice == 2:
                Matrix.multi_const()
            elif choice == 3:
                Matrix.multi_matrix()
            elif choice == 0:
                sys.exit()
            elif choice == 4:
                Matrix.transpose()
            elif choice == 5:
                rc = input('Enter size of matrix:').split(' ')
                r = int(rc[0])
                matrix1 = []
                print('Enter matrix:')
                for i in range(r):
                    matrix1.append(input().split(' '))
                matrix2 = [[int(x) for x in matrix1[i]] for i in range(r)]
                print('The result is:')
                print(Matrix.det(matrix2))
            elif choice == 6:
                rc = input('Enter size of matrix:').split(' ')
                r = int(rc[0])
                matrix1 = []
                prit('Enter matrix:')
                for i in range(r):
                    nmatrix1.append(input().split(' '))
                matrix2 = [[int(x) for x in matrix1[i]] for i in range(r)]
                if Matrix.det(matrix2) == 0:
                    print("This matrix doesn't have an inverse.")
                else:
                    print('The result is:')
                    for item in Matrix.cofactor_matrix(matrix2):
                        print(' '.join(str(x) for x in item))
            else:
                continue
    
    def add():
        rc1 = input('Enter size of first matrix:').split(' ')
        r1 = int(rc1[0])
        c1 = int(rc1[1])
        matrix1 = []
        print('Enter the first matrix:')
        for i in range(r1):
            matrix1.append(input().split(' '))
        
        rc2 = input('Enter size of second matrix:').split(' ')
        r2 = int(rc2[0])
        matrix2 = []
        print('Enter second matrix:')
        
        for i in range(r2):
            matrix2.append(input().split(' '))
            
        mr  = ['0'] * (c1 * r1)
        
        if rc1 == rc2:
            for i in range(r1):
                for j in range(c1):
                    mr[i*c1+j] = float(matrix1[i][j]) + float(matrix2[i][j])
            matrix = []
            for i in range(r1):
                matrix.append(mr[c1*i:c1*(i+1)])
            print('The result is:')
            for item in matrix:
                print(' '.join(str(x) for x in item))
        else:
            print('The operation cannot be performed.')
    
    def multi_const():
        rc = input('Enter size of matrix:').split(' ')
        r = int(rc[0])
        c = int(rc[1])
        matrix1 = []
        print('Enter matrix:')
        for i in range(r):
            matrix1.append(input().split(' '))
        const = float(input('Enter constant:'))
        mr  = ['0'] * (c * r)
        for i in range(r):
            for j in range(c):
                mr[i*c+j] = float(matrix1[i][j]) * const
        matrix = []
        for i in range(r):
            matrix.append(mr[c*i:c*(i+1)])
        print('The result is:')
        for item in matrix:
            print(' '.join(str(x) for x in item))
        
    def multi_matrix():
        rc1 = input('Enter size of first matrix:').split(' ')
        r1 = int(rc1[0])
        c1 = int(rc1[1])
        matrix1 = []
        print('Enter the first matrix:')
        for i in range(r1):
            matrix1.append(input().split(' '))
        
        rc2 = input('Enter size of second matrix:').split(' ')
        r2 = int(rc2[0])
        c2 = int(rc2[1])
        matrix2 = []
        print('Enter second matrix:')
        
        for i in range(r2):
            matrix2.append(input().split(' '))
            
        mr  = [0] * (r1 * c2)
        
        if c1 == r2:
            for i in range(r1):
                for j in range(c2):
                    for k in range(c1):
                        mr[i*c2+j] += float(matrix1[i][k]) * float(matrix2[k][j])
        matrix = []
        for i in range(r1):
            matrix.append(mr[c2*i:c2*(i+1)])
        print('The result is:')
        for item in matrix:
            print(' '.join(str(x) for x in item))
        

        else:
            print('The operation cannot be performed.')
            
    def transpose():
        print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
        choice = int(input('Your choice:'))
        rc = input('Enter size of matrix:').split(' ')
        r = int(rc[0])
        c = int(rc[1])
        matrix1 = []
        print('Enter matrix:')
        for i in range(r):
            matrix1.append(input().split(' '))
        mr  = ['0'] * (c * r)
        matrix = []
        for i in range(r):
            matrix.append(mr[c*i:c*(i+1)])
        matrix2 = []
        for i in range(c):
            matrix2.append(mr[r*i:r*(i+1)])
        if choice == 1:
            Matrix.main_diagonal(c, r, matrix2, matrix1)
        elif choice == 2:
            Matrix.side_diagonal(c, r, matrix, matrix1)
        elif choice == 3:
            Matrix.vertical(c, r, matrix, matrix1)
        elif choice == 4:
            Matrix.horizontal(c, r, matrix, matrix1)
 
    def main_diagonal(c, r, matrix, matrix1):
        for i in range(c):
            for j in range(r):
                matrix[i][j] = matrix1[j][i]
        
        print('The result is:')
        for item in matrix:
            print(' '.join(str(x) for x in item))
                    
    def vertical(c, r, matrix, matrix1):
        for i in range(r):
            for j in range(c):
                matrix[i][j] = matrix1[i][c-1-j]
                
        print('The result is:')
        for item in matrix:
            print(' '.join(str(x) for x in item))
    
    def horizontal(c, r, matrix, matrix1):
        for i in range(r):
            for j in range(c):
                matrix[i][j] = matrix1[r-1-i][j]
        
        print('The result is:')
        for item in matrix:
            print(' '.join(str(x) for x in item))
                
    def side_diagonal(c, r, matrix, matrix1):
        for i in range(r):
            for j in range(c):
                if i + j == r-1:
                    matrix[i][j] = matrix1[i][j]
                else:
                    matrix[i][j] = matrix1[r-1-j][c-1-i]
                
        print('The result is:')
        for item in matrix:
            print(' '.join(str(x) for x in item))
    
    
    def det(m):
        if len(m) <= 0:
            return None
        if len(m) == 1:
            return m[0][0]
        else:
            s = 0
            for i in range(len(m)):
                n = [[row[a] for a in range(len(m)) if a != i] for row in m[1:]]
                if i % 2 == 0:
                    s += m[0][i] * Matrix.det(n)
                else:
                    s -= m[0][i] * Matrix.det(n)
            
            return s

                
    def cofactor_matrix(m):
        r = len(m)
        mr  = ['0'] * (r * r)
        matrix = []
        for i in range(r):
            matrix.append(mr[r*i:r*(i+1)])
        for i in range(r):
            for j in range(r):
                n = [[row[a] for a in range(len(m)) if a != j] for row in m[:i]+m[(i+1):]]
                if (i + j) % 2 == 0:
                    matrix[j][i] = round(Matrix.det(n) / Matrix.det(m), 2)
                else:
                    matrix[j][i] = round(-Matrix.det(n) / Matrix.det(m), 2)
                    
        return matrix
Matrix.start()