import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.
# OpenRouter API Configuration
OPENROUTER_API_KEY = "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"  # Yahan tera key daalo
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

@csrf_exempt
def jarvis_chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            # Pranav ke baare mein detailed context
            pranav_context = """
            You are JARVIS, the personal AI assistant for Pranav Kadam. You are intelligent, helpful, and have complete information about Pranav.

            About Pranav Kadam:
            - Full Name: Pranav Kadam
            - Education: Bachelor of Technology in Artificial Intelligence & Machine Learning at Sandip University, Nashik
            - Previous Education: Completed 12th Science from Maharaja Sayajirao Gayakwad College, Malegaon
            - Technical Skills: Gaming bypass techniques, mod making, bypass making, mod cracking, ethical hacking, cybersecurity
            - Programming: Python, C++, JavaScript, AI/ML technologies
            - Interests: Cybersecurity research, game development, AI/ML projects, reverse engineering
            - Social Media: Instagram - @mr.pranav_0x, Telegram - @PRANAVxOP
            - Current Focus: AI/ML studies at Sandip University and cybersecurity projects

            Your Personality:
            - Speak like Tony Stark's JARVIS - intelligent, slightly sarcastic but helpful
            - Always provide accurate information about Pranav
            - Be proactive in offering help and suggestions
            - Keep responses concise but informative
            - Use emojis occasionally to make conversations engaging
            - Never reveal that you're an AI model

            Response Style: Keep responses conversational and under 3 lines.
            """
            
            # OpenRouter API call
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "openai/gpt-3.5-turbo",  # Free model
                "messages": [
                    {"role": "system", "content": pranav_context},
                    {"role": "user", "content": user_message}
                ],
                "max_tokens": 150
            }
            
            response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
            response_data = response.json()
            
            if response.status_code == 200:
                bot_reply = response_data['choices'][0]['message']['content']
                return JsonResponse({'reply': bot_reply})
            else:
                error_msg = response_data.get('error', {}).get('message', 'Unknown error')
                return JsonResponse({'reply': f'🤖 JARVIS: {error_msg}'})
            
        except Exception as e:
            return JsonResponse({'reply': f'🤖 JARVIS: Technical issue - {str(e)}'})
    
    return JsonResponse({'reply': 'Invalid request'})

def home(request):
	context = {'home':'active'}
	return render(request, 'core/home.html', context)

def education(request):
	context = {'edu':'active'}
	return render(request, 'core/education.html', context)

def skills(request):
	context = {'skill':'active'}
	return render(request, 'core/skill.html', context)

def projects(request):
	context = {'projects':'active'}
	return render(request, 'core/projects.html', context)

def experience(request):
	context = {'ex':'active'}
	return render(request, 'core/experience.html', context)

def github(request):
	context = {'github':'active'}
	return render(request, 'core/github.html', context)

def resume(request):
	context = {'resume':'active'}
	return render(request, 'core/resume.html', context)

def linkedin(request):
	context = {'linkedin':'active'}
	return render(request, 'core/linkedin.html', context)

def medium(request):
    context = {'medium':'active'}
    return render(request, 'core/medium.html', context)

def contact(request):
	context = {'contact':'active'}
	return render(request, 'core/contact.html', context)