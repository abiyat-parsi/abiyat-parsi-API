from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Poets
from .serializers import poetsSerializer
import requests


class get_poets(APIView):
    def get(self, request):
        pid = self.request.query_params.get("pid") or ""

        poets = Poets.objects.all()
        count = poets.count()

        if pid.isdigit():
            _ = Poets.objects.filter(p_id=pid)
            if _:
                poets = _

        offset = self.request.query_params.get("offset") or 0
        try:
            offset = int(offset)
        except ValueError:
            offset = 0
        length = self.request.query_params.get("length") or count
        try:
            length = int(length)
        except ValueError:
            length = count

        serialized = poetsSerializer(poets, many=True)
        return Response(dict(
            poets=serialized.data[offset:offset+length],
            all_count=count
        ))


class get_poem(APIView):
    def get(self, request, count):
        p_id = self.request.query_params.get('p') or 1
        poems = []
        for _ in range(count):
            poem = requests.get(
                f'http://c.ganjoor.net/beyt-json.php?p={p_id}').json()
            poet = Poets.objects.filter(name=poem['poet']).first()
            del poem['poet']
            poems.append(dict(
                poet=dict(
                    name=poet.name,
                    p_id=poet.p_id,
                    pic=poet.pic,
                    link=poet.link,
                ),
                **poem
            ))
        return Response(poems)


def github(request):
    return HttpResponse("<a href=\"https://github.com/abiyat-parsi\">Source on github</a>")
