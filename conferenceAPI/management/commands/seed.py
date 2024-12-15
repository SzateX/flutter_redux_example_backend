import random
from django.utils import timezone
from django.core.management.base import BaseCommand
from conferenceAPI.models import Place, Speaker, Lecture
from datetime import timedelta

# Zestawy danych
BUILDINGS = ["Centrum Nauki", "Budynek Innowacji", "Akademia Przyszłości", "Sala Konferencyjna 'Horyzont'"]
ROOMS = ["Sala Alfa", "Sala Beta", "Sala Główna", "Sala 404", "Sala Delta"]
SPEAKER_FIRST_NAMES = ["Jan", "Anna", "Piotr", "Maria", "Krzysztof", "Ewa", "Zofia", "Andrzej"]
SPEAKER_LAST_NAMES = ["Kowalski", "Nowak", "Zieliński", "Wiśniewska", "Kamiński", "Lewandowski", "Szymańska", "Wójcik"]
SPEAKER_SPECIALTIES = [
    "ekspert od sztucznej inteligencji",
    "specjalista ds. cyberbezpieczeństwa",
    "guru baz danych",
    "pasjonat przetwarzania języka naturalnego",
    "architekt systemów IoT",
    "badacz w dziedzinie robotyki",
    "profesor z zakresu kwantowych obliczeń",
    "entuzjasta technologii blockchain",
]

LECTURE_TOPICS = [
    "Sztuczna inteligencja w codziennym życiu",
    "Nowoczesne podejście do cyberbezpieczeństwa",
    "Przyszłość Internetu Rzeczy (IoT)",
    "Blockchain i kryptowaluty – mit czy przyszłość?",
    "Przetwarzanie języka naturalnego (NLP) w praktyce",
    "Robotyka w przemyśle i edukacji",
    "Obliczenia kwantowe – wstęp i przyszłe zastosowania",
    "Big Data i analiza danych na przykładach",
]

LECTURE_DESCRIPTIONS = [
    "Interesujące spojrzenie na rozwój technologii oraz jej wpływ na naszą codzienność.",
    "Dogłębna analiza trendów i nowoczesnych rozwiązań stosowanych w branży.",
    "Praktyczne przykłady zastosowań oraz potencjalne wyzwania, które czekają na specjalistów.",
    "Warsztaty pełne wiedzy praktycznej i innowacyjnych pomysłów.",
    "Prezentacja oparta na najnowszych badaniach oraz technologicznych nowinkach.",
    "Spotkanie z ekspertem z wieloletnim doświadczeniem w tej dziedzinie.",
]


class Command(BaseCommand):
    help = "Seeds the database with sample data for Place, Speaker, and Lecture models."

    def handle(self, *args, **kwargs):
        # Tworzenie miejsc
        places = []
        for i in range(4):
            place = Place.objects.create(
                building_name=random.choice(BUILDINGS),
                room_name=random.choice(ROOMS),
            )
            places.append(place)
        self.stdout.write(self.style.SUCCESS("Places created."))

        # Tworzenie prelegentów
        speakers = []
        for i in range(8):
            first_name = random.choice(SPEAKER_FIRST_NAMES)
            last_name = random.choice(SPEAKER_LAST_NAMES)
            specialty = random.choice(SPEAKER_SPECIALTIES)
            speaker = Speaker.objects.create(
                name=first_name,
                surname=last_name,
                description=f"{first_name} {last_name} to {specialty} z wieloletnim doświadczeniem.",
            )
            speakers.append(speaker)
        self.stdout.write(self.style.SUCCESS("Speakers created."))

        # Tworzenie wykładów
        start_time = timezone.now()
        for i in range(6):
            title = random.choice(LECTURE_TOPICS)
            description = random.choice(LECTURE_DESCRIPTIONS)
            lecture = Lecture.objects.create(
                title=title,
                description=description,
                begin_time=start_time + timedelta(hours=i * 2),
                end_time=start_time + timedelta(hours=i * 2 + 1),
                place_id=random.choice(places),
            )
            # Losowe przypisanie od 1 do 3 prelegentów
            selected_speakers = random.sample(speakers, k=random.randint(1, 3))
            for speaker in selected_speakers:
                lecture.speakers.add(speaker)

            self.stdout.write(self.style.SUCCESS(f"Lecture '{title}' created with {len(selected_speakers)} speaker(s)."))

        self.stdout.write(self.style.SUCCESS("Seeding completed successfully!"))
