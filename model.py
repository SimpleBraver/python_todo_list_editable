#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

def get_todos():

    # 参数分别为：地址，用户名，密码，数据库名称
    db = pymysql.connect("localhost", "root", "root", "todo")
    cursor = db.cursor()
    cursor.execute("SELECT * from todo_list")
    data = cursor.fetchall()
    db.close()
    return data

def new_todo(text):
    db = pymysql.connect("localhost", "root", "root", "todo")
    cursor = db.cursor()
    try:
        sql = "INSERT INTO todo_list (title) VALUES('%s')" %(text);
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

def del_todo(id):
    db = pymysql.connect("localhost", "root", "root", "todo")
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM todo_list WHERE id = '%s'"%id)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

def get_todo(id):
    db = pymysql.connect("localhost", "root", "root", "todo")
    cursor = db.cursor()
    try:
        sql = "SELECT * from todo_list WHERE id = '%s'"%id
        cursor.execute(sql)
        todo = cursor.fetchall()
        print 'todo===',todo[0]
        return todo[0]
    except:
        db.rollback()
    finally:
        db.close()

def update_todo(id, text):
    db = pymysql.connect("localhost", "root", "root", "todo")
    cursor = db.cursor()
    try:
        sql = "UPDATE todo_list set title = '%s' WHERE id = '%s'"%(text,id);
        print  'sql===',sql;
        # sql = "UPDATE todo_list set title = 'kkkkkooooooooooo' WHERE id = '7'"
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()