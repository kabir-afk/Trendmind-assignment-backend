from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from google import genai
from django.conf import settings

# Create your views here.

length_map = {
    "short": "Keep the post between 100–150 words.",
    "medium": "Keep the post between 200–300 words.",
    "long": "Keep the post under 450 words."
}
class GeneratePost(APIView):
    def post(self,req):
        tone = req.data.get("tone")
        targetAudience = req.data.get("targetAudience")
        topic = req.data.get("topic")
        length = req.data.get("length")
        
        if not settings.GEMINI_API_KEY:
            return Response(
                {"error": "GEMINI_API_KEY not configured"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        length_instruction = length_map.get(length, length_map["short"])

        prompt = f"""You are an expert LinkedIn content strategist.
                    Write a LinkedIn post using the following parameters:
                        Tone: {tone}
                        Target Audience: {targetAudience}
                        Topic: {topic}
                        Length: {length_instruction}
                    Constraints:
                        - Start with a strong hook in the first 2 lines.
                        - Use short paragraphs.
                        - Speak directly to the target audience.
                        - Provide actionable insight.
                        - Avoid generic motivational fluff.
                        - End with a thought-provoking question."""
        response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt)
        return Response({'post':response.text},status=status.HTTP_200_OK)