from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from forum.models import Category, Thread, Post


class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Category.objects.all().delete()
        Thread.objects.all().delete()
        Post.objects.all().delete()

        # Create dummy users
        usernames = ['user1', 'user2', 'user3', 'user4']
        users = []

        for username in usernames:
            user = User.objects.create_user(
                username=username, password='password', email=f'{username}@example.com')
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user {username}'))

        # Create dummy categories
        categories = [
            Category.objects.create(
                name='Tech', description='Technology related discussions'),
            Category.objects.create(
                name='Health', description='Health and wellness topics'),
            Category.objects.create(
                name='Travel', description='Travel tips and experiences'),
            Category.objects.create(
                name='Food', description='Food recipes and cooking tips')
        ]

        # Create dummy threads
        threads = [
            Thread.objects.create(
                title='Latest in AI', content='Discuss the latest trends in AI.', category=categories[0], author=users[0]),
            Thread.objects.create(
                title='Healthy Eating', content='Tips and advice on healthy eating.', category=categories[1], author=users[1]),
            Thread.objects.create(title='Best Travel Destinations',
                                  content='Share your favorite travel destinations and experiences.', category=categories[2], author=users[2]),
            Thread.objects.create(title='Quick and Easy Recipes',
                                  content='Share quick and easy recipes for busy people.', category=categories[3], author=users[3])
        ]

        # Create dummy posts
        posts = [
            Post.objects.create(
                content='AI is evolving rapidly with new advancements.', thread=threads[0], author=users[1]),
            Post.objects.create(
                content='Eating more fruits and vegetables can improve your health.', thread=threads[1], author=users[0]),
            Post.objects.create(
                content='I loved my trip to Japan last year. The culture and food were amazing!', thread=threads[2], author=users[3]),
            Post.objects.create(
                content='Try this 15-minute pasta recipe for a quick meal.', thread=threads[3], author=users[2]),
            Post.objects.create(
                content='AI is making strides in machine learning and natural language processing.', thread=threads[0], author=users[2]),
            Post.objects.create(
                content='Incorporating nuts and seeds into your diet can be very beneficial.', thread=threads[1], author=users[3]),
            Post.objects.create(
                content='The beaches in Bali are fantastic for relaxation.', thread=threads[2], author=users[1]),
            Post.objects.create(
                content='Here’s a quick recipe for a healthy smoothie.', thread=threads[3], author=users[0])
        ]

        self.stdout.write(self.style.SUCCESS(
            'Dummy data created successfully!'))