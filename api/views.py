from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from google import genai
from django.conf import settings

# Create your views here.


class GeneratePost(APIView):
    # def get(self,req):
    #     return Response('hellow',status=status.HTTP_200_OK)
    def post(self,req):
        tone, targetAudience,topic,length = req.data.values()
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        prompt = f"""You are an expert LinkedIn content strategist.
                    Write a LinkedIn post using the following parameters:
                        Tone: {tone}
                        Target Audience: {targetAudience}
                        Topic: {topic}
                        Length: {length}
                    Constraints:
                        - Start with a strong hook in the first 2 lines.
                        - Use short paragraphs.
                        - Speak directly to the target audience.
                        - Provide actionable insight.
                        - Avoid generic motivational fluff.
                        - End with a thought-provoking question."""
        response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt)
        return Response(f'post:{response.text}',status=status.HTTP_201_CREATED)
        
