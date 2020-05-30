import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from groups.models import Group
from groups.serializers import GroupSerializer


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_group(request, group_id):
    group = Group.objects.get(id=group_id)
    serializer = GroupSerializer(group, many=False)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def list_groups(request):
    group = Group.objects.all()
    serializer = GroupSerializer(group, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_group(request):
    try:
        payload = json.loads(request.body)
        group = Group.objects.create(
            name=payload["name"],
            color=payload["color"],
            admin=payload["admin"]
        )
        serializer = GroupSerializer(group)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_group(request, group_id):
    payload = json.loads(request.body)
    try:
        group_item = Group.objects.filter(id=group_id)
        group_item.update(**payload)
        group = Group.objects.get(id=group_id)
        serializer = GroupSerializer(group)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_group(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
        group.delete()
        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
