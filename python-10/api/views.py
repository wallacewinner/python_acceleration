
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter


@api_view(['POST'])
def lambda_function(request):
    question = request.data.get('question')

    table = list(Counter(question).elements())
    table_ordered = sorted(table, key=table.count, reverse=True)
    
    return Response({'solution': table_ordered})
