from django.shortcuts import render

# Create your views here.
from app01 import models,serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from django.http import Http404



from rest_framework import mixins
from rest_framework import generics



# class PublisherList(generics.ListCreateAPIView):
#     queryset = models.Publisher.objects.all()
#     serializer_class = serializers.PulisherSerializer
#
#
# class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Publisher.objects.all()
#     serializer_class = serializers.PulisherSerializer



# # 混合类方法，简化了get和post方法的编写
# class PublisherList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = models.Publisher.objects.all()
#     serializer_class = serializers.PulisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# # 要继承APIView这个类
# class PublisherList(APIView):
#     """
#     列出所有的出版社或者创建一个新的出版社
#     """
#     def get(self, request, format=None):
#         queryset = models.Publisher.objects.all() # 查询出所有出版社
#         s = serializers.PulisherSerializer(queryset, many=True)
#         return Response(s.data)
#
#     def post(self, request, format=None):
#         s = serializers.PulisherSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#

# # 混合类方法，简化了get、put和delete方法的编写
# class PublisherDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = models.Publisher.objects.all()
#     serializer_class = serializers.PulisherSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class PublisherDetail(APIView):
#     """
#     针对单个出版社，进行查看、修改、删除
#     """
#     def get_object(self, pk):
#         try:
#             return models.Publisher.objects.get(pk=pk)
#         except models.Publisher.DoesNotExist:
#             raise Http404
#
#     # 查看具体的某一个出版社信息
#     def get(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         s = serializers.PulisherSerializer(publisher)
#         return Response(s.data)
#
#     # 修改
#     def put(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         s = serializers.PulisherSerializer(publisher, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # 删除
#     def delete(self, request, pk, format=None):
#         publisher = self.get_object(pk)
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#










# #
# # 装饰器，里面写被允许的请求方法（如果是PUT方法，则抛出异常）
# @api_view(['GET','POST'])
# def publisher_list(request):
#     """
#     列出所有的出版社，或者创建一个新的出版社
#     """
#
#     # 如果是获取所有的出版社
#     if request.method == "GET":
#         queryset = models.Publisher.objects.all() # 取出所有的出版社
#         s = serializers.PulisherSerializer(queryset, many=True)
#         return Response(s.data)
#
#     # 如果是创建新的出版社
#     elif request.method == 'POST':
#         s = serializers.PulisherSerializer(data=request.data)
#         if s.is_valid(): # 如果数据有效
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def publisher_detail(request, pk):
#     """
#     获取，更新或删除一个出版社实例
#     """
#     try: # 获取一个出版社，要传一个出版社编号（pk）进来
#         publisher = models.Publisher.objects.get(pk=pk) # pk就是出版社的编号，127.0.0.1:8000/publisher/'pk'
#     except models.Publisher.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         s = serializers.PulisherSerializer(publisher)
#         return Response(s.data)
#
#     elif request.method == 'PUT':  # 是put就要更新
#         s = serializers.PulisherSerializer(publisher, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#

def publisher_list(request):

    # 取出model数据库里的文件
    queryset = models.Publisher.objects.all()

    # # 把每一个对象手动转化成字典
    # data = []
    # for i in queryset:
    #     p_temp = {
    #         "name":i.name,
    #         "address":i.address,
    #     }
    #     data.append(p_temp)

    # 利用model_to_dict自动把对象转化成字典格式，就不需要把对象一个个列出来
    # 缺点是图片等没法转化成字典
    data = []
    from django.forms.models import model_to_dict
    for i in queryset:
        data.append(model_to_dict(i))


    import json
    # 把列表形式的data转成json格式
    return HttpResponse(json.dumps(data), content_type="application/json")

    # # 序列化方法直接转化成json，不需要json.dumps把字典类型的data再转换为json
    # from django.core import serializers
    # data = serializers.serialize("json", queryset)
    # return HttpResponse(data, content_type="application/json")
    #
    #
    #
    #
    # serializer = serializers.PulisherSerializer(queryset, many=True)
    # import json
    # # # 把列表形式的data转成json格式
    # return HttpResponse(json.dumps(serializer.data), content_type="application/json")
