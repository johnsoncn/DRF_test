


from rest_framework import serializers
from app01 import models

# 自己定义一个序列化（把model里的内容重写一下，很相似）
# class PulisherSerializer(serializers.Serializer):
#     id = serializers.ImageField(read_only=True)
#     name = serializers.CharField(max_length=32)
#     address = serializers.CharField(max_length=128)
#
#     def create(self, validated_data):
#         return models.Publisher.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name",instance.name)
#         instance.address = validated_data.get("address", instance.address)
#         instance.save()
#         return instance

# 继承serializers.ModelSerializer这个类之后，就不需要跟上面一样再把models的内容重写一遍
# 只需要提取字段
class PulisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = (
            "id",
            "name",
            "address",
        )