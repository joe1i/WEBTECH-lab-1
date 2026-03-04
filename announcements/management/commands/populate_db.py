import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from announcements.models import Announcement
from reactions.models import Reaction
from faker import Faker

User = get_user_model()
fake = Faker('uk_UA')  # Генеруємо дані українською


class Command(BaseCommand):
    help = 'Наповнює базу даних тестовими користувачами, оголошеннями та реакціями'

    def handle(self, *args, **options):
        self.stdout.write('Починаємо генерацію даних...')

        # 1. Створення звичайних користувачів
        users = []
        for _ in range(15):  # Створимо 15 користувачів
            gender = random.choice(['M', 'F', 'O'])
            user = User.objects.create_user(
                email=fake.unique.email(),
                username=fake.unique.user_name(),
                first_name=fake.first_name_male() if gender == 'M' else fake.first_name_female(),
                last_name=fake.last_name_male() if gender == 'M' else fake.last_name_female(),
                gender=gender,
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=60),
                bio=fake.text(max_nb_chars=200),
                password='testpassword123'
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f'Створено 15 користувачів.'))

        # 2. Отримання або створення адміністратора (автора оголошень)
        admin_user, created = User.objects.get_or_create(
            email='admin@example.com',
            defaults={
                'username': 'admin',
                'first_name': 'Головний',
                'last_name': 'Адмін',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('adminpass123')
            admin_user.save()

        # 3. Створення оголошень
        announcements = []
        for _ in range(10):  # Створимо 10 оголошень
            announcement = Announcement.objects.create(
                title=fake.sentence(nb_words=5),
                content=fake.text(max_nb_chars=1000),
                author=admin_user,
                views_count=random.randint(10, 100)
            )
            announcements.append(announcement)
        self.stdout.write(self.style.SUCCESS(f'Створено 10 оголошень.'))

        # 4. Створення реакцій (імітація активності)
        reaction_types = ['like', 'heart', 'fire', 'sad']
        reactions_created = 0

        for announcement in announcements:
            # Вибираємо випадкову кількість користувачів (від 3 до 10), які залишать реакцію на це оголошення
            reacting_users = random.sample(users, random.randint(3, 10))
            for user in reacting_users:
                Reaction.objects.create(
                    announcement=announcement,
                    user=user,
                    reaction_type=random.choice(reaction_types)
                )
                reactions_created += 1

        self.stdout.write(self.style.SUCCESS(f'Створено {reactions_created} реакцій.'))
        self.stdout.write(self.style.SUCCESS('Базу даних успішно наповнено!'))