from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import User


class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id:
            res = User.objects.filter(pk=id).values('username', 'age', 'gender')
            if res:
                return Response({
                    'state': 200,
                    'message': '查询成功',
                    'results': res,
                })
        else:
            res = User.objects.all().values('username', 'age', 'gender')
            return Response({
                'state': 200,
                'message': '查询成功',
                'results': list(res),
            })

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        if username and age and password:
            if gender:
                User.objects.create(username=username, age=age, gender=gender, password=password)
            res = User.objects.create(username=username, age=age, password=password)
            return Response({
                'state': 200,
                'message': '添加成功',
                'result': {'username': res.username, 'age': res.age, 'gender': res.gender},
            })
        return Response({
            'state': 400,
            'message': '添加失败',
        })

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id:
            User.objects.filter(pk=id).delete()
            return Response({
                'state': 200,
                'message': '删除成功',
            })
        else:
            User.objects.all().delete()
            return Response({
                'state': 200,
                'message': '删除成功',
            })
