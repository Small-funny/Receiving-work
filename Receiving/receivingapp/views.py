# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.forms import fields
from django import forms
from django.http import JsonResponse
import os


class UploadForm(forms.Form):
    user = fields.CharField()
    img = fields.FileField()


def upload1(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    else:
        files = request.FILES.get('f1')
        if files:
            f = open('软工1601班软件项目开发实训作业/' + files.name, 'wb')
            for line in files.chunks():
                f.write(line)
            f.close()
            return HttpResponse('文件 '+files.name+'('+str(files.size)+'B)'+' 已上传至 软工1601班软件开发实训 作业中！')

        files = request.FILES.get('f2')
        if files:
            f = open('软工1601班编译原理作业/' + files.name, 'wb')
            for line in files.chunks():
                f.write(line)
            f.close()
            return HttpResponse('文件 '+files.name+'('+str(files.size)+'B)'+' 已上传至 软工1601班编译原理 作业中！')

        files = request.FILES.get('f3')
        if files:
            f = open('软工1601班学术论文指导写作作业/' + files.name, 'wb')
            for line in files.chunks():
                f.write(line)
            f.close()
            return HttpResponse('文件 '+files.name+'('+str(files.size)+'B)'+' 已上传至 软工1601班学术论文指导写作 作业中！')

        files = request.FILES.get('f4')
        if files:
            f = open('软工1601班高级程序设计作业/' + files.name, 'wb')
            for line in files.chunks():
                f.write(line)
            f.close()
            return HttpResponse('文件 '+files.name+'('+str(files.size)+'B)'+' 已上传至 软工1601班高级程序设计 作业中！')

        files = request.FILES.get('f5')
        if files:
            f = open('软工1601班文件1/' + files.name, 'wb')
            for line in files.chunks():
                f.write(line)
            f.close()
            return HttpResponse('文件 '+files.name+'('+str(files.size)+'B)'+' 已上传至 附加文件夹一 中！')

        files = request.FILES.get('f6')
        if files:
            f = open('软工1601班文件2/' + files.name, 'wb')
            for line in files.chunks():
                f.write(line)
            f.close()
            return HttpResponse('文件 ' + files.name + '(' + str(files.size) + 'B)' + ' 已上传至 附加文件夹二 中！')

        return HttpResponse('上传失败！')

'''
def show_files(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    else:
        data = request.POST.get('find')
        list = []
        if not data:
            return HttpResponse('请选择查询目标！')
        print(data)
        if data == '软件项目开发实战':
            list = os.listdir('../软工1601班软件项目开发实训作业')
        elif data == '研究方法与学术论文指导':
            list = os.listdir('../软工1601班学术论文指导写作作业')
        elif data == '编译原理':
            list = os.listdir('../软工1601班编译原理作业')
        elif data == '高级程序设计':
            list = os.listdir('../软工1601班高级程序设计作业')
        elif data == '文件一':
            list = os.listdir('../软工1601班文件1')
        elif data == '文件二':
            list = os.listdir('../软工1601班文件2')
        dic = {}
        num = 1
        for i in list:
            dic[str(num)] = i
            num += 1
        return JsonResponse(dic)
'''
