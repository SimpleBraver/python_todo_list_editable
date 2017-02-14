#!/usr/bin/python
# -*- coding: UTF-8 -*-

import web
import model

# url路径，根据实际情况惊醒配置，这里简单用两种方式。
urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete',
    '/edit/(\d+)','Edit',
)

### Templates
render = web.template.render('templates', base='base')

# Index类
class Index:
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull,
                         size=30,
                         description="Post title:"),
    )

    def GET(self):
        todos = model.get_todos()
        return render.index(todos)

    def POST(self):
        # 根据输入框的name值，获取输入值
        web_data = web.input()
        txt = web_data.input_text_add
        model.new_todo(txt);

        # 跳转回首页
        raise web.seeother('/')

# 删除类
class Delete:
    def POST(self, id):
        model.del_todo(id)

        # 跳转回首页
        raise web.seeother('/')

# 编辑类
class Edit:
    def GET(self,id):
        print 'in edit get=====',id
        todo = model.get_todo(id)
        return render.edit(todo)

    def POST(self,id):

        web_data = web.input()
        txt = web_data.input_text_edit
        print 'in edit post=====',txt
        model.update_todo(id, txt);
        # 跳转回首页
        raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()