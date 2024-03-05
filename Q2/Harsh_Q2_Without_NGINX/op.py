import requests
url = 'http://localhost:5000/summarize'

input_text = {
    'text': 'Digital training on AWS Skill Builder. Our portfolio of 600+ digital courses on AWS Skill Builder covers 30+ AWS services and solutions, and are designed to be consumed by anyone around the globe, at their pace, and at various skill levels. Digital training allows you to develop skills and knowledge for any of the AWS domains, from machine learning, to networking, security, and more, with short videos. We have the training to meet the needs of various knowledge and skill levels, whether you’re just starting to learn about the AWS Cloud, or have been working on it for years. Our courses are developed by AWS experts and our trainers are all AWS Certified. If you’re new to cloud or in a non-IT role, start with AWS Cloud Practitioner Essentials. It provides a foundational understanding of the AWS Cloud and helps learners prepare for the AWS Certified Cloud Practitioner exam.AWS Cloud Quest: Cloud Practitioner role. Explore this 3D role-playing game, designed by AWS Training and Certification, to help build practical AWS experience. To win, complete a 12-part quest, having fun while building cloud skills and engaging in a virtual city environment. Gameplay includes videos, quizzes, and hands-on exercises based on real-world business scenarios.'
}
response = requests.post(url, json=input_text)

print(response.json())
