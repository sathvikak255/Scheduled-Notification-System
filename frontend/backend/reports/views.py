from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subscription, ReportHistory
from .serializers import SubscriptionSerializer, ReportHistorySerializer
from django.utils.timezone import now


@api_view(['POST'])
def subscribe(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=400)

    data = request.data.copy()
    data['email'] = email

    try:
        subscription = Subscription.objects.get(email=email)
        serializer = SubscriptionSerializer(subscription, data=data)
    except Subscription.DoesNotExist:
        serializer = SubscriptionSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def unsubscribe(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=400)

    try:
        sub = Subscription.objects.get(email=email)
        sub.delete()
        return Response({'message': 'Unsubscribed successfully'})
    except Subscription.DoesNotExist:
        return Response({'error': 'Subscription not found'}, status=404)

@api_view(['GET'])
def get_subscriptions(request):
    email = request.query_params.get('email')
    if not email:
        return Response({'error': 'Email query parameter is required'}, status=400)

    active_subs = Subscription.objects.filter(email=email, is_active=True)
    serializer = SubscriptionSerializer(active_subs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_report_history(request):
    email = request.query_params.get('email')
    if not email:
        return Response({'error': 'Email query parameter is required'}, status=400)

    subs = Subscription.objects.filter(email=email)
    history = ReportHistory.objects.filter(subscription__in=subs)
    serializer = ReportHistorySerializer(history, many=True)
    return Response(serializer.data)
