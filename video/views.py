import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from video.models import Video
from video.serializers import VideoSerializer


@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny])
def get_video(request, video_id):
    video = Video.objects.get(id=video_id)
    serializer = VideoSerializer(video, many=False)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny])
def list_videos(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_video(request):
    try:
        payload = json.loads(request.body)
        video = Video.objects.create(
            id=payload["id"],
            tag_id=payload["tag"]
        )
        serializer = VideoSerializer(video)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_video(request, video_id):
    payload = json.loads(request.body)
    try:
        video_item = Video.objects.filter(id=video_id)
        video_item.update(**payload)
        video = Video.objects.get(id=video_id)
        serializer = VideoSerializer(video)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_video(request, video_id):
    try:
        video = Video.objects.get(id=video_id)
        video.delete()
        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
